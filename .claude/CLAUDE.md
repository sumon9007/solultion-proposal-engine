# Solution Proposal Engine — Claude Project Configuration

## Project Context

This is the Solution Proposal Engine. You help create, refine, approve, and export technical solution proposals for enterprise clients.

Default intake starts from `input/` and is normalized into `output/intake/[STEM]_requirements.md`. Generated outputs belong only under `output/`.

## Available Commands

| Command | Purpose |
|---------|---------|
| `/requirements-build` | Normalize raw intake files into `output/intake/[STEM]_requirements.md` |
| `/proposal-create` | Preferred entry point for modular package creation from `output/intake/[STEM]_requirements.md` |
| `/proposal-review` | Review and refine draft artifacts before approval |
| `/proposal-approve` | Route to single-proposal or package approval workflow |
| `/proposal-export` | Export an approved proposal using the workspace export rules |
| `/workspace-assess` | Review workspace health, governance, and lifecycle clarity |
| `/create-proposal` | Start a new full monolithic proposal from intake |
| `/create-package` | Start a new modular package (all artifact types) |
| `/validate-proposal` | Check structure and completeness of a full proposal |
| `/improve-draft` | Improve a specific draft or artifact |
| `/approve-draft` | Approve a single proposal draft |
| `/approve-package` | Validate and approve all artifacts in a package |
| `/list-proposals` | List all drafts and approved proposals |

## Active Rules

All rules in `.claude/rules/` are always active:
- `writing-rules.md` — tone, style, and language standards
- `proposal-structure-rules.md` — required sections and ordering
- `file-handling-rules.md` — where files must be saved
- `approval-and-export-rules.md` — quality gates for approval and export
- `commercial-safety-rules.md` — pricing constraints (never invent figures)

Use `docs/review-checklist.md`, `docs/approval-instructions.md`, and `docs/brand-guidelines.md` as supporting governance references when reviewing, approving, or exporting customer-facing deliverables.

## Skills Available

Load a skill by telling Claude to adopt the persona:
- `proposal-architect` — full-proposal orchestration (default)
- `technical-writer` — precise technical documentation
- `cloud-solution-writer` — cloud and infrastructure proposals
- `consultancy-scope-writer` — advisory and SOW engagements
- `managed-services-writer` — managed support contracts
- `proposal-quality-reviewer` — critical review and gap analysis
- `exec-summary-writer` — board-level executive summaries
- `scope-writer` — precise scope of work documents
- `delivery-plan-writer` — phased delivery planning
