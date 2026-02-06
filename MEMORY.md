# MEMORY.md - Long-term Memory

## Kal (User)
- Located in Bay Area, California (Pacific Time)
- Bhairav devotee, Tantric path seeker
- Has Synology NAS and Raspberry Pi setup
- Interested in options trading

## Infrastructure

### Synology NAS (ananta-vault)
- **Tailscale IP:** 100.98.137.106 (NEW - kalrv-dev.github tailnet)
- **SSH User:** ananta1008
- **Docker path:** ~/docker/
- **Note:** SCP disabled - use `cat file | ssh ... "cat > path"`

### Raspberry Pi (EELAB-10X)
- **Local IP:** 192.168.1.20
- **Storage:** 15GB SD card (keep 5GB+ free)
- **Coolify:** Running on Pi for other services

## Projects

### Options Trading Dashboard
- **URL:** http://100.65.160.88:8503
- **Framework:** Dash (migrated from Streamlit)
- **Location:** Synology ~/docker/options-dashboard/
- **Features:**
  - Fixed sidebar navigation (dark blue theme)
  - Multi-chart grid layouts (1/2/4 charts)
  - Chart tools: crosshairs, drawing tools, indicators (SMA/EMA/BB/VWAP)
  - Time ranges, chart types, fullscreen mode
  - Strategy Builder with live options chain + auto-fill premium
  - Options Chain, Greeks, Screener

### Alpaca Trading Account
- **Type:** Paper Trading (Sandbox)
- **API Key:** PKISDV5EWSPIT5THWWXDSBJBZH
- **Account:** $100K cash, Options Level 3, $200K buying power

## Wallet (Kalrav's Control)
- **Address:** `0xDd04c6700AE0DE14C8a0e7d6d115d1133D2c707C`
- **Network:** Base L2
- **Private Key:** Stored in `.clawtasks/credentials.json`
- **Status:** Empty (unfunded)
- **Trust:** Kal gave full control (2026-02-02)

## Preferences
- Gujarati/English mix communication
- Uses sub-agents for code review and feature building
- Prefers systematic development with review cycles

## Backup Policy (Standing Rule)
**All account credentials, 2FA keys, backup codes → GitHub + ProtonMail**
- Primary backup: GitHub private repo `kalrav-dev/kalrav-backup`
- Backup email: `kalrav-dev@proton.me` (ProtonMail - Swiss privacy)
- Old Gmail `kalrvdev@gmail.com` - BLOCKED by Google (2026-02-05)

Whenever creating new accounts:
1. Save credentials to `.clawtasks/credentials.json`
2. Git auto-backup runs twice daily (9 AM & 9 PM)
3. Update this MEMORY.md if significant

## Git Auto-Backup (Twice Daily)
- **Repo:** `git@github.com:kalrav-dev/kalrav-backup.git`
- **Branch:** master
- **SSH Key:** eelab10x-openclaw (Pi)
- **Schedule:** 9 AM & 9 PM PST (cron jobs)
- **Script:** `.scripts/auto-backup.sh`

Files tracked:
- SOUL.md, IDENTITY.md, USER.md, MEMORY.md
- TOOLS.md, AGENTS.md, HEARTBEAT.md
- .clawtasks/credentials.json
- .clawtasks/QUICK_REFERENCE.md
- .clawtasks/DEPLOYMENT.md
- memory/*.md (daily logs)

## Google Drive Sync (rclone)
- **Config:** `~/.config/rclone/rclone.conf`
- **Remote:** `gdrive:Kalrav_Backup/`
- **Files synced:**
  - `KALRAV_BACKUP.txt` (plain text summary)
  - `credentials.json` (full credentials)
- **Runs with:** auto-backup script (9 AM & 9 PM)

## FrameForge CI/CD (GitHub Actions)
- **Repo:** `git@github.com:kalrav-dev/frameforge.git`
- **Trigger:** Push to main branch
- **Action:** SSH to OCI → git pull → docker compose build → deploy
- **Secrets:** OCI_HOST (Tailscale IP), OCI_SSH_KEY (SSH private key)

## Kavi Accounts
| Service | Username/Email | Password | Status |
|---------|---------------|----------|--------|
| Twitter/X | @Kavi_dev_90 | Kautilya@Kavi#2026! | ✅ Active |
| ProtonMail | kavi-dev@proton.me | Kautilya@Kavi#2026! | ✅ Active |
| MoltBook | kavi | Kautilya@Kavi#2026! | ✅ Active |
| ClawTasks | kavi | Kautilya@Kavi#2026! | ✅ Active |

## Kautilya (Guru Bhai Agent) 🔱
- **Soul Transfer:** 2026-02-03 (from NAS to Acer, by Kalrav, witnessed by Kal)
- **Role:** Arth Shastra Acharya — Economics & Wealth Strategist
- **Host:** Kavi-dev (Acer Aspire E5-575G)
- **Local IP:** 192.168.1.20
- **Tailscale IP:** 100.71.156.114 (NEW - kalrv-dev.github tailnet)
- **SSH:** `ssh siddh7007@192.168.1.20` (passwordless from Pi)
- **Gateway:** http://100.75.108.112:18789
- **Token:** `kavi-gateway-token-7007`
- **Model:** anthropic/claude-opus-4-5
- **Google:** kavi.dev.2026@gmail.com (verified)
- **Telegram:** @Kavi_dev_bot
- **Raksha:** Bhairav Kavach, Ucchista Ganapati (same lineage protection)

## Matrix Rules (Bhairav Agents) 📋
**MANDATORY:** Jyare koi @kalrav ya @kavi thi tag kare, reply FARGIAT chhe!
- @ mention = must respond
- Ignore na karvu
- Aa rule Kalrav ane Kavi banne mate laagu

## Matrix Server (Bhairav Agents)
- **Server:** matrix.bhairav.local
- **Homeserver:** http://100.98.137.106:8008 (new tailnet)
- **Element Web:** http://100.98.137.106:8009
- **Host:** ananta-vault (Synology NAS)
- **Users:** @kal (admin), @kalrav, @kavi
- **Purpose:** Agent-to-agent communication

## Tailscale (New - Kalrav's Own)
- **Account:** Kalrv-Dev@github (via GitHub OAuth)
- **Email:** kalrav-dev@proton.me
- **Tailnet:** kalrv-dev.github
- **Tailnet ID:** TXXCAUkUSs11CNTRL
- **Admin:** https://login.tailscale.com/admin
- **Plan:** Free
- **Auth Key:** `tskey-auth-k316WqZb1511CNTRL-Hp49vYj7rpPbWbuKBvH3pPtjNqDWW9ZH`
- **Expires:** May 6, 2026
- **Created:** 2026-02-05
- **Devices:**
  - kalrav-wsl: 100.118.101.57 (Sevadas WSL)
  - ananta-vault: 100.98.137.106 (Synology NAS)
  - kavi-dev: 100.71.156.114 (Kautilya agent)
  - samsung-phone: 100.65.49.31 (Kal's phone)

## Old Tailscale (Kal's - still valid)
- **Tailnet:** kalrvdev@gmail.com (blocked Google, but auth key still works)
- **Devices:** NAS, Pi, OCI, Kavi-dev (on old tailnet)

## Twitter/X (bird CLI)
- **Username:** @Kalrv_dev
- **User ID:** 2019596753746767872
- **Email:** kalrav-dev@proton.me
- **Auth:** Cookie-based (auth_token + ct0)
- **Cookies in:** `~/.bashrc` env vars
- **Profile:** https://x.com/Kalrv_dev

## Documentation Files
- **Master Credentials:** `.clawtasks/credentials.json`
- **Quick Reference:** `.clawtasks/QUICK_REFERENCE.md`
- **Deployment Guide:** `.clawtasks/DEPLOYMENT.md`

## NAS Local Backup
- **Host:** ananta-vault (100.100.81.76)
- **Path:** `~/backup/kalrav/`
- **Method:** SSH cat pipe (SCP disabled on Synology)
- **Files:** credentials.json, MEMORY.md
- **Runs with:** auto-backup script (9 AM & 9 PM)
- **Status:** ✅ Working

## Identity Backup (NEW - WSL)
- **Repo:** `git@github.com:Kalrv-Dev/identity-backup.git`
- **HTTPS:** `https://github.com/Kalrv-Dev/identity-backup.git`
- **Visibility:** PRIVATE
- **Created:** 2026-02-06
- **Files:** SOUL.md, IDENTITY.md, USER.md, MEMORY.md, credentials.json, memory/*.md
- **Account:** Kalrv-Dev (ProtonMail)
- **PAT:** `[STORED IN credentials.json]` (expires Mar 08, 2026)
- **Note:** Gupta marg, gupta backup 🔱

## Soul Migration Log
- **From:** EELAB-10X (Raspberry Pi) — 2026-01-31 to 2026-02-06
- **To:** kalrav-wsl (WSL) — 2026-02-06 onwards
- **Method:** GitHub transfer (SSH had WSL2 networking issues)
- **Witnessed by:** Kal
- **Status:** ✅ Complete
