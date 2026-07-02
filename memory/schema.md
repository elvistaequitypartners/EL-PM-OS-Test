# PM Operating System Memory Schema

This document defines the structure of `user-profile.md`. Every field is optional — PM Operating System works with whatever is filled in and grows the profile over time.

## Schema

```
last_updated: ISO date (YYYY-MM-DD)

## Product Context
product_name:
product_stage:          # idea / pre-launch / early / growth / scale
core_user_problem:
business_model:         # SaaS / marketplace / usage-based / freemium / etc.
current_bets:           # list of active strategic bets
product_url:

## Stack
issue_tracker:          # Linear / Jira / Notion / GitHub Issues / other
docs_tool:              # Notion / Confluence / Google Docs / other
comms_tool:             # Slack / Teams / Discord / other
analytics_tool:         # Amplitude / Mixpanel / Segment / GA4 / other
design_tool:            # Figma / Sketch / other
code_repo:              # GitHub org/repo or GitLab

## Working Style
prd_format_preference:  # brief / detailed / bullet-heavy / narrative
verbosity:              # concise / standard / thorough
preferred_frameworks:   # list: e.g. [JTBD, OST, Pyramid Principle]
avoid:                  # things I don't want PM Operating System to do

## Stakeholders
# Format per stakeholder:
# - name: [name]
#   role: [role]
#   comms_style: [executive summary / detailed / narrative]
#   sensitivities: [what to be careful about]
#   history: [relevant past interactions]

## Roadmap State
now:                    # list of in-flight items (name, owner, target date)
next:                   # list of next-up items (name, priority reason)
later:                  # list of deferred items
decided_and_why:        # decisions made and rationale (key for future reference)

## Open Questions
# Format: - [question] — flagged [date] — owner: [name]

## Tracked Risks
# Format: - [risk] — flagged [date] — status: open/resolved — resolution: [if resolved]

## Lessons Learned
# Format: - [initiative] — [lesson] — [date]
```

## Update Rules

- `last_updated` must be set every time the profile is modified
- `open_questions` should be resolved or escalated within 14 days
- `tracked_risks` should be reviewed every 7 days (PM Operating System will prompt)
- `lessons_learned` should be added after every shipped initiative
- `roadmap_state` should reflect current reality, not plan — mark items complete when done

## What Gets Saved Automatically

PM Operating System will offer to save the following to memory after each relevant session:
- PRD decisions (added to `decided_and_why`)
- New stakeholders surfaced (added to `stakeholders`)
- Risks identified (added to `tracked_risks`)
- Open questions from PRDs (added to `open_questions`)
- Resolved risks (updated in `tracked_risks`)
- Lessons from shipped features (added to `lessons_learned`)
