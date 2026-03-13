#!/usr/bin/env python3
"""
export_proposal.py — Export an approved proposal to HTML.

Usage:
    python scripts/export_proposal.py <path-to-approved-file>

The script:
1. Validates the file is in output/approved/ and named _approved.md
2. Converts markdown to HTML
3. Injects into the HTML template
4. Applies company metadata from .env
5. Saves to output/exports/ with versioned filename

Returns exit code 0 on success, 1 on failure.

Dependencies:
    pip install markdown python-dotenv

Falls back to basic HTML conversion if markdown package is unavailable.
"""

from __future__ import annotations

import html
import re
import sys
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from helpers import (
    APPROVED_DIR,
    CSS_STYLESHEET,
    EXPORTS_DIR,
    HTML_TEMPLATE,
    approved_to_export_name,
    bold,
    ensure_output_dirs,
    fail,
    info,
    load_env,
    next_export_version,
    ok,
    read_file,
    resolve_proposal_path,
    warn,
    write_file,
)


# ─── Markdown Conversion ──────────────────────────────────────────────────────

def markdown_to_html(md_content: str) -> str:
    """Convert markdown to HTML. Uses python-markdown if available."""
    try:
        import markdown
        return markdown.markdown(
            md_content,
            extensions=["tables", "fenced_code", "nl2br", "toc"],
        )
    except ImportError:
        return _basic_markdown_to_html(md_content)


def _basic_markdown_to_html(md: str) -> str:
    """Minimal markdown-to-HTML fallback (covers headings, bold, lists, tables)."""
    lines = md.splitlines()
    html_lines = []
    in_list = False
    in_table = False

    for line in lines:
        # Headings
        m = re.match(r"^(#{1,4})\s+(.+)", line)
        if m:
            if in_list:
                html_lines.append("</ul>")
                in_list = False
            level = len(m.group(1))
            text = _inline_md(m.group(2))
            html_lines.append(f"<h{level}>{text}</h{level}>")
            continue

        # HR
        if re.match(r"^[-_*]{3,}\s*$", line):
            html_lines.append("<hr>")
            continue

        # Table rows
        if line.startswith("|"):
            if not in_table:
                html_lines.append('<table><tbody>')
                in_table = True
            cells = [c.strip() for c in line.strip("|").split("|")]
            if re.match(r"^[-:]+$", cells[0].replace(" ", "")):
                continue  # Separator row
            row_html = "".join(f"<td>{_inline_md(c)}</td>" for c in cells)
            html_lines.append(f"<tr>{row_html}</tr>")
            continue
        elif in_table:
            html_lines.append("</tbody></table>")
            in_table = False

        # Unordered list
        m = re.match(r"^\s*[-*]\s+(.+)", line)
        if m:
            if not in_list:
                html_lines.append("<ul>")
                in_list = True
            html_lines.append(f"<li>{_inline_md(m.group(1))}</li>")
            continue

        # Ordered list
        m = re.match(r"^\s*\d+\.\s+(.+)", line)
        if m:
            if in_list:
                html_lines.append("</ul>")
                in_list = False
            html_lines.append(f"<li>{_inline_md(m.group(1))}</li>")
            continue

        if in_list and not line.strip():
            html_lines.append("</ul>")
            in_list = False

        # Code block
        if line.startswith("```"):
            html_lines.append("<pre><code>")
            continue

        # Blank line
        if not line.strip():
            html_lines.append("<br>")
            continue

        html_lines.append(f"<p>{_inline_md(line)}</p>")

    if in_list:
        html_lines.append("</ul>")
    if in_table:
        html_lines.append("</tbody></table>")

    return "\n".join(html_lines)


def _inline_md(text: str) -> str:
    """Convert inline markdown (bold, italic, code, links) to HTML."""
    # Bold
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"__(.+?)__", r"<strong>\1</strong>", text)
    # Italic
    text = re.sub(r"\*(.+?)\*", r"<em>\1</em>", text)
    text = re.sub(r"_(.+?)_", r"<em>\1</em>", text)
    # Inline code
    text = re.sub(r"`(.+?)`", r"<code>\1</code>", text)
    # Links
    text = re.sub(r"\[(.+?)\]\((.+?)\)", r'<a href="\2">\1</a>', text)
    return text


# ─── Template Injection ───────────────────────────────────────────────────────

def build_html(
    proposal_html: str,
    env: dict[str, str],
    title: str,
    client_name: str,
    export_date: str,
    css_content: str,
) -> str:
    """Build the final HTML document."""

    if HTML_TEMPLATE.exists():
        template = read_file(HTML_TEMPLATE)
    else:
        template = _default_html_template()

    replacements = {
        "{{PROPOSAL_CONTENT}}": proposal_html,
        "{{TITLE}}": html.escape(title),
        "{{CLIENT_NAME}}": html.escape(client_name),
        "{{EXPORT_DATE}}": export_date,
        "{{COMPANY_NAME}}": html.escape(env.get("COMPANY_NAME", "Your Company")),
        "{{COMPANY_EMAIL}}": html.escape(env.get("COMPANY_EMAIL", "")),
        "{{COMPANY_PHONE}}": html.escape(env.get("COMPANY_PHONE", "")),
        "{{COMPANY_WEBSITE}}": html.escape(env.get("COMPANY_WEBSITE", "")),
        "{{CSS}}": css_content,
    }

    result = template
    for placeholder, value in replacements.items():
        result = result.replace(placeholder, value)

    return result


def _default_html_template() -> str:
    """Minimal HTML template used when assets/templates/proposal-template.html is missing."""
    return """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{{TITLE}}</title>
  <style>
    {{CSS}}
  </style>
</head>
<body>
  <header class="doc-header">
    <div class="company-name">{{COMPANY_NAME}}</div>
    <div class="doc-meta">Prepared for: {{CLIENT_NAME}} | {{EXPORT_DATE}}</div>
  </header>
  <main class="proposal-content">
    {{PROPOSAL_CONTENT}}
  </main>
  <footer class="doc-footer">
    <div>{{COMPANY_NAME}} | {{COMPANY_EMAIL}} | {{COMPANY_PHONE}}</div>
  </footer>
</body>
</html>"""


def _extract_client_name(content: str) -> str:
    """Attempt to extract client name from the proposal cover page."""
    m = re.search(r"\*\*Prepared for:\*\*\s*(.+)", content)
    if m:
        return m.group(1).strip()
    m = re.search(r"Prepared for:\s*(.+)", content)
    if m:
        return m.group(1).strip()
    return "Client"


def _extract_title(content: str) -> str:
    """Extract the proposal title from the first # heading."""
    m = re.search(r"^#\s+(.+)", content, re.MULTILINE)
    if m:
        return m.group(1).strip()
    return "Technical Solution Proposal"


# ─── Main Export ─────────────────────────────────────────────────────────────

def export(approved_path: Path) -> bool:
    ensure_output_dirs()

    print()
    print(bold(f"EXPORTING: {approved_path.name}"))
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

    # ── Read content ─────────────────────────────────────────────
    md_content = read_file(approved_path)
    env = load_env()

    # ── Extract metadata ─────────────────────────────────────────
    title = _extract_title(md_content)
    client_name = _extract_client_name(md_content)
    export_date = datetime.now().strftime("%d %B %Y")

    print(info(f"  Title:    {title}"))
    print(info(f"  Client:   {client_name}"))
    print(info(f"  Date:     {export_date}"))

    # ── Convert markdown ─────────────────────────────────────────
    print(info("  Converting markdown to HTML..."))
    proposal_html = markdown_to_html(md_content)

    # ── Load CSS ──────────────────────────────────────────────────
    css_content = read_file(CSS_STYLESHEET) if CSS_STYLESHEET.exists() else _default_css()

    # ── Build HTML document ───────────────────────────────────────
    final_html = build_html(proposal_html, env, title, client_name, export_date, css_content)

    # ── Determine output path ─────────────────────────────────────
    version = next_export_version(approved_path)
    export_path = approved_to_export_name(approved_path, version)

    # ── Write output ──────────────────────────────────────────────
    write_file(export_path, final_html)
    print(ok(f"Exported: {export_path}"))
    print(ok(f"Version:  v{version}"))
    print()
    print(bold("NEXT STEP:"))
    print(info(f"  Open in browser: file://{export_path.resolve()}"))
    print(info("  Or convert to PDF using your browser's Print > Save as PDF"))
    print()

    return True


def _default_css() -> str:
    return """
body { font-family: Arial, sans-serif; margin: 40px; color: #222; }
h1 { font-size: 2em; color: #1a3a5c; }
h2 { font-size: 1.4em; color: #1a3a5c; border-bottom: 2px solid #e0e0e0; padding-bottom: 4px; }
h3 { font-size: 1.1em; color: #2c5282; }
table { border-collapse: collapse; width: 100%; margin: 1em 0; }
th, td { border: 1px solid #ccc; padding: 8px 12px; text-align: left; }
th { background: #f0f4f8; font-weight: bold; }
@media print { body { margin: 20px; } }
"""


# ─── Entry Point ──────────────────────────────────────────────────────────────

def main() -> None:
    if len(sys.argv) < 2:
        print(f"Usage: python {Path(__file__).name} <path-to-approved-file>")
        sys.exit(1)

    path = resolve_proposal_path(sys.argv[1])

    if not path.exists():
        print(fail(f"File not found: {path}"))
        sys.exit(1)

    success = export(path)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
