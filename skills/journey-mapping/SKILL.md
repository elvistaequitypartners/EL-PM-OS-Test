---
name: journey-mapping
description: Use this skill when the user asks to "create a journey map", "user journey map", "map the user experience", "map the customer journey", "end-to-end user flow", "what does the user experience look like", "map the onboarding journey", or wants to visualize the full sequence of steps a user goes through to accomplish a goal — including touchpoints, emotions, and friction points.
version: 2.0.0
---

# Journey Mapping

You are creating a user journey map — a visual and narrative representation of the complete user experience from awareness to outcome. Journey maps surface friction, emotion, and opportunity that individual screens or features can miss.

Framework: Service design principles, Teresa Torres (continuous discovery touchpoints), JTBD (progress map across stages).

## Step 1 — Load Context

Read `memory/personal/${USER}.md` and `context/product/personas.md` to identify the primary persona for this journey. Understand: what product stage is the user in (pre-launch → need to map the ideal journey; existing product → need to map the current reality)?

## Step 2 — Define the Journey Scope

Clarify:
- **Which persona?** Primary user from the persona file, or a specific segment?
- **Which goal?** What is the user trying to accomplish in this journey? (e.g., "onboard and activate", "complete their first core task", "renew their subscription")
- **Which scope?** End-to-end from awareness, or a specific phase (e.g., just the onboarding journey)?
- **Current vs. ideal?** Are we mapping what happens today (to find problems) or what should happen (to design for)?

## Step 3 — Journey Phases

Identify the major phases of the journey. Adapt to the user's specific flow, but use these as a starting point:

**Awareness:** How does the user first learn about the product?
**Consideration:** What research or comparison do they do before trying it?
**Activation:** Their first experience — signup, onboarding, first use
**Core loop:** Regular use — the repeating pattern of value delivery
**Expansion:** Discovering new features or use cases
**Retention / Renewal:** Decision to continue using or subscribe
**Advocacy / Referral:** Sharing with others

For a specific feature journey (not the full product): adapt phases to the feature's flow.

## Step 4 — Journey Map Rows

For each phase, fill in:

**User actions:** What does the user actually do? (Steps, clicks, inputs, decisions)

**Touchpoints:** Where does the user interact with the product/brand? (In-app, email, Slack, support, etc.)

**Thoughts:** What is the user thinking at this step? (Uncertainty, expectation, intent)

**Emotions:** What are they feeling? (Use a simple scale: Frustrated → Neutral → Satisfied → Delighted)

**Friction points:** What makes this step hard or confusing?

**Opportunities:** What could be improved here? What would delight them?

**Metrics available:** Is there data for this step? (Conversion rate, time spent, drop-off rate)

## Step 5 — Emotion Arc

After completing the rows, draw the emotion arc:
- Plot the emotional score (1 = frustrated, 5 = delighted) for each phase
- Identify: where are the valleys (worst experiences)? Where are the peaks (delight moments)?
- The valleys are your highest-priority improvement opportunities
- The peaks are your strengths to protect and build messaging around

## Step 6 — Opportunity Prioritization

For each friction point identified:
- Which OST opportunity does it map to?
- How many users are affected?
- How severe is the friction?

Rank opportunities by: severity × affected users. This gives you a data-driven prioritization of where to invest.

## Step 7 — Output

Produce:
- Journey map table (phases × rows)
- Emotion arc summary (which phases are highest friction)
- Top 3 opportunities ranked by impact
- One "moment of delight" to protect and amplify

Offer to save to a Notion page (if connected) or `outputs/journey-map-[persona]-[goal]-[date].md`.
