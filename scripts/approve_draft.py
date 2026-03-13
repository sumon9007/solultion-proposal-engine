#!/usr/bin/env python3
"""
approve_draft.py — Validate and promote a draft proposal to approved status.

Usage:
    python scripts/approve_draft.py <path-to-draft>

The script:
1. Validates the draft (must pass all checks)
2. Copies it to output/approved/ with _approved.md suffix
3. Logs the approval to output/approved/approval-log.json
4. Prints the path to the approved file

Returns exit code 0 on success, 1 on failure.
"""

from __future__ import annotations

import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from helpers import (
    APPROVED_DIR,
    append_approval_log,
    bold,
    build_log_entry,
    draft_to_approved_name,
    ensure_output_dirs,
    fail,
    info,
    ok,
    parse_stem,
    read_file,
    resolve_proposal_path,
    warn,
)
from validate_proposal import validate


# ─── Approval ─────────────────────────────────────────────────────────────────

def approve(draft_path: Path) -> bool:
    ensure_output_dirs()

    print()
    print(bold(f"APPROVING: {draft_path.name}"))
    print("=" * 60)

    # ── 1. Validate ───────────────────────────────────────────────
    print(info("Running validation checks..."))
    result = validate(draft_path)

    if not result.passed:
        print()
        print(fail(bold("APPROVAL BLOCKED — Validation failed.")))
        print(fail(f"  {len(result.issues)} issue(s) must be resolved first."))
        print()
        print("Issues found:")
        for issue in result.issues:
            print(f"  ❌ {issue}")
        print()
        print(info("Fix these issues and re-run this script, or use:"))
        print(info(f"  python scripts/validate_proposal.py {draft_path}"))
        return False

    print(ok("Validation PASSED."))
    print()

    # ── 2. Check draft naming ─────────────────────────────────────
    if "_draft.md" not in draft_path.name:
        print(warn(f"File does not end with '_draft.md': {draft_path.name}"))
        print(warn("Expected naming: YYYY-MM-DD_[client]_[type]_draft.md"))
        answer = input("Continue anyway? (yes/no): ").strip().lower()
        if answer != "yes":
            print(info("Approval cancelled."))
            return False

    # ── 3. Determine approved path ────────────────────────────────
    approved_path = draft_to_approved_name(draft_path)

    if approved_path.exists():
        print(warn(f"Approved file already exists: {approved_path.name}"))
        print(warn("Overwriting an approved file is a serious action."))
        answer = input("Overwrite? (yes/no): ").strip().lower()
        if answer != "yes":
            print(info("Approval cancelled."))
            return False

    # ── 4. Confirm approval intent ────────────────────────────────
    print()
    print(info(f"  Draft:    {draft_path.name}"))
    print(info(f"  Approved: {approved_path.name}"))
    print()
    answer = input("Approve this draft? (yes/no): ").strip().lower()
    if answer != "yes":
        print(info("Approval cancelled."))
        return False

    # ── 5. Copy to approved ───────────────────────────────────────
    shutil.copy2(draft_path, approved_path)
    print(ok(f"Proposal approved: {approved_path}"))

    # ── 6. Log approval ───────────────────────────────────────────
    stem_parts = parse_stem(draft_path.stem.replace("_proposal_draft", "").replace("_draft", ""))
    stem = f"{stem_parts[0]}_{stem_parts[1]}_{stem_parts[2]}" if stem_parts else ""
    log_entry = build_log_entry(
        draft_file=str(draft_path),
        approved_file=str(approved_path),
        stem=stem,
        artifact_type="proposal",
    )
    append_approval_log(log_entry)
    print(ok(f"Approval logged to: {APPROVED_DIR / 'approval-log.json'}"))

    # ── 7. Next step ──────────────────────────────────────────────
    print()
    print(bold("NEXT STEP — Export to HTML:"))
    print(info(f"  python scripts/export_proposal.py {approved_path}"))
    print()

    return True


# ─── Main ─────────────────────────────────────────────────────────────────────

def main() -> None:
    if len(sys.argv) < 2:
        print(f"Usage: python {Path(__file__).name} <path-to-draft>")
        sys.exit(1)

    path = resolve_proposal_path(sys.argv[1])

    if not path.exists():
        print(fail(f"File not found: {path}"))
        sys.exit(1)

    success = approve(path)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
