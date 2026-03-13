# Approval Instructions

## Purpose

This document defines when draft proposal artifacts may be promoted to approved status.

## Approval Conditions

- Validation passes
- Review checklist passes
- The customer context and scope are still current
- Pricing is confirmed or intentionally carries the approved safety marker
- No internal notes, placeholders, or drafting prompts remain

## Approval Actions

1. Validate the draft or package
2. Confirm explicit approval intent
3. Copy the approved artifact into `output/approved/`
4. Preserve the original draft
5. Record the approval in `output/approved/approval-log.json`

## Immutability

Approved files are treated as locked records.

If changes are needed after approval:
- create a new draft
- rerun review and validation
- approve the revised version explicitly

Do not silently edit approved content in place.
