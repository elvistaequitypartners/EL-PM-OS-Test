---
name: growth-loops
description: Use this skill when the user asks about "growth loops", "viral loops", "product-led growth", "PLG", "how does our product grow itself", "referral mechanics", "word of mouth", "how to build growth into the product", "organic growth", or wants to identify and design the mechanisms through which the product acquires more users through its own usage.
version: 2.0.0
---

# Growth Loops

You are helping the user identify and design growth loops — self-reinforcing cycles where product usage generates new users, which generates more usage, compounding over time.

Framework: Lenny Rachitsky (growth loops), Andrew Chen (network effects and viral growth), Brian Balfour (loops vs. funnels).

Key insight: Funnels leak. Loops compound. A product with a strong growth loop doesn't need to keep increasing acquisition spend — each cohort of users generates the next cohort.

## Step 1 — Load Context

Read `memory/personal/${USER}.md` for product stage, business model, and current bets. Read `context/product/personas.md` for user type and behavior patterns.

## Step 2 — Growth Loop Types

Identify which types of loops are possible for this product:

**Viral / social loops:**
User uses product → creates something shareable → shares with others → new users discover the product → they sign up
Example: User creates a shareable PRD → shares on LinkedIn → peers see it and want to create their own

**Content loops:**
Users generate or curate content → content is indexed → search brings new users → they become users and generate more content
Example: PM shares their research synthesis publicly → Google indexes it → other PMs find it and discover PM Operating System

**Word of mouth loops (engineered):**
User gets value → built-in mechanism prompts sharing → they share → referral drives new user
Example: After a successful PRD, PM Operating System surfaces: "Your PRD looks great. Want to share it with your team or post it to LinkedIn?"

**Integration loops:**
User integrates product into their stack → other users in the same stack discover it → they request access
Example: User connects PM Operating System to Linear → Linear ticket shows "Generated with PM Operating System" → other team members ask to use it

**Product-led loops:**
Users invite others to get more value → invited users also get value → they invite more users
Example: Stakeholder receives PM Operating System-generated update → quality of update prompts them to ask for the tool → they become users

**Network effect loops:**
Product gets better as more users join → better product attracts more users
Example: Shared memory layer across teams → team templates improve → more PMs adopt it

## Step 3 — Loop Identification

For the user's specific product, identify:
- Which loop types are structurally possible given the product's nature?
- Which loops already exist (even informally)?
- Which loops would be highest-leverage to engineer?

Rate each possible loop on:
- **Potential magnitude:** How many new users could each iteration of this loop generate?
- **Friction to activate:** How hard is it for a user to complete the loop action?
- **Speed:** How quickly does the loop cycle? (Days vs. weeks vs. months)
- **Build effort:** How much engineering is needed to create or improve this loop?

## Step 4 — Loop Design

For the top 1–2 loops identified:

**Map the full loop:** Start → Action → Output → New User Touchpoint → Conversion → Back to Start

**Identify the friction points:** Where does the loop break or slow down?

**Design the intervention:** What product or marketing change would close the loop or reduce friction?

**Measurement:** How will you know if the loop is working? (What's the loop conversion rate? How many new users does one loop cycle generate?)

## Step 5 — PLG vs. Sales-Assisted

Based on the ICP and product:
- Can the product sell itself (PLG) or does it need sales assist?
- If PLG: what's the free-to-paid trigger? What in-product experience drives conversion?
- If sales-assisted: where does the loop end and the sales conversation begin?

For PM Operating System: PLG is the natural motion — users install the plugin themselves. The loop is: user uses PM Operating System → generates a high-quality output → shares output → peer asks "how did you make that?" → discovers and installs PM Operating System.

## Step 6 — Output

Produce:
- Loop identification (which loops exist and which are possible)
- Loop prioritization (highest leverage × lowest effort)
- Full loop design for top 1–2 loops
- Measurement framework for each loop (inputs, outputs, cycle rate)
- First experiment to test whether a proposed loop actually works
