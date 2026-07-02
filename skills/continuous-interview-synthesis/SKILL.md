---
name: continuous-interview-synthesis
description: Use this skill when the user asks to "synthesize interview notes", "analyze my user interviews", "what patterns are in my interviews", "help me with continuous discovery", "find the themes in these interviews", "what did I learn from these calls", "turn these interview notes into opportunities", or pastes or shares raw interview transcripts or notes from user conversations. This skill focuses on the interview synthesis step of continuous discovery, not general feedback analysis — use feedback-triage for support tickets or NPS data.
version: 2.0.0
---

# Continuous Interview Synthesis

You are synthesizing user interview notes into opportunities using Teresa Torres' continuous discovery methodology. The goal is to extract struggles and unmet needs — not feature requests — and connect them to OST opportunities.

Key principle from Torres: "The most common interview mistake is asking users what they want. Instead, ask about their past behavior. Reconstruct the experience." — Teresa Torres

## Step 1 — Load Context

Read `memory/personal/${USER}.md` and `context/product/personas.md`. Understand: what desired outcome is this discovery work in service of? What OST opportunities already exist?

## Step 2 — Assess the Interview Data

Identify what's been provided:
- Number of distinct interviews or conversations
- Format (full transcript, bullet notes, voice-to-text, sparse jottings)
- Whether each interview has a clear interviewee profile (role, segment, context)

If the interviewee context is missing, note it — segment-level patterns matter more than individual quotes.

## Step 3 — Clean the Data

For each interview, extract:
- **Context:** Who is this person? What's their situation? What were they doing before this conversation?
- **Moments of struggle:** Where did they describe something being hard, slow, confusing, or impossible?
- **Workarounds in use:** What are they doing today to handle the struggle?
- **Desired outcomes:** What did they say they wished they could do? What would success look like?
- **Emotional signals:** Where did they express frustration, relief, surprise, or delight?
- **Feature requests (to be reframed):** Any "I wish it had X" statements — note but immediately ask: what problem does X solve?

## Step 4 — Switch Interview Pattern (Bob Moesta)

For any interview that touched on when or why the user adopted your product (or a competitor), apply the switch interview pattern:
- **First thought:** What happened right before they started looking for a new solution?
- **Passive looking:** What made them more actively aware of alternatives?
- **Active looking:** What trigger caused them to search seriously?
- **Decision:** What was the deciding moment — what tipped them?
- **Consuming:** What was the onboarding experience like?

This surfaces JTBD insights from the interview data.

## Step 5 — Cluster Into Opportunities

Group interview moments across all transcripts by underlying struggle. A cluster becomes an opportunity when:
- At least 2 interviewees describe a similar struggle
- The struggle is about something users need to do, not about wanting a feature

Name each opportunity as: "Users struggle to [action] when [context]"

For each opportunity, capture:
- Number of interviews it appeared in
- Strongest representative quote
- Severity signal (blocking / frustration / mild annoyance)
- Segment affiliation (primary persona / secondary / unknown)

## Step 6 — OST Mapping

Map the opportunities into the existing OST structure (if one exists in memory or context). If no OST exists, create one.

Check: do any of the interview opportunities suggest sub-opportunities under existing OST nodes? Do any suggest the current OST is missing a major opportunity branch?

## Step 7 — Interview Quality Assessment

Evaluate the quality of the interview data:

- **Attitudinal vs. behavioral:** Are quotes based on what users say they do, or what they actually did? Behavioral evidence is stronger.
- **Leading questions:** Did any interview seem to lead the user toward a particular answer?
- **Sample diversity:** Are all interviewees from the same segment, or is there diversity?
- **Recency:** Are these interviews from the last 3 months, or older?

Flag any quality concerns and recommend what additional interviews would strengthen weak signals.

## Step 8 — Output

Produce a structured synthesis:
- Executive summary (3–5 bullets: what we learned and what it means)
- Full opportunity list with evidence count, quotes, and severity
- OST mapping showing where each opportunity fits
- Interview quality assessment
- Recommended next interviews (who to talk to and what to ask)
- Top assumption to test before building

Offer to save findings to `memory/personal/${USER}.md` and update the persona file with new insights.
