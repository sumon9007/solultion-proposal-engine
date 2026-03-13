"""
helpers.py — Shared utilities for the Solution Proposal Engine scripts.
"""

from __future__ import annotations

import json
import re
import sys
from datetime import datetime
from pathlib import Path

# ─── Project Paths ────────────────────────────────────────────────────────────

PROJECT_ROOT = Path(__file__).resolve().parent.parent
_OUTPUT = PROJECT_ROOT / "output"
DRAFTS_DIR = _OUTPUT / "drafts" / "proposals"      # full proposals — legacy compat path
APPROVED_BASE = _OUTPUT / "approved"               # parent dir — holds approval log
APPROVED_DIR = APPROVED_BASE / "proposals"         # full proposals — legacy compat path
EXPORTS_DIR = _OUTPUT / "exports"
PACKAGES_DIR = _OUTPUT / "packages"
APPROVAL_LOG = APPROVED_BASE / "approval-log.json"
HTML_TEMPLATE = PROJECT_ROOT / "assets" / "templates" / "proposal-template.html"
CSS_STYLESHEET = PROJECT_ROOT / "assets" / "templates" / "proposal-style.css"

# ─── Artifact Types ───────────────────────────────────────────────────────────

ARTIFACT_TYPES = ["proposal", "exec-summary", "scope", "delivery-plan", "pricing"]

ARTIFACT_DRAFT_DIRS: dict[str, Path] = {
    "proposal":      _OUTPUT / "drafts" / "proposals",
    "exec-summary":  _OUTPUT / "drafts" / "exec-summaries",
    "scope":         _OUTPUT / "drafts" / "scopes",
    "delivery-plan": _OUTPUT / "drafts" / "delivery-plans",
    "pricing":       _OUTPUT / "drafts" / "pricing",
}

ARTIFACT_APPROVED_DIRS: dict[str, Path] = {
    "proposal":      _OUTPUT / "approved" / "proposals",
    "exec-summary":  _OUTPUT / "approved" / "exec-summaries",
    "scope":         _OUTPUT / "approved" / "scopes",
    "delivery-plan": _OUTPUT / "approved" / "delivery-plans",
    "pricing":       _OUTPUT / "approved" / "pricing",
}

# Pricing artifacts MUST contain this marker OR real monetary values.
# Claude must never invent day rates, totals, or commercial estimates.
COMMERCIAL_SAFETY_MARKER = "[PRICING REQUIRED — DO NOT SEND WITHOUT SIGN-OFF]"

# ─── Required Section Headings ────────────────────────────────────────────────

REQUIRED_SECTIONS = [
    "Executive Summary",
    "Understanding of Requirements",
    "Proposed Solution",
    "Scope of Work",
    "Deliverables",
    "Assumptions",
    "Exclusions",
    "Pricing",
    "Timeline",
    "About Us",
    "Next Steps",
    "Legal",
]

# Accepted heading variants (lowercased for matching)
SECTION_VARIANTS: dict[str, list[str]] = {
    "Executive Summary": ["executive summary"],
    "Understanding of Requirements": [
        "understanding of requirements",
        "client requirements",
        "your requirements",
    ],
    "Proposed Solution": ["proposed solution", "our solution", "solution overview"],
    "Scope of Work": ["scope of work", "scope", "statement of work"],
    "Deliverables": ["deliverables", "key deliverables"],
    "Assumptions": [
        "assumptions",
        "assumptions and dependencies",
        "assumptions & dependencies",
    ],
    "Exclusions": ["exclusions", "out of scope"],
    "Pricing": ["pricing", "investment", "indicative pricing", "commercial summary"],
    "Timeline": ["timeline", "project timeline", "delivery plan", "high-level plan"],
    "About Us": ["about us", "company profile", "why us", "our credentials"],
    "Next Steps": ["next steps", "how to proceed"],
    "Legal": ["legal notes", "legal", "terms and conditions", "disclaimer", "terms"],
}

PLACEHOLDER_PATTERNS = [
    r"\[TBD\]",
    r"\[INSERT",
    r"\[YOUR ",
    r"\bTODO\b",
    r"\bPLACEHOLDER\b",
    r"\bXXX\b",
]

WORD_COUNT_MINIMUMS: dict[str, int] = {
    "Executive Summary": 100,
    "Scope of Work": 150,
}

# ─── Colour Output ────────────────────────────────────────────────────────────

GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"
BOLD = "\033[1m"


def ok(msg: str) -> str:
    return f"{GREEN}✅ {msg}{RESET}"


def fail(msg: str) -> str:
    return f"{RED}❌ {msg}{RESET}"


def warn(msg: str) -> str:
    return f"{YELLOW}⚠️  {msg}{RESET}"


def info(msg: str) -> str:
    return f"{CYAN}{msg}{RESET}"


def bold(msg: str) -> str:
    return f"{BOLD}{msg}{RESET}"


# ─── File Utilities ───────────────────────────────────────────────────────────

def resolve_proposal_path(path_arg: str) -> Path:
    """Resolve a proposal file path, accepting absolute or relative paths."""
    p = Path(path_arg)
    if p.is_absolute():
        return p
    # Try relative to CWD first, then project root
    if p.exists():
        return p.resolve()
    relative_to_root = PROJECT_ROOT / p
    if relative_to_root.exists():
        return relative_to_root.resolve()
    return p.resolve()  # Return anyway; caller will check existence


def read_file(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(fail(f"File not found: {path}"))
        sys.exit(1)
    except PermissionError:
        print(fail(f"Permission denied reading: {path}"))
        sys.exit(1)


def write_file(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def ensure_output_dirs() -> None:
    for d in ARTIFACT_DRAFT_DIRS.values():
        d.mkdir(parents=True, exist_ok=True)
    for d in ARTIFACT_APPROVED_DIRS.values():
        d.mkdir(parents=True, exist_ok=True)
    PACKAGES_DIR.mkdir(parents=True, exist_ok=True)
    EXPORTS_DIR.mkdir(parents=True, exist_ok=True)


# ─── Heading Extraction ───────────────────────────────────────────────────────

def extract_headings(content: str) -> list[str]:
    """Return list of all heading texts (## or # level) from markdown."""
    headings = []
    for line in content.splitlines():
        m = re.match(r"^#{1,3}\s+(.+)", line)
        if m:
            headings.append(m.group(1).strip())
    return headings


def find_section_content(content: str, heading_text: str) -> str:
    """Extract text content under a specific heading until the next heading."""
    lines = content.splitlines()
    in_section = False
    section_lines = []
    heading_pattern = re.compile(r"^#{1,3}\s+" + re.escape(heading_text) + r"\s*$", re.IGNORECASE)
    any_heading_pattern = re.compile(r"^#{1,3}\s+")

    for line in lines:
        if heading_pattern.match(line):
            in_section = True
            continue
        if in_section:
            if any_heading_pattern.match(line):
                break
            section_lines.append(line)

    return "\n".join(section_lines)


def count_words(text: str) -> int:
    return len(text.split())


# ─── Approval Log ─────────────────────────────────────────────────────────────

def load_approval_log() -> list[dict]:
    if not APPROVAL_LOG.exists():
        return []
    try:
        return json.loads(APPROVAL_LOG.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return []


def append_approval_log(entry: dict) -> None:
    log = load_approval_log()
    log.append(entry)
    APPROVAL_LOG.write_text(json.dumps(log, indent=2), encoding="utf-8")


# ─── Filename Utilities ───────────────────────────────────────────────────────

def draft_to_approved_name(draft_path: Path) -> Path:
    """Convert a draft filename to its approved equivalent."""
    name = draft_path.name.replace("_draft.md", "_approved.md")
    return APPROVED_DIR / name


def approved_to_export_name(approved_path: Path, version: int = 1) -> Path:
    """Convert an approved filename to its HTML export name."""
    base = approved_path.stem.replace("_approved", "")
    return EXPORTS_DIR / f"{base}_v{version}.html"


def next_export_version(approved_path: Path) -> int:
    """Determine the next export version number for a proposal."""
    base = approved_path.stem.replace("_approved", "")
    existing = list(EXPORTS_DIR.glob(f"{base}_v*.html"))
    if not existing:
        return 1
    versions = []
    for f in existing:
        m = re.search(r"_v(\d+)\.html$", f.name)
        if m:
            versions.append(int(m.group(1)))
    return max(versions) + 1 if versions else 1


# ─── Artifact Path Utilities ──────────────────────────────────────────────────

def artifact_draft_path(stem: str, artifact_type: str) -> Path:
    """Return the expected draft path for an artifact given a shared stem."""
    if artifact_type not in ARTIFACT_DRAFT_DIRS:
        raise ValueError(f"Unknown artifact type '{artifact_type}'. Valid: {ARTIFACT_TYPES}")
    return ARTIFACT_DRAFT_DIRS[artifact_type] / f"{stem}_{artifact_type}_draft.md"


def artifact_approved_path(stem: str, artifact_type: str) -> Path:
    """Return the expected approved path for an artifact given a shared stem."""
    if artifact_type not in ARTIFACT_APPROVED_DIRS:
        raise ValueError(f"Unknown artifact type '{artifact_type}'. Valid: {ARTIFACT_TYPES}")
    return ARTIFACT_APPROVED_DIRS[artifact_type] / f"{stem}_{artifact_type}_approved.md"


def package_manifest_path(stem: str) -> Path:
    """Return the path for a package manifest JSON file."""
    return PACKAGES_DIR / f"{stem}_package.json"


def load_package_manifest(stem: str) -> dict:
    """Load a package manifest. Returns empty dict if not found."""
    path = package_manifest_path(stem)
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}


def save_package_manifest(stem: str, manifest: dict) -> None:
    """Persist a package manifest to disk."""
    PACKAGES_DIR.mkdir(parents=True, exist_ok=True)
    package_manifest_path(stem).write_text(
        json.dumps(manifest, indent=2, default=str), encoding="utf-8"
    )


def build_stem(date: str, client_slug: str, solution_type: str) -> str:
    """Build a shared package stem from its components."""
    return f"{date}_{client_slug}_{solution_type}"


def parse_stem(stem: str) -> tuple[str, str, str] | None:
    """Parse a stem into (date, client_slug, solution_type). Returns None on bad format."""
    m = re.match(r"^(\d{4}-\d{2}-\d{2})_([a-z0-9-]{1,20})_([a-z0-9-]+)$", stem)
    if not m:
        return None
    return m.group(1), m.group(2), m.group(3)


# ─── Env Loader ───────────────────────────────────────────────────────────────

def load_env() -> dict[str, str]:
    """Load .env file without requiring python-dotenv. Returns key-value pairs."""
    env_file = PROJECT_ROOT / ".env"
    env: dict[str, str] = {}
    if not env_file.exists():
        return env
    for line in env_file.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        env[key.strip()] = value.strip().strip('"').strip("'")
    return env
