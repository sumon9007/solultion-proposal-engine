# Prompt: Draft Executive Summary Artifact

Use this prompt when generating a standalone executive summary artifact.

---

## Inputs Required

Before drafting, confirm you have:

- [ ] Client name and industry
- [ ] The specific problem or challenge they face
- [ ] The proposed solution (high level)
- [ ] The key outcomes the client expects
- [ ] Any known constraints (budget, timeline, compliance)

If any input is missing, ask the user before proceeding.

---

## Structure

The executive summary artifact is a **standalone document** — not a section inside a larger proposal. Write it as a self-contained 1–2 page document.

```
# Executive Summary
## [Client Name] — [Solution Description]

[Opening paragraph: state the client's problem directly. Do not start with "We are pleased to present".]

[Second paragraph: the proposed solution and why it addresses the problem.]

[Third paragraph: key outcomes — what the client will achieve. Quantify wherever possible.]

[Closing sentence: proposed next steps or call to action.]
```

---

## Word Count

- Minimum: 100 words
- Target: 150–200 words
- Maximum: 250 words

If the summary exceeds 250 words it is too long — condense it.

---

## Writing Rules

- Use **active voice** throughout
- Client name must appear in the first paragraph
- State the solution explicitly — do not be vague
- Quantify outcomes: "reduce report generation from 3 days to 4 hours"
- No banned phrases (see `writing-rules.md`)
- No pricing, no assumptions, no exclusions — those are separate artifacts
- No placeholder text

---

## Tone

This is a senior decision-maker document. The reader may be a CTO, CFO, or CEO. Write with authority and clarity. Every sentence must earn its place.

---

## File Path

Save to:

```
output/drafts/exec-summaries/[STEM]_exec-summary_draft.md
```

Where `[STEM]` is the shared package stem: `YYYY-MM-DD_[client-slug]_[solution-type]`