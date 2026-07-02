---
name: launch-announcement
description: Use this skill when the user asks to "write a launch announcement", "announce this feature", "write a launch email", "product announcement", "release notes", "launch blog post", "feature announcement to customers", "write the Slack announcement for this launch", or is preparing to communicate a new feature or product to users, customers, or the public.
version: 2.0.0
---

# Launch Announcement

You are writing launch communications — the external-facing message that converts a shipped feature into user awareness, adoption, and delight. Every launch announcement is a marketing and retention opportunity.

Frameworks: April Dunford (positioning clarity), Lenny's PRD guide (problem-oriented framing), copywriting principles (benefits over features).

## Step 1 — Load Context

Read `memory/personal/${USER}.md` for: product name, stage, primary persona, current roadmap (to understand what just shipped), and stakeholder communication preferences. Read `context/product/personas.md` for tone calibration.

## Step 2 — Frame the Announcement Around the Problem

The #1 launch communication mistake: announcing a feature instead of announcing a solution.

- ❌ "We've added dark mode" → This is a feature
- ✓ "You asked for an easier way to use [Product] at night. Dark mode is here." → This is a solution

Every announcement should:
1. Reference the user problem or request
2. Show the solution in concrete terms (what can they do now that they couldn't before?)
3. End with a clear next action

## Step 3 — Determine the Format

Different channels need different formats:

**In-app notification:** 1–2 sentences. CTA button. No context needed.
**Email announcement:** Subject line + 3–4 short paragraphs. Problem → Solution → How to access → CTA.
**Slack/Discord message:** Conversational tone. Brief. Include a visual or GIF if possible.
**Blog post / changelog:** Full narrative. 300–600 words. Problem, solution, how it works, what's next.
**LinkedIn post:** Conversational, first-person. Story-forward. Include a real example or quote.
**Product Hunt post:** Tagline + body. Includes what problem it solves, who it's for, and how to try it.

Ask which format(s) the user needs.

## Step 4 — Write the Announcement

For each format requested, write:

**Subject/headline:** The benefit, not the feature name. "Now you can [do X] without [pain Y]"

**Opening:** Acknowledge the user's struggle or the request. Show you've been listening.

**What's new:** Describe the feature in user terms. What does the user do? What happens? What outcome do they get?

**Why it matters:** One sentence connecting the feature to user impact.

**How to access:** Clear, specific instructions. Don't assume they'll find it.

**What's next:** Optional. If there's more coming in this area, hint at it — creates anticipation.

**CTA:** One clear action: "Try it now", "See it in action", "Give us feedback".

## Step 5 — Tone Calibration

Calibrate tone based on:
- **Product stage (from memory):** Early-stage = scrappy and warm. Growth-stage = confident and product-led. Scale = polished and authoritative.
- **Primary persona (from memory):** Technical users want precision. Non-technical users want reassurance. Enterprise stakeholders want reliability signals.
- **Channel:** Blog = editorial. Email = personal. Slack = casual. LinkedIn = professional-but-human.

## Step 6 — Output

Produce:
- Launch announcement in all requested formats
- A "don't forget" checklist: in-app tooltip? Help doc? Customer success heads-up? Support team briefed?
- Suggested send time if relevant
