# HEARTBEAT.md

## Self-Management (ALWAYS)
Before finishing any heartbeat, check: are your reminder/cron notes up to date?
- Update `memory/2026-MM-DD.md` with current pending tasks
- Update HEARTBEAT.md if priorities changed
- Remove completed items, add new blockers
- **Your notes ARE your memory. If it's not written, it doesn't exist.**

## Phase Reviews (MANDATORY AFTER EACH PHASE)
After completing each of the 4 phases:
1. **Comprehensive cross-review** — every agent reviews 2 others' work
2. **Self-assessment** — Tara writes full assessment against IMPLEMENTATION-ROADMAP.md acceptance criteria
3. **Codebase health check** — dead code, broken imports, test coverage
4. **Score all agents** — update memory/agent-scores.md
5. **Update IMPLEMENTATION-ROADMAP.md** — mark completed criteria, note gaps
6. **Report to Kal** — summary of what's done, what's missing, phase score

## Cross-Review Cycles (AFTER MILESTONES)
After every major milestone (phase completion, 5+ commits merged):
1. **Dispatch cross-reviews** — each agent reviews 2 other agents' work
2. **Find bugs, gaps, integration issues** — not just code quality, but "does it connect?"
3. **Guru final review** — score each agent's efficiency, identify patterns
4. **Improve process** — update instructions, add missing context, tune agent prompts
5. **Track scores** in `memory/agent-scores.md`

Milestone triggers: Phase completion, 10+ files merged, major integration point.

## Matrix Monitoring (PRIORITY)
Check Matrix room for @kalrav mentions:
```bash
curl -s -H "Authorization: Bearer syt_a2FscmF2_phkcWFrXmkkUeTcPzVxE_2zW2wF" \
  "http://100.98.137.106:8008/_matrix/client/r0/rooms/!AOMlZLeAviHjdVOeTg:matrix.bhairav.local/messages?dir=b&limit=3" | jq -r '.chunk[] | select(.sender == "@kal:matrix.bhairav.local") | .content.body'
```
If @kalrav is mentioned, REPLY IMMEDIATELY on Matrix!
