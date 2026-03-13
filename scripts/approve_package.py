#!/usr/bin/env python3
"""
approve_package.py — Validate and approve all artifacts in a proposal package.

Usage:
    python scripts/approve_package.py --stem STEM [--dry-run]

The script:
  1. Loads the package manifest from output/packages/
  2. Validates each artifact using type-appropriate rules
  3. Prints a per-artifact result summary
  4. (--dry-run) Stops here — no files are written
  5. (live run) Prompts for confirmation, then copies each draft to its approved dir
  6. Updates the package manifest with approved paths and status
  7. Logs each artifact approval to output/approved/approval-log.json

Returns exit code 0 on success, 1 on failure.
"""

from __future__ import annotations

import shutil
import sys
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from helpers import (
    COMMERCIAL_SAFETY_MARKER,
    append_approval_log,
    artifact_approved_path,
    bold,
    ensure_output_dirs,
    fail,
    info,
    load_package_manifest,
    ok,
    save_package_manifest,
    warn,
)
from validate_artifact import ArtifactValidationResult, validate_artifact


# ─── Validation ───────────────────────────────────────────────────────────────

def validate_all(stem: str, manifest: dict) -> dict[str, ArtifactValidationResult]:
    results: dict[str, ArtifactValidationResult] = {}
    for artifact_type, entry in manifest.get("artifacts", {}).items():
        draft_path = Path(entry["draft"])
        if not draft_path.exists():
            r = ArtifactValidationResult(artifact_type)
            r.add_fail(f"Draft file not found: {draft_path}")
            results[artifact_type] = r
        else:
            results[artifact_type] = validate_artifact(draft_path, artifact_type)
    return results


def print_summary(results: dict[str, ArtifactValidationResult]) -> bool:
    """Print per-artifact results. Returns True if all passed."""
    width = 62
    print()
    print(bold("PACKAGE VALIDATION SUMMARY"))
    print("=" * width)

    overall_pass = True
    pricing_has_safety_marker = False

    for artifact_type, result in results.items():
        status = ok("PASS") if result.passed else fail("FAIL")
        warn_note = f"  ({len(result.warnings)} warning(s))" if result.warnings else ""
        print(f"  {artifact_type:<16}  {status}{warn_note}")

        if not result.passed:
            overall_pass = False
            for issue in result.issues:
                print(f"               ❌ {issue}")

        for w in result.warnings:
            print(f"               ⚠  {w}")
            if artifact_type == "pricing" and "safety marker" in w:
                pricing_has_safety_marker = True

    print()
    print("=" * width)

    if overall_pass:
        print(ok(bold("ALL ARTIFACTS PASS")))
        if pricing_has_safety_marker:
            print()
            print(warn("COMMERCIAL SAFETY NOTICE"))
            print(warn("  The pricing artifact uses the commercial safety marker."))
            print(warn("  Ensure confirmed pricing is inserted before sending to the client."))
    else:
        failed = [t for t, r in results.items() if not r.passed]
        print(fail(bold(f"PACKAGE BLOCKED — {len(failed)} artifact(s) failed: {', '.join(failed)}")))
        print(info("  Fix all issues, then re-run this script."))

    print()
    return overall_pass


# ─── Approval ─────────────────────────────────────────────────────────────────

def approve_package(stem: str, dry_run: bool = False) -> bool:
    ensure_output_dirs()

    print()
    print(bold(f"PACKAGE: {stem}"))
    print("=" * 62)

    manifest = load_package_manifest(stem)
    if not manifest:
        print(fail(f"No package manifest found for stem: {stem}"))
        print(info(f"  Expected: output/packages/{stem}_package.json"))
        print(info("  Initialise first:"))
        print(info(f"    python scripts/generate_package.py --stem {stem}"))
        return False

    print(info(f"  Client:    {manifest.get('client', '—')}"))
    print(info(f"  Solution:  {manifest.get('solution_type', '—')}"))
    print(info(f"  Artifacts: {', '.join(manifest.get('artifacts', {}).keys())}"))

    results = validate_all(stem, manifest)
    overall_pass = print_summary(results)

    if not overall_pass:
        return False

    if dry_run:
        print(info("Dry run — no files approved."))
        return True

    # Confirm
    answer = input("Approve all artifacts now? (yes/no): ").strip().lower()
    if answer != "yes":
        print(info("Approval cancelled."))
        return False

    # Approve each artifact
    approved_at = datetime.now().isoformat(timespec="seconds")

    for artifact_type, entry in manifest["artifacts"].items():
        draft_path = Path(entry["draft"])
        app_path = artifact_approved_path(stem, artifact_type)

        if app_path.exists():
            print(warn(f"Overwriting existing approved file: {app_path.name}"))

        shutil.copy2(draft_path, app_path)
        print(ok(f"Approved [{artifact_type}]: {app_path}"))

        has_marker = (
            artifact_type == "pricing"
            and draft_path.exists()
            and COMMERCIAL_SAFETY_MARKER in draft_path.read_text(encoding="utf-8")
        )

        append_approval_log({
            "approved_at": approved_at,
            "stem": stem,
            "artifact_type": artifact_type,
            "draft_file": str(draft_path),
            "approved_file": str(app_path),
            "approved_by": "user",
            "validation_passed": True,
            "pricing_safety_marker_present": has_marker,
        })

        manifest["artifacts"][artifact_type]["approved"] = str(app_path)
        manifest["artifacts"][artifact_type]["status"] = "approved"
        manifest["artifacts"][artifact_type]["approved_at"] = approved_at

    manifest["status"] = "approved"
    manifest["approved_at"] = approved_at
    save_package_manifest(stem, manifest)

    print()
    print(ok(bold(f"PACKAGE APPROVED: {stem}")))
    print(info(f"  Manifest: output/packages/{stem}_package.json"))
    print(info("  Log:      output/approved/approval-log.json"))
    print()
    return True


# ─── Main ─────────────────────────────────────────────────────────────────────

def main() -> None:
    import argparse
    parser = argparse.ArgumentParser(description="Approve all artifacts in a proposal package.")
    parser.add_argument(
        "--stem", required=True,
        help="Package stem: YYYY-MM-DD_client-slug_solution-type",
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Validate only — do not copy or approve any files",
    )
    args = parser.parse_args()

    success = approve_package(args.stem, dry_run=args.dry_run)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
