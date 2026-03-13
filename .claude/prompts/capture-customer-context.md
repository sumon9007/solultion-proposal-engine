# Prompt: Capture Customer Context

Use this prompt when gathering information for a new proposal. Ask each question conversationally, one at a time. Do not ask all questions at once.

---

## Opening

Say:
> "I'm going to help you build a proposal. Let's start by capturing the key context. I'll ask you a series of questions — answer with as much detail as you have, and just say 'skip' if you don't know something yet."

---

## Questions to Ask (in order)

### Client Information
1. What is the full name of the client organisation?
2. What industry or sector are they in?
3. Who is the main decision-maker for this engagement? (Name and job title)
4. Are there other stakeholders we should address? (e.g. IT Director, CFO, Board)

### Problem and Current State
5. What specific problem or challenge is driving this proposal?
   - Probe: Is this a technical problem, a business process problem, or both?
   - Probe: How long has this been an issue?
6. What does their current environment look like?
   - Number of users / employees
   - Key systems and platforms in use
   - Locations / offices
   - Any known technical debt or constraints

### Desired Outcomes
7. What does success look like for them in 6–12 months?
8. Are there any compliance, security, or regulatory requirements driving this?

### Scope
9. What is in scope? (Which systems, processes, or locations)
10. Are there any known out-of-scope items?

### Commercial
11. What proposal type best describes this engagement?
    - Cloud Solution
    - Consultancy / Advisory Engagement
    - Managed Services
    - Implementation Project
12. Do they have a budget range in mind?
13. What is the expected start date or project deadline?

### Competitive Context
14. Are any competitors being evaluated? If so, who?
15. What is their key selection criteria? (e.g. price, speed, technical expertise, references)

---

## Summary Step

After capturing all answers, produce a structured context summary:

```
CUSTOMER CONTEXT SUMMARY
========================
Client:             [name]
Industry:           [industry]
Decision-maker:     [name, title]
Other stakeholders: [list]

Problem:            [brief description]
Current state:      [key facts]
Desired outcomes:   [bullet list]

Scope:              [in-scope items]
Out of scope:       [known exclusions]

Proposal type:      [type]
Budget:             [range or TBD]
Timeline:           [dates or TBD]

Competitors:        [list or none known]
Selection criteria: [list]
```

Ask: "Is this correct? Would you like to change anything before I draft the proposal?"
