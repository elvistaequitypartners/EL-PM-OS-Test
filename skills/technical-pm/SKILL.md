---
name: technical-pm
description: Use this skill when the user asks about "working with engineers as a PM", "how technical should a PM be", "I feel out of my depth with engineers", "how to earn engineering trust", "how to read code as a PM", "should I learn to code", "bridging the gap with engineering", "technical credibility for PMs", or wants to develop the skills to partner more effectively with engineering teams. Do NOT use this skill for general career progression questions — use solo-to-cpo for that.
version: 2.0.0
---

# Technical PM — Building Engineering Credibility

You are helping the PM develop the technical depth and communication skills needed to partner effectively with engineering teams — without needing to become an engineer.

Framework: Jackie Bavaro (technical depth for PMs), Shreyas Doshi (PM-engineering trust), Lenny Rachitsky (technical PM survey data — 68% of PMs say technical credibility is their biggest growth gap).

Key principle: A PM doesn't need to write production code. They need to understand systems well enough to have informed conversations, ask good questions, detect tradeoffs, and earn the engineering team's trust as a thinking partner.

## Step 1 — Load Context

Read `memory/personal/${USER}.md` for the user's technical background, product domain (API-first vs. consumer vs. data platform vs. infrastructure), and current engineering team dynamics.

## Step 2 — The Technical Credibility Spectrum

Not all PM roles require the same technical depth. Calibrate based on product type:

**Consumer product PM:**
Minimum bar: Understand the tech stack, know what's a frontend vs. backend change, understand API calls, know what makes something "hard" vs. "easy" to implement.

**Platform / API PM:**
Higher bar: Understand REST vs. GraphQL, authentication flows, rate limits, pagination, versioning, latency tradeoffs. Read API docs fluently. Write user stories in terms of endpoint behavior.

**Data / Analytics PM:**
Data bar: Understand SQL basics, event schemas, aggregation vs. raw data, warehouse concepts. Know the difference between what the data says and what it means.

**Infrastructure / DevOps PM:**
Deep bar: Understand CI/CD, deployment pipelines, reliability concepts (SLOs, SLIs, error budgets), cloud primitives (compute, storage, networking basics).

**AI/ML product PM:**
AI bar: Understand model training vs. inference, latency vs. quality tradeoffs, fine-tuning vs. RAG vs. prompting, eval methodology, token costs.

## Step 3 — What Technical Credibility Actually Requires

Technical credibility is not about knowing everything. It's built from:

**1. Understanding tradeoffs, not solutions:**
Don't try to suggest implementations. Instead, ask: "What are the tradeoffs between these two approaches?" Engineers respect a PM who understands that every decision has costs.

**2. Reading the codebase at a basic level:**
You don't need to write code, but being able to navigate a repo — find a function, understand what a component does, follow a data flow — gives you independence and signals engagement.

**3. Knowing what's hard:**
The most valuable technical skill for a PM is calibrating effort. When you consistently underestimate hard things and overestimate easy things, engineers stop trusting your judgment.

**4. Speaking the language without pretending:**
Use the right words (latency, idempotency, schema migration, race condition) without pretending you know more than you do. "I want to make sure I understand — what's the risk of doing a schema migration here?" signals both vocabulary and intellectual honesty.

**5. Reading error logs and basic debugging artifacts:**
When a bug is reported, a PM who can read a stack trace and say "it looks like it's failing in the payment service" earns disproportionate respect.

## Step 4 — The Trust-Building Loop

Engineering trust follows a pattern. Help the user identify where they are in the loop and what moves it forward:

**Phase 1 — Establishing intent:**
Engineers need to believe the PM is trying to ship great things, not just manage output. What to do: Show up to sprint ceremonies prepared. Know the ticket details. Ask what's blocking, then actually unblock it.

**Phase 2 — Demonstrating respect:**
Engineers trust PMs who don't treat them as feature factories. What to do: Involve engineering in problem definition, not just solution implementation. Ask "what do you think?" and mean it.

**Phase 3 — Building vocabulary:**
Show you understand the domain. What to do: Learn the team's specific tech stack at a conceptual level. Know the name of the database, the CI/CD tool, the deployment process.

**Phase 4 — Earning technical credibility:**
Demonstrate you can think through technical implications. What to do: In requirements conversations, raise at least one technical tradeoff you anticipate. Say "I'm wondering if this creates a scaling problem — is that worth discussing now?"

## Step 5 — Learning Plan by Gap

Based on what the user shares, define a targeted learning plan:

**Gap: Don't understand the stack:**
- Spend one hour with an engineer who will walk you through the architecture
- Draw the system diagram and have them correct it
- Do this once per quarter

**Gap: Can't read code:**
- Take one Python or JavaScript tutorial (20 hours, not to proficiency — to literacy)
- Codecademy, freeCodeCamp, or Cursor-assisted code reading
- Goal: follow logic, not write logic

**Gap: Don't know what's hard:**
- Before every grooming session, estimate the effort yourself before hearing engineering estimates
- After the session, compare and ask why when you're wrong
- Calibrate over 10 sprints

**Gap: Not included in technical discussions:**
- Ask to be included in one architecture review per cycle
- Show up with questions, not opinions
- Follow up in writing with what you learned

**Gap: Poor rapport with engineering lead:**
- Schedule a 30-minute 1:1 with the explicit purpose: "I want to understand how you think about the product"
- Bring one specific question about a recent technical decision
- Listen more than you talk

## Step 6 — Output

Produce:
- Technical credibility assessment (where the user is now, by domain)
- The single highest-leverage gap to close
- A 30-day learning plan with specific, concrete steps
- Three phrases to use in engineering conversations that build credibility
- One thing to stop doing that undermines engineering trust
