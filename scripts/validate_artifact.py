#!/usr/bin/env python3
"""
validate_artifact.py — Lightweight validation for individual proposal artifacts.

Each artifact type has its own validation rules:

  proposal       Full 13-section validation (delegates to validate_proposal.py)
  exec-summary   Word count ≥100, client name present, no placeholders
  scope          Word count ≥150, change control, client responsibilities, ≥3 items
  delivery-plan  Phases/milestones, duration or date references, no placeholders
  pricing        Real monetary values OR the commercial safety marker

Usage:
    python scripts/validate_artifact.py <path> [--type TYPE]

    If --type is omitted the type is inferred from the filename.

Returns exit code 0 on PASS, 1 on FAIL.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from helpers import (
    ARTIFACT_TYPES,
    COMMERCIAL_SAFETY_MARKER,
    PLACEHOLDER_PATTERNS,
    bold,
    count_words,
    fail,
    info,
    ok,
    read_file,
    resolve_proposal_path,
    warn,
)


# ─── Result ───────────────────────────────────────────────────────────────────

class ArtifactValidationResult:
    def __init__(self, artifact_type: str) -> None:
        self.artifact_type = artifact_type
        self.passes: list[str] = []
        self.issues: list[str] = []
        self.warnings: list[str] = []

    def add_pass(self, msg: str) -> None:
        self.passes.append(msg)

    def add_fail(self, msg: str) -> None:
        self.issues.append(msg)

    def add_warn(self, msg: str) -> None:
        self.warnings.append(msg)

    @property
    def passed(self) -> bool:
        return len(self.issues) == 0


# ─── Shared Checks ────────────────────────────────────────────────────────────

def _check_no_placeholders(content: str, result: ArtifactValidationResult) -> None:
    found: list[str] = []
    for pattern in PLACEHOLDER_PATTERNS:
        found.extend(re.findall(pattern, content, re.IGNORECASE))
    if found:
        unique = list(set(found))[:5]
        result.add_fail(f"Placeholder text found: {', '.join(unique)}")
    else:
        result.add_pass("No placeholder text")


def _check_min_words(content: str, minimum: int, result: ArtifactValidationResult) -> None:
    wc = count_words(content)
    if wc >= minimum:
        result.add_pass(f"Word count: {wc} (minimum {minimum})")
    else:
        result.add_fail(f"Word count: {wc} — minimum {minimum} required")


# ─── Executive Summary ────────────────────────────────────────────────────────

def validate_exec_summary(content: str) -> ArtifactValidationResult:
    result = ArtifactValidationResult("exec-summary")
    _check_no_placeholders(content, result)
    _check_min_words(content, 100, result)

    # Heuristic: proper noun present (proxy for client name)
    common_words = {"the", "a", "an", "this", "our", "we", "your", "their", "it", "is"}
    words = content.split()
    proper_nouns = [
        w for w in words
        if w and w[0].isupper() and w.lower() not in common_words and len(w) > 2
    ]
    if proper_nouns:
        result.add_pass("Client name appears present in executive summary")
    else:
        result.add_warn("Client name may be missing — verify manually")

    wc = count_words(content)
    if wc > 200:
        result.add_warn(f"Executive summary is {wc} words — recommended maximum is 200")

    return result


# ─── Scope ────────────────────────────────────────────────────────────────────

def validate_scope(content: str) -> ArtifactValidationResult:
    result = ArtifactValidationResult("scope")
    _check_no_placeholders(content, result)
    _check_min_words(content, 150, result)

    content_lower = content.lower()

    if "change control" in content_lower or "change request" in content_lower:
        result.add_pass("Change control statement present")
    else:
        result.add_fail(
            "Change control statement missing — scope must reference the change control process"
        )

    client_resp_patterns = [
        "client will", "client is responsible", "client must",
        "customer will", "customer is responsible", "customer must",
        "the client shall",
    ]
    if any(p in content_lower for p in client_resp_patterns):
        result.add_pass("Client responsibilities explicitly stated")
    else:
        result.add_warn("Client responsibilities not explicitly stated — verify manually")

    items = re.findall(r"^(\s*[-*]|\s*\d+\.)", content, re.MULTILINE)
    if len(items) >= 3:
        result.add_pass(f"Scope items: {len(items)} listed (minimum 3)")
    else:
        result.add_fail(f"Too few scope items: {len(items)} found — minimum 3 required")

    return result


# ─── Delivery Plan ────────────────────────────────────────────────────────────

def validate_delivery_plan(content: str) -> ArtifactValidationResult:
    result = ArtifactValidationResult("delivery-plan")
    _check_no_placeholders(content, result)
    _check_min_words(content, 100, result)

    if re.search(
        r"\bphase\s*\d+|\bstage\s*\d+|\bsprint\s*\d+|\bmilestone\b|\bworkstream\b",
        content, re.IGNORECASE,
    ):
        result.add_pass("Phase or milestone references present")
    else:
        result.add_warn("No explicit phase or milestone references — verify structure manually")

    duration_patterns = [
        r"\d+\s*(day|week|month|sprint)s?",
        r"\b(Q[1-4]|H[12])\s*\d{4}",
        r"\d{4}-\d{2}-\d{2}",
        r"\b(January|February|March|April|May|June|July|August"
        r"|September|October|November|December)\b",
        r"w/c\s+\d",
    ]
    if any(re.search(p, content, re.IGNORECASE) for p in duration_patterns):
        result.add_pass("Duration or date references present")
    else:
        result.add_fail(
            "No duration or date references — delivery plan must include timing"
        )

    return result


# ─── Pricing ──────────────────────────────────────────────────────────────────

def validate_pricing(content: str) -> ArtifactValidationResult:
    result = ArtifactValidationResult("pricing")

    has_safety_marker = COMMERCIAL_SAFETY_MARKER in content
    has_monetary = bool(
        re.search(
            r"[£€$]\s*[\d,]+|[\d,]+\s*(days?|hrs?|per\s+month|per\s+year|per\s+annum)",
            content, re.IGNORECASE,
        )
    )

    # Generic forbidden placeholders (the official safety marker is the only allowed one)
    forbidden: list[str] = []
    for pattern in PLACEHOLDER_PATTERNS:
        forbidden.extend(re.findall(pattern, content, re.IGNORECASE))
    forbidden = [f for f in forbidden if f not in COMMERCIAL_SAFETY_MARKER]

    if forbidden:
        result.add_fail(
            f"Forbidden placeholder text: {', '.join(set(forbidden))[:3]} — "
            f"use the commercial safety marker instead: {COMMERCIAL_SAFETY_MARKER}"
        )

    if has_monetary:
        result.add_pass("Pricing contains monetary values")
        if has_safety_marker:
            result.add_warn(
                "Both monetary values and the commercial safety marker are present — "
                "remove the marker before sending to client"
            )
    elif has_safety_marker:
        result.add_warn(
            "Pricing uses commercial safety marker — populate with confirmed figures "
            "before client delivery"
        )
    else:
        result.add_fail(
            "Pricing artifact has neither monetary values nor the commercial safety marker. "
            f"Add: {COMMERCIAL_SAFETY_MARKER}"
        )

    return result


# ─── Full Proposal (delegates to validate_proposal.py) ────────────────────────

def validate_full_proposal(path: Path) -> ArtifactValidationResult:
    from validate_proposal import validate
    proposal_result = validate(path)
    result = ArtifactValidationResult("proposal")
    result.passes = list(proposal_result.passes)
    result.issues = list(proposal_result.issues)
    result.warnings = list(proposal_result.warnings)
    return result


# ─── Dispatcher ───────────────────────────────────────────────────────────────

def validate_artifact(path: Path, artifact_type: str | None = None) -> ArtifactValidationResult:
    """Validate an artifact. Infer type from filename if not given."""
    if artifact_type is None:
        name = path.stem
        for t in ARTIFACT_TYPES:
            if f"_{t}_" in name or name.endswith(f"_{t}"):
                artifact_type = t
                break
        if artifact_type is None:
            artifact_type = "proposal"

    content = read_file(path)

    if artifact_type == "proposal":
        return validate_full_proposal(path)
    elif artifact_type == "exec-summary":
        return validate_exec_summary(content)
    elif artifact_type == "scope":
        return validate_scope(content)
    elif artifact_type == "delivery-plan":
        return validate_delivery_plan(content)
    elif artifact_type == "pricing":
        return validate_pricing(content)
    else:
        result = ArtifactValidationResult(artifact_type)
        result.add_warn(f"No validator for type '{artifact_type}' — checking placeholders only")
        _check_no_placeholders(content, result)
        return result


# ─── Report ───────────────────────────────────────────────────────────────────

def print_artifact_report(path: Path, result: ArtifactValidationResult) -> None:
    width = 60
    print()
    print(bold(f"ARTIFACT VALIDATION — {result.artifact_type.upper()}"))
    print("=" * width)
    print(f"File: {path}")
    print()
    for p in result.passes:
        print(ok(p))
    for w in result.warnings:
        print(warn(w))
    for issue in result.issues:
        print(fail(issue))
    print()
    print("=" * width)
    if result.passed:
        print(ok(bold("PASS")))
    else:
        print(fail(bold(f"FAIL — {len(result.issues)} issue(s)")))
    print()


# ─── Main ─────────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(description="Validate a proposal artifact.")
    parser.add_argument("path", help="Path to the artifact file")
    parser.add_argument(
        "--type", dest="artifact_type", choices=ARTIFACT_TYPES,
        help="Artifact type (inferred from filename if omitted)",
    )
    args = parser.parse_args()

    path = resolve_proposal_path(args.path)
    if not path.exists():
        print(fail(f"File not found: {path}"))
        sys.exit(1)

    result = validate_artifact(path, args.artifact_type)
    print_artifact_report(path, result)
    sys.exit(0 if result.passed else 1)


if __name__ == "__main__":
    main()