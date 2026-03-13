You are approving a proposal draft. Follow these steps precisely.

## Step 1 — Identify the draft

If the user has not provided a file path, list the files in `output/drafts/` and ask which one to approve.

## Step 2 — Validate before approving

Run the full validation checklist from `.claude/commands/validate-proposal.md` against the draft.

If validation FAILS:
- Report the issues clearly
- Tell the user: "This proposal cannot be approved until all validation issues are resolved."
- Offer to fix the issues using `/improve-draft`
- STOP — do not proceed with approval

If validation PASSES, proceed to Step 3.

## Step 3 — Confirm intent

Ask the user:
> "Validation passed. Are you ready to approve this proposal? Once approved, it will be locked and moved to `output/approved/`. (yes/no)"

If no — stop without changes.
If yes — proceed to Step 4.

## Step 4 — Approve

1. Determine the approved filename by replacing `_draft.md` with `_approved.md`
2. Copy the draft content to `output/approved/[approved-filename]`
3. Tell the user: "Proposal approved and saved to `output/approved/[approved-filename]`"

## Step 5 — Suggest export

Suggest the next step:
> "To export this proposal to HTML, run:
> `python scripts/export_proposal.py output/approved/[approved-filename]`"

## Rules

- NEVER approve a proposal that fails validation
- NEVER modify the content of the proposal during approval — copy as-is
- NEVER delete the draft file after approval
