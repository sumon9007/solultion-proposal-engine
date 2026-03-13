Validate the proposal at the file path provided by the user (or ask for it if not provided).

## Validation Checklist

Read the proposal file and check each item below. Report PASS or FAIL for each.

### Section Presence (required headings)

Check that all 13 sections exist as headings (## or #):

- [ ] Cover Page (or title block with client name, date, document reference)
- [ ] Executive Summary
- [ ] Understanding of Requirements
- [ ] Proposed Solution
- [ ] Scope of Work
- [ ] Deliverables
- [ ] Assumptions & Dependencies (or "Assumptions and Dependencies")
- [ ] Exclusions
- [ ] Indicative Pricing (or "Pricing" / "Investment")
- [ ] Timeline (or "Project Timeline" / "Delivery Plan")
- [ ] About Us (or "Company Profile" / "Why Us")
- [ ] Next Steps
- [ ] Legal Notes (or "Terms" / "Legal")

### Content Quality

- [ ] No placeholder text present: `[TBD]`, `[INSERT]`, `TODO`, `PLACEHOLDER`, `XXX`
- [ ] Client name mentioned at least once in the Executive Summary
- [ ] Pricing section contains at least one line item with a value (not just headings)
- [ ] Deliverables section lists at least 3 specific deliverable items
- [ ] Timeline section has at least one date or duration reference
- [ ] Assumptions section has at least 3 items

### Word Count

- [ ] Executive Summary: minimum 100 words
- [ ] Proposed Solution: minimum 200 words
- [ ] Scope of Work: minimum 150 words

## Output Format

Report results as:

```
VALIDATION REPORT
=================
File: [path]
Date: [date]

SECTION CHECK
✅ Executive Summary — present
✅ Proposed Solution — present
❌ Exclusions — MISSING

CONTENT QUALITY
✅ No placeholder text found
❌ Pricing section has no line items

WORD COUNT
✅ Executive Summary: 145 words (minimum 100)
❌ Scope of Work: 87 words (minimum 150)

─────────────────────────────────────────────────
RESULT: FAIL — 3 issue(s) found. Fix before approving.
```

After reporting, offer to help fix any FAIL items.
