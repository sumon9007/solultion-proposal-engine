# Prompt: Draft Scope Artifact

Use this prompt when generating a standalone scope of work artifact.

---

## Inputs Required

Before drafting, confirm you have:

- [ ] Client name
- [ ] What is included in scope (systems, users, sites, workloads)
- [ ] What the client is responsible for
- [ ] Any known exclusions (to be placed in a separate exclusions artifact)
- [ ] The expected engagement model (fixed-price / time-and-materials / retained)

If scope boundaries are unclear, ask the user before drafting.

---

## Structure

```
# Scope of Work
## [Client Name] — [Solution Description]

### In-Scope

[Bulleted list of what is included. Be specific: name systems, user counts, locations, phases.]

### Client Responsibilities

[Bulleted list of what the client must provide or do. Examples: access to systems, named
contacts, timely sign-off, provision of test data.]

### Change Control

Any work not listed in the In-Scope section above is out of scope. Changes to scope must be
agreed in writing via a Change Request. Our team will provide a cost and timeline impact
assessment for any requested change before work begins.

### Engagement Model

[Describe: fixed-price, time-and-materials, or retained. State what this means practically.]
```

---

## Rules

- The change control statement is **mandatory** — do not omit it
- Client responsibilities must be listed explicitly — not implied
- Do not price anything in this document — that belongs in the pricing artifact
- Do not add assumptions here — those go in the full proposal
- Minimum 150 words
- No placeholder text

---

## File Path

Save to:

```
output/drafts/scopes/[STEM]_scope_draft.md
```