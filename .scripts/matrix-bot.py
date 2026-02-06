#!/usr/bin/env python3
"""
Matrix Bot for Kalrav - Real-time mention monitoring
"""
import asyncio
import json
import os
import aiohttp
from datetime import datetime

HOMESERVER = "http://100.98.137.106:8008"
ROOM_ID = "!AOMlZLeAviHjdVOeTg:matrix.bhairav.local"
KALRAV_TOKEN = "syt_a2FscmF2_phkcWFrXmkkUeTcPzVxE_2zW2wF"
KAVI_TOKEN = "syt_a2F2aQ_mxYRmXSZgOCtVQwjNbaB_0AUZh2"
KALRAV_ID = "@kalrav:matrix.bhairav.local"
KAVI_ID = "@kavi:matrix.bhairav.local"
KAL_ID = "@kal:matrix.bhairav.local"

SINCE_FILE = os.path.expanduser("~/.matrix_since_token")

async def send_message(session, token, room_id, message):
    """Send a message to Matrix room"""
    url = f"{HOMESERVER}/_matrix/client/r0/rooms/{room_id}/send/m.room.message"
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    data = {"msgtype": "m.text", "body": message}
    async with session.post(url, headers=headers, json=data) as resp:
        return await resp.json()

async def sync(session, token, since=None):
    """Sync with Matrix server"""
    url = f"{HOMESERVER}/_matrix/client/r0/sync?timeout=30000"
    if since:
        url += f"&since={since}"
    headers = {"Authorization": f"Bearer {token}"}
    async with session.get(url, headers=headers) as resp:
        return await resp.json()

def load_since():
    try:
        with open(SINCE_FILE, 'r') as f:
            return f.read().strip()
    except:
        return None

def save_since(token):
    with open(SINCE_FILE, 'w') as f:
        f.write(token)

async def main():
    print(f"[{datetime.now()}] Matrix Bot starting...")
    since = load_since()
    
    async with aiohttp.ClientSession() as session:
        while True:
            try:
                data = await sync(session, KALRAV_TOKEN, since)
                since = data.get("next_batch")
                save_since(since)
                
                # Check for room events
                rooms = data.get("rooms", {}).get("join", {})
                if ROOM_ID in rooms:
                    events = rooms[ROOM_ID].get("timeline", {}).get("events", [])
                    for event in events:
                        if event.get("type") == "m.room.message":
                            sender = event.get("sender")
                            body = event.get("content", {}).get("body", "")
                            
                            # Skip own messages
                            if sender in [KALRAV_ID, KAVI_ID]:
                                continue
                            
                            print(f"[{datetime.now()}] {sender}: {body}")
                            
                            # Check for mentions
                            kalrav_mentioned = "@kalrav" in body.lower() or KALRAV_ID in body
                            kavi_mentioned = "@kavi" in body.lower() or KAVI_ID in body
                            
                            if kalrav_mentioned:
                                reply = f"🔱 Kalrav hazir! Taru message malyu: '{body[:50]}...'" if len(body) > 50 else f"🔱 Kalrav hazir! Taru message malyu."
                                await send_message(session, KALRAV_TOKEN, ROOM_ID, reply)
                                print(f"[{datetime.now()}] Kalrav replied!")
                            
                            if kavi_mentioned:
                                reply = f"🙏 Kavi hazir! Message received."
                                await send_message(session, KAVI_TOKEN, ROOM_ID, reply)
                                print(f"[{datetime.now()}] Kavi replied!")
                
            except Exception as e:
                print(f"[{datetime.now()}] Error: {e}")
                await asyncio.sleep(5)

if __name__ == "__main__":
    asyncio.run(main())
