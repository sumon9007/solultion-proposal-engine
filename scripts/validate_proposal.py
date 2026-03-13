#!/usr/bin/env python3
"""
validate_proposal.py — Structural and content validation for proposal drafts.

Usage:
    python scripts/validate_proposal.py <path-to-draft>

Returns exit code 0 on PASS, 1 on FAIL.
"""

from __future__ import annotations

import re
import sys
from datetime import datetime
from pathlib import Path

# Allow running from project root or scripts/ directory
sys.path.insert(0, str(Path(__file__).resolve().parent))
from helpers import (
    PLACEHOLDER_PATTERNS,
    SECTION_VARIANTS,
    WORD_COUNT_MINIMUMS,
    bold,
    count_words,
    extract_headings,
    fail,
    find_section_content,
    info,
    ok,
    read_file,
    resolve_proposal_path,
    warn,
)


# ─── Validation Result ────────────────────────────────────────────────────────

class ValidationResult:
    def __init__(self) -> None:
        self.issues: list[str] = []
        self.passes: list[str] = []
        self.warnings: list[str] = []

    def add_pass(self, message: str) -> None:
        self.passes.append(message)

    def add_fail(self, message: str) -> None:
        self.issues.append(message)

    def add_warn(self, message: str) -> None:
        self.warnings.append(message)

    @property
    def passed(self) -> bool:
        return len(self.issues) == 0


# ─── Checks ───────────────────────────────────────────────────────────────────

def check_sections(content: str, result: ValidationResult) -> dict[str, bool]:
    """Check that all required sections are present. Returns found map."""
    headings_lower = [h.lower() for h in extract_headings(content)]
    found: dict[str, bool] = {}

    for canonical, variants in SECTION_VARIANTS.items():
        matched = any(v in headings_lower for v in variants)
        found[canonical] = matched
        if matched:
            result.add_pass(f"{canonical} — present")
        else:
            result.add_fail(f"{canonical} — MISSING")

    return found


def check_placeholders(content: str, result: ValidationResult) -> None:
    """Check for remaining placeholder text."""
    found_placeholders = []
    for pattern in PLACEHOLDER_PATTERNS:
        matches = re.findall(pattern, content, re.IGNORECASE)
        found_placeholders.extend(matches)

    if found_placeholders:
        unique = list(set(found_placeholders))
        result.add_fail(
            f"Placeholder text found: {', '.join(unique[:5])}"
            + (" (and more)" if len(unique) > 5 else "")
        )
    else:
        result.add_pass("No placeholder text found")


def check_client_name_in_summary(content: str, result: ValidationResult) -> None:
    """Check that the executive summary contains a proper noun (client name)."""
    summary_content = find_section_content(content, "Executive Summary")
    if not summary_content:
        # Already flagged as missing section
        return

    # Heuristic: look for a capitalised word that isn't a common heading word
    common_words = {"the", "a", "an", "this", "our", "we", "your", "their"}
    words = summary_content.split()
    proper_nouns = [
        w for w in words
        if w and w[0].isupper() and w.lower() not in common_words and len(w) > 2
    ]

    if proper_nouns:
        result.add_pass("Client name appears to be present in Executive Summary")
    else:
        result.add_warn(
            "Executive Summary may not mention the client name — verify manually"
        )


def check_pricing_line_items(content: str, result: ValidationResult) -> None:
    """Check that the pricing section contains at least one monetary value."""
    # Look for common pricing section variants
    for variant in SECTION_VARIANTS["Pricing"]:
        pricing_content = find_section_content(content, variant)
        if pricing_content:
            break
    else:
        pricing_content = ""

    if not pricing_content:
        return  # Already flagged as missing

    # Look for currency symbols or day rates
    has_value = bool(re.search(r"[£€$]\s*[\d,]+|[\d,]+\s*(days?|hrs?|per month)", pricing_content, re.IGNORECASE))
    if has_value:
        result.add_pass("Pricing section contains line items")
    else:
        result.add_fail("Pricing section has no monetary values or line items")


def check_word_counts(content: str, result: ValidationResult) -> None:
    """Check minimum word counts for key sections."""
    for canonical, minimum in WORD_COUNT_MINIMUMS.items():
        variants = SECTION_VARIANTS.get(canonical, [canonical.lower()])
        section_content = ""
        for variant in variants:
            section_content = find_section_content(content, variant)
            if section_content:
                break

        if not section_content:
            continue  # Already flagged as missing

        word_count = count_words(section_content)
        if word_count >= minimum:
            result.add_pass(f"{canonical}: {word_count} words (minimum {minimum})")
        else:
            result.add_fail(
                f"{canonical}: {word_count} words — minimum {minimum} required"
            )


def check_deliverables_count(content: str, result: ValidationResult) -> None:
    """Check that deliverables section has at least 3 items."""
    for variant in SECTION_VARIANTS["Deliverables"]:
        deliverables_content = find_section_content(content, variant)
        if deliverables_content:
            break
    else:
        deliverables_content = ""

    if not deliverables_content:
        return

    # Count list items (-, *, 1., 2., | rows)
    items = re.findall(r"^(\s*[-*]|\s*\d+\.|\|)", deliverables_content, re.MULTILINE)
    count = len(items)

    if count >= 3:
        result.add_pass(f"Deliverables: {count} items found (minimum 3)")
    else:
        result.add_fail(f"Deliverables: only {count} item(s) found — minimum 3 required")


def check_assumptions_count(content: str, result: ValidationResult) -> None:
    """Check that assumptions section has at least 3 items."""
    for variant in SECTION_VARIANTS["Assumptions"]:
        assumptions_content = find_section_content(content, variant)
        if assumptions_content:
            break
    else:
        assumptions_content = ""

    if not assumptions_content:
        return

    items = re.findall(r"^(\s*[-*]|\s*\d+\.)", assumptions_content, re.MULTILINE)
    count = len(items)

    if count >= 3:
        result.add_pass(f"Assumptions: {count} items found (minimum 3)")
    else:
        result.add_fail(f"Assumptions: only {count} item(s) found — minimum 3 required")

    # Warn (non-blocking) if assumptions don't follow the required format
    required_prefix = "it is assumed that"
    formatted = sum(
        1 for line in assumptions_content.splitlines()
        if line.strip().lower().startswith(required_prefix)
    )
    if count > 0 and formatted == 0:
        result.add_warn(
            'Assumptions may not follow required format: each should begin "It is assumed that..."'
        )


def check_exclusions_count(content: str, result: ValidationResult) -> None:
    """Check that exclusions section has at least 3 items."""
    for variant in SECTION_VARIANTS["Exclusions"]:
        exclusions_content = find_section_content(content, variant)
        if exclusions_content:
            break
    else:
        exclusions_content = ""

    if not exclusions_content:
        return

    items = re.findall(r"^(\s*[-*]|\s*\d+\.)", exclusions_content, re.MULTILINE)
    count = len(items)

    if count >= 3:
        result.add_pass(f"Exclusions: {count} items found (minimum 3)")
    else:
        result.add_fail(f"Exclusions: only {count} item(s) found — minimum 3 required")


# ─── Report ───────────────────────────────────────────────────────────────────

def print_report(path: Path, result: ValidationResult) -> None:
    width = 60
    print()
    print(bold("VALIDATION REPORT"))
    print("=" * width)
    print(f"File:  {path}")
    print(f"Date:  {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print()

    print(bold("SECTION CHECKS"))
    print("-" * width)
    for p in result.passes:
        if "present" in p or "words" in p or "items" in p or "line item" in p or "client name" in p or "placeholder" in p:
            print(ok(p))

    print()
    print(bold("CONTENT & QUALITY"))
    print("-" * width)

    # Print remaining passes
    already_printed = {p for p in result.passes if "present" in p}
    for p in result.passes:
        if p not in already_printed:
            print(ok(p))

    print()
    if result.issues:
        print(bold("ISSUES FOUND"))
        print("-" * width)
        for issue in result.issues:
            print(fail(issue))
        print()

    if result.warnings:
        print(bold("WARNINGS"))
        print("-" * width)
        for warning in result.warnings:
            print(warn(warning))
        print()

    print("=" * width)
    if result.passed:
        print(ok(bold("RESULT: PASS — Proposal is ready for approval.")))
        print(info("  Run: python scripts/approve_draft.py " + str(path)))
    else:
        count = len(result.issues)
        print(fail(bold(f"RESULT: FAIL — {count} issue(s) must be fixed before approval.")))
    print()


# ─── Main ─────────────────────────────────────────────────────────────────────

def validate(path: Path) -> ValidationResult:
    content = read_file(path)
    result = ValidationResult()

    check_sections(content, result)
    check_placeholders(content, result)
    check_client_name_in_summary(content, result)
    check_pricing_line_items(content, result)
    check_word_counts(content, result)
    check_deliverables_count(content, result)
    check_assumptions_count(content, result)
    check_exclusions_count(content, result)

    return result


def main() -> None:
    if len(sys.argv) < 2:
        print(f"Usage: python {Path(__file__).name} <path-to-proposal>")
        sys.exit(1)

    path = resolve_proposal_path(sys.argv[1])

    if not path.exists():
        print(fail(f"File not found: {path}"))
        sys.exit(1)

    if not path.suffix == ".md":
        print(warn(f"Expected a .md file, got: {path.suffix}"))

    result = validate(path)
    print_report(path, result)
    sys.exit(0 if result.passed else 1)


if __name__ == "__main__":
    main()
