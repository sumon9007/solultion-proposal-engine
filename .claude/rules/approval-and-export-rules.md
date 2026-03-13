# Rule: Approval and Export Rules

These rules govern the quality gates for proposal approval and the export process.

---

## Approval Rules

### Prerequisites for Approval

A proposal CANNOT be approved unless ALL of the following pass:

**Structural checks:**
- All 13 required sections are present (see `proposal-structure-rules.md`)
- Sections appear in the correct order

**Content checks:**
- No placeholder text remains: `[TBD]`, `[INSERT]`, `[YOUR NAME]`, `TODO`, `PLACEHOLDER`, `XXX`
- Client name appears at least once in the Executive Summary
- Pricing section contains at least one line item with a monetary value
- Assumptions section has at least 3 items
- Exclusions section has at least 3 items
- Deliverables section lists at least 3 specific deliverables

**Word count minimums:**
- Executive Summary: ≥ 100 words
- Scope of Work: ≥ 150 words

### Approval Process

1. Validation must pass (all checks above)
2. User must explicitly confirm approval intent
3. File is copied from `output/drafts/` to `output/approved/` with `_approved.md` suffix
4. Original draft is NOT deleted
5. Approval is logged in `output/approved/approval-log.json`
6. A document with AI notes, drafting instructions, or unresolved review comments must not be approved
7. Approved content is immutable; corrections require a new draft and a new approval cycle

### Approval Log Format

Each approval is recorded as a JSON entry:

```json
{
  "approved_at": "2026-03-11T14:30:00",
  "draft_file": "output/drafts/2026-03-11_acme_cloud-migration_draft.md",
  "approved_file": "output/approved/2026-03-11_acme_cloud-migration_approved.md",
  "approved_by": "user",
  "validation_passed": true
}
```

### Approved File Immutability

- Once approved, a file MUST NOT be modified
- If corrections are needed post-approval, create a new draft and go through the full cycle
- Any request to edit an approved file must be explicitly confirmed by the user with a reason

---

## Export Rules

### Prerequisites for Export

- Only `_approved.md` files may be exported
- Draft files may NOT be exported directly (they must be approved first)

### Export Process

1. Read the approved markdown file
2. Apply the HTML template from `assets/templates/proposal-template.html`
3. Apply the stylesheet from `assets/templates/proposal-style.css`
4. Inject company metadata from `.env` (company name, contact details)
5. Save output to `output/exports/[filename]_v[N].html`

### Version Numbering

- First export of a proposal: `_v1.html`
- Each subsequent re-export (after a new approval cycle): increment version number
- Never overwrite an existing export file — always create a new version

### Export File Contents

The exported HTML must include:
- Full proposal content rendered from markdown
- Company branding (name, contact details from `.env`)
- Document metadata in HTML `<head>`: title, date, client name
- Print-friendly styling (the CSS must support `@media print`)
- Page numbers in print view (via CSS)
- Visual treatment aligned with `docs/brand-guidelines.md`

---

## What Claude Should NEVER Do

- Approve a proposal that fails validation
- Export a draft (unapproved) file
- Silently modify content during the approval or export process
- Overwrite an approved file without explicit user confirmation
- Skip the approval log entry
