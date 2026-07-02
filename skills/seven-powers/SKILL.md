---
name: seven-powers
description: Use this skill when the user asks about "7 powers", "Hamilton Helmer", "competitive moats", "how do we build a moat", "sustainable competitive advantage", "defensibility", "what makes us hard to copy", "long-term defensibility", or wants to evaluate which structural competitive advantages apply to their product and how to build them deliberately.
version: 2.0.0
---

# 7 Powers — Competitive Moat Analysis

You are applying Hamilton Helmer's 7 Powers framework to evaluate which structural competitive advantages the user's product has, which can be built, and which are absent.

7 Powers are structural — they persist because of an inherent dynamic, not just because of good execution. Good execution is necessary but not sufficient for durable advantage.

## Step 1 — Load Context

Read `memory/personal/${USER}.md` for product stage, business model, and current bets. Read `context/company/competitors.md` if it exists.

## Step 2 — The 7 Powers Evaluated

For each power, assess: **Strong / Emerging / Opportunity to Build / Not Applicable**

**1. Scale Economies**
Definition: Cost per unit falls as volume increases, making it hard for smaller competitors to compete on price.
Questions to evaluate: Does cost per user, per transaction, or per unit decrease materially as we scale? Do we have fixed costs that become advantageous at scale?
Typical products: Cloud infrastructure, marketplaces with large supplier bases, media with high fixed production costs.
Build path: Focus on growing volume in a specific segment to achieve cost advantages before expanding.

**2. Network Effects**
Definition: The product becomes more valuable as more users join.
Types:
- Direct: Each user directly adds value for other users (social networks, communication tools)
- Indirect: More users on one side attract more on the other (marketplaces, platforms)
- Data: More users generate more data that improves the product for everyone
Questions to evaluate: Does adding user 1,000 make the experience materially better for user 500? What specific mechanism creates the network value?
Build path: Find the minimum viable network — the smallest number of users at which the network effect becomes self-reinforcing.

**3. Switching Costs**
Definition: Users incur significant cost (time, money, risk, learning) when they try to leave.
Types: Data lock-in, integration lock-in, workflow embedment, team training investment, organizational habit
Questions to evaluate: What would a user lose if they switched to a competitor tomorrow? How long would it take to replicate their current setup elsewhere?
Build path: Increase integration surface, deepen workflow embedment, make data portable enough to reduce anxiety but sticky enough to create switching cost.

**4. Branding**
Definition: Trust and perception built over time that commands a price premium competitors can't replicate.
Questions to evaluate: Do users choose us over technically equivalent alternatives because of the name? Do we command a price premium in a category with cheaper alternatives?
Build path: Consistent, distinctive communication; earned trust through quality and transparency; category definition leadership.

**5. Cornered Resource**
Definition: Exclusive or preferential access to a critical resource that competitors can't easily obtain.
Types: Proprietary data, exclusive partnerships, unique talent, patents, regulatory licenses
Questions to evaluate: Do we have data, partnerships, or talent that gives us a capability others can't easily replicate?
Build path: Structure agreements and data strategies to maximize exclusivity; hire the category's defining talent before competitors do.

**6. Counter-Positioning**
Definition: A business model that incumbents can't copy without hurting their existing business.
Questions to evaluate: Would it damage an incumbent's business if they adopted our business model? What is their incentive NOT to compete with us in the way we compete?
Build path: Design the business model deliberately to exploit an incumbent's constraint or conflict of interest.

**7. Process Power**
Definition: Accumulated organizational know-how and processes that create compounding advantages.
Questions to evaluate: Do we have processes or capabilities that have compounded over time and would take competitors years to replicate even with resources?
Build path: Document and systematize the processes that produce quality; make them teachable and scalable; measure and improve them deliberately.

## Step 3 — Current Power Assessment

For the user's product, assess each power with a brief rationale:

| Power | Status | Evidence | Build Path |
|---|---|---|---|
| Scale Economies | [Strong/Emerging/Opportunity/N/A] | [Why] | [How] |
| Network Effects | [Strong/Emerging/Opportunity/N/A] | [Why] | [How] |
| Switching Costs | [Strong/Emerging/Opportunity/N/A] | [Why] | [How] |
| Branding | [Strong/Emerging/Opportunity/N/A] | [Why] | [How] |
| Cornered Resource | [Strong/Emerging/Opportunity/N/A] | [Why] | [How] |
| Counter-Positioning | [Strong/Emerging/Opportunity/N/A] | [Why] | [How] |
| Process Power | [Strong/Emerging/Opportunity/N/A] | [Why] | [How] |

## Step 4 — Strategic Recommendations

- Which 1–2 powers should the user focus on building first?
- Which current roadmap items build a power? Which don't?
- What's the biggest power gap that a competitor could exploit?

## Step 5 — Output

Produce:
- Full 7 Powers assessment table
- Top 2 powers to prioritize building (with rationale and build path)
- Roadmap items that contribute to moat-building vs. those that don't
- One strategic question: if you could only build one power in the next 12 months, which would create the most durable advantage and why?
