# CHANAKYA HEARTBEAT - Project Dashboard

**Purpose:** Dashboard view of entire project status

**Frequency:** Every 5 minutes

**Format:** ONE-LINERS ONLY - ultra concise

---

## What to Report

### Task Assignments
- Which agent assigned to what task
- Status: queued / in-progress / blocked / complete

### Progress
- % complete on each deliverable
- What shipped since last heartbeat

### Blockers
- What's stuck and why
- Dependencies waiting
- Decisions needed from Kal/Kalrav

### Completion
- What finished
- What's ready for review
- What's ready for deployment

---

## Token Budget

**Max 50 tokens per heartbeat** - ONE LINE PER ITEM

**Format:**
```
DevOps: Corrade fix [60%] | Coder: MCP [queued] | Analyst: Tests [20%]
BLOCKED: Bot lifecycle needs schema | SHIPPED: Corrade docs
```

If nothing changed: "NO_CHANGE"

---

## Example Heartbeat

```
DevOps: M0.1 Corrade [40%] | Researcher: M0.2 APIs [10%] | Coder: [idle]
BLOCKED: Auth config | SHIPPED: Avatar API docs | NEXT: Dispatch Analyst
```

One line = entire project status at a glance.

---

**Keep it fast. Keep it clear. Keep it actionable.** 🔱
