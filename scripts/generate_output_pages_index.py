#!/usr/bin/env python3
"""
Build a curated GitHub Pages site from client-ready output artifacts.
"""

from __future__ import annotations

import shutil
from datetime import UTC, datetime
from html import escape
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = PROJECT_ROOT / "output"
PUBLISH_DIR = PROJECT_ROOT / ".pages-site"
INDEX_PATH = PUBLISH_DIR / "index.html"

PUBLISHED_SECTIONS = [
    ("intake", "Requirements Intake", "Normalized engagement inputs prepared for proposal drafting."),
    ("drafts", "Draft Artifacts", "Active proposal work in progress across all artifact types."),
    ("approved", "Approved Artifacts", "Locked proposal artifacts ready for audit, review, or publishing."),
    ("exports", "Published Exports", "Rendered HTML proposals and other distributed outputs."),
    ("packages", "Package Manifests", "Package metadata and traceability records for multi-artifact engagements."),
]


def reset_publish_dir() -> None:
    if PUBLISH_DIR.exists():
        shutil.rmtree(PUBLISH_DIR)
    PUBLISH_DIR.mkdir(parents=True, exist_ok=True)


def copy_tree(section_name: str) -> list[Path]:
    source = OUTPUT_DIR / section_name
    destination = PUBLISH_DIR / section_name
    files: list[Path] = []

    if not source.exists():
        return files

    for path in sorted(source.rglob("*")):
        if not path.is_file() or path.name == ".gitkeep":
            continue
        rel = path.relative_to(source)
        target = destination / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, target)
        files.append(target)
    return files


def extract_label(path: Path) -> str:
    name = path.stem
    for suffix in ("_approved", "_draft", "_proposal", "_requirements"):
        if name.endswith(suffix):
            name = name[: -len(suffix)]
    return name.replace("_", " ")


def extract_meta(path: Path) -> tuple[str, str]:
    parts = path.stem.split("_")
    if len(parts) >= 3:
        client = parts[1].replace("-", " ").title()
        solution_type = parts[2].replace("-", " ").title()
        return client, solution_type
    return "Unknown Client", "General"


def card_html(base: Path, path: Path) -> str:
    rel_path = path.relative_to(base).as_posix()
    client, solution_type = extract_meta(path)
    label = escape(extract_label(path))
    modified = datetime.fromtimestamp(path.stat().st_mtime, UTC).strftime("%Y-%m-%d")
    ext = path.suffix.replace(".", "").upper() or "FILE"
    return (
        "<article class=\"artifact-card\">"
        f"<p class=\"artifact-kicker\">{escape(solution_type)} · {escape(ext)}</p>"
        f"<h3>{label}</h3>"
        f"<p class=\"artifact-client\">{escape(client)}</p>"
        "<div class=\"artifact-meta\">"
        f"<span>Updated {modified}</span>"
        f"<a href=\"{rel_path}\">Open</a>"
        "</div>"
        "</article>"
    )


def build_section(section_name: str, title: str, description: str, files: list[Path]) -> str:
    if files:
        cards = "".join(card_html(PUBLISH_DIR, path) for path in files)
    else:
        cards = "<p class=\"empty-state\">Nothing published in this section yet.</p>"

    return (
        "<section class=\"library-section\">"
        f"<div class=\"section-heading\"><h2>{escape(title)}</h2><p>{escape(description)}</p></div>"
        f"<div class=\"artifact-grid\">{cards}</div>"
        "</section>"
    )


def build_index(section_files: dict[str, list[Path]]) -> None:
    generated_at = datetime.now(UTC).strftime("%Y-%m-%d %H:%M UTC")
    total_files = sum(len(paths) for paths in section_files.values())
    has_sensitive_workflow_content = bool(section_files.get("intake") or section_files.get("drafts"))
    warning_banner = ""
    hero_warning_badge = ""
    if has_sensitive_workflow_content:
        hero_warning_badge = (
            "<span class=\"hero-alert\">Internal content live: intake or draft artifacts are included</span>"
        )
        warning_banner = (
            "<section class=\"warning-banner\">"
            "<strong>Internal-only warning:</strong> "
            "This published view currently includes intake or draft content. "
            "Do not use this Pages site for public or client-facing sharing unless those sections are removed from the deployment."
            "</section>"
        )
    sections = "".join(
        build_section(name, title, description, section_files[name])
        for name, title, description in PUBLISHED_SECTIONS
    )

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="Client-ready proposal library published from the Solution Proposal Engine workspace.">
    <title>Proposal Operations Hub</title>
  <style>
    :root {{
      color-scheme: light;
      --bg: #edf3f7;
      --ink: #112033;
      --muted: #5b6b7d;
      --line: #d4dde7;
      --panel: rgba(255, 255, 255, 0.92);
      --navy: #0f1e33;
      --blue: #0b5fff;
      --teal: #0f9d8a;
      --soft: #eaf2ff;
      --shadow: 0 20px 55px rgba(15, 30, 51, 0.08);
    }}
    * {{
      box-sizing: border-box;
    }}
    body {{
      margin: 0;
      font-family: Aptos, "Segoe UI", sans-serif;
      color: var(--ink);
      background:
        radial-gradient(circle at top right, rgba(11, 95, 255, 0.10), transparent 24%),
        radial-gradient(circle at top left, rgba(15, 157, 138, 0.10), transparent 20%),
        linear-gradient(180deg, #f8fbff 0%, var(--bg) 100%);
    }}
    .shell {{
      max-width: 1180px;
      margin: 0 auto;
      padding: 32px 20px 72px;
    }}
    .hero {{
      padding: 34px;
      border: 1px solid rgba(255, 255, 255, 0.5);
      border-radius: 28px;
      background:
        linear-gradient(135deg, rgba(15, 30, 51, 0.96), rgba(11, 95, 255, 0.90)),
        linear-gradient(180deg, #12284a 0%, #0b5fff 100%);
      color: white;
      box-shadow: var(--shadow);
      overflow: hidden;
      position: relative;
    }}
    .hero::after {{
      content: "";
      position: absolute;
      inset: auto -70px -90px auto;
      width: 250px;
      height: 250px;
      border-radius: 50%;
      background: rgba(255, 255, 255, 0.08);
    }}
    .eyebrow {{
      margin: 0 0 12px;
      font-size: 0.8rem;
      letter-spacing: 0.18em;
      text-transform: uppercase;
      opacity: 0.85;
    }}
    h1 {{
      margin: 0;
      max-width: 12ch;
      font-size: clamp(2.1rem, 5vw, 4.1rem);
      line-height: 0.96;
      letter-spacing: -0.03em;
    }}
    .hero-copy {{
      margin: 16px 0 0;
      max-width: 64ch;
      color: rgba(255, 255, 255, 0.85);
      line-height: 1.6;
    }}
    .hero-meta {{
      display: flex;
      flex-wrap: wrap;
      gap: 12px;
      margin-top: 22px;
    }}
    .hero-meta span {{
      padding: 10px 14px;
      border-radius: 999px;
      background: rgba(255, 255, 255, 0.12);
      backdrop-filter: blur(8px);
      font-size: 0.92rem;
    }}
    .hero-alert {{
      display: inline-flex;
      align-items: center;
      margin-top: 18px;
      padding: 9px 14px;
      border-radius: 999px;
      background: linear-gradient(180deg, rgba(255, 209, 102, 0.25), rgba(255, 166, 43, 0.28));
      border: 1px solid rgba(255, 199, 82, 0.32);
      color: #fff3d2;
      font-size: 0.84rem;
      font-weight: 700;
      letter-spacing: 0.04em;
      text-transform: uppercase;
    }}
    .section-stack {{
      display: grid;
      gap: 22px;
      margin-top: 26px;
    }}
    .warning-banner {{
      margin-top: 20px;
      padding: 16px 18px;
      border: 1px solid rgba(193, 71, 31, 0.25);
      border-radius: 18px;
      background: linear-gradient(180deg, #fff4e8 0%, #ffeedc 100%);
      color: #7f3117;
      box-shadow: 0 10px 28px rgba(127, 49, 23, 0.08);
      line-height: 1.55;
    }}
    .warning-banner strong {{
      color: #5e210d;
    }}
    .library-section {{
      padding: 24px;
      border: 1px solid var(--line);
      border-radius: 24px;
      background: var(--panel);
      box-shadow: var(--shadow);
    }}
    .section-heading {{
      display: flex;
      justify-content: space-between;
      gap: 20px;
      align-items: end;
      margin-bottom: 18px;
    }}
    .section-heading h2 {{
      margin: 0;
      font-size: 1.35rem;
    }}
    .section-heading p {{
      margin: 0;
      max-width: 44ch;
      color: var(--muted);
      line-height: 1.5;
    }}
    .artifact-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
      gap: 16px;
    }}
    .artifact-card {{
      padding: 18px;
      border: 1px solid var(--line);
      border-radius: 18px;
      background: white;
      min-height: 190px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }}
    .artifact-kicker {{
      margin: 0 0 10px;
      color: var(--teal);
      font-size: 0.78rem;
      font-weight: 700;
      letter-spacing: 0.06em;
      text-transform: uppercase;
    }}
    .artifact-card h3 {{
      margin: 0;
      font-size: 1.12rem;
      line-height: 1.3;
    }}
    .artifact-client {{
      margin: 10px 0 0;
      color: var(--muted);
      line-height: 1.5;
    }}
    .artifact-meta {{
      display: flex;
      justify-content: space-between;
      gap: 14px;
      align-items: center;
      margin-top: 20px;
      font-size: 0.92rem;
      color: var(--muted);
    }}
    .artifact-meta a {{
      color: var(--blue);
      font-weight: 700;
      text-decoration: none;
    }}
    .artifact-meta a:hover {{
      text-decoration: underline;
    }}
    .empty-state {{
      margin: 0;
      padding: 16px 18px;
      border-radius: 16px;
      background: var(--soft);
      color: var(--muted);
    }}
    @media (max-width: 780px) {{
      .hero {{
        padding: 26px;
      }}
      .section-heading {{
        display: block;
      }}
      .section-heading p {{
        margin-top: 8px;
      }}
      .artifact-meta {{
        display: block;
      }}
      .artifact-meta a {{
        display: inline-block;
        margin-top: 8px;
      }}
    }}
  </style>
</head>
<body>
  <main class="shell">
    <section class="hero">
      <p class="eyebrow">Solution Proposal Engine</p>
      <h1>Internal Proposal Operations Hub</h1>
      <p class="hero-copy">This Pages site is designed as an internal workspace view across the full proposal lifecycle, including intake, drafts, approvals, exports, and package traceability. It is intended for internal operations only.</p>
      {hero_warning_badge}
      <div class="hero-meta">
        <span>{total_files} published file(s)</span>
        <span>Generated {generated_at}</span>
      </div>
    </section>
    {warning_banner}
    <div class="section-stack">
      {sections}
    </div>
  </main>
</body>
</html>
"""

    INDEX_PATH.write_text(html, encoding="utf-8")


def main() -> None:
    reset_publish_dir()
    section_files = {name: copy_tree(name) for name, _, _ in PUBLISHED_SECTIONS}
    build_index(section_files)
    (PUBLISH_DIR / ".nojekyll").write_text("", encoding="utf-8")


if __name__ == "__main__":
    main()
