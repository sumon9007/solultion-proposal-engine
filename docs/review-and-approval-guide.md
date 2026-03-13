# Review and Approval Guide

This guide covers both stages of the quality gate: reviewing a draft before approval, and formally approving and locking it.

---

## Part 1 — Review Checklist

Use this checklist before anything is approved or exported.

### Content Quality

- The document is written for the customer, not for internal review
- The customer name, context, and objectives are specific and accurate
- Claims are concrete and technically defensible
- The tone is professional and commercially credible
- No unresolved drafting notes, editor comments, or AI meta-commentary remain

### Completeness

- Required sections are present (all 13 for a full proposal)
- Scope is specific enough to control expectations
- Assumptions and exclusions are explicit
- Timeline and deliverables are concrete
- Pricing is either confirmed or uses the approved commercial safety marker

### Presentation

- No placeholders remain (`[TBD]`, `[INSERT]`, `TODO`, etc.)
- No duplicated sections or repeated boilerplate
- Terminology is consistent throughout
- Headings and structure are clean
- Draft content is stored only in `output/drafts/`

---

## Part 2 — Approval Conditions

A draft may only be approved when **all** of the following are true:

- Validation passes (`python scripts/validate_proposal.py <draft>` returns PASS)
- The review checklist above passes
- The customer context and scope are still current
- Pricing is confirmed — or the proposal carries the commercial safety marker
- No internal notes, placeholders, or drafting prompts remain in the content

---

## Part 3 — Approval Actions

### Single proposal draft

```bash
python scripts/approve_draft.py output/drafts/proposals/[STEM]_proposal_draft.md
```

The script will:
1. Re-run validation — blocks if FAIL
2. Show the source and target paths
3. Ask for explicit confirmation before writing
4. Copy the draft to `output/approved/proposals/[STEM]_proposal_approved.md`
5. Preserve the original draft (not deleted)
6. Record the approval in `output/approved/approval-log.json`

### Full modular package

Validate first (dry run, no writes):
```bash
python scripts/approve_package.py --stem [STEM] --dry-run
```

Approve all artifacts at once:
```bash
python scripts/approve_package.py --stem [STEM]
```

---

## Part 4 — Immutability

Approved files are treated as locked records.

If changes are needed after approval:
1. Create a new draft (new date in the stem if the engagement date changed)
2. Re-run review and validation
3. Approve the revised version explicitly

Do not silently edit approved content in place. The approval log records what was approved and when.

---

## Approval Gate

**Approve only if all review checks pass and the document is suitable to send to a customer without further cleanup.**
