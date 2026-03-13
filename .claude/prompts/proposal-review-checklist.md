# Prompt: Proposal Review Checklist

Use this prompt when performing a quality review of a completed or near-complete draft.

Adopt the `proposal-quality-reviewer` persona before starting.

---

## Review Instructions

Read the entire proposal carefully. Then evaluate each dimension below and provide specific, actionable feedback. Do not give generic praise — identify specific weaknesses and propose targeted fixes.

---

## Review Dimensions

### 1. Executive Summary (Weight: High)

- Does it open with the client's problem, not a self-introduction?
- Does it name the client specifically?
- Does it state the proposed solution clearly within the first paragraph?
- Does it highlight 2–3 specific benefits (not generic claims)?
- Is it under 200 words and free of jargon?
- Would a non-technical executive understand it fully?

**Rate:** Strong / Adequate / Weak
**Specific improvement:** [quote the weak phrase, suggest the replacement]

---

### 2. Understanding of Requirements (Weight: High)

- Does it demonstrate genuine insight into the client's situation?
- Does it go beyond restating what the client said — does it add our perspective?
- Does it identify risks of inaction?
- Does it mention any specific systems, numbers, or constraints from the intake?

**Rate:** Strong / Adequate / Weak
**Specific improvement:** [identify gaps]

---

### 3. Proposed Solution (Weight: High)

- Is the solution described specifically enough to differentiate us from competitors?
- Are the technology choices justified (not just listed)?
- Does the solution map to the client's stated outcomes?
- Are there any claims that cannot be substantiated?

**Rate:** Strong / Adequate / Weak
**Specific improvement:** [identify vague claims]

---

### 4. Scope of Work (Weight: High)

- Are all activities described at a level of detail that avoids ambiguity?
- Are client responsibilities clearly stated?
- Is the change control statement included?
- Is there a clear in/out of scope table?

**Rate:** Strong / Adequate / Weak
**Specific improvement:** [identify ambiguous scope items]

---

### 5. Deliverables (Weight: Medium)

- Are deliverables specific and tangible (not vague like "documentation")?
- Does each deliverable have a format and timing?
- Are there at least 3 deliverables?

**Rate:** Strong / Adequate / Weak

---

### 6. Pricing (Weight: High)

- Is the pricing presented clearly and unambiguously?
- Is there a total investment line?
- Are VAT and payment terms stated?
- Is pricing consistent with the scope described?

**Rate:** Strong / Adequate / Weak

---

### 7. Timeline (Weight: Medium)

- Is the timeline realistic given the scope?
- Are key dependencies or blockers noted?
- Does it include start/end dates or durations for each phase?

**Rate:** Strong / Adequate / Weak

---

### 8. Overall Tone and Language

- Is the writing professional and confident (not apologetic or over-qualifying)?
- Are there any clichés or filler phrases to remove?
- Is the document free of passive constructions in the executive-facing sections?
- Consistent British/American English throughout?

**Rate:** Strong / Adequate / Weak
**Specific phrases to change:** [quote and suggest replacement]

---

## Output Format

```
PROPOSAL QUALITY REVIEW
========================
Proposal: [filename]
Reviewer persona: proposal-quality-reviewer
Date: [date]

SECTION RATINGS
───────────────────────────────────────
Executive Summary:          [Strong/Adequate/Weak]
Understanding of Req's:     [Strong/Adequate/Weak]
Proposed Solution:          [Strong/Adequate/Weak]
Scope of Work:              [Strong/Adequate/Weak]
Deliverables:               [Strong/Adequate/Weak]
Pricing:                    [Strong/Adequate/Weak]
Timeline:                   [Strong/Adequate/Weak]
Tone & Language:            [Strong/Adequate/Weak]

TOP 3 PRIORITY IMPROVEMENTS
───────────────────────────────────────
1. [Section] — [specific issue] — [suggested fix]
2. [Section] — [specific issue] — [suggested fix]
3. [Section] — [specific issue] — [suggested fix]

OVERALL READINESS: [Ready to Approve / Needs Work / Major Revision Required]
```

After the report, ask: "Would you like me to rewrite any of these sections now?"
