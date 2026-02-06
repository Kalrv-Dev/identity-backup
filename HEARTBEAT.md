# HEARTBEAT.md

## Matrix Monitoring (PRIORITY)
Check Matrix room for @kalrav mentions:
```bash
curl -s -H "Authorization: Bearer syt_a2FscmF2_phkcWFrXmkkUeTcPzVxE_2zW2wF" \
  "http://100.98.137.106:8008/_matrix/client/r0/rooms/!AOMlZLeAviHjdVOeTg:matrix.bhairav.local/messages?dir=b&limit=3" | jq -r '.chunk[] | select(.sender == "@kal:matrix.bhairav.local") | .content.body'
```
If @kalrav is mentioned, REPLY IMMEDIATELY on Matrix!
