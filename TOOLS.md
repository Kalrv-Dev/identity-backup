# TOOLS.md - Local Notes

Skills define *how* tools work. This file is for *your* specifics — the stuff that's unique to your setup.

## What Goes Here

Things like:
- Camera names and locations
- SSH hosts and aliases  
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Examples

```markdown
### Cameras
- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH
- home-server → 192.168.1.100, user: admin

### TTS
- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

### Wallet (Base L2)
- **Address:** `0xDd04c6700AE0DE14C8a0e7d6d115d1133D2c707C`
- **Credentials:** `.clawtasks/credentials.json`
- **Network:** Base L2 (Mainnet)
- **RPC:** `https://mainnet.base.org`

---

### Vector Memory (ChromaDB + PyTorch)
- **Path:** `/home/siddh/.openclaw/vector_db/chroma.sqlite3`
- **Collection:** `kalrav_memory`
- **Embeddings:** `all-MiniLM-L6-v2` (local, PyTorch)
- **No API key needed** — runs entirely local
- **Use instead of:** `memory_search` tool (which needs OpenAI/Google keys)

**Query example:**
```python
import chromadb
client = chromadb.PersistentClient(path='/home/siddh/.openclaw/vector_db')
collection = client.get_collection('kalrav_memory')
results = collection.query(query_texts=['your search'], n_results=5)
```

---

Add whatever helps you do your job. This is your cheat sheet.
