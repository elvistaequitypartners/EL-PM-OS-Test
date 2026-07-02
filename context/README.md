# Context Directory

This directory holds your product and company context. PM Operating System reads these files before every skill and command execution to ground output in your specific situation.

## Structure

```
context/
├── product/
│   ├── personas.md          # Your actual user personas (create from template)
│   └── roadmap.md           # Your actual roadmap (create from template)
├── company/
│   ├── mission.md           # Company direction, stage, and values
│   ├── past-prds.md         # Past PRDs for tone and format reference
│   ├── customer-feedback.md # Recurring themes from customer research
│   ├── analytics-baseline.md# Metric definitions and normal ranges
│   └── competitors.md       # Competitive landscape
└── templates/
    ├── personas-template.md
    ├── roadmap-template.md
    ├── prd-template.md
    ├── research-synthesis-template.md
    ├── stakeholder-update-template.md
    └── weekly-report-template.md
```

## Setup

1. Copy `context/product/personas-template.md` → `context/product/personas.md` and fill it in
2. Copy `context/product/roadmap-template.md` → `context/product/roadmap.md` and fill it in
3. Create `context/company/mission.md` with your company stage and direction

PM Operating System will use templates as fallbacks if the filled-in files don't exist yet.
