# Solution Proposal Engine — Memory

## Architecture

**Modular Package Factory** — the primary workflow as of 2026-03-11.

A "package" is a shared-stem group of 5 independent artifact files:

| Artifact | Draft dir | Approved dir |
|----------|-----------|--------------|
| proposal | output/drafts/proposals/ | output/approved/proposals/ |
| exec-summary | output/drafts/exec-summaries/ | output/approved/exec-summaries/ |
| scope | output/drafts/scopes/ | output/approved/scopes/ |
| delivery-plan | output/drafts/delivery-plans/ | output/approved/delivery-plans/ |
| pricing | output/drafts/pricing/ | output/approved/pricing/ |

Stem format: `YYYY-MM-DD_[client-slug]_[solution-type]`
Artifact filename: `[STEM]_[artifact-type]_draft.md`
Package manifest: `output/packages/[STEM]_package.json`

## Key Constants (helpers.py)

- `ARTIFACT_TYPES` — ordered list of 5 types
- `ARTIFACT_DRAFT_DIRS` / `ARTIFACT_APPROVED_DIRS` — dicts keyed by type
- `COMMERCIAL_SAFETY_MARKER` — `[PRICING REQUIRED — DO NOT SEND WITHOUT SIGN-OFF]`
- `PACKAGES_DIR` — `output/packages/`
- `DRAFTS_DIR` / `APPROVED_DIR` — point to `proposals/` subdir (backward compat)

## Scripts

| Script | Purpose |
|--------|---------|
| generate_package.py | Creates manifest + dirs. Claude writes content. |
| approve_package.py | Validates + approves all artifacts atomically |
| validate_artifact.py | Per-type validator (exec-summary/scope/delivery-plan/pricing/proposal) |
| validate_proposal.py | Full 13-section validator (unchanged) |
| approve_draft.py | Single-draft approver (unchanged) |

## Commercial Safety Rule

- Claude NEVER invents pricing figures
- If pricing unknown → insert `COMMERCIAL_SAFETY_MARKER` exactly
- Validator: safety marker = PASS with warning; no marker AND no monetary values = FAIL
- Rule file: `.claude/rules/commercial-safety-rules.md`

## Commands

- `/create-package` — modular package intake + generation
- `/approve-package` — package approval workflow
- `/create-proposal` — monolithic 13-section proposal (still supported)

## Skills

- `exec-summary-writer`, `scope-writer`, `delivery-plan-writer` — new modular skills
- Original skills unchanged