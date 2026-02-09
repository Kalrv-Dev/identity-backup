---
name: jules
description: Interact with Jules (Google's AI coding agent) via REST API. Create coding tasks, review PRs, list sessions, poll status, and pull results. Use when user wants to assign coding tasks to Jules, check Jules session status, list Jules sessions, create PRs via Jules, or automate code changes on GitHub repos connected to Jules.
---

# Jules — Google AI Coding Agent

## Setup

API key must be set as environment variable:
```bash
export JULES_API_KEY="your-key-here"
```

If not set, check `~/.bashrc` or ask user for the key.

Base URL: `https://jules.googleapis.com/v1alpha`
Auth header: `x-goog-api-key: $JULES_API_KEY`

## Quick Reference

### List connected repos
```bash
curl -s -H "x-goog-api-key: $JULES_API_KEY" \
  "https://jules.googleapis.com/v1alpha/sources" | jq '.sources[].id'
```

### Create a task (auto-PR)
```bash
curl -s 'https://jules.googleapis.com/v1alpha/sessions' \
  -X POST -H "Content-Type: application/json" \
  -H "x-goog-api-key: $JULES_API_KEY" \
  -d '{
    "prompt": "TASK DESCRIPTION HERE",
    "sourceContext": {
      "source": "sources/github/OWNER/REPO",
      "githubRepoContext": { "startingBranch": "main" }
    },
    "automationMode": "AUTO_CREATE_PR",
    "title": "PR Title"
  }'
```

`automationMode` options:
- `"AUTO_CREATE_PR"` — auto-create PR when done
- Omit field — no auto-PR (manual export)

### Check session status
```bash
curl -s -H "x-goog-api-key: $JULES_API_KEY" \
  "https://jules.googleapis.com/v1alpha/sessions/SESSION_ID" \
  | jq '{state: .state, title: .title}'
```

States: `QUEUED`, `IN_PROGRESS`, `COMPLETED`, `FAILED`

### List sessions
```bash
curl -s -H "x-goog-api-key: $JULES_API_KEY" \
  "https://jules.googleapis.com/v1alpha/sessions?pageSize=10" \
  | jq '.sessions[] | {id: .id, title: .title, state: .state}'
```

Supports `pageSize` and `pageToken` for pagination.

### Send follow-up message to session
```bash
curl -s "https://jules.googleapis.com/v1alpha/sessions/SESSION_ID/activities" \
  -X POST -H "Content-Type: application/json" \
  -H "x-goog-api-key: $JULES_API_KEY" \
  -d '{"userMessage": {"text": "Also fix the typo on line 42"}}'
```

### Get session activities (conversation log)
```bash
curl -s -H "x-goog-api-key: $JULES_API_KEY" \
  "https://jules.googleapis.com/v1alpha/sessions/SESSION_ID/activities" \
  | jq '.activities[]'
```

## CLI Alternative

If `jules` CLI is installed (`npm i -g @google/jules`) and authenticated:
```bash
jules new --repo OWNER/REPO "task description"
jules remote list --session
jules remote pull --session SESSION_ID
jules teleport SESSION_ID  # clone + checkout + apply patch
```

Note: CLI requires browser OAuth login (`jules login`). May not work in headless/WSL environments. Prefer API for automation.

## Task Prompting Tips

- Be specific about file paths and what to change
- Mention the branch (default: main)
- For fixes: describe the bug, expected behavior, and affected code
- For features: describe the desired outcome and constraints
- Jules can read the full repo — reference existing patterns

## Known Repos (as of 2026-02-08)

| Source | Repo |
|--------|------|
| `sources/github/siddh7007/Ananta-Platform-Saas` | Main SaaS platform |
| `sources/github/siddh7007/mayadwip-portal` | MaYaDwip virtual world portal |

## Limits

- Daily session limit: 300 (Ultra plan)
- API is alpha — specs may change
- Jules cannot merge PRs — only create them
- Jules works on one branch per session
