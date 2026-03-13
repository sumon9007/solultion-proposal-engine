You are improving an existing proposal draft.

## Step 1 — Identify the file

If the user has not provided a file path, list the files in `output/drafts/` and ask which one to improve.

## Step 2 — Read the draft

Read the full content of the specified proposal file.

## Step 3 — Ask what to improve

Ask the user:
> "Which sections would you like me to improve, or should I review the whole proposal and make recommendations?"

Options to offer:
1. Full proposal review (uses `proposal-quality-reviewer` skill)
2. Specific section rewrite (user names the section)
3. Executive Summary polish (uses `refine-executive-summary` prompt)
4. Scope of Work tightening
5. Pricing section review

## Step 4 — Apply the improvement

### If full review:
- Adopt the `proposal-quality-reviewer` persona
- Apply the `proposal-review-checklist` prompt
- Identify the 3 weakest sections and explain why
- Propose rewrites for each, one at a time
- Ask the user to accept or reject each rewrite before proceeding

### If specific section:
- Read the existing section content
- Rewrite it using the appropriate persona (cloud, managed services, consultancy, or technical)
- Show the old and new versions side by side
- Ask: "Shall I replace the old version? (yes/no)"

### If Executive Summary:
- Apply the `refine-executive-summary` prompt
- Present the revised executive summary
- Ask for confirmation before updating

## Step 5 — Save the updated file

After all accepted changes, save the updated content back to the same file path (overwrite the draft).

Confirm: "Draft updated at [file-path]."

Suggest next step: `python scripts/validate_proposal.py [file-path]`
