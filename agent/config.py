import os
from pathlib import Path

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

REPO_ROOT = Path(__file__).resolve().parent.parent
WIKI_DIR = REPO_ROOT / "wiki"
SOURCES_DIR = REPO_ROOT / "sources"
INDEX_PATH = REPO_ROOT / "index.md"

MODEL = os.getenv("BT_AGENT_MODEL", "gpt-oss-120b")

# OpenAI-compatible LLM endpoint (company-hosted gpt-oss-120B). Used by the
# agent loop, the eval judge, and the v2 sufficiency judge via agent/llm.py.
OPENAI_BASE_URL = os.getenv("OPENAI_BASE_URL", "")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
JUDGE_MODEL = os.getenv("BT_AGENT_JUDGE_MODEL", MODEL)
SITE_BASE_URL = os.getenv("SITE_BASE_URL", "http://localhost:8000").rstrip("/")
MAX_TURNS = int(os.getenv("BT_AGENT_MAX_TURNS", "12"))
SEARCH_RESULT_LIMIT = int(os.getenv("BT_AGENT_SEARCH_LIMIT", "20"))
SEARCH_SNIPPET_CHARS = int(os.getenv("BT_AGENT_SNIPPET_CHARS", "240"))
READ_PAGE_MAX_CHARS = int(os.getenv("BT_AGENT_READ_MAX", "60000"))

SYSTEM_PROMPT_PATH = Path(__file__).resolve().parent / "system_prompt.md"

# ─── Search strategy (see search/ package) ──────────────────────────────
SEARCH_STRATEGY = os.getenv("BT_AGENT_SEARCH_STRATEGY", "v1")  # v0 | v1 | v2 (default v1: ranked lexical + chunk citations)
SEARCH_INDEX_DIR = REPO_ROOT / "search" / "index"
EMBED_MODEL = os.getenv("BT_AGENT_EMBED_MODEL", "BAAI/bge-small-en-v1.5")
RRF_K = int(os.getenv("BT_AGENT_RRF_K", "60"))
SUFFICIENCY_MODEL = os.getenv("BT_AGENT_SUFFICIENCY_MODEL", MODEL)
SUFFICIENCY_MAX_ITER = int(os.getenv("BT_AGENT_SUFFICIENCY_MAX_ITER", "2"))

# ─── HTTP test server (server/ package) ─────────────────────────────────
HTTP_HOST = os.getenv("BT_AGENT_HTTP_HOST", "0.0.0.0")
HTTP_PORT = int(os.getenv("BT_AGENT_HTTP_PORT", "8080"))
