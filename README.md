# Solution Proposal Engine

An AI-assisted workspace for producing repeatable, customer-facing technical proposals with clear draft, review, approval, and export controls.

## Canonical Workflow

This workspace now treats the modular package flow as the default operating model.

1. Capture raw customer material in `input/raw/`
2. Normalize it into `output/intake/[STEM]_requirements.md`
3. Generate draft artifacts into `output/drafts/`
4. Review and refine the drafts
5. Approve artifacts into `output/approved/`
6. Export client-ready deliverables into `output/exports/`

The monolithic single-proposal flow is still supported, but it is secondary.

## Core Files

- `input/` — raw customer intake area for RFPs, emails, Word files, PDFs, and notes
- `output/intake/[STEM]_requirements.md` — primary normalized intake file for each engagement
- `workspace-context.md` — concise operating model for the workspace
- `CLAUDE.md` — root instructions for AI-assisted work in this repository
- `docs/requirement-capture-flow.md` — step-by-step intake normalization guide
- `docs/proposal-lifecycle.md` — end-to-end lifecycle guidance
- `docs/review-checklist.md` — human and AI review gate
- `docs/approval-instructions.md` — approval and publishing rules
- `docs/brand-guidelines.md` — brand guidance for Word, PowerPoint, PDF, and HTML outputs

## Project Structure

```text
solution-proposal-engine/
├── .claude/
├── assets/
│   ├── static/
│   └── templates/
├── input/
│   ├── raw/
│   ├── working/
│   ├── normalized/
│   └── archive/
├── context/
│   ├── customers/
│   ├── opportunities/
│   └── reusable/
├── docs/
├── output/
│   ├── intake/
│   ├── drafts/
│   ├── approved/
│   ├── exports/
│   └── packages/
├── scripts/
└── workspace-context.md
```

## Quick Start

1. Place customer source material into `input/raw/`
2. Update `input/source-register.md`
3. Run `/requirements-build`
4. Review `output/intake/[STEM]_requirements.md`
5. Run `/proposal-create`
6. Review outputs in `output/drafts/`
7. Validate and approve
8. Export the approved proposal

See `docs/requirement-capture-flow.md` for the intake process and `docs/workspace-usage.md` for the full operating steps.

## GitHub Pages

This repository includes a GitHub Actions workflow that publishes the `output/` directory to GitHub Pages.

How it works:

1. On every push to `main` that changes `output/` or the Pages workflow, GitHub Actions runs `.github/workflows/publish-output-pages.yml`
2. The workflow generates `output/index.html` so the published site has a browsable landing page
3. The workflow deploys the full `output/` directory to GitHub Pages

To enable it in GitHub:

1. Open the repository settings
2. Go to `Pages`
3. Set the source to `GitHub Actions`
4. Push changes to `main` or run the workflow manually from the `Actions` tab

The published site will expose the current contents of:

- `output/intake/`
- `output/drafts/`
- `output/approved/`
- `output/exports/`
- `output/packages/`

## Environment

Copy `.env.example` to `.env` and configure your company identity and export settings.

## Dependencies

```bash
pip install markdown python-dotenv
```
