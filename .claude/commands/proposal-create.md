Alias command for the preferred proposal creation workflow.

## Purpose

Use this command as the default entry point for a new engagement.

## Instructions

1. Read the relevant `output/intake/[STEM]_requirements.md` file
2. If no intake file exists, or the intake file is empty, outdated, or not yet normalized from `input/`, direct the user to run `/requirements-build` first
3. If required details are still missing after normalization, ask focused follow-up questions
4. Default to the modular package workflow in `.claude/commands/create-package.md`
5. Use the shared stem naming convention
6. Save drafts only under `output/drafts/`

If the user explicitly wants a single monolithic proposal, use `.claude/commands/create-proposal.md` instead.
