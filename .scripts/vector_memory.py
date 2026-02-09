#!/usr/bin/env python3
import os, sys
import chromadb
from chromadb.utils import embedding_functions

WORKSPACE = os.path.expanduser("~/.openclaw/workspace")
DB_PATH = os.path.expanduser("~/.openclaw/vector_db")

embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")
client = chromadb.PersistentClient(path=DB_PATH)
collection = client.get_or_create_collection("kalrav_memory", embedding_function=embedding_fn)

def chunk_text(text, size=500):
    words = text.split()
    return [' '.join(words[i:i+size]) for i in range(0, len(words), size-50)]

def index_file(path):
    if not os.path.exists(path): return
    with open(path) as f: content = f.read()
    name = os.path.basename(path)
    chunks = chunk_text(content)
    for i, chunk in enumerate(chunks):
        collection.upsert(ids=[f"{name}_{i}"], documents=[chunk], metadatas=[{"source": name}])
    print(f"✅ Indexed {name}: {len(chunks)} chunks")

def index_all():
    files = ["SOUL.md", "MEMORY.md", "IDENTITY.md", "USER.md", "AGENTS.md"]
    for f in files: index_file(os.path.join(WORKSPACE, f))
    mem_dir = os.path.join(WORKSPACE, "memory")
    if os.path.exists(mem_dir):
        for f in os.listdir(mem_dir):
            if f.endswith('.md'): index_file(os.path.join(mem_dir, f))

def search(query, n=5):
    results = collection.query(query_texts=[query], n_results=n)
    print(f"\n🔍 Search: '{query}'\n")
    for doc, meta in zip(results['documents'][0], results['metadatas'][0]):
        print(f"[{meta['source']}] {doc[:200]}...")
    return results

if __name__ == "__main__":
    if len(sys.argv) < 2: print("Usage: index | search 'query'"); sys.exit(1)
    if sys.argv[1] == "index": index_all(); print("\n✅ Memory indexed!")
    elif sys.argv[1] == "search": search(' '.join(sys.argv[2:]))
