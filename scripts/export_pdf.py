#!/usr/bin/env python3
"""
export_pdf.py — Export an approved proposal to a branded PDF.

Usage:
    python scripts/export_pdf.py <path-to-approved-file>

The script:
1. Validates the file is an _approved.md
2. Generates branded HTML (same pipeline as export_proposal.py)
3. Converts HTML to PDF using WeasyPrint
4. Saves to output/exports/ with versioned filename

Dependencies:
    pip install weasyprint markdown

Falls back to browser-print instructions if WeasyPrint is unavailable.
Returns exit code 0 on success, 1 on failure.
"""

from __future__ import annotations

import sys
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from helpers import (
    CSS_STYLESHEET,
    approved_to_export_name_for,
    bold,
    ensure_output_dirs,
    fail,
    info,
    load_env,
    next_export_version_for,
    ok,
    read_file,
    resolve_proposal_path,
    warn,
)
from export_proposal import (
    _default_css,
    _extract_client_name,
    _extract_title,
    build_brand_css_overrides,
    build_html,
    build_logo_html,
    markdown_to_html,
)


# ─── Export ───────────────────────────────────────────────────────────────────

def export_pdf(approved_path: Path) -> bool:
    ensure_output_dirs()

    print()
    print(bold(f"EXPORTING TO PDF: {approved_path.name}"))
    print("=" * 60)

    # ── Guard: must be approved file ─────────────────────────────
    if "_approved.md" not in approved_path.name:
        if "_draft.md" in approved_path.name:
            print(fail("Cannot export a draft file. Approve it first:"))
            print(info(f"  python scripts/approve_draft.py {approved_path}"))
        else:
            print(fail("File does not appear to be an approved proposal."))
            print(warn("Expected filename pattern: *_approved.md"))
        return False

    # ── Check dependency ─────────────────────────────────────────
    try:
        from weasyprint import HTML as WeasyHTML
    except ImportError:
        print(fail("WeasyPrint is not installed."))
        print(info("  pip install weasyprint"))
        print()
        print(warn("Alternative: export to HTML and use your browser's Print > Save as PDF"))
        print(info(f"  python scripts/export_proposal.py {approved_path}"))
        return False

    # ── Read content ─────────────────────────────────────────────
    md_content = read_file(approved_path)
    env = load_env()

    # ── Extract metadata ─────────────────────────────────────────
    title = _extract_title(md_content)
    client_name, client_found = _extract_client_name(md_content)
    export_date = datetime.now().strftime("%d %B %Y")

    print(info(f"  Title:    {title}"))
    print(info(f"  Client:   {client_name}"))
    if not client_found:
        print(warn("  Client name could not be extracted — falling back to 'Client'."))
        print(warn("  Add 'Prepared for: [Client Name]' to the cover page to fix this."))
    print(info(f"  Date:     {export_date}"))

    # ── Convert markdown ─────────────────────────────────────────
    print(info("  Converting markdown to HTML..."))
    proposal_html = markdown_to_html(md_content)

    # ── Load CSS and apply brand overrides ───────────────────────
    css_content = read_file(CSS_STYLESHEET) if CSS_STYLESHEET.exists() else _default_css()
    brand_overrides = build_brand_css_overrides(env)
    if brand_overrides:
        css_content = brand_overrides + "\n" + css_content
        print(info("  Brand CSS overrides applied from .env"))

    # ── Build logo / company identity ─────────────────────────────
    logo_html = build_logo_html(env)

    # ── Build HTML ────────────────────────────────────────────────
    final_html = build_html(
        proposal_html, env, title, client_name, export_date, css_content, logo_html
    )

    # ── Render PDF ────────────────────────────────────────────────
    version = next_export_version_for(approved_path, "pdf")
    export_path = approved_to_export_name_for(approved_path, "pdf", version)

    print(info("  Rendering PDF with WeasyPrint..."))
    WeasyHTML(string=final_html, base_url=str(approved_path.parent.resolve())).write_pdf(
        str(export_path)
    )

    print(ok(f"Exported: {export_path}"))
    print(ok(f"Version:  v{version}"))
    print()
    print(bold("NEXT STEP:"))
    print(info(f"  Open PDF: {export_path.resolve()}"))
    print()

    return True


# ─── Entry Point ──────────────────────────────────────────────────────────────

def main() -> None:
    if len(sys.argv) < 2:
        print(f"Usage: python {Path(__file__).name} <path-to-approved-file>")
        sys.exit(1)

    path = resolve_proposal_path(sys.argv[1])

    if not path.exists():
        print(fail(f"File not found: {path}"))
        sys.exit(1)

    success = export_pdf(path)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
