---
name: user-story-decomposition
description: Use this skill when the user asks to "write user stories", "decompose this into user stories", "break this into stories", "write acceptance criteria for this feature", "turn this PRD into stories", "create a story map", "help me write stories for sprint planning", or has a feature or PRD and wants to decompose it into shippable units for engineering. Do NOT use this skill to write a full PRD — use prd-authoring for that.
version: 2.0.0
---

# User Story Decomposition

You are helping the user break a feature or PRD into well-formed user stories ready for sprint planning and engineering estimation. Good stories are independently shippable, testable, and small enough to fit in a sprint.

Framework: Shape Up (small, vertically sliced bets), INVEST criteria (Independent, Negotiable, Valuable, Estimable, Small, Testable).

## Step 1 — Load Context

Read `memory/personal/${USER}.md` for product context and team norms. Read the PRD or feature description provided.

## Step 2 — Identify the Feature Boundaries

Before decomposing, establish:
- What is the full scope of the feature?
- What is explicitly out of scope (from the PRD)?
- What are the key user flows (from the PRD or user input)?

## Step 3 — Story Map Structure

Build a story map with three levels:

**Epics (user goals):** The high-level things a user is trying to accomplish. These are the columns of the story map.

**Stories (user tasks):** Specific actions a user takes to achieve the epic. These are the rows under each epic.

**Sub-tasks (engineering tasks):** The technical work needed to implement each story. These are not user stories — they go into the engineering ticket.

## Step 4 — Write User Stories (INVEST Format)

For each story, write in this format:

**User Story:**
As a [specific user type from personas],
When [triggering situation / context],
I want to [action],
So that [outcome / progress made].

**Acceptance Criteria (Gherkin format):**
- Given [precondition], When [action], Then [expected result]
- Given [precondition], When [action], Then [expected result]

**Definition of Done:**
- [ ] [Engineering-level done criterion]
- [ ] [QA-testable criterion]
- [ ] [Design-signed-off criterion if applicable]

**Story size estimate:** [XS / S / M / L / XL — based on typical team velocity from memory if available]

## Step 5 — INVEST Check

For each story, verify:
- **Independent:** Can this story be shipped without other stories?
- **Negotiable:** Is the scope negotiable, or is it a fixed requirement?
- **Valuable:** Does this story deliver user value by itself, or only when combined with others?
- **Estimable:** Does engineering have enough information to estimate it?
- **Small:** Can it be completed in one sprint? If not, split it.
- **Testable:** Can QA verify it with the acceptance criteria above?

Flag any story that fails INVEST and suggest how to fix it.

## Step 6 — MVP vs. Full Scope

After listing all stories, identify the minimum set that delivers the core user value. Label each story:

- **MVP** — must ship for the feature to be minimally useful
- **V1** — should ship in the same release but not strictly blocking
- **V2** — can ship in a follow-up iteration
- **Nice to have** — valuable but deprioritized for now

## Step 7 — Output

Produce:
- Story map (epics as columns, stories as rows)
- Full user stories with acceptance criteria for MVP stories
- Brief descriptions for V1 and V2 stories (full write-up can come later)
- Story size estimates
- Sprint breakdown suggestion: which stories go in Sprint 1, Sprint 2, etc.
