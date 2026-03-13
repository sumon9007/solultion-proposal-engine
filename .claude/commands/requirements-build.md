Normalize raw customer source material into `output/intake/[STEM]_requirements.md`.

## Purpose

Use this command before proposal creation when the customer has provided input material such as an RFP, email thread, Word document, PDF, or meeting notes.

## Instructions

1. Inspect `input/source-register.md`
2. Review files under `input/raw/` that are relevant to the active opportunity
3. Extract facts only:
   - client context
   - current challenge
   - desired outcomes
   - scope
   - technical constraints
   - timeline
   - commercial status
   - stakeholder and procurement signals
4. Build the intake stem using the standard naming convention: `YYYY-MM-DD_[client-slug]_[solution-type]`
5. Write a normalized summary into `output/intake/[STEM]_requirements.md`
6. If the source material conflicts, record the conflict clearly in the intake file
7. If key information is missing, list targeted follow-up questions at the end of the intake file

## Rules

- Prefer customer-provided facts over inference
- Do not invent pricing, scope, or commitments
- Keep raw source files in `input/raw/`
- Keep temporary extraction notes in `input/working/`
- Do not start proposal drafting until `output/intake/[STEM]_requirements.md` is reviewed
