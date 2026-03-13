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

## Deprecated Paths

Root-level `drafts/` and `approved/` folders are deprecated and should not be used for new work.
