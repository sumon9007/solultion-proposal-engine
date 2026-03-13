# Workspace Context

## Purpose

This workspace is used to generate professional, repeatable solution proposals for multiple customer engagements.

## Canonical Operating Model

1. Capture raw customer material in `input/raw/`
2. Normalize source material into `output/intake/[STEM]_requirements.md`
3. Generate one proposal package with a shared stem
4. Store drafts only in `output/drafts/`
5. Approve only completed, reviewed artifacts into `output/approved/`
6. Publish rendered deliverables into `output/exports/`

## Primary Workflow

The preferred workflow is modular and package-based. A package may contain:

- `proposal`
- `exec-summary`
- `scope`
- `delivery-plan`
- `pricing`

All artifacts share the stem:

`YYYY-MM-DD_[client-slug]_[solution-type]`

## Source-of-Truth Rules

- `input/raw/` is the source area for customer-provided files
- `output/intake/[STEM]_requirements.md` is the normalized intake source for proposal creation
- `assets/static/` holds reusable approved content
- `context/reusable/` holds reusable reference knowledge
- `docs/` holds governance and operating guidance
- `output/` holds generated deliverables only

## Approval Rule

Nothing moves from `output/drafts/` to `output/approved/` until it passes review and validation.

## First-Time Setup

Before running the export script for the first time, configure your company details:

```bash
cp .env.example .env
```

Then edit `.env` and populate:

```
COMPANY_NAME=Your Company Name
COMPANY_EMAIL=proposals@yourcompany.com
COMPANY_PHONE=+44 20 XXXX XXXX
COMPANY_WEBSITE=https://www.yourcompany.com
```

Without `.env`, the HTML export will fall back to generic placeholder values.

## Deprecated Paths

Root-level `drafts/` and `approved/` folders are deprecated and should not be used for new work.
`output/html/` and `output/pdf/` have been removed — all exports go to `output/exports/`.
