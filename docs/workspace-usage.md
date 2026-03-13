# Workspace Usage Guide

This guide explains how to use the Solution Proposal Engine day-to-day.

## Prerequisites

1. Claude Code installed and running
2. Python 3.9+ available
3. Dependencies installed: `pip install markdown python-dotenv`
4. `.env` file configured from `.env.example`

---

## Intake First

Before starting a proposal, collect the available customer source material in `input/raw/` and list it in `input/source-register.md`.
Then normalize that material into `customer_requirements.md`. Treat that file as the default intake source for proposal generation. If the user provides fresher details in chat, update the working context accordingly.

---

## Step 0 — Normalize Customer Inputs

Place files into the relevant folders:

```text
input/raw/rfp/
input/raw/email/
input/raw/word/
input/raw/pdf/
input/raw/notes/
input/raw/reference/
```

Then run:

```
/requirements-build
```

Review the generated `customer_requirements.md` before creating a proposal.

---

## Option A — Modular Package (Recommended)

Use this flow for new engagements. It produces five independent artifacts that can be reviewed and approved separately.

### Step 1 — Launch the package intake

```
/proposal-create
```

Claude will read `customer_requirements.md`, ask any missing structured questions, and then generate all artifact files.

### Step 2 — Review each artifact

Artifacts are written to their typed subdirectories:

```
output/drafts/exec-summaries/[STEM]_exec-summary_draft.md
output/drafts/scopes/[STEM]_scope_draft.md
output/drafts/delivery-plans/[STEM]_delivery-plan_draft.md
output/drafts/pricing/[STEM]_pricing_draft.md
output/drafts/proposals/[STEM]_proposal_draft.md
```

### Step 3 — Refine iteratively

```
/improve-draft output/drafts/scopes/2026-03-11_acme_cloud-migration_scope_draft.md
```

Or target a specific section:

```
Improve the Phase 2 section of output/drafts/delivery-plans/2026-03-11_acme_cloud-migration_delivery-plan_draft.md.
The client wants a 4-week mobilisation phase before any build activity.
```

### Step 4 — Validate the package (dry run)

```bash
python scripts/approve_package.py --stem 2026-03-11_acme_cloud-migration --dry-run
```

### Step 5 — Approve the package

```bash
python scripts/approve_package.py --stem 2026-03-11_acme_cloud-migration
```

This validates, then copies all drafts to their approved subdirectories and logs every approval.

---

## Option B — Full Monolithic Proposal

Use this flow for simpler engagements or when a single document is preferred.

### Step 1 — Launch the intake workflow

```
/create-proposal
```

Claude generates a single 13-section proposal.

### Step 2 — Validate

```bash
python scripts/validate_proposal.py output/drafts/proposals/2026-03-11_acme_cloud-migration_proposal_draft.md
```

### Step 3 — Approve

```bash
python scripts/approve_draft.py output/drafts/proposals/2026-03-11_acme_cloud-migration_proposal_draft.md
```

---

## Listing All Proposals

```
/list-proposals
```

Claude will scan all typed subdirectories under `output/drafts/` and `output/approved/` and return a formatted summary.

---

## Exporting to HTML

```bash
python scripts/export_proposal.py output/approved/proposals/2026-03-11_acme_cloud-migration_proposal_approved.md
```

Output is saved to `output/exports/`. Open in any browser or convert to PDF via Print > Save as PDF.

For visual consistency across HTML, PDF, Word, and PowerPoint outputs, follow `docs/brand-guidelines.md`.

---

## Pricing Safety

If pricing has not been confirmed by the client, Claude will insert the commercial safety marker:

```
[PRICING REQUIRED — DO NOT SEND WITHOUT SIGN-OFF]
```

This is the only valid behaviour when pricing is unknown. Claude will not estimate, suggest ranges, or use benchmarks. The marker must be replaced with confirmed figures by the commercial team before the document is sent.

---

## Using Specialised Writing Skills

To switch Claude's writing persona mid-session:

```
Act as a scope-writer and rewrite the In-Scope section for a 12-month managed services contract.
```

Available skills:
- `proposal-architect` — default, full-proposal orchestration
- `technical-writer` — precise, structured technical documentation
- `cloud-solution-writer` — cloud migration and architecture
- `consultancy-scope-writer` — advisory and assessment engagements
- `managed-services-writer` — recurring support contracts
- `proposal-quality-reviewer` — critical review and gap analysis
- `exec-summary-writer` — board-level executive summaries
- `scope-writer` — precise scope of work documents
- `delivery-plan-writer` — phased delivery planning

---

## Working with Static Content

Standard boilerplate lives in `assets/static/`. Update these files to match your company's details:

| File | Contains |
|------|----------|
| `company-profile.md` | About Us section |
| `assumptions.md` | Standard assumptions |
| `exclusions.md` | Standard exclusions |
| `legal-notes.md` | Legal and liability boilerplate |
| `standard-next-steps.md` | Call-to-action and signing process |
| `service-overview-consulting.md` | Consulting service description |
| `service-overview-implementation.md` | Implementation service description |
| `service-overview-managed-services.md` | Managed services description |

---

## Tips

- Always run `/validate-proposal` before sending a draft to a client
- Use `/improve-draft` iteratively — one section at a time gives better results than asking for a full rewrite
- Keep the context window clean: start a new Claude session for each new proposal
- Commit only the scaffold files to Git — never commit completed proposals unless required by policy
