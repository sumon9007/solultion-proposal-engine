# Solution Proposal Engine

An AI-assisted workspace for producing repeatable, customer-facing technical proposals with clear draft, review, approval, and export controls.

## Canonical Workflow

This workspace now treats the modular package flow as the default operating model.

1. Capture raw customer material in `input/raw/`
2. Normalize it into `customer_requirements.md`
3. Generate draft artifacts into `output/drafts/`
4. Review and refine the drafts
5. Approve artifacts into `output/approved/`
6. Export client-ready deliverables into `output/exports/`

The monolithic single-proposal flow is still supported, but it is secondary.

## Core Files

- `input/` — raw customer intake area for RFPs, emails, Word files, PDFs, and notes
- `customer_requirements.md` — primary intake file for each engagement
- `workspace-context.md` — concise operating model for the workspace
- `CLAUDE.md` — root instructions for AI-assisted work in this repository
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
│   ├── drafts/
│   ├── approved/
│   ├── exports/
│   └── packages/
├── scripts/
├── customer_requirements.md
└── workspace-context.md
```

## Quick Start

1. Place customer source material into `input/raw/`
2. Update `input/source-register.md`
3. Run `/requirements-build`
4. Review `customer_requirements.md`
5. Run `/proposal-create`
6. Review outputs in `output/drafts/`
7. Validate and approve
8. Export the approved proposal

See `docs/workspace-usage.md` for the operating steps.

## Environment

Copy `.env.example` to `.env` and configure your company identity and export settings.

## Dependencies

```bash
pip install markdown python-dotenv
```
