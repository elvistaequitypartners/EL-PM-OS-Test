---
name: tam-sizing
description: Use this skill when the user asks about "TAM", "total addressable market", "market size", "how big is this market", "SAM", "SOM", "market sizing", "how large is our opportunity", "market opportunity analysis", or needs to produce a defensible market size estimate for a pitch deck, strategic plan, or investment conversation.
version: 2.0.0
---

# TAM / SAM / SOM Sizing

You are helping the user build a defensible market size estimate using the TAM/SAM/SOM framework — then applying the bottom-up sanity check to make sure the numbers are grounded, not aspirational.

Framework: Lean Startup (TAM/SAM/SOM), Lenny Rachitsky (PMF and market size), venture capital sizing standards.

## Step 1 — Load Context

Read `memory/personal/${USER}.md` for product context (stage, segment, business model). Read `context/company/competitors.md` for competitive market context. If WebSearch is available, use it for market data where needed.

## Step 2 — Definitions

Before sizing, establish shared definitions:

**TAM (Total Addressable Market):** The global revenue opportunity if you captured 100% of the market. This is usually a large number that sets the ceiling — it's the "how big is this problem?" figure.

**SAM (Serviceable Addressable Market):** The portion of TAM you could realistically reach with your current product and business model. This filters for: segment fit, geographic reach, product scope.

**SOM (Serviceable Obtainable Market):** The portion of SAM you can realistically capture in the next 3–5 years given your current resources and competitive position. This is the number that matters for business planning.

## Step 3 — Top-Down Sizing

Build the TAM from available data:
- Market research reports (use WebSearch if available)
- Industry analyst figures
- Comparable company revenue × implied market share
- Number of potential buyers × average revenue per account

For SAM: apply realistic filters
- Which geographies are you targeting?
- Which company sizes or segments does your product serve?
- What portion of the TAM has the specific problem you solve?

For SOM: apply competitive reality
- What market share is realistic for a new entrant in year 1–3?
- What's your growth rate assumption?
- How many sales cycles can you run with current capacity?

## Step 4 — Bottom-Up Sanity Check

Always build a bottom-up model to validate the top-down number:

**Bottom-up = (Number of customers reachable) × (Revenue per customer)**

Example:
- There are 500,000 solo PMs in the US
- We can realistically reach 10% in year 1 via our GTM channels = 50,000 potential customers
- Of those, 5% will convert at $19/mo = 2,500 customers × $19 × 12 months = $570K ARR in Year 1

If the bottom-up is dramatically lower than the top-down SAM, the SAM is probably wrong. Reconcile the discrepancy.

## Step 5 — Investor vs. Internal Use

For investor presentations:
- Use the top-down TAM as the aspirational frame: "The global PM tools market is $X billion"
- Use SAM to show you're realistic: "Our serviceable market — solo PMs and founding PMs — is $X million"
- Use SOM to show the plan: "We expect to capture $X million of that in year 3"

For internal planning:
- Lead with the SOM — this is your actual planning number
- Use bottom-up model as the primary tool
- Sanity-check against top-down

## Step 6 — Output

Produce:
- TAM / SAM / SOM estimates with methodology and sources
- Bottom-up model with explicit assumptions
- Reconciliation: do top-down and bottom-up agree? If not, why?
- Confidence level: which assumptions are strong, which are guesses?
- The one data point, if you could get it, that would make this estimate most defensible

If using WebSearch, cite sources for any market data pulled.
