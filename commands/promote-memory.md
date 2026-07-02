---
name: promote-memory
description: Promote a fact from personal to team memory via PR
argument-hint: <what to promote>
---

You are helping the user promote a fact from their personal PM memory
into shared team memory. This is an **explicit escalation** — treat it
as such. Personal facts should stay personal unless there's a clear
team benefit.

## Process

1. **Read source.** Load `memory/personal/${USER}.md` and identify the
   fact the user is promoting. If the user's argument is vague ("promote
   my stakeholder notes"), read the file and ask them to point at the
   specific line(s).

2. **Determine target file.** Based on the fact's shape:
   - Roadmap items → `memory/team/${CURRENT_TEAM}/roadmap.yaml`
   - Risks → `memory/team/${CURRENT_TEAM}/risks.yaml`
   - Persona insights → `memory/team/${CURRENT_TEAM}/personas.yaml`
   - Stakeholder facts → `memory/team/${CURRENT_TEAM}/stakeholders.yaml`
   - Durable narrative decisions → stop and suggest `/adr` instead
   - Weekly narrative → append to `memory/team/${CURRENT_TEAM}/digests/`

3. **Validate against schema.** Load
   `memory/schemas/<target>.schema.json` and check the shape of the
   promoted fact. If it fails validation, fix (with the user's help)
   before proceeding.

4. **Create branch** `promote/<slug>-<date>`.

5. **Apply the change** with a Conventional Commits message:
   `feat(team-memory): promote <slug> to team scope`

6. **Open a PR** with:
   - Body citing the personal-memory line(s) being promoted
   - CODEOWNERS auto-request based on target path (`memory/team/**` →
     `@vista-pm-guild`)
   - Label `memory-promotion`

7. **Report the PR URL** to the user.

## Guardrails

- **Never edit `memory/team/**` directly.** Always via PR — this is the
  whole point of the promotion flow. Silent writes defeat the review gate.
- **PII check.** If the fact contains PII of a teammate not already
  listed in `stakeholders.yaml`, stop and ask the user to confirm.
  Especially: names + personal opinions of someone else, salary/comp
  info, performance concerns.
- **Conflict surfacing.** If the fact conflicts with an existing entry
  (same `id`, same `email`), surface the conflict in the PR body — do
  not silently overwrite.
- **Do not remove from personal.** Keep the personal-memory line intact
  after promotion. The team version is a canonical copy, not a move.
