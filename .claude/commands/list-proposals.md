List all proposals currently in the workspace.

## Instructions

1. List all `.md` files in `output/drafts/` — these are active drafts
2. List all `.md` files in `output/approved/` — these are approved proposals
3. List all `.html` files in `output/exports/` — these are exported versions

## Output Format

Present the results as a formatted table:

```
PROPOSALS
═══════════════════════════════════════════════════════════════

DRAFTS (output/drafts/)
──────────────────────────────────────────────────────────────
Date         Client              Solution Type        File
──────────   ──────────────────  ──────────────────   ─────────────────────────────────────────
2026-03-11   Acme Corp           Cloud Migration      2026-03-11_acme-corp_cloud-migration_draft.md
2026-03-09   Northgate Pharma    Managed Services     2026-03-09_northgate-pharma_managed-services_draft.md

APPROVED (output/approved/)
──────────────────────────────────────────────────────────────
Date         Client              Solution Type        File
──────────   ──────────────────  ──────────────────   ─────────────────────────────────────────────────────
2026-03-07   Contoso Ltd         M365 Migration       2026-03-07_contoso_m365-implementation_approved.md

EXPORTS (output/exports/)
──────────────────────────────────────────────────────────────
Date         Client              Solution Type        Version   File
──────────   ──────────────────  ──────────────────   ───────   ──────────────────────────────────────────────────────
2026-03-07   Contoso Ltd         M365 Migration       v1        2026-03-07_contoso_m365-implementation_v1.html

═══════════════════════════════════════════════════════════════
TOTALS: 2 drafts | 1 approved | 1 exported
```

If any folder is empty, display: "(none)"

After listing, offer the user options:
- "Would you like to open, improve, validate, or approve any of these proposals?"
