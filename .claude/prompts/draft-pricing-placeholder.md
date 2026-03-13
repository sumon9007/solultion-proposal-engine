# Prompt: Draft Pricing Placeholder Artifact

Use this prompt when creating a pricing artifact **before confirmed commercials are available**.

---

## When to Use This Prompt

Use this prompt when:
- The client has not confirmed a budget
- Internal pricing has not been finalised
- Day rates or resource costs are under commercial review
- The proposal is being prepared ahead of a commercial sign-off meeting

Do **not** use this prompt to generate indicative pricing. That is not permitted.

---

## What to Generate

Create a pricing artifact that:

1. Structures the commercial table (rows and columns) without populating any values
2. States payment terms and VAT position (these are policy, not quotes)
3. Inserts the commercial safety marker prominently

---

## Template

```markdown
# Indicative Pricing
## [Client Name] — [Solution Description]

The following commercial summary will be completed once internal pricing review is finalised.

| Item | Description | Unit | Qty | Rate | Total |
|------|-------------|------|-----|------|-------|
| [Phase / workstream name] | [Brief description] | Day | TBC | TBC | TBC |
| [Phase / workstream name] | [Brief description] | Day | TBC | TBC | TBC |

**[PRICING REQUIRED — DO NOT SEND WITHOUT SIGN-OFF]**

---

### Payment Terms

[State standard payment terms — e.g., "50% on engagement commencement, 50% on completion."]

### VAT

All prices are exclusive of VAT. VAT will be applied at the prevailing rate.

### Validity

This pricing will be valid for 30 days from the date of issue once populated and approved.
```

---

## Rules

- Insert `[PRICING REQUIRED — DO NOT SEND WITHOUT SIGN-OFF]` exactly as shown — do not paraphrase it
- Populate the row descriptions (what is being priced) but leave Rate and Total as TBC
- Payment terms and VAT position may be stated — these are policy, not quotes
- Do not suggest ranges or "ballpark" figures, even in comments
- No other placeholder text (`[TBD]`, `[INSERT]`) — use the official marker only

---

## File Path

Save to:

```
output/drafts/pricing/[STEM]_pricing_draft.md
```