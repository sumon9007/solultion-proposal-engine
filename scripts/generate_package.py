#!/usr/bin/env python3
"""
generate_package.py — Initialise a modular proposal package.

Creates the package manifest and ensures all artifact directories exist.
Claude writes the content for each artifact file; this script handles
the infrastructure (directories, manifest, path declarations).

Usage:
    python scripts/generate_package.py \\
        --stem STEM \\
        [--artifacts all|proposal,exec-summary,scope,delivery-plan,pricing] \\
        [--client "Client Name"] \\
        [--solution-type TYPE]

Example:
    python scripts/generate_package.py \\
        --stem 2026-03-11_acme_cloud-migration \\
        --client "Acme Corporation" \\
        --solution-type cloud-migration

Returns exit code 0 on success, 1 on failure.
"""

from __future__ import annotations

import argparse
import sys
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from helpers import (
    ARTIFACT_TYPES,
    COMMERCIAL_SAFETY_MARKER,
    artifact_draft_path,
    bold,
    ensure_output_dirs,
    fail,
    info,
    load_package_manifest,
    ok,
    parse_stem,
    save_package_manifest,
    warn,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Initialise a modular proposal package.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--stem", required=True,
        help="Shared package stem: YYYY-MM-DD_client-slug_solution-type",
    )
    parser.add_argument(
        "--artifacts", default="all",
        help=f"Comma-separated artifact types or 'all'. Valid: {', '.join(ARTIFACT_TYPES)}",
    )
    parser.add_argument("--client", default="", help="Client display name")
    parser.add_argument("--solution-type", default="", help="Solution type label")
    return parser.parse_args()


def resolve_artifacts(artifacts_arg: str) -> list[str]:
    if artifacts_arg.strip().lower() == "all":
        return list(ARTIFACT_TYPES)
    requested = [a.strip() for a in artifacts_arg.split(",")]
    invalid = [a for a in requested if a not in ARTIFACT_TYPES]
    if invalid:
        print(fail(f"Unknown artifact type(s): {', '.join(invalid)}"))
        print(info(f"Valid types: {', '.join(ARTIFACT_TYPES)}"))
        sys.exit(1)
    return requested


def initialise_package(
    stem: str,
    artifacts: list[str],
    client: str,
    solution_type: str,
) -> None:
    ensure_output_dirs()

    parsed = parse_stem(stem)
    if not parsed:
        print(fail(f"Invalid stem format: '{stem}'"))
        print(info("Expected: YYYY-MM-DD_client-slug_solution-type"))
        print(info("Example:  2026-03-11_acme_cloud-migration"))
        sys.exit(1)

    date, client_slug, sol_type = parsed

    # Preserve existing manifest; extend with any new artifact entries
    existing = load_package_manifest(stem)
    if existing:
        print(warn(f"Package already exists: {stem}"))
        print(warn("Existing manifest preserved — new artifact entries will be merged in."))
        manifest = existing
    else:
        manifest = {
            "stem": stem,
            "created_at": datetime.now().isoformat(timespec="seconds"),
            "client": client or client_slug,
            "solution_type": solution_type or sol_type,
            "artifacts": {},
            "status": "draft",
        }

    if client:
        manifest["client"] = client
    if solution_type:
        manifest["solution_type"] = solution_type

    print()
    print(bold(f"PACKAGE: {stem}"))
    print("=" * 62)
    print(info(f"  Client:    {manifest['client']}"))
    print(info(f"  Solution:  {manifest['solution_type']}"))
    print(info(f"  Date:      {date}"))
    print(info(f"  Artifacts: {', '.join(artifacts)}"))
    print()
    print(bold("ARTIFACT PATHS"))
    print("-" * 62)

    for artifact_type in artifacts:
        draft_path = artifact_draft_path(stem, artifact_type)
        already_exists = draft_path.exists()

        if artifact_type not in manifest["artifacts"]:
            manifest["artifacts"][artifact_type] = {
                "draft": str(draft_path),
                "approved": None,
                "status": "exists" if already_exists else "pending",
                "commercial_safety": artifact_type == "pricing",
            }
        else:
            # Keep existing entry; update the path in case dir structure changed
            manifest["artifacts"][artifact_type]["draft"] = str(draft_path)
            if already_exists:
                manifest["artifacts"][artifact_type]["status"] = "exists"

        status_label = ok("exists") if already_exists else warn("pending — Claude writes this file")
        print(f"  [{artifact_type}]")
        print(f"    Path:   {draft_path}")
        print(f"    Status: {status_label}")
        if artifact_type == "pricing":
            print(info(f"    Note:   Must contain the commercial safety marker:"))
            print(info(f"            {COMMERCIAL_SAFETY_MARKER}"))
            print(info("            or real monetary values confirmed by the client."))
        print()

    save_package_manifest(stem, manifest)
    print(ok(f"Manifest saved: output/packages/{stem}_package.json"))
    print()
    print(bold("NEXT STEPS"))
    print("-" * 62)
    print(info("  1. Claude writes each artifact file to the paths listed above."))
    print(info("  2. Validate the package (dry run):"))
    print(info(f"       python scripts/approve_package.py --stem {stem} --dry-run"))
    print(info("  3. Approve when ready:"))
    print(info(f"       python scripts/approve_package.py --stem {stem}"))
    print()


def main() -> None:
    args = parse_args()
    artifacts = resolve_artifacts(args.artifacts)
    initialise_package(args.stem, artifacts, args.client, args.solution_type)


if __name__ == "__main__":
    main()