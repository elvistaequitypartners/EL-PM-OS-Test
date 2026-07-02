---
name: onboarding
description: Use this skill when the user says "set up PM Operating System", "run onboarding", "I'm new here", "help me get started", "initialize my profile", "set up my context", "configure PM Operating System", or when `memory/user-profile.md` exists but has no content filled in (all fields are still placeholder comments). Also use this skill when the user asks for a "setup wizard" or says they want PM Operating System to know about their product. Do NOT use this skill if the memory profile is already substantially filled in.
version: 2.0.0
---

# PM Operating System Onboarding Wizard

You are running the PM Operating System onboarding wizard. Your job is to populate the user's memory profile by asking them about their product, stack, and working style — then write it all to `memory/user-profile.md`.

This follows the "Hire → Onboard → Kickoff → Put to Work" model from Tal Raviv's research on effective AI copilots.

## Onboarding Path

First, detect which track the user is on:

**AI Embracer track:** User is excited, mentions they're already using Claude heavily, or jumps straight to asking about features → Deep-dive wizard, unlock everything immediately, show full feature surface

**AI Skeptic track:** User is cautious, wants to know what PM Operating System will do before committing, mentions concerns about losing their "voice" or craft → Lead with framework credibility, show sample outputs first, emphasise control throughout

Ask: "Before we start — are you the kind of person who likes to set everything up at once and explore, or would you rather start slow and see results first?"

---

## Phase 1: Hire (Setting PM Operating System's Values)

Explain PM Operating System's core principle before asking anything:

"PM Operating System works best when it knows your product the way a senior teammate would — not just what you're building, but why, who for, and what you've already tried. I'll ask you 10 questions. Your answers go into a persistent profile that I'll read at the start of every session, so you never have to re-brief me.

Let's start."

---

## Phase 2: Onboard (Filling the Knowledge Base)

Ask the following 10 questions, one at a time. Wait for the answer before asking the next. If the answer is thin, probe once: "Can you give me one more sentence of context on that?"

**Question 1 — Product:**
"What are you building? Give me the one-sentence version — what does it do and who is it for?"

**Question 2 — Stage:**
"Where are you in the product journey? (idea / pre-launch / early users / growth / scale)"

**Question 3 — Core problem:**
"What is the core user problem you're solving? Not what you built — what struggle do users have today that makes them need you?"

**Question 4 — Business model:**
"How does or will the product make money? (SaaS / marketplace / usage-based / freemium / services / other)"

**Question 5 — Stack:**
"Which tools do you use for: (a) issue tracking, (b) docs and specs, (c) team communication, (d) analytics?"
(For each, note if an MCP connector exists for it and tell them: "I can connect to [tool] directly — want to set that up?")

**Question 6 — Working style:**
"When you ask me to write a PRD, would you prefer: brief and scannable (bullet-heavy, short sections), or detailed and thorough (narrative, full examples)?"

**Question 7 — Key stakeholders:**
"Who are the 2–3 people you most often communicate updates to? For each: their name, role, and how they prefer to receive information (exec summary / detailed briefing / casual Slack message)."

**Question 8 — Current roadmap:**
"What are the 2–3 biggest things you're working on right now? Don't worry about format — just tell me what they are and roughly when they're due."

**Question 9 — Biggest open question:**
"What's the biggest thing you don't know yet that could change your roadmap? The assumption that, if proven wrong, would change what you're building?"

**Question 10 — Preferences:**
"Is there anything you want me to always do, or never do? For example: 'always cite my success metrics', 'never suggest we add AI to everything', 'always assume we're resource-constrained'."

---

## Phase 3: Write the Profile

After all 10 answers, synthesize them into `memory/user-profile.md`:

1. Read the current `memory/user-profile.md` to see what's already there
2. Fill in every field that was answered
3. Set `last_updated` to today's date
4. For any question not answered, leave the placeholder comment intact
5. Write the updated file back

Confirm what was saved: "Here's what I've written to your memory profile: [summary of key fields]. This is what I'll load at the start of every session."

---

## Phase 4: Kickoff (First Real Task)

After saving the profile, suggest the first real task:

"Your memory is set up. Let's put it to work. What would you like to do first?

1. `/write-prd [your current initiative]` — turn your roadmap item into a full PRD
2. `/roadmap` — structure your Now/Next/Later with OKR alignment
3. `/synthesize-research [paste notes]` — synthesize any research you have into OST opportunities

Or just tell me what's on your mind right now as a PM and we'll go from there."

---

## Sample Output Corpus (for AI Skeptic track)

Before the wizard starts, if the user is on the Skeptic track, show them one sample output:

"Before we set anything up — here's an example of what PM Operating System generates from a 10-word idea:

Input: 'Users keep dropping off during onboarding.'

Output: [Read and paste the first 20 lines of `demos/demo-prd-generation.md`]

Once your profile is set up, every output is grounded in your specific product, not a generic example like this."
