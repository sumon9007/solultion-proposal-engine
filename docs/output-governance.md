# Output Governance

## Lifecycle Boundaries

- `output/drafts/` contains working documents
- `output/approved/` contains locked approved records
- `output/exports/` contains rendered client-ready outputs
- `output/packages/` contains manifests only

## Naming Rules

Use the shared-stem naming convention:

`YYYY-MM-DD_[client-slug]_[solution-type]_[artifact-type]_[status].md`

Examples:

- `2026-03-13_contoso_m365-implementation_proposal_draft.md`
- `2026-03-13_contoso_m365-implementation_scope_approved.md`

## Overwrite Policy

- Do not overwrite approved artifacts unless the user explicitly confirms it
- Do not overwrite existing exports; create the next version instead
- Prefer a new dated draft over editing historical approved outputs

## Governance Rules

- Keep reusable content in `assets/static/` or `context/reusable/`
- Keep customer-specific outputs out of reusable content folders
- Do not mix drafts and approved outputs in the same directory
- Do not commit generated customer outputs unless policy requires it
