# Input Intake Structure

Use the `input/` area to collect raw customer materials before drafting a proposal.

## Goal

Turn mixed source material such as RFPs, emails, Word files, PDFs, meeting notes, and commercial references into a single normalized file:

`output/intake/[STEM]_requirements.md`

## Workflow

1. Place source files into the appropriate `input/raw/` subfolder
2. Record what was received in `input/source-register.md`
3. Run the intake normalization step using `/requirements-build`
4. Review the generated `output/intake/[STEM]_requirements.md`
5. Start proposal generation with `/proposal-create`

## Folder Rules

- `input/raw/` stores original customer-provided material
- `input/working/` stores extracted notes or temporary analysis artifacts
- `input/normalized/` stores stable structured intake summaries if needed
- `input/archive/` stores superseded intake packages when an opportunity is complete

Do not write proposal drafts into `input/`.
