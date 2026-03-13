#!/usr/bin/env python3
"""
Build a simple index.html for publishing the output/ directory via GitHub Pages.
"""

from __future__ import annotations

from datetime import UTC, datetime
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = PROJECT_ROOT / "output"
INDEX_PATH = OUTPUT_DIR / "index.html"


SECTIONS = [
    ("intake", "Requirements Intake"),
    ("drafts", "Draft Artifacts"),
    ("approved", "Approved Artifacts"),
    ("exports", "Published Exports"),
    ("packages", "Package Manifests"),
]


def iter_files(section_dir: Path) -> list[Path]:
    return sorted(
        [
            path
            for path in section_dir.rglob("*")
            if path.is_file()
            and path.name != ".gitkeep"
            and path.name != "index.html"
        ]
    )


def file_list_html(base_dir: Path, files: list[Path]) -> str:
    if not files:
        return "<p class=\"empty\">No files published in this section yet.</p>"

    items = []
    for path in files:
        rel_path = path.relative_to(base_dir).as_posix()
        label = rel_path
        modified = datetime.fromtimestamp(path.stat().st_mtime).strftime("%Y-%m-%d %H:%M")
        items.append(
            "<li>"
            f"<a href=\"{rel_path}\">{label}</a>"
            f"<span>{modified}</span>"
            "</li>"
        )
    return "<ul>" + "".join(items) + "</ul>"


def build_section(section_key: str, title: str) -> str:
    section_dir = OUTPUT_DIR / section_key
    files = iter_files(section_dir) if section_dir.exists() else []
    return (
        "<section>"
        f"<h2>{title}</h2>"
        f"{file_list_html(OUTPUT_DIR, files)}"
        "</section>"
    )


def main() -> None:
    generated_at = datetime.now(UTC).strftime("%Y-%m-%d %H:%M UTC")
    sections = "".join(build_section(key, title) for key, title in SECTIONS)

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Solution Proposal Engine Output</title>
  <style>
    :root {{
      color-scheme: light;
      --bg: #f4f7fb;
      --panel: #ffffff;
      --text: #122033;
      --muted: #5a6b82;
      --line: #d5e0ed;
      --accent: #0b5fff;
      --accent-soft: #eaf1ff;
    }}
    * {{
      box-sizing: border-box;
    }}
    body {{
      margin: 0;
      font-family: Aptos, "Segoe UI", sans-serif;
      background: linear-gradient(180deg, #eef4ff 0%, var(--bg) 100%);
      color: var(--text);
    }}
    main {{
      max-width: 980px;
      margin: 0 auto;
      padding: 48px 20px 72px;
    }}
    header {{
      margin-bottom: 28px;
    }}
    h1 {{
      margin: 0 0 8px;
      font-size: 2.2rem;
    }}
    .lead {{
      margin: 0;
      color: var(--muted);
      max-width: 64ch;
      line-height: 1.5;
    }}
    .stamp {{
      margin-top: 12px;
      font-size: 0.95rem;
      color: var(--muted);
    }}
    .grid {{
      display: grid;
      gap: 18px;
    }}
    section {{
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 18px;
      padding: 20px;
      box-shadow: 0 12px 32px rgba(16, 31, 56, 0.06);
    }}
    h2 {{
      margin: 0 0 14px;
      font-size: 1.1rem;
    }}
    ul {{
      list-style: none;
      padding: 0;
      margin: 0;
    }}
    li {{
      display: flex;
      justify-content: space-between;
      gap: 16px;
      padding: 10px 0;
      border-top: 1px solid var(--line);
    }}
    li:first-child {{
      border-top: 0;
      padding-top: 0;
    }}
    a {{
      color: var(--accent);
      text-decoration: none;
      overflow-wrap: anywhere;
    }}
    a:hover {{
      text-decoration: underline;
    }}
    span {{
      color: var(--muted);
      font-size: 0.9rem;
      white-space: nowrap;
    }}
    .empty {{
      margin: 0;
      padding: 12px 14px;
      border-radius: 12px;
      background: var(--accent-soft);
      color: var(--muted);
    }}
    @media (max-width: 720px) {{
      li {{
        display: block;
      }}
      span {{
        display: block;
        margin-top: 6px;
      }}
    }}
  </style>
</head>
<body>
  <main>
    <header>
      <h1>Solution Proposal Engine Output</h1>
      <p class="lead">This site publishes the current contents of the workspace output directory so intake files, artifacts, exports, and package manifests are easy to browse from GitHub Pages.</p>
      <p class="stamp">Generated {generated_at}</p>
    </header>
    <div class="grid">
      {sections}
    </div>
  </main>
</body>
</html>
"""

    INDEX_PATH.write_text(html, encoding="utf-8")


if __name__ == "__main__":
    main()
