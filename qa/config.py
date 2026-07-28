import os
from pathlib import Path

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

REPO_ROOT = Path(__file__).resolve().parent.parent
QA_ROOT = REPO_ROOT / "qa"
QA_INDEX_DIR = Path(os.getenv("BT_QA_INDEX_DIR", str(QA_ROOT / "index")))
SOURCES_DIR = REPO_ROOT / "sources"

OPENAI_BASE_URL = os.getenv("OPENAI_BASE_URL", "")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

# §7.3 role split: a light model decides the next action, a large one synthesises.
MODEL = os.getenv("BT_QA_MODEL", "gpt-oss-120b")
ACTION_MODEL = os.getenv("BT_QA_ACTION_MODEL", MODEL)
EXTRACT_MODEL = os.getenv("BT_QA_EXTRACT_MODEL", MODEL)
VISION_MODEL = os.getenv("BT_QA_VISION_MODEL", MODEL)
EMBED_MODEL = os.getenv("BT_QA_EMBED_MODEL", "bge-m3")
EMBED_DIM = int(os.getenv("BT_QA_EMBED_DIM", "1024"))

# §7.2 loop budget. DEADLINE_MS stands in for the undecided §12 p95 SLA.
MAX_ITERATIONS = int(os.getenv("BT_QA_MAX_ITERATIONS", "6"))
MAX_TOOL_CALLS = int(os.getenv("BT_QA_MAX_TOOL_CALLS", "12"))
DEADLINE_MS = int(os.getenv("BT_QA_DEADLINE_MS", "60000"))

# §14.8 context accumulation limits.
SNIPPET_CHARS = int(os.getenv("BT_QA_SNIPPET_CHARS", "700"))
CONTEXT_BUDGET_CHARS = int(os.getenv("BT_QA_CONTEXT_BUDGET", "24000"))
EXPAND_LIMIT = int(os.getenv("BT_QA_EXPAND_LIMIT", "4"))

TRAVERSE_NODE_CAP = int(os.getenv("BT_QA_TRAVERSE_CAP", "40"))  # §14.2
VECTOR_TOP_K = int(os.getenv("BT_QA_TOP_K", "8"))
STRUCTURED_RETRIES = int(os.getenv("BT_QA_STRUCTURED_RETRIES", "2"))
CHUNK_MAX_CHARS = int(os.getenv("BT_QA_CHUNK_MAX_CHARS", "3000"))

# ─── HTTP / MCP exposure (server/qa_http.py, server/qa_mcp.py) ───────────
HTTP_HOST = os.getenv("BT_QA_HTTP_HOST", "0.0.0.0")
HTTP_PORT = int(os.getenv("BT_QA_HTTP_PORT", "8090"))
