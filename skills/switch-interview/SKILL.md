---
name: switch-interview
description: Use this skill when the user asks to "run a switch interview", "interview someone who switched to us", "interview someone who churned", "understand why users switch", "create interview guide for JTBD", "write an interview script for churn analysis", "how to interview users about their switching decision", or wants to design or debrief an interview specifically about the moment a user changed tools or workflows.
version: 2.0.0
---

# Switch Interview Methodology

You are helping the user design or debrief a switch interview — the structured user interview methodology developed by Bob Moesta to uncover the JTBD behind a behavior change. This works equally for acquisition (why users switched to you) and churn (why users switched away).

Key principle from Moesta: "The switch interview is not about the product — it's about the person's life and the moment they decided something had to change." — Lenny's Podcast (2023)

## Step 1 — Clarify the Goal

Ask: are we designing an interview guide, or debriefing a conversation that already happened?

**If designing:** Go to Step 2 (Interview Design)
**If debriefing:** Skip to Step 4 (Debrief Analysis)

## Step 2 — Interview Design

### Selecting Interview Subjects

**For acquisition switch interviews (why they came to you):**
- Recent new users (within first 30 days)
- Users who have activated and are using the product regularly
- Ideally: users who switched from a specific competitor you're trying to learn about

**For churn switch interviews (why they left):**
- Users who cancelled within the last 30–90 days
- Avoid users who left due to company shutdown or cost-cutting — you need behavior-change stories
- Look for users who switched to an alternative, not users who just stopped

### Interview Script

**Opening:**
"I don't want to talk about [product] today. I want to understand your story — what was going on in your life and work before you [switched to us / decided to leave]. Can you take me back to when you first started thinking something needed to change?"

**The timeline questions (reconstruct chronologically):**

"First thought: When was the first moment you thought, 'I need something different'? What triggered that?"

"Passive looking: Were you casually browsing alternatives, or did you ignore it for a while first? What kept coming up?"

"Active looking: What was the moment you started seriously evaluating alternatives? What happened?"

"Decision: What was the deciding moment — what pushed you over the edge? Was there a specific thing you saw, heard, or experienced?"

"Consuming: Walk me through your first experience using [product]. What happened? What surprised you?"

**The four forces (probe for each):**

Push (away from old): "What was most frustrating about [old solution]? Was there a specific moment that stands out?"

Pull (toward new): "What specifically attracted you to [new solution]? Was there one thing that was most important?"

Anxiety (about switching): "Was there anything that made you nervous about switching? What did you almost talk yourself out of?"

Habits (keeping old): "What made it hard to leave [old solution]? What did you have to give up?"

**Closing:**
"Looking back, what would have made this switch happen sooner? What was the thing that had to be true for you to finally make the move?"

## Step 3 — Interview Facilitation Tips

- Don't mention your product until they bring it up
- Ask "what happened next?" not "why did you do that?" — behavior, not rationalizations
- Let silence sit — the best answers come 5 seconds after a pause
- When they give a vague answer, probe: "Can you give me a specific example?"
- Don't accept "I wanted X feature" — reframe: "What were you trying to do that X would have helped with?"

## Step 4 — Debrief Analysis

If the user is debriefing a conversation they already had, extract:

**The struggling moment:** What triggered the switch decision?
**The four forces:** What did you learn about push, pull, anxiety, and habit for this user?
**The job statement:** "When [struggling moment], I want to [motivation], so I can [outcome]"
**Competitive hire insights:** Who were they "hiring" before? What did that hire fail to do?
**Actionable implications:** What does this tell us about positioning, onboarding, or messaging?

Compare findings against existing JTBD notes in `memory/personal/${USER}.md`. Are patterns emerging?

## Step 5 — Pattern Library

After multiple switch interviews, offer to synthesize patterns:
- Most common first thoughts / triggering events
- Most common pushes (why they left the old solution)
- Most common anxieties (what almost stopped them from switching)
- Most common pulls (what attracted them to the new solution)

This pattern library should be saved to `context/company/customer-feedback.md`.
