You are starting a new technical solution proposal. Follow these steps precisely.

## Step 1 — Customer Intake

Ask the user the following questions one at a time. Wait for each answer before asking the next.

1. **Client name** — What is the full name of the client organisation?
2. **Industry** — What industry are they in?
3. **Primary contact** — Who is the main decision-maker? (Name and title)
4. **Problem statement** — What specific problem or challenge are they trying to solve? Ask them to be as specific as possible.
5. **Current state** — What does their current environment look like? (Systems, headcount, locations)
6. **Desired outcomes** — What does success look like in 6–12 months?
7. **Scope** — How many users / sites / systems are in scope?
8. **Proposal type** — Is this a (a) Cloud Solution, (b) Consultancy Engagement, (c) Managed Services, or (d) Implementation Project?
9. **Budget** — Do they have a budget range in mind, or is this TBD?
10. **Timeline** — What is the target start date or deadline?
11. **Competition** — Are you aware of any competitors being evaluated?

## Step 2 — Confirm and Summarise

Summarise the captured context back to the user and ask: "Is this correct, or would you like to update anything?"

## Step 3 — Generate the Draft

Once confirmed:

1. Select the appropriate skill persona based on proposal type:
   - Cloud Solution → cloud-solution-writer
   - Consultancy → consultancy-scope-writer
   - Managed Services → managed-services-writer
   - Implementation → technical-writer

2. Read these static assets:
   - `assets/static/company-profile.md`
   - `assets/static/assumptions.md`
   - `assets/static/exclusions.md`
   - `assets/static/legal-notes.md`
   - `assets/static/standard-next-steps.md`

3. Read the relevant service overview:
   - `assets/static/service-overview-[type].md`

4. Draft all 13 required sections using the `draft-proposal-from-context` prompt as your guide.

5. Determine today's date in YYYY-MM-DD format.

6. Save the draft to:
   `output/drafts/[YYYY-MM-DD]_[client-slug]_[solution-type]_draft.md`

7. Confirm the file path to the user and suggest running:
   `python scripts/validate_proposal.py [file-path]`
