# File Naming Convention

All proposal files in this project follow a strict naming convention for consistency and discoverability.

## Shared Stem

All artifacts in a package share a common stem:

```
YYYY-MM-DD_[client-slug]_[solution-type]
```

### Stem Components

| Component | Description | Example |
|-----------|-------------|---------|
| `YYYY-MM-DD` | ISO date — package creation date | `2026-03-11` |
| `client-slug` | Client name, lowercase, hyphen-separated, max 20 chars | `acme-corp` |
| `solution-type` | Standard solution type identifier | `cloud-migration` |

### Full Artifact Filename

```
[STEM]_[artifact-type]_[status].[ext]
```

| Component | Values |
|-----------|--------|
| `artifact-type` | `requirements`, `proposal`, `exec-summary`, `scope`, `delivery-plan`, `pricing` |
| `status` | `draft`, `approved` |
| `ext` | `.md` (artifacts), `.html` (exports), `.json` (manifests) |

For the intake artifact, use this simplified pattern:

```
[STEM]_requirements.md
```

This file lives in `output/intake/` and acts as the normalized intake source before proposal drafting begins.

---

## Solution Type Values

Use one of these standard values for `solution-type`:

| Value | Use When |
|-------|----------|
| `cloud-migration` | Cloud migration or lift-and-shift projects |
| `cloud-architecture` | Cloud design and architecture engagements |
| `managed-services` | Ongoing support and operations contracts |
| `security-assessment` | Security audit or assessment proposals |
| `m365-implementation` | Microsoft 365 deployment or migration |
| `azure-implementation` | Azure infrastructure deployment |
| `consultancy-engagement` | Advisory or discovery engagements |
| `data-platform` | Data, analytics, or BI platform proposals |
| `network-refresh` | Network infrastructure projects |
| `disaster-recovery` | DR and business continuity proposals |

If none of these fit, use a short descriptive lowercase hyphenated phrase.

---

## Status Values

| Value | Description |
|-------|-------------|
| `draft` | Active work in progress — in typed subdirectory under `output/drafts/` |
| `approved` | Approved and locked — in typed subdirectory under `output/approved/` |
| `v1`, `v2` | Exported HTML versions — in `output/exports/` |

---

## Examples

```
# Stem for Acme Corp cloud migration package (11 March 2026)
2026-03-11_acme_cloud-migration

# Intake artifact
output/intake/2026-03-11_acme_cloud-migration_requirements.md

# Draft artifacts
output/drafts/proposals/2026-03-11_acme_cloud-migration_proposal_draft.md
output/drafts/exec-summaries/2026-03-11_acme_cloud-migration_exec-summary_draft.md
output/drafts/scopes/2026-03-11_acme_cloud-migration_scope_draft.md
output/drafts/delivery-plans/2026-03-11_acme_cloud-migration_delivery-plan_draft.md
output/drafts/pricing/2026-03-11_acme_cloud-migration_pricing_draft.md

# Package manifest
output/packages/2026-03-11_acme_cloud-migration_package.json

# Approved artifacts
output/approved/proposals/2026-03-11_acme_cloud-migration_proposal_approved.md
output/approved/exec-summaries/2026-03-11_acme_cloud-migration_exec-summary_approved.md

# HTML export of the full proposal
output/exports/2026-03-11_acme_cloud-migration_proposal_v1.html
```

---

## Client Slug Rules

- Lowercase only
- Replace spaces and special characters with hyphens
- Remove common suffixes: Ltd, plc, Inc, LLC, Corp (optional but preferred for brevity)
- Maximum 20 characters

| Client Name | Slug |
|-------------|------|
| Acme Corporation | `acme` |
| National Life Company | `national-life` |
| Northgate Pharma Ltd | `northgate-pharma` |
| H&M Logistics | `hm-logistics` |
| UK Department for Transport | `uk-dft` |
