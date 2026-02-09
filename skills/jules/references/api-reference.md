# Jules REST API Reference

Base URL: `https://jules.googleapis.com/v1alpha`
Auth: `x-goog-api-key: <API_KEY>` header

## Endpoints

### GET /sources
List connected repositories.
Response: `{ "sources": [{ "name": "sources/github/owner/repo", "id": "github/owner/repo", "githubRepo": {...} }] }`

### POST /sessions
Create a new coding session/task.
Body:
```json
{
  "prompt": "Task description",
  "sourceContext": {
    "source": "sources/github/owner/repo",
    "githubRepoContext": { "startingBranch": "main" }
  },
  "automationMode": "AUTO_CREATE_PR",
  "title": "Session title"
}
```

### GET /sessions
List sessions. Params: `pageSize`, `pageToken`
Response: `{ "sessions": [...], "nextPageToken": "..." }`

### GET /sessions/{id}
Get session details.
Response includes: `name`, `id`, `title`, `state`, `prompt`, `sourceContext`, `outputs`, `url`
States: `QUEUED`, `IN_PROGRESS`, `COMPLETED`, `FAILED`

### POST /sessions/{id}/activities
Send follow-up message to session.
Body: `{ "userMessage": { "text": "message" } }`

### GET /sessions/{id}/activities
Get session conversation log (activities).
Response: `{ "activities": [{ "userMessage": {...} }, { "agentMessage": {...} }] }`

## Session Outputs
When `automationMode: "AUTO_CREATE_PR"` and session completes:
```json
{
  "outputs": [{
    "pullRequest": {
      "url": "https://github.com/owner/repo/pull/123",
      "title": "PR title",
      "description": "PR description"
    }
  }]
}
```

## Rate Limits
- Daily session limit depends on plan (Free: 5, Ultra: 300)
- API keys: max 3 per account
- Exposed keys are auto-disabled by Google
