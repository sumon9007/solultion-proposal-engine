# Requirement Capture Flow

This guide explains how the requirement-capture flow works before proposal drafting begins.

## Purpose

The requirement-capture flow converts raw customer material into one clean internal intake file:

- raw source files go into `input/raw/`
- the normalized summary is written to `output/intake/[STEM]_requirements.md`

The proposal workflow should start from `output/intake/[STEM]_requirements.md`, not directly from the raw PDF, email, or Word document.

## When To Use It

Use this flow whenever the customer sends:

- an RFP
- a PDF requirements document
- an email thread
- a Word document
- workshop notes
- supporting references such as pricing assumptions or architecture notes

## Folder Roles

- `input/raw/` stores the original customer files
- `input/source-register.md` records what sources were received
- `input/working/` stores extracted text or temporary analysis notes
- `output/intake/[STEM]_requirements.md` stores the normalized facts for proposal creation

## How It Works

### 1. Place source files in the right folder

Examples:

- PDF requirements document -> `input/raw/pdf/`
- RFP document -> `input/raw/rfp/`
- email export -> `input/raw/email/`
- Word file -> `input/raw/word/`
- meeting notes -> `input/raw/notes/`

### 2. Update the source register

Open `input/source-register.md` and record:

- client name
- opportunity name
- solution type
- source file name
- source location
- gaps already known

This gives the intake step a clear source-of-truth for what should be reviewed.

### 3. Run the requirement-capture command

Use:

```text
/requirements-build
```

This command is intended to do the following:

1. read `input/source-register.md`
2. inspect the relevant files under `input/raw/`
3. extract the important facts only
4. write a normalized summary into `output/intake/[STEM]_requirements.md`
5. record open questions and conflicting details instead of guessing

### 4. Normalize, do not draft

The output of this step is not a proposal.

At this stage we only capture:

- client context
- business challenge
- desired outcomes
- scope and exclusions
- technical constraints
- timeline signals
- pricing status
- procurement and approval constraints
- open questions

This prevents proposal language from being mixed with raw intake notes.

### 5. Review the normalized requirements

Before proposal creation, review `output/intake/[STEM]_requirements.md` and check:

- are the main facts correct
- are important constraints captured
- are unknowns clearly listed
- are there any conflicts between source documents

If something is still unclear, update the file or ask follow-up questions before drafting.

### 6. Start proposal creation

Once the requirements file is good enough, start the next step:

```text
/proposal-create
```

That proposal step should read `output/intake/[STEM]_requirements.md` as the intake source.

## What Good Output Looks Like

A good `output/intake/[STEM]_requirements.md` should:

- summarize the customer need clearly
- separate facts from assumptions
- call out missing commercial details
- identify scope limits
- capture important customer wording worth preserving
- be strong enough to guide proposal drafting without rereading every raw file

## Example Flow For A PDF

1. Put the PDF in `input/raw/pdf/`
2. Add the file entry to `input/source-register.md`
3. Run `/requirements-build`
4. Review the generated `output/intake/[STEM]_requirements.md`
5. Confirm or refine open questions
6. Run `/proposal-create`

## Practical Note

If the raw file is a PDF, Claude may first extract its text into `input/working/` before summarizing it. That extracted text is a working artifact only. The real output of the capture step is still `output/intake/[STEM]_requirements.md`.

## Rule Of Thumb

Raw files answer: "What did the customer send?"

`output/intake/[STEM]_requirements.md` answers: "What do we now understand well enough to propose against?"
