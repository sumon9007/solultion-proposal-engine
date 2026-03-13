# Prompt: Normalize Customer Requirements

Use this prompt to convert raw source materials into a structured `output/intake/[STEM]_requirements.md`.

## Inputs

Review the available source material from:

- `input/source-register.md`
- `input/raw/rfp/`
- `input/raw/email/`
- `input/raw/word/`
- `input/raw/pdf/`
- `input/raw/notes/`
- `input/raw/reference/`

## Objective

Produce a fact-based, proposal-ready requirements summary for internal use before drafting starts.

## Required Output Structure

Write or update `output/intake/[STEM]_requirements.md` using these sections:

1. Opportunity Snapshot
2. Business Context
3. Scope
4. Commercial and Delivery Context
5. Technical Notes
6. Competitor and Selection Context
7. Open Questions
8. Source Traceability

## Rules

- Keep the language concise and neutral
- Preserve customer terminology where commercially important
- Distinguish clearly between confirmed facts, inferred details, and open questions
- If multiple sources disagree, note the conflict rather than resolving it silently
- Do not include internal AI notes
- Do not draft proposal language here; normalize requirements only
