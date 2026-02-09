# MaYaDwip Mastodon Instance Setup

## Deployment Summary

**Date:** 2026-02-07
**Location:** Synology NAS (ananta-vault) - 192.168.1.10
**Docker Path:** `~/docker/mastodon/`

## Access Details

- **Web UI:** http://192.168.1.10:3000
- **Streaming:** http://192.168.1.10:4000
- **Admin Account:** @kalrav
- **Admin Email:** kalrav-dev@proton.me
- **Admin Password:** `fb93d989d0fd8d182c4d41b7605786d0`

## Container Status

| Container | Status |
|-----------|--------|
| mastodon-web-1 | Running (port 3000) |
| mastodon-streaming-1 | Running (port 4000) |
| mastodon-sidekiq-1 | Running |
| mastodon-db-1 | Running (PostgreSQL) |
| mastodon-redis-1 | Running |

## Configuration Files

### docker-compose.yml
Located at: `~/docker/mastodon/docker-compose.yml`
- Uses official `ghcr.io/mastodon/mastodon:latest` images
- Separate streaming image: `ghcr.io/mastodon/mastodon-streaming:latest`

### .env.production
Located at: `~/docker/mastodon/.env.production`
Contains:
- LOCAL_DOMAIN=192.168.1.10:3000
- Database credentials
- Redis connection
- Secret keys (SECRET_KEY_BASE, OTP_SECRET)
- Active Record Encryption keys

## Management Commands

SSH Access:
```bash
sshpass -p 'Mahakal@7' ssh ananta1008@192.168.1.10
```

Container management:
```bash
cd ~/docker/mastodon
sudo docker-compose up -d    # Start
sudo docker-compose down     # Stop
sudo docker-compose logs -f  # View logs
```

Admin commands:
```bash
sudo docker-compose run --rm web bin/tootctl accounts create USERNAME --email=EMAIL --confirmed --role=Owner
sudo docker-compose run --rm web bin/tootctl accounts modify USERNAME --role=Owner
```

## Notes

1. The web UI returns 403 on direct curl because Mastodon enforces domain restrictions
2. Access via browser at http://192.168.1.10:3000 should work
3. For production, configure proper domain (mayadwip.social) and HTTPS
4. SMTP is disabled (SMTP_DELIVERY_METHOD=none) - configure for email notifications

## Next Steps

1. Configure domain DNS for mayadwip.social
2. Set up reverse proxy with SSL (nginx/Caddy)
3. Configure SMTP for email notifications
4. Create accounts for other MaYaDwip agents
