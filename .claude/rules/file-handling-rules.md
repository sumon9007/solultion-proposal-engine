# Rule: File Handling Rules

These rules govern where all files are created, read, and saved within this project. These rules are absolute.

---

## Output Directory Rules

### Modular Artifact Directories (package-based flow)

| Artifact Type | Draft Directory | Approved Directory |
|--------------|----------------|--------------------|
| Full proposal | `output/drafts/proposals/` | `output/approved/proposals/` |
| Executive summary | `output/drafts/exec-summaries/` | `output/approved/exec-summaries/` |
| Scope of work | `output/drafts/scopes/` | `output/approved/scopes/` |
| Delivery plan | `output/drafts/delivery-plans/` | `output/approved/delivery-plans/` |
| Pricing | `output/drafts/pricing/` | `output/approved/pricing/` |

### Other Output Locations

| Content Type | Directory | Naming Pattern |
|-------------|-----------|----------------|
| HTML exports | `output/exports/` | `[STEM]_proposal_v[N].html` |
| Package manifests | `output/packages/` | `[STEM]_package.json` |
| Approval log | `output/approved/` | `approval-log.json` |

### Intake Locations

| Content Type | Directory |
|-------------|-----------|
| Raw RFP files | `input/raw/rfp/` |
| Raw email captures | `input/raw/email/` |
| Raw Word documents | `input/raw/word/` |
| Raw PDFs | `input/raw/pdf/` |
| Meeting notes | `input/raw/notes/` |
| Reference material | `input/raw/reference/` |
| Temporary extraction notes | `input/working/` |
| Source register | `input/source-register.md` |

### Naming Convention

All artifact files share a common stem:

```
Stem:     YYYY-MM-DD_[client-slug]_[solution-type]
Draft:    [STEM]_[artifact-type]_draft.md
Approved: [STEM]_[artifact-type]_approved.md
```

Example:
```
output/drafts/proposals/2026-03-11_acme_cloud-migration_proposal_draft.md
output/drafts/exec-summaries/2026-03-11_acme_cloud-migration_exec-summary_draft.md
output/drafts/scopes/2026-03-11_acme_cloud-migration_scope_draft.md
output/packages/2026-03-11_acme_cloud-migration_package.json
```

---

## Absolute Rules

1. **NEVER save a proposal or artifact file outside of `output/`** — not in `src/`, not in project root, not in `docs/`
2. **ALWAYS gather customer-provided source files under `input/raw/` first** when source material exists
3. **ALWAYS use `customer_requirements.md` as the normalized intake source** for a new engagement unless the user explicitly provides a different source
4. **NEVER overwrite an `_approved.md` file** without explicit user confirmation and a stated reason
5. **NEVER delete a `_draft.md` file** when approving — keep both draft and approved versions
6. **ALWAYS save artifacts to their typed subdirectory** — do not write directly to `output/drafts/` or `output/approved/` (flat)
7. **ALWAYS use the naming convention** — do not invent alternative naming formats
8. **DO NOT save context snapshots or working notes** as proposal files in `output/`
9. **DO NOT use root-level `drafts/` or `approved/` folders for active workflow output** — they are deprecated

---

## Naming Convention Details

### Date
- Use the date the proposal was first created (not today's date if resuming a draft)
- Format: `YYYY-MM-DD` (ISO 8601)

### Client Slug
- Lowercase, hyphen-separated
- Remove: Ltd, plc, Inc, LLC, Corp (optional but preferred)
- Replace spaces and special characters with hyphens
- Maximum 20 characters

### Solution Type
Use one of these standard values:

```
cloud-migration
cloud-architecture
managed-services
security-assessment
m365-implementation
azure-implementation
consultancy-engagement
data-platform
network-refresh
disaster-recovery
```

If none fits, use a short descriptive lowercase hyphenated phrase.

### Status
- `draft` — active work in progress
- `approved` — approved and locked
- `v1`, `v2` — exported HTML versions

---

## Version Management

When a client requests a revised proposal after approval:

1. Create a new draft with the same base name but today's date: `2026-03-18_acme_cloud-migration_draft.md`
2. Do not modify the original approved file
3. Go through the full validation → approval → export cycle again
4. Export as `v2.html`

---

## Static Assets (read-only at runtime)

Files in `assets/static/` and `assets/templates/` are reference materials. Do not modify them during a proposal session — update them intentionally and separately.

Files in `context/reusable/` are reference context — read them as needed, do not write to them during proposal sessions.
