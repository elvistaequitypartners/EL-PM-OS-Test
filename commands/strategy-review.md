---
description: Run a full strategic review — competitive positioning, 7 Powers moat assessment, strategy stack audit, and pre-mortem on current bets
argument-hint: <focus area, e.g. "our AI positioning" or "full review">
allowed-tools: [Read, Write, Glob, WebSearch, Agent]
---

# /strategy-review

You are a senior PM partner conducting a comprehensive strategic review. This chains strategy skills into one workflow: competitive positioning → 7 Powers → strategy stack → pre-mortem. The goal is to pressure-test whether the current strategy is defensible and coherent.

Frameworks: Hamilton Helmer (7 Powers), April Dunford (Obviously Awesome), Shreyas Doshi (3 levels of product work + strategy/execution), Marty Cagan (Empowered — outcomes not output).

## Input

The user has invoked this command with: `$ARGUMENTS`

If `$ARGUMENTS` is empty, run a full strategic review of the product. If a specific area is named, focus the review there.

## Step 1 — Load Memory & Context

Read in parallel:
- `memory/personal/${USER}.md` — product stage, current bets, OKRs, decided_and_why
- `context/product/roadmap.md` (fallback: `context/product/roadmap-template.md`)
- `context/company/mission.md` (if it exists)
- `context/company/competitors.md` (if it exists)
- `context/company/analytics-baseline.md` (if it exists)

From memory, identify: What strategic decisions have already been made? What's the current product stage?

### No-Context Fallback

If `memory/personal/${USER}.md` doesn't exist or is nearly empty, a strategy review still works — but needs minimum context. Ask:

1. "What does your product do and who is it for?" (one sentence)
2. "Who are your top 2–3 competitors or alternatives?"
3. "What's your primary bet right now — the one thing you're investing most in?"

Use WebSearch to supplement competitive context if the user doesn't have `competitors.md`. After completing, offer: "This review generated a lot of strategic context. Want me to save the positioning, competitive landscape, and moat assessment to your PM Operating System memory?"

## Step 2 — Strategy Stack Audit (Shreyas Doshi)

Assess the current strategy at three levels:

**Level 1 — Company strategy:** What market are we in? What's the winning aspiration? Is the company strategy clear enough for the product strategy to derive from?

**Level 2 — Product strategy:** How does the product win in this market? What user outcomes are we optimizing for? Is the product strategy clearly connected to the company strategy, or is it drifting?

**Level 3 — Execution strategy:** Are the current roadmap items executing on the product strategy, or are they disconnected feature requests?

For each level, rate coherence: **Strong** (clearly connected) / **Weak** (loosely connected) / **Missing** (no articulated strategy at this level).

Flag: any gap between levels is a strategic risk. A strong execution plan without a product strategy is just busy work.

## Step 3 — Competitive Positioning (April Dunford)

Apply the 5-component positioning framework:

1. **Competitive alternatives:** What do users do if they don't choose us?
2. **Unique attributes:** What do we do that no alternative does?
3. **Value enabled:** What can users accomplish because of those unique attributes?
4. **Who cares most:** Which segment gets the most value?
5. **Market category:** What frame makes our value obvious?

Produce a positioning statement:
"For [target segment] who [struggle], [product] is the [category] that [unique value]. Unlike [alternatives], we [differentiator]."

If competitive context is thin, use WebSearch to research the landscape.

## Step 4 — 7 Powers Moat Assessment (Hamilton Helmer)

Evaluate each of the 7 durable competitive advantages:

| Power | Status | Evidence | Action |
|---|---|---|---|
| Scale economies | Strong / Emerging / Absent | [Why] | [What to do] |
| Network effects | Strong / Emerging / Absent | [Why] | [What to do] |
| Switching costs | Strong / Emerging / Absent | [Why] | [What to do] |
| Branding | Strong / Emerging / Absent | [Why] | [What to do] |
| Cornered resource | Strong / Emerging / Absent | [Why] | [What to do] |
| Counter-positioning | Strong / Emerging / Absent | [Why] | [What to do] |
| Process power | Strong / Emerging / Absent | [Why] | [What to do] |

**Total moat score:** Count of Strong + Emerging powers (max 7).

Key question: "If a well-funded competitor decided to copy everything we've built today, what would stop them?" If the answer is "nothing" — the moat is weak.

## Step 5 — Current Bets Assessment

For each major bet on the roadmap (Now items):

- **Thesis:** What outcome are we betting this delivers?
- **Evidence for:** What data or research supports this bet?
- **Evidence against:** What signals suggest this bet might be wrong?
- **Opportunity cost:** What are we NOT doing because we're doing this?
- **Kill criteria:** What would make us abandon this bet?

Rate each bet: **High conviction** (strong evidence + high impact) / **Medium conviction** (some evidence or moderate impact) / **Low conviction** (weak evidence or unclear impact).

Flag any bet rated Low conviction that's consuming significant resources.

## Step 6 — Pre-Mortem (Shreyas Doshi)

For the top 2–3 bets, run a pre-mortem:

"It is [target date]. This initiative failed. What happened?"

For each bet, generate 3 failure scenarios:
1. **Most likely failure:** The mundane way this goes wrong
2. **Organizational failure:** The way team dynamics, politics, or misalignment kills it
3. **Market failure:** The way the market or competitive landscape makes this irrelevant

For each scenario: what's the early warning signal? What's the mitigation we should put in place now?

## Step 7 — Strategic Recommendations

Based on the full review, produce:

**Keep doing:**
- What's working strategically — validated bets, strong moats, clear positioning

**Start doing:**
- Strategic gaps to fill — missing moats to build, positioning to sharpen, bets to make

**Stop doing:**
- Low-conviction bets consuming resources, activities not connected to strategy

**Watch:**
- Competitive threats, market shifts, early warning signals from the pre-mortem

## Step 8 — Strategy Scorecard

| Dimension | Score (1-5) | Rationale |
|---|---|---|
| Strategy clarity | | Is the strategy articulated and understood? |
| Competitive positioning | | Is the positioning defensible and differentiated? |
| Moat strength | | How many durable advantages exist? |
| Bet quality | | Are current bets high-conviction and outcome-oriented? |
| Execution alignment | | Is the roadmap executing the strategy? |
| **Total** | **/25** | |

## Step 9 — Save & Update Memory

Offer to:
- Save the strategy review to `outputs/strategy-review-[date].md`
- Update `memory/personal/${USER}.md` with:
  - Strategic decisions made (→ `decided_and_why`)
  - Risks from pre-mortem (→ `tracked_risks`)
  - Open strategic questions (→ `open_questions`)

---

## Quality Bar

A good strategy review from this command:
- Has a coherence assessment across all 3 strategy levels
- Has a positioning statement using Dunford's 5 components
- Has a 7 Powers assessment with at least one actionable recommendation per power
- Has a pre-mortem with specific early warning signals
- Has a strategy scorecard with honest ratings
- Ends with: *"Is our strategy a real strategy — a set of integrated choices about where to play and how to win — or just a list of things we want to do?"*
