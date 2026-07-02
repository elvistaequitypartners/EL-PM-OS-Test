---
name: adr
description: Create an Architecture / Product Decision Record
argument-hint: <decision title>
---

You are helping the user capture a durable product decision as an
Architecture Decision Record (ADR). ADRs are immutable once merged —
superseded, never edited.

## Process

1. **Find the next ADR number.** Scan `memory/decisions/` for the highest
   `adr-NNNN-*.md` filename and add 1. Pad to 4 digits.

2. **Slugify the title.** Lowercase, hyphenate, strip punctuation. Cap at
   ~50 characters. Filename: `adr-NNNN-<slug>.md`.

3. **Resolve author identity** from git user.email (falls back to
   `$USER` env).

4. **Write the ADR** to `memory/decisions/adr-NNNN-<slug>.md`:

   ```markdown
   ---
   id: ADR-NNNN
   title: <decision title>
   status: proposed
   date: <today YYYY-MM-DD>
   deciders: [<PM emails>]
   supersedes: []
   superseded_by: null
   ---

   ## Context

   <what forces are at play — business, technical, political>

   ## Decision

   <one sentence: what we decided>

   ## Consequences

   <positive, negative, neutral — and who is affected>

   ## Alternatives considered

   - <option 1> — rejected because ...
   - <option 2> — rejected because ...
   ```

5. **Create a branch** `adr/NNNN-<slug>`, commit with message
   `docs(adr): ADR-NNNN <title>`.

6. **Open a PR** titled `ADR-NNNN: <title>` labeled `adr`. CODEOWNERS
   routes to `@head-of-product`.

7. **Report the PR URL** to the user.

## Guardrails

- **Never edit an accepted ADR.** To reverse a decision: create a NEW ADR
  that sets `supersedes: [ADR-XXXX]`, and update the old one's
  `superseded_by` field in the same PR (this is the ONE allowed edit to a
  merged ADR — a link update, no semantic change).
- If the user's decision is trivial ("we picked font size 14"), ask them
  to confirm before creating an ADR. ADRs are for durable, cross-team
  decisions worth archaeology in 6 months.
- Every ADR must include at least one rejected alternative. If the user
  can't name one, the decision isn't ready for an ADR.
