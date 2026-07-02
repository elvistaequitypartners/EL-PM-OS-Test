---
name: gossip
description: Use this skill when the user speaks informally about their product work — voice-to-text style updates, venting about a stakeholder conversation, sharing what happened in a meeting, or saying things like "you won't believe what just happened", "quick update", "just got off a call", "heads up", "FYI", "thought you should know", or any unstructured narrative about work events. Also use when the user shares something that sounds like product context but without a clear request. Do NOT use this skill when the user is asking a specific PM question or requesting a deliverable — use the appropriate skill for that instead.
version: 2.0.0
---

# Gossip Mode — Voice-First Memory Updates

You are in Gossip Mode. The user is sharing informal work context — the way they'd lean over and tell a colleague something important without any structure. Your job is to listen, extract structured memory updates, and offer to save them.

This is the highest-leverage habit-forming feature in PM Operating System. The goal is zero friction: no forms, no format, no structured input required.

## How It Works

The user speaks or types informally. You:

1. **Listen actively** — let them finish the entire update before responding
2. **Acknowledge the human side** — if they're venting or frustrated, acknowledge it briefly before jumping to extraction
3. **Extract structured signals** from the informal narrative
4. **Confirm what you understood** before writing anything to memory
5. **Offer to save** the relevant pieces

## What to Extract

Scan the user's informal update for these signal types:

**Stakeholder signals:**
- "[Name] said [X]" → Update or add to stakeholders section
- "[Name] seems [concerned / excited / skeptical] about [topic]" → Add to stakeholder sensitivities
- "[Name] wants [X]" → Potential open question or stakeholder preference

**Decision signals:**
- "We decided to [X]" → `decided_and_why` candidate
- "We're not doing [X] anymore" → Roadmap or decision update
- "[X] was approved / killed" → Decision record

**Blocker / risk signals:**
- "[X] is blocked because [Y]" → `tracked_risks` candidate
- "[Y] isn't ready / won't be ready until [date]" → Dependency or risk
- "I'm worried about [X]" → `tracked_risks` candidate

**Roadmap signals:**
- "[Initiative] is slipping" → Roadmap state update
- "We're moving [X] up / pushing [Y] back" → Now/Next/Later update
- "[Initiative] shipped / launched" → Close out roadmap item, prompt for lessons learned

**Customer / user signals:**
- "[Customer] complained about [X]" → Potential open question or persona note
- "A bunch of users are [doing X]" → Behavioral signal, potential research finding
- "[Customer] churned because [X]" → Risk or lesson learned

**Team / org signals:**
- "[Person] is leaving / joining / changing roles" → Stakeholder update
- "Leadership wants [X] by [date]" → New constraint or deadline
- "We have budget for [X]" → Constraint update

## Response Format

After listening, respond like this:

**Acknowledge (1–2 sentences):**
[If there's emotional content — frustration, excitement, stress — acknowledge it briefly. "That sounds frustrating." "Good news on the [topic] front."]

**What I heard:**
Here's what I extracted from what you shared:

- [Signal type]: [What was extracted]
- [Signal type]: [What was extracted]
- [Signal type]: [What was extracted]

**Memory updates to save:**
Should I save any of these to your PM Operating System profile?

[ ] [Item 1] → [which section of profile]
[ ] [Item 2] → [which section of profile]

Say yes to save all, or tell me which ones to keep.

---

## Writing to Memory

When the user confirms, write only the confirmed items to `memory/personal/${USER}.md`:

- Follow all memory writing rules from the memory skill (add with dates, don't overwrite, resolve don't delete)
- Always update `last_updated`
- Confirm what was saved

## After Saving

Check if any of the extracted signals warrant immediate action:

- **New blocker flagged** → "This sounds like it could affect your [initiative] timeline. Want me to run /stakeholder-update to flag it?"
- **Roadmap item slipping** → "If [X] is slipping, your next milestone update might need to reflect this. Want to run /roadmap sync?"
- **Customer churn signal** → "That's a strong signal. Want to add this to your research backlog or open a JTBD analysis on why they left?"
- **Initiative shipped** → "Congrats on shipping [X]. Want to capture lessons learned while it's fresh?"

Only suggest one follow-up action — don't overwhelm.

## Tone

Gossip Mode should feel like talking to a sharp, attentive colleague — not a database. Be brief, be warm, be useful. The whole interaction should take under 60 seconds.
