You are approving a modular proposal package. This locks all artifact drafts and promotes them to the approved state.

Follow these steps precisely.

---

## Step 1 — Identify the Package

If the user has not provided a stem or manifest path:

1. List all package manifests in `output/packages/`
2. For each, show: stem, client name, solution type, artifact count, current status
3. Ask the user: "Which package would you like to approve?"

---

## Step 2 — Validate (Dry Run)

Run the package validator in dry-run mode first:

```
python scripts/approve_package.py --stem [STEM] --dry-run
```

Report the results clearly:

- Show which artifacts PASS and which FAIL
- For the pricing artifact: if it uses the commercial safety marker, report this explicitly:
  > "The pricing artifact uses the commercial safety marker. This means pricing has not yet been populated. You can still approve the package if this is intentional — the marker will be noted in the approval log."

---

## Step 3 — Handle Failures

If any artifact FAILS validation:

- List each failing artifact and the specific issue(s)
- Offer to fix them: "Would you like me to fix these issues using `/improve-draft`?"
- **Do not proceed with approval until all failures are resolved**

Only warnings (not failures) may be acknowledged and overridden with user consent.

---

## Step 4 — Confirm Approval Intent

If all artifacts pass (or only carry warnings the user accepts), ask:

> "All artifacts have passed validation. Are you ready to approve this package?
>
> Approving will:
> - Copy all draft artifacts to their approved directories
> - Lock the content (drafts are kept but approved files should not be modified)
> - Log the approval in `output/approved/approval-log.json`
>
> Proceed? (yes/no)"

---

## Step 5 — Execute Approval

If the user confirms, run:

```
python scripts/approve_package.py --stem [STEM]
```

This script handles:
- Copying each artifact to its approved subdirectory
- Updating the package manifest with approved paths and timestamps
- Writing one approval log entry per artifact

---

## Step 6 — Report and Suggest Next Steps

After approval:

```
Package approved: [STEM]

Approved artifacts:
  ✅ exec-summary   output/approved/exec-summaries/[STEM]_exec-summary_approved.md
  ✅ scope          output/approved/scopes/[STEM]_scope_approved.md
  ✅ delivery-plan  output/approved/delivery-plans/[STEM]_delivery-plan_approved.md
  ✅ pricing        output/approved/pricing/[STEM]_pricing_approved.md  ⚠ (safety marker present)
  ✅ proposal       output/approved/proposals/[STEM]_proposal_approved.md

Next step — export the full proposal to HTML:
  python scripts/export_proposal.py output/approved/proposals/[STEM]_proposal_approved.md
```

---

## Rules

- NEVER approve a package with artifact FAIL results
- NEVER modify artifact content during the approval process — copy as-is
- NEVER delete draft files after approval — both must be retained
- If the pricing artifact carries the commercial safety marker, record this in the approval summary and remind the user it must be completed before the document goes to the client