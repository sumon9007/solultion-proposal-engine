# Prompt: Draft Delivery Plan Artifact

Use this prompt when generating a standalone delivery plan artifact.

---

## Inputs Required

Before drafting, confirm you have:

- [ ] Client name
- [ ] Target start date or proposed start window
- [ ] Total engagement duration (if known)
- [ ] Key milestones or phases
- [ ] Any fixed deadlines or blackout dates
- [ ] Team composition or resource model (if relevant)

If timing has not been agreed, use indicative durations (e.g., "Week 1–2") rather than
calendar dates. Ask the user what is known before drafting.

---

## Structure

```
# Delivery Plan
## [Client Name] — [Solution Description]

### Overview

[One paragraph: total duration, number of phases, overall delivery model.]

### Phase Breakdown

#### Phase 1 — [Name] (Duration: [X weeks / X days])

[What happens in this phase. Who does what. Key outputs.]

**Milestone:** [Deliverable or gate at the end of this phase]

#### Phase 2 — [Name] (Duration: [X weeks / X days])

...

### Key Milestones

| Milestone | Target Date / Week | Owner |
|-----------|-------------------|-------|
| Kick-off meeting | Week 1 | Joint |
| ... | ... | ... |

### Assumptions

[Any timing assumptions — e.g., "Client sign-off within 5 business days of each phase review."]
```

---

## Rules

- Every phase must have a duration (weeks, days, or calendar reference)
- At least one milestone table or list is required
- Do not include pricing — that belongs in the pricing artifact
- Indicative durations are acceptable when calendar dates are not confirmed
- Minimum 100 words
- No placeholder text (`[TBD]`, `[INSERT]`, etc.)

---

## File Path

Save to:

```
output/drafts/delivery-plans/[STEM]_delivery-plan_draft.md
```