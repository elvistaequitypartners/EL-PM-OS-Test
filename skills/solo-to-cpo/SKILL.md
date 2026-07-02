---
name: solo-to-cpo
description: Use this skill when the user asks about "career path to CPO", "how do I become a CPO", "PM career progression", "path from PM to VP Product", "PM career growth", "how do I grow as a PM", "what does the PM career ladder look like", "solo PM to product leader", or wants to understand and plan their PM career trajectory from individual contributor to product leadership.
version: 2.0.0
---

# Solo PM → Founding PM → CPO Career Arc

You are helping the user understand and plan their PM career trajectory. The PM career is not a linear ladder — it's a series of capability expansions, each requiring different skills and different proofs of competency.

Framework: Jackie Bavaro (Cracking the PM Career), Lenny Rachitsky (PM career survey, communication as most valued skill), Shreyas Doshi (altitude and horizon framework).

## Step 1 — Load Context

Read `memory/personal/${USER}.md` for the user's current role context and product stage. This determines where they are on the arc and what the next step looks like.

## Step 2 — The Arc

**Stage 1 — Solo PM (PM0 / PM1):**
You're doing all PM activities: discovery, execution, stakeholder management, metrics. No specialization yet. The test: can you own an outcome end-to-end without needing constant guidance?

Core skills to develop: problem framing, user research synthesis, PRD writing, stakeholder communication, prioritization.
Evidence to demonstrate: "Here's a feature I owned end-to-end, from discovery to launch to measured impact."

**Stage 2 — Senior PM:**
You influence beyond your product area. You drive strategy, not just execution. You make other people around you better.
The test: can you work at the strategy level without prompting? Can you tell the difference between an execution problem and a strategy problem?

Core skills to develop: strategy-stack thinking, OKR definition, competitive positioning, stakeholder influence without authority.
Evidence to demonstrate: "Here's a strategic decision I drove that changed what the company built."

**Stage 3 — Principal PM / Staff PM:**
You set the product direction for a whole area. You represent the product point of view in leadership conversations. You mentor and develop other PMs.
The test: can you develop the product vision for an area, defend it with evidence, and execute against it across multiple teams?

**Stage 4 — Director of Product:**
You manage PMs and scale PM craft across a team. You're responsible for the health of the PM function as well as product outcomes.
The test: can you hire and develop great PMs? Can you create an environment where good product thinking happens even when you're not in the room?

**Stage 5 — VP Product / CPO:**
You own the entire product strategy and P&L implications. You influence company strategy, not just product decisions. You're the voice of the customer and the customer of the engineering organization.
The test: can you set a product vision that attracts talent, convinces investors, and aligns the whole company?

## Step 3 — Current Stage Assessment

Based on what the user shares, assess:
- Which stage are they at currently?
- What is the primary gap between their current stage and the next?
- Which skills are strong, which are underdeveloped?

Lenny's survey data on most valued PM skills (n=1,000, 600+ companies):
1. Communication (most valued)
2. Execution
3. Product sense

If any of these three are weak, they're the priority before anything else.

## Step 4 — Next Step Plan

For the user's next stage, define:

**Skill to build:** What's the highest-leverage capability to develop in the next 6 months?

**Evidence to create:** What specific work product would prove this capability to a hiring manager or promotion committee?

**Opportunity to seek:** What type of project, team, or initiative gives the best context to develop this skill?

**Reading/learning:** Which resources would most directly develop this skill? (Reference: Bavaro's Cracking the PM Career, Doshi's articles on Linkedin, Lenny's newsletter archives)

**Mentor to find:** What type of person would most accelerate this development? (A CPO who was a solo PM? A principal PM who crossed the strategy-execution boundary?)

## Step 5 — The Founding PM Path

If the user is on the founding PM path (early-stage company, first PM):

The Founding PM role is uniquely high-stakes and high-growth. Specifics:
- You'll do everything: discovery, strategy, roadmap, PRD, QA, CS, analytics — simultaneously
- The test is: did the product ship? Did users care? Did the company survive?
- The skill that matters most: judgment under ambiguity. There's no playbook.
- What to prioritize: Get to PMF evidence. Every week that doesn't move toward PMF evidence is a week too long.
- The accelerant: AI assistance (like PM Operating System) can function like having a senior PM peer — especially for frameworks and structure the Founding PM hasn't developed muscle memory for yet.

## Step 6 — Output

Produce:
- Arc stage assessment (where the user is now and why)
- Gap analysis (what's needed to get to the next stage)
- 6-month development plan with specific skills, evidence to create, and opportunities to seek
- One book or resource recommendation that would most help at this specific stage
