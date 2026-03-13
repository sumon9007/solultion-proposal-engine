You are creating a modular proposal package. A package is a set of individual artifact files that share a common stem, enabling each document to be drafted, reviewed, and approved independently.

Follow these steps precisely.

---

## Step 1 — Intake

Ask the user the following questions. You may ask them all at once if the user prefers a quick intake, or one at a time.

1. **Client name** — Full name of the client organisation
2. **Industry** — What sector are they in?
3. **Problem statement** — What specific challenge are they trying to solve?
4. **Solution type** — What kind of engagement is this? (cloud-migration / cloud-architecture / managed-services / security-assessment / m365-implementation / azure-implementation / consultancy-engagement / data-platform / network-refresh / disaster-recovery)
5. **Scope summary** — How many users, systems, or sites are in scope?
6. **Target outcomes** — What does success look like in 6–12 months?
7. **Timeline** — Is there a target start date or hard deadline?
8. **Budget / Pricing** — Has pricing been confirmed, or is this TBD?
9. **Which artifacts?** — All five (proposal, exec-summary, scope, delivery-plan, pricing), or a subset?

---

## Step 2 — Confirm and Build the Stem

From the answers above:

1. Build the client slug (lowercase, hyphenated, max 20 chars, strip Ltd/plc/Inc)
2. Confirm the solution type from the standard list
3. Set the date to today: `YYYY-MM-DD`
4. Compose the shared stem: `YYYY-MM-DD_[client-slug]_[solution-type]`

Show the user the stem and confirm: "I will use this stem for all artifacts: `[STEM]`. Is that correct?"

---

## Step 3 — Initialise the Package

Run:

```
python scripts/generate_package.py \
    --stem [STEM] \
    --artifacts [comma-separated or "all"] \
    --client "[Client Full Name]" \
    --solution-type [solution-type]
```

This creates the package manifest and all necessary output directories.

---

## Step 4 — Select Skill Persona

Based on solution type, adopt the appropriate writing persona:

| Solution Type | Skill |
|--------------|-------|
| cloud-migration, cloud-architecture, azure-implementation | cloud-solution-writer |
| consultancy-engagement, security-assessment | consultancy-scope-writer |
| managed-services | managed-services-writer |
| m365-implementation, data-platform, network-refresh, disaster-recovery | technical-writer |

---

## Step 5 — Read Static Assets

Read these files before drafting any artifact:

- `assets/static/company-profile.md`
- `assets/static/assumptions.md`
- `assets/static/exclusions.md`
- `assets/static/legal-notes.md`
- `assets/static/standard-next-steps.md`
- `assets/static/service-overview-[type].md` (if it exists)

---

## Step 6 — Draft Each Artifact

Draft each requested artifact using its dedicated prompt:

| Artifact | Prompt | Skill |
|----------|--------|-------|
| exec-summary | `.claude/prompts/draft-exec-summary.md` | exec-summary-writer |
| scope | `.claude/prompts/draft-scope.md` | scope-writer |
| delivery-plan | `.claude/prompts/draft-delivery-plan.md` | delivery-plan-writer |
| pricing | `.claude/prompts/draft-pricing-placeholder.md` | (no override needed) |
| proposal | `.claude/prompts/draft-proposal-from-context.md` | (active skill) |

Save each artifact to the path provided by `generate_package.py` (or the standard path):

```
output/drafts/exec-summaries/[STEM]_exec-summary_draft.md
output/drafts/scopes/[STEM]_scope_draft.md
output/drafts/delivery-plans/[STEM]_delivery-plan_draft.md
output/drafts/pricing/[STEM]_pricing_draft.md
output/drafts/proposals/[STEM]_proposal_draft.md
```

---

## Step 7 — Commercial Safety Check

**Pricing artifact ONLY:**

- If the user provided confirmed pricing figures → use them exactly as given
- If pricing is TBD or unknown → insert `[PRICING REQUIRED — DO NOT SEND WITHOUT SIGN-OFF]` and do not estimate

**Never invent, estimate, or suggest pricing figures.**

---

## Step 8 — Confirm Output

Once all artifacts are written, report to the user:

```
Package created: [STEM]

Artifacts written:
  ✅ exec-summary   output/drafts/exec-summaries/[STEM]_exec-summary_draft.md
  ✅ scope          output/drafts/scopes/[STEM]_scope_draft.md
  ✅ delivery-plan  output/drafts/delivery-plans/[STEM]_delivery-plan_draft.md
  ✅ pricing        output/drafts/pricing/[STEM]_pricing_draft.md
  ✅ proposal       output/drafts/proposals/[STEM]_proposal_draft.md

Next steps:
  Validate:  python scripts/approve_package.py --stem [STEM] --dry-run
  Improve:   /improve-draft [artifact path]
  Approve:   python scripts/approve_package.py --stem [STEM]
```