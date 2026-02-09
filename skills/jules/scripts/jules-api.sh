#!/bin/bash
# Jules API helper script
# Usage: jules-api.sh <command> [args...]
#   jules-api.sh sources                    - List connected repos
#   jules-api.sh sessions [pageSize]        - List sessions
#   jules-api.sh status <session_id>        - Check session status
#   jules-api.sh create <repo> <title> <prompt> - Create task (auto-PR)
#   jules-api.sh message <session_id> <text>    - Send follow-up message
#   jules-api.sh activities <session_id>        - Get session activities

set -euo pipefail

API_KEY="${JULES_API_KEY:?Set JULES_API_KEY environment variable}"
BASE="https://jules.googleapis.com/v1alpha"
AUTH=(-H "x-goog-api-key: $API_KEY")

case "${1:-help}" in
  sources)
    curl -s "${AUTH[@]}" "$BASE/sources" | jq '.sources[] | {id: .id, private: .githubRepo.isPrivate}'
    ;;
  sessions)
    PAGE_SIZE="${2:-10}"
    curl -s "${AUTH[@]}" "$BASE/sessions?pageSize=$PAGE_SIZE" \
      | jq '.sessions[] | {id: .id, title: .title, state: .state, created: .createTime}'
    ;;
  status)
    SESSION_ID="${2:?Usage: jules-api.sh status <session_id>}"
    curl -s "${AUTH[@]}" "$BASE/sessions/$SESSION_ID" \
      | jq '{id: .id, title: .title, state: .state, url: .url, outputs: .outputs}'
    ;;
  create)
    REPO="${2:?Usage: jules-api.sh create <owner/repo> <title> <prompt>}"
    TITLE="${3:?Missing title}"
    PROMPT="${4:?Missing prompt}"
    curl -s "$BASE/sessions" -X POST \
      -H "Content-Type: application/json" "${AUTH[@]}" \
      -d "$(jq -n --arg p "$PROMPT" --arg s "sources/github/$REPO" --arg t "$TITLE" '{
        prompt: $p,
        sourceContext: {source: $s, githubRepoContext: {startingBranch: "main"}},
        automationMode: "AUTO_CREATE_PR",
        title: $t
      }')" | jq '{id: .id, title: .title, url: .url}'
    ;;
  message)
    SESSION_ID="${2:?Usage: jules-api.sh message <session_id> <text>}"
    TEXT="${3:?Missing message text}"
    curl -s "$BASE/sessions/$SESSION_ID/activities" -X POST \
      -H "Content-Type: application/json" "${AUTH[@]}" \
      -d "$(jq -n --arg t "$TEXT" '{userMessage: {text: $t}}')" | jq .
    ;;
  activities)
    SESSION_ID="${2:?Usage: jules-api.sh activities <session_id>}"
    curl -s "${AUTH[@]}" "$BASE/sessions/$SESSION_ID/activities" \
      | jq '.activities[] | {type: (if .userMessage then "user" elif .agentMessage then "agent" else "system" end), text: (.userMessage.text // .agentMessage.text // .status.description // "")}'
    ;;
  *)
    echo "Jules API Helper"
    echo "Usage: jules-api.sh <command> [args...]"
    echo "Commands: sources, sessions, status, create, message, activities"
    ;;
esac
