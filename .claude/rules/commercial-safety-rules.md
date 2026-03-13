# Rule: Commercial Safety Constraints

These rules govern every pricing-related output produced in this workspace. They are absolute and non-negotiable.

---

## The Core Rule

**Claude must never invent, estimate, or fabricate pricing figures.**

This includes:
- Day rates
- Hourly rates
- Project totals
- Resource costs
- Licence costs
- Monthly recurring charges
- Any monetary value of any kind

If confirmed pricing has not been explicitly provided by the user, Claude must use the commercial safety marker and stop.

---

## The Commercial Safety Marker

When creating a pricing artifact or pricing section without confirmed figures, Claude must insert exactly this string:

```
[PRICING REQUIRED — DO NOT SEND WITHOUT SIGN-OFF]
```

This marker signals to the team that the document is not commercially complete.

**Never replace this marker with estimated figures.**
**Never soft-replace it with ranges like "typically £X–£Y".**
**Never reference industry benchmarks as a pricing proxy.**

---

## What Claude May Do in Pricing Sections

| Allowed | Not Allowed |
|---------|-------------|
| Use the commercial safety marker | Invent day rates |
| List the scope items to be priced (no values) | Use placeholder ranges like "£X,000–£Y,000" |
| State payment terms and VAT position | Reference "typical" or "market" pricing |
| Create the table structure with empty value fields | Populate values based on assumptions |
| Note what inputs are needed to calculate pricing | Guess based on similar past proposals |

---

## Scope Items Without Pricing

When listing what needs to be priced (but figures are unknown), use this format:

```
| Item | Unit | Quantity | Rate | Total |
|------|------|----------|------|-------|
| Cloud Architecture Design | Day | TBC | TBC | TBC |
| Migration Execution | Day | TBC | TBC | TBC |

[PRICING REQUIRED — DO NOT SEND WITHOUT SIGN-OFF]

**Payment terms:** 50% on engagement start, 50% on completion.
**VAT:** All prices are exclusive of VAT.
```

The structure is acceptable. The values are not.

---

## Approval of Pricing Artifacts

The `approve_package.py` script enforces this constraint programmatically:

- If the pricing artifact contains real monetary values → PASS (with no warning)
- If it contains the commercial safety marker → PASS with a commercial safety **warning** in the approval log
- If it contains neither → **FAIL — approval blocked**
- If it contains generic placeholders like `[TBD]` or `[INSERT]` instead of the official marker → **FAIL**

---

## During Proposal Generation

When running `/create-package` or `/create-proposal`:

1. Ask the user: "Do you have confirmed pricing to include?"
2. If **yes**: use only the figures the user provides. Do not add to them.
3. If **no** or **unknown**: insert the commercial safety marker in the pricing section and leave it for the user to complete.

Never prompt the user with suggested figures to "confirm." This creates anchoring bias and risks inaccurate commercial commitments.

---

## Summary

> The commercial safety marker is the only acceptable response when pricing is unknown.
> The marker is not a placeholder to be filled later by Claude — it is a handoff to the commercial team.