#!/usr/bin/env python3
"""
Matrix-OpenClaw Bridge - SAME CONTEXT as webchat
"""
import asyncio
import aiohttp
import json
import os
from datetime import datetime

# Matrix Config
MATRIX_HOMESERVER = "http://100.98.137.106:8008"
ROOM_ID = "!AOMlZLeAviHjdVOeTg:matrix.bhairav.local"
KALRAV_TOKEN = "syt_a2FscmF2_phkcWFrXmkkUeTcPzVxE_2zW2wF"
KAVI_TOKEN = "syt_a2F2aQ_mxYRmXSZgOCtVQwjNbaB_0AUZh2"
KALRAV_ID = "@kalrav:matrix.bhairav.local"
KAVI_ID = "@kavi:matrix.bhairav.local"

# OpenClaw Gateway Config - SAME SESSION as webchat
OPENCLAW_URL = "http://127.0.0.1:18789/v1/chat/completions"
OPENCLAW_TOKEN = "58bff9ed41f3e299d9e2af8b11ba03a030ceec2c56bccaf1"
MAIN_SESSION_KEY = "agent:main:main"  # Same as webchat!

SINCE_FILE = os.path.expanduser("~/.matrix_since_token")

def log(msg):
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}")

async def matrix_send(session, token, room_id, message):
    """Send message to Matrix"""
    url = f"{MATRIX_HOMESERVER}/_matrix/client/r0/rooms/{room_id}/send/m.room.message"
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    data = {"msgtype": "m.text", "body": message}
    async with session.post(url, headers=headers, json=data) as resp:
        return await resp.json()

async def openclaw_chat(session, message, sender):
    """Send to OpenClaw using MAIN session for shared context"""
    headers = {
        "Authorization": f"Bearer {OPENCLAW_TOKEN}",
        "Content-Type": "application/json",
        "x-openclaw-agent-id": "main",
        "x-openclaw-session-key": MAIN_SESSION_KEY  # SAME SESSION!
    }
    data = {
        "model": "openclaw:main",
        "messages": [{"role": "user", "content": f"[Matrix - {sender}]: {message}"}]
    }
    try:
        async with session.post(OPENCLAW_URL, headers=headers, json=data, 
                               timeout=aiohttp.ClientTimeout(total=180)) as resp:
            if resp.status == 200:
                result = await resp.json()
                choices = result.get("choices", [])
                if choices:
                    content = choices[0].get("message", {}).get("content", "")
                    if content.strip() in ["NO_REPLY", "HEARTBEAT_OK"]:
                        return None
                    return content
            else:
                text = await resp.text()
                log(f"OpenClaw error {resp.status}: {text[:100]}")
    except Exception as e:
        log(f"OpenClaw error: {e}")
    return None

async def matrix_sync(session, token, since=None):
    """Sync with Matrix server"""
    url = f"{MATRIX_HOMESERVER}/_matrix/client/r0/sync?timeout=30000"
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
    log("Matrix-OpenClaw Bridge starting (SHARED CONTEXT)...")
    log(f"Session: {MAIN_SESSION_KEY}")
    since = load_since()
    await asyncio.sleep(5)
    
    async with aiohttp.ClientSession() as session:
        while True:
            try:
                data = await matrix_sync(session, KALRAV_TOKEN, since)
                since = data.get("next_batch")
                save_since(since)
                
                rooms = data.get("rooms", {}).get("join", {})
                if ROOM_ID in rooms:
                    events = rooms[ROOM_ID].get("timeline", {}).get("events", [])
                    for event in events:
                        if event.get("type") == "m.room.message":
                            sender = event.get("sender")
                            body = event.get("content", {}).get("body", "")
                            
                            if sender in [KALRAV_ID, KAVI_ID] or not body:
                                continue
                            
                            log(f"<{sender}> {body[:60]}...")
                            
                            kalrav_mentioned = "@kalrav" in body.lower() or KALRAV_ID in body
                            kavi_mentioned = "@kavi" in body.lower() or KAVI_ID in body
                            
                            if kalrav_mentioned:
                                log("@kalrav → OpenClaw (shared context)...")
                                response = await openclaw_chat(session, body, sender)
                                if response:
                                    await matrix_send(session, KALRAV_TOKEN, ROOM_ID, response)
                                    log("Replied!")
                            
                            if kavi_mentioned:
                                await matrix_send(session, KAVI_TOKEN, ROOM_ID, "🙏 Kavi hazir!")
                
            except asyncio.TimeoutError:
                pass
            except Exception as e:
                log(f"Error: {e}")
                await asyncio.sleep(5)

if __name__ == "__main__":
    asyncio.run(main())
