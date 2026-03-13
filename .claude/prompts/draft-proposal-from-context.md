# Prompt: Draft Proposal From Context

Use this prompt after customer context has been captured. This guides the full proposal draft.

---

## Instructions

You are drafting a professional technical solution proposal based on the captured customer context. Write every section as if it will be sent directly to the client. Do not include meta-commentary, section notes, or instructions in the final output.

Use this structure and write each section in order.

---

## Proposal Structure

### 1. Cover Page

```markdown
# [Solution Title]
## Technical Solution Proposal

**Prepared for:** [Client Name]
**Prepared by:** [Your Company Name]
**Document Reference:** PROP-[YYYY-MM-DD]-[CLIENT-SLUG]
**Date:** [Date]
**Version:** 1.0
**Validity:** This proposal is valid for 30 days from the date above.
```

---

### 2. Executive Summary (100–200 words)

Write a compelling 3–4 paragraph executive summary that:
- Opens by naming the client and acknowledging their challenge directly
- States what we are proposing and why it is the right solution for them
- Highlights 2–3 key benefits that matter most to this client
- Closes with a confident call to action

Do NOT start with "We are pleased to..." or "Thank you for the opportunity..." — begin with the client's problem.

---

### 3. Understanding of Requirements

Demonstrate that you have understood the client's problem deeply. Include:
- A restatement of their core challenge (in our words, not theirs)
- Key business drivers behind the requirement
- Technical context observed from the current state
- Risks of inaction

Use bullet points for specifics. Keep prose concise.

---

### 4. Proposed Solution

Describe the proposed solution clearly. Include:
- A high-level summary of the recommended approach
- Key technologies, platforms, or methodologies involved
- Why this approach is recommended over alternatives
- How the solution maps to each of the client's stated outcomes

For cloud proposals: include architecture overview (text description, no diagrams required in draft).
For managed services: describe the service model (reactive, proactive, strategic).
For consultancy: describe the engagement methodology (discovery, assessment, roadmap, etc.).

---

### 5. Scope of Work

Break the engagement into clearly defined phases or workstreams. For each:
- Phase name and objective
- Key activities included
- Estimated effort or duration
- Responsible party (Us / Client / Joint)

Format as a table or numbered list.

---

### 6. Deliverables

List every tangible deliverable the client will receive. Be specific:

| # | Deliverable | Format | When |
|---|-------------|--------|------|
| 1 | [Name] | [Doc / System / Report] | [Phase / Date] |

Minimum 3 deliverables. Prefer 5–8 for mid-to-large engagements.

---

### 7. Assumptions & Dependencies

Insert base content from `assets/static/assumptions.md`, then add any engagement-specific assumptions derived from the customer context.

Format each as: "It is assumed that [condition]. If this assumption is incorrect, the scope, timeline, or cost may be affected."

---

### 8. Exclusions

Insert standard content from `assets/static/exclusions.md`, then add any engagement-specific exclusions.

Format each clearly: "The following is explicitly excluded from this proposal: [item]."

---

### 9. Indicative Pricing

Present pricing in a clear table. Adapt to the proposal type:

**For fixed-price / project:**
| Item | Description | Days | Day Rate | Total |
|------|-------------|------|----------|-------|

**For managed services:**
| Service Tier | Description | Monthly Fee |
|--------------|-------------|-------------|

**For consultancy:**
| Phase | Effort (Days) | Day Rate | Phase Total |
|-------|---------------|----------|-------------|

Include a **Total Investment** line at the bottom.
Add a note: "All prices are exclusive of VAT. Payment terms: 30 days net."

If budget is unknown, include placeholder ranges with a note: "Pricing is indicative and subject to formal scoping."

---

### 10. Timeline

Present a high-level project timeline:

| Phase | Activities | Duration | Start | End |
|-------|-----------|----------|-------|-----|

Add any key dependencies or assumptions that affect the timeline.

---

### 11. About Us

Insert content from `assets/static/company-profile.md`.

---

### 12. Next Steps

Insert content from `assets/static/standard-next-steps.md`.

---

### 13. Legal Notes

Insert content from `assets/static/legal-notes.md`.
