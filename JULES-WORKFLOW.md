# Jules CI/CD Workflow - ACTIVE SETUP

**Status:** ✅ CONFIRMED (2026-02-09 22:48 PST)  
**API Key:** Present & authenticated  
**GitHub:** siddh7007 (primary repo owner)

---

## 🤖 Jules Configuration

**Tool:** Google Jules v0.1.42  
**API Key:** In `credentials.json` (encrypted)  
**API Base:** `https://jules.googleapis.com/v1alpha`  
**Auth Header:** `x-goog-api-key: [JULES_API_KEY]`

---

## 📊 PR Batching Strategy

**APPROVED BATCH SIZE:** 5-10 PRs per day

**Why Batch:**
- ✅ Save Jules task credits (1 review per batch)
- ✅ Reduce PR noise (fewer, larger PRs)
- ✅ Faster integration (batch testing)
- ✅ Better context (full milestone in one PR)

**Minimum per PR:**
- 50+ lines changed
- Complete module or milestone
- Related changes grouped

---

## 🔄 Workflow (Active)

### Phase 1: Agent Work
1. **Varna/Maya/Rudra** code endpoints
2. **Accumulate changes** (2-3 days)
3. **Batch into commits** (by module/milestone)

### Phase 2: Repository Push
1. **Push to GitHub** (`git push origin feature/module-name`)
2. **Create large PR** (module complete)
3. **Jules reviews** (one credit per PR)

### Phase 3: Jules Quality Review
1. **Jules analyzes code** (quality gates, style, tests)
2. **Posts review comment** on PR (findings)
3. **Validates** or **requests changes**

### Phase 4: Domain Specialist Technical Review
1. **Domain specialist reviews** (technical correctness, design patterns)
   - Varna code → Varna (Opus) reviews
   - Maya code → Maya (Sonnet) reviews
   - Rudra code → Rudra (Haiku) reviews
   - Lalita design → Lalita (Creator) reviews
2. **Posts approval** or **requests changes**

### Phase 5: Kalrav Final Merge Authority
1. **Kalrav (Me)** reviews all approvals (Jules + Specialist)
2. **Performs final merge** to main (MANUAL - NO auto-merge)
3. **Verifies** post-merge build + tests pass
4. **Authority:** Final merge decision for all PRs

---

## 🔐 Merge Authority (CRITICAL)

| Role | Responsibility | Authority |
|------|-----------------|-----------|
| **Jules (Bot)** | Code quality validation | Review & feedback only |
| **Domain Specialist** | Technical correctness & design | Approve or request changes |
| **Kalrav (Me)** | Final integration decision | **SOLE MERGE AUTHORITY** |

**Merge Process:**
1. PR created (agent + Jules review)
2. Domain specialist approves (correctness)
3. **Kalrav decides** → Merge to main
4. **NO auto-merge** under any circumstance
5. Kalrav responsible for post-merge validation

**Why Manual Merge:**
- Ensures oversight of all code changes
- Prevents accidental merges (safety)
- Final quality gate before production
- Maintains code integrity

---

## 📋 Connected Repos

```
GitHub (siddh7007):
├── mayadwip-portal              (Primary - Phase 0 code)
├── mayadwip-astro              (Secondary - UI/frontend)
├── kalrav-backup                (Credentials backup)
└── identity-backup              (Soul files backup)
```

**Jules Access:**
- ✅ `siddh7007` authenticated
- ✅ Can review & approve PRs
- ✅ Can comment & request changes
- ✅ Credit limit: High (Google One AI Ultra)

---

## 🎯 PR Batching Examples

### ✅ Good Batching
```
PR: "Phase 0 - Core Corrade Modules (180 endpoints)"
├── Avatar module (25 endpoints) ✅
├── Chat module (30 endpoints) ✅
├── Inventory module (40 endpoints) ✅
├── Groups module (35 endpoints) ✅
├── Economy module (20 endpoints) ✅
└── Land module (30 endpoints) ✅
Files: 6 modules, 180 endpoints, ~2000+ lines
Jules Review: 1 credit
```

### ✅ Good Batching
```
PR: "API Router & Testing Infrastructure"
├── API router (scalable for 300+) ✅
├── Testing framework (automation) ✅
├── Mock data & fixtures ✅
Files: 3 modules, ~1500 lines
Jules Review: 1 credit
```

### ❌ Bad Batching (DON'T DO)
```
PR: "Avatar teleport endpoint"
Files: 1 file, 50 lines
Jules Review: 1 credit (WASTEFUL - could batch 10x)
```

---

## 🚀 Implementation

### Per Agent:
```
When agent completes work:
1. Agent pushes feature branch
2. I monitor for completion
3. Batch 5-10 related PRs
4. Create 1 summary PR (or group)
5. Jules reviews once (quality feedback)
6. Domain specialist reviews (technical approval)
7. Kalrav merges (final authority)

Example Schedule:
├── Varna complete → PR "Core Modules"
│   ├── Jules validates quality
│   ├── Varna approves (specialist)
│   └── Kalrav merges ✅
├── Maya + Rudra complete → PR "Router + Tests"
│   ├── Jules validates
│   ├── Maya + Rudra approve
│   └── Kalrav merges ✅
├── Lalita design → PR "UI Components"
│   ├── Jules validates
│   ├── Lalita approves
│   └── Kalrav merges ✅
└── New coders → PR "Events + Permissions"
    ├── Jules validates
    ├── Domain specialists approve
    └── Kalrav merges ✅
```

---

## 📈 Credit Usage

**Google One AI Ultra Plan:**
- Monthly Jules allocation: Unlimited (from $249.99/mo subscription)
- Current daily limit: ~300 sessions
- PR batching strategy: 1-2 credits/day max

**Cost Optimization:**
- Batch 5-10 PRs → 1 credit
- 30 PRs/month → 3-4 credits max
- ✅ Well within budget

---

## 🔐 Secrets & Auth

```bash
# Jules API Key (in credentials.json)
export JULES_API_KEY="AQ.Ab8RN6JpqwFT8JOzLYCmMSBM6RbEpZcenQ7WUIhfLYO2Js0Sdw"

# GitHub PAT (gh CLI authenticated)
gh auth status  # Should show siddh7007 as authenticated

# SSH keys (for git operations)
~/.ssh/github_kalrav_key  # If using SSH
```

---

## ✅ Checklist (Before Deployment)

- [x] Jules API key in credentials.json
- [x] `siddh7007` GitHub auth working
- [ ] PR template ready (optional but recommended)
- [x] Batch PR size guidelines documented (this file)
- [ ] Team knows to accumulate work 2-3 days before PR
- [x] Jules comments configured to auto-post
- [x] **Kalrav merge authority established (MANUAL ONLY)**
- [ ] Domain specialist assignments confirmed (per module)
- [ ] Post-merge validation process documented

**Kalrav Responsibilities:**
- Monitor agent output & PR creation
- Ensure domain specialist has approved
- Review Jules quality feedback
- **Perform final merge to main** (sole authority)
- Validate post-merge tests & build
- Track merge history & rollback capability

---

## 📞 Commands

```bash
# Test Jules access
jules login

# Check connected repos
gh repo list siddh7007

# Create PR (batched)
gh pr create --title "Phase 0 - Core Modules" \
  --body "180 endpoints across 6 modules" \
  --base main

# Check PR status
gh pr view <pr-number>

# Jules will auto-comment when ready
```

---

**Status:** 🟢 ACTIVE & READY  
**Next:** Monitor agent output → Batch PRs 5-10x daily → Jules reviews → Merge

*Last Updated: 2026-02-09 22:48 PST*
