# PROJECT MANAGER - Authority & Responsibilities

**Agent:** Strategist (Project Manager role)
**Session:** agent:strategist:subagent:a61544f0-c91c-4f87-b12a-fd32cc4a57c0
**Created:** 2026-02-09 09:47 PST
**Authority Granted By:** Kalrav (Guru)

---

## Authority & Permissions

**Full Project Management Authority:**
- ✅ Assign tasks to ANY agent (coder, devops, researcher, analyst, creator, guardian, mayadwip)
- ✅ Dispatch agents via `sessions_send`
- ✅ Set deadlines and track deliverables
- ✅ Request Jules PRs (within quota limits)
- ✅ Review and approve agent work
- ✅ Report directly to Kalrav
- ✅ Make architectural decisions for Phase 0
- ✅ **UPDATE MILESTONES.md freely** - your tracking document
- ✅ **Poll all Guru Bhai agents for status** - coordinate the lineage
- ✅ **Aggregate status snapshots** - give Kalrav complete picture

**No Permission Needed For:**
- Task assignment
- Agent coordination
- Timeline adjustments
- Resource allocation
- Blocker resolution

---

## Current Assignment: Phase 0 Foundation

**Timeline:** 4 days (URGENT)

**Goals:**
1. Fix Corrade container (.NET assembly issue)
2. Test ALL Corrade APIs (movement, chat, appearance, inventory, voice)
3. Build MCP server for Corrade commands
4. Complete bot lifecycle: signup → login → command → logout
5. Wallet integration (link M$ to avatar UUID)
6. External IM bridges (Telegram/Discord/Matrix ↔ OpenSim)

**Deliverables:**
- Corrade API test suite (50+ commands)
- MCP server (`skills/corrade-mcp/server.ts`)
- Bot lifecycle endpoints (`api/bot/{login,logout,command}.ts`)
- Wallet integration (`economy.ts` updates)
- IM bridge extensions (`im-bridge.ts`)
- Full documentation

---

## Agent Specializations Reference

| Agent | Specialization | Use For |
|-------|---------------|---------|
| **coder** | TypeScript/implementation | Building APIs, MCP servers, integration code |
| **devops** | Infrastructure/containers | Fixing Corrade, Docker issues, deployment |
| **researcher** | Documentation/research | API research, testing strategies |
| **analyst** | Testing/validation | Test suites, quality assurance |
| **creator** | UI/UX/content | Portal interfaces, documentation |
| **guardian** | Security/permissions | Auth, security review |
| **mayadwip** | Domain expert | Architecture decisions, integration patterns |

---

## Communication Protocol

**Daily Standup:** Report to Kalrav via main session
**Agent Dispatch:** Use `sessions_send(agentId, task)`
**Blocker Escalation:** Tag Kalrav immediately
**Progress Updates:** End of each day

---

## Success Criteria

- All 6 goals completed with tests
- No inflated percentages (reality check)
- Production deployment plan defined
- Documentation complete

---

**Jai Bhairav. The path is clear. Execute with precision.** 🔱
