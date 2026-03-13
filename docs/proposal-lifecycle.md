# Proposal Lifecycle

This document describes the end-to-end lifecycle of a technical solution proposal within this workspace.

## Source of Truth

- `input/raw/` stores the original customer-provided materials
- `output/intake/[STEM]_requirements.md` is the normalized intake artifact for a new engagement
- `output/drafts/` contains work in progress only
- `output/approved/` contains approved and locked artifacts only
- `output/exports/` contains client-ready rendered deliverables
- `output/packages/` stores package manifests and shared artifact traceability

## Lifecycle A — Full Monolithic Proposal

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   INTAKE    │───▶│   DRAFT     │───▶│  VALIDATE   │───▶│  APPROVE    │───▶│   EXPORT    │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
  /create-proposal  Claude writes     scripts/            scripts/            scripts/
  Capture context   to proposals/     validate_           approve_            export_
                    subdir            proposal.py         draft.py            proposal.py
```

## Lifecycle B — Modular Package (recommended)

```
┌─────────────┐    ┌──────────────────────────────┐    ┌─────────────┐    ┌─────────────┐
│   INTAKE    │───▶│   GENERATE PACKAGE           │───▶│  VALIDATE   │───▶│  APPROVE    │
└─────────────┘    └──────────────────────────────┘    └─────────────┘    └─────────────┘
  /create-package   scripts/generate_package.py         scripts/            scripts/
  Capture context   Claude writes each artifact          approve_package     approve_package
                    to typed subdirectories              --dry-run           (live run)

  Artifacts produced per package:
  ├── output/drafts/proposals/        [STEM]_proposal_draft.md
  ├── output/drafts/exec-summaries/   [STEM]_exec-summary_draft.md
  ├── output/drafts/scopes/           [STEM]_scope_draft.md
  ├── output/drafts/delivery-plans/   [STEM]_delivery-plan_draft.md
  ├── output/drafts/pricing/          [STEM]_pricing_draft.md
  └── output/packages/               [STEM]_package.json  ← manifest
```

---

## Stage 1: Raw Intake Collection

**Command:** `/requirements-build`

**What happens:**
1. Customer source files are stored in `input/raw/`
2. The source list is maintained in `input/source-register.md`
3. Claude reviews the relevant source material
4. Claude normalizes the intake into `output/intake/[STEM]_requirements.md`

**Output:** A reviewed `output/intake/[STEM]_requirements.md` file ready for proposal drafting

---

## Stage 2: Intake (Customer Context Capture)

**Command:** `/proposal-create` or `/create-package`

**What happens:**
1. Claude reads `output/intake/[STEM]_requirements.md` first
2. Claude asks structured follow-up questions using the `capture-customer-context` prompt if the intake file is incomplete
3. User provides or confirms: client name, industry, pain points, solution scope, budget range, timeline, stakeholders
4. Claude begins drafting once the intake is complete

**Output:** A populated package manifest and draft artifacts in `output/drafts/`

**Files used:**
- `.claude/prompts/capture-customer-context.md`
- `.claude/skills/proposal-architect.md`

---

## Stage 3: Draft Generation

**Command:** `/proposal-create` or `/create-package`

**What happens:**
1. Claude reads customer context and relevant static assets
2. Selects appropriate skill persona (cloud, managed services, consultancy, or implementation)
3. Drafts all 13 required sections
4. Inserts boilerplate from `assets/static/` for assumptions, exclusions, legal notes, next steps, and company profile

**Output:** Complete draft markdown files in typed subdirectories

**Naming:** `YYYY-MM-DD_[client-slug]_[solution-type]_draft.md`

**Files used:**
- `.claude/prompts/draft-proposal-from-context.md`
- `assets/static/*.md`
- `context/reusable/proposal-writing-guidelines.md`

---

## Stage 4: Validation

**Command:** `python scripts/validate_proposal.py <path-to-draft>`

**What happens:**
1. Script checks that all 13 required section headings are present
2. Flags any remaining placeholder text (`[TBD]`, `[INSERT]`, `TODO`)
3. Verifies minimum word count per section
4. Checks that pricing section contains at least one line item
5. Returns PASS or FAIL with a detailed report

**Output:** Validation report printed to stdout

---

## Stage 5: Review and Refinement

**Command:** `/proposal-review <path>` or `/improve-draft <path>`

**What happens:**
1. Claude reads the existing draft
2. Applies the `proposal-review-checklist` prompt
3. Identifies weak sections, vague claims, or missing specifics
4. Suggests targeted rewrites section by section
5. User accepts or rejects each suggestion

**Iteration:** Repeat validation + refinement until PASS

**Files used:**
- `.claude/prompts/proposal-review-checklist.md`
- `.claude/skills/proposal-quality-reviewer.md`
- `.claude/prompts/refine-executive-summary.md`

---

## Stage 6: Approval

**Command:** `/proposal-approve`, `/approve-package`, or `python scripts/approve_draft.py <path-to-draft>`

**What happens:**
1. Script re-runs validation — rejects if FAIL
2. Copies file from `output/drafts/` to `output/approved/`
3. Renames file: `_draft.md` → `_approved.md`
4. Writes an approval record to `output/approved/approval-log.json`
5. Original draft is retained (not deleted)

**Output:** Approved file in `output/approved/`

---

## Stage 7: Export

**Command:** `/proposal-export` or one of the export scripts below

| Format | Command | Dependency |
|--------|---------|------------|
| HTML | `python scripts/export_proposal.py <approved.md>` | `pip install markdown` |
| PDF | `python scripts/export_pdf.py <approved.md>` | `pip install weasyprint` |
| Word | `python scripts/export_word.py <approved.md>` | `pip install python-docx` |

**What happens (all formats):**
1. Script guards against draft files — only `_approved.md` files are accepted
2. Reads company metadata and brand settings from `.env`
3. Injects brand colours (CSS variable overrides) and logo if `LOGO_PATH` is set
4. Saves versioned output to `output/exports/` (auto-increments `v1`, `v2`, etc.)

**Output examples:**
```
output/exports/[STEM]_proposal_v1.html
output/exports/[STEM]_proposal_v1.pdf
output/exports/[STEM]_proposal_v1.docx
```

---

## Status Summary

| Status | Location | Filename Pattern |
|--------|----------|-----------------|
| Draft (proposal) | `output/drafts/proposals/` | `[STEM]_proposal_draft.md` |
| Draft (exec-summary) | `output/drafts/exec-summaries/` | `[STEM]_exec-summary_draft.md` |
| Draft (scope) | `output/drafts/scopes/` | `[STEM]_scope_draft.md` |
| Draft (delivery-plan) | `output/drafts/delivery-plans/` | `[STEM]_delivery-plan_draft.md` |
| Draft (pricing) | `output/drafts/pricing/` | `[STEM]_pricing_draft.md` |
| Package manifest | `output/packages/` | `[STEM]_package.json` |
| Approved | `output/approved/[type]/` | `[STEM]_[type]_approved.md` |
| Exported (HTML) | `output/exports/` | `[STEM]_proposal_v[N].html` |
| Exported (PDF) | `output/exports/` | `[STEM]_proposal_v[N].pdf` |
| Exported (Word) | `output/exports/` | `[STEM]_proposal_v[N].docx` |
