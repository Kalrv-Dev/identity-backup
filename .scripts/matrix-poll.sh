#!/bin/bash
# Matrix polling script for Kalrav

HOMESERVER="http://100.98.137.106:8008"
ROOM_ID="!AOMlZLeAviHjdVOeTg:matrix.bhairav.local"
TOKEN="syt_a2FscmF2_phkcWFrXmkkUeTcPzVxE_2zW2wF"
LAST_EVENT_FILE="$HOME/.matrix_last_event"

# Fetch recent messages
curl -s -H "Authorization: Bearer $TOKEN" \
  "$HOMESERVER/_matrix/client/r0/rooms/$ROOM_ID/messages?dir=b&limit=3" | \
  jq -r '.chunk[] | select(.sender == "@kal:matrix.bhairav.local") | .content.body' | head -1
