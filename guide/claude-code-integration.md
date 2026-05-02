# Connecting Bluetooth Spec Wiki to Claude Code

This guide explains how to use the Bluetooth Spec Wiki as a knowledge source
with [Claude Code](https://claude.ai/code) — Anthropic's CLI for Claude.

---

## Quick Start

```bash
# Clone the wiki
git clone https://github.com/yalex-kim/bluetooth_wiki.git
cd bluetooth_wiki

# Open Claude Code
claude

# Ask questions
> What's new in Bluetooth 6.0?
> What changed between Bluetooth 5.1 and 5.2?
> How does Channel Sounding work?
> Explain LE Audio and Isochronous Channels
```

Claude Code will automatically read `CLAUDE.md` and use it to navigate the wiki.

---

## How It Works

The wiki follows [Karpathy's LLM Wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f):

1. **CLAUDE.md** in the repo root programs Claude as a disciplined wiki maintainer
2. **index.md** acts as a content catalog — Claude reads this first to find relevant pages
3. **wiki/** contains the curated knowledge pages Claude uses to answer questions
4. **sources/specs/** stores the raw spec PDFs and their conversions (Layer 1, read-only)

When you open Claude Code in this directory, it reads `CLAUDE.md` automatically,
which tells it how to navigate and maintain the wiki.

---

## Setup Options

### Option 1: Simple Query Mode (Read-Only)

Just open Claude Code and ask questions. Claude reads the wiki to answer.

```bash
cd bluetooth_wiki
claude

# Example queries:
> Which Bluetooth version introduced LE Audio?
> What is the difference between CIS and BIS?
> How does PAwR work and what is it used for?
> What security features were added in Core Spec 5.4?
> Compare BLE Coded PHY S=2 vs S=8 — when should I use each?
```

### Option 2: With MCP Filesystem Server (Recommended)

For the best experience, use the MCP Filesystem server so Claude can efficiently
read multiple wiki files:

**Install the MCP filesystem server:**
```bash
npm install -g @modelcontextprotocol/server-filesystem
```

**Configure in `~/.claude/claude.json`** (or project `.claude/claude.json`):
```json
{
  "mcpServers": {
    "bluetooth-wiki": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "/absolute/path/to/bluetooth_wiki"
      ]
    }
  }
}
```

With MCP filesystem, Claude can search across all wiki files simultaneously,
making complex multi-version questions much faster.

### Option 3: CLAUDE.md in Your Project

If you're working on a Bluetooth project, add the wiki as a submodule and
reference it from your project's CLAUDE.md:

```bash
# In your Bluetooth project:
git submodule add https://github.com/yalex-kim/bluetooth_wiki.git docs/bluetooth-wiki

# Add to your project's CLAUDE.md:
cat >> CLAUDE.md << 'EOF'

## Bluetooth Specification Reference

A Bluetooth Core Spec wiki is available at `docs/bluetooth-wiki/`.
When answering Bluetooth-related questions:
1. Read `docs/bluetooth-wiki/index.md` first
2. Follow the query routing guide in that index
3. Load relevant wiki pages for context
EOF
```

---

## Example Queries and What Claude Will Do

### Version-specific questions

**Query**: "What PHY options are available in Bluetooth 5.0?"

**Claude's process**:
1. Reads `index.md` → routes to `wiki/versions/core-spec-5.0.md`
2. Finds LE 2M PHY and LE Coded PHY entries
3. Returns answer with spec citations `[Core 5.0, Vol 6, Part B, §1.2]`

### Comparison questions

**Query**: "What changed between Bluetooth 5.1 and 5.2?"

**Claude's process**:
1. Reads `index.md` → routes to `wiki/version-diff/diff-5.1-to-5.2.md`
2. Returns the pre-indexed diff with all added/modified/removed features

### Concept questions

**Query**: "How does LE Secure Connections pairing work?"

**Claude's process**:
1. Reads `index.md` → routes to `wiki/concepts/security.md`
2. Finds the LE Secure Connections section
3. Returns explanation with ECDH, pairing methods, key distribution

### Multi-version tracking

**Query**: "When was each new PHY introduced in Bluetooth LE?"

**Claude's process**:
1. Reads `wiki/concepts/ble-architecture.md` (has version history table)
2. Cross-references with version pages for confirmation
3. Returns timeline: LE 1M (4.0), LE 2M + Coded (5.0)

---

## Ingesting Full Spec PDFs (Optional but Recommended)

The wiki ships with **seed knowledge** (manually written summaries).
For the most accurate, citation-heavy answers, ingest the full spec PDFs:

```bash
# 1. Download PDFs
./scripts/download_specs.sh

# 2. Convert to Markdown
pip install -U opendataloader-pdf
python scripts/convert_to_md.py

# 3. Check status
python scripts/ingest.py --status

# 4. Generate ingest prompt for Claude
python scripts/ingest.py 6.0

# 5. Open Claude Code and run the ingest
claude
> [paste the generated prompt, or use /read .prompts/ingest-6.0.md]
```

After ingestion, wiki pages are enriched with exact spec section references,
more precise feature descriptions, and implementation details from the spec text.

---

## Maintaining the Wiki

### Adding a New Spec Version

When Bluetooth SIG releases a new Core Spec version:

```bash
# 1. Download the new spec
./scripts/download_specs.sh 7.0   # (future version)

# 2. Convert to Markdown
python scripts/convert_to_md.py 7.0

# 3. Open Claude Code
claude

# 4. Run the INGEST operation
> Ingest Core Spec 7.0 from sources/specs/core-spec-7.0.md into the wiki.
> Create wiki/versions/core-spec-7.0.md and wiki/version-diff/diff-6.0-to-7.0.md
> Update index.md and log.md
```

### Running a Lint Check

Periodically verify wiki consistency:

```bash
python scripts/ingest.py --lint   # Generate lint prompt
claude
> [paste the lint prompt]
```

### What Claude Will Do During Lint

- Verify all `index.md` links resolve
- Check that version pages agree with diff pages
- Flag stale "new in X.Y" claims
- Identify orphan pages not in index
- Report missing cross-references

---

## Tips for Best Results

1. **Always start from the repo root** so Claude Code reads `CLAUDE.md` automatically
2. **For version-specific questions**, mention the version number explicitly:
   "In Core Spec 6.0, how does Channel Sounding differ from direction finding in 5.1?"
3. **For implementation questions**, ask for developer impact:
   "I'm implementing a BLE scanner — how should I use DBAF in Bluetooth 6.0?"
4. **For citations**, ask explicitly:
   "With spec section references, explain how CIS is established in 5.2"
5. **After ingesting full spec PDFs**, questions about obscure spec details
   (specific bit fields, state machine transitions, exact PDU formats) become answerable

---

## Repository Structure Reference

```
bluetooth_wiki/
├── CLAUDE.md                    ← Read automatically by Claude Code (wiki schema)
├── index.md                     ← Content catalog (Claude reads this on every query)
├── log.md                       ← Activity log
├── wiki/
│   ├── overview.md
│   ├── versions/                ← core-spec-5.0.md through core-spec-6.0.md
│   ├── version-diff/            ← diff-5.0-to-5.1.md through diff-5.4-to-6.0.md
│   └── concepts/                ← ble-architecture, classic-bluetooth, security, profiles
├── sources/
│   ├── README.md                ← Download instructions
│   └── specs/                   ← PDFs + converted .md files (gitignored)
├── scripts/
│   ├── download_specs.sh        ← Automated PDF downloader
│   ├── convert_to_md.py         ← OpenDataLoader PDF converter
│   └── ingest.py                ← Ingest workflow helper
└── guide/
    └── claude-code-integration.md  ← This file
```

---

## Troubleshooting

**Claude doesn't seem to be using the wiki:**
- Make sure you're running `claude` from the `bluetooth_wiki` directory
- Check that `CLAUDE.md` exists in the root
- Try: `> Read CLAUDE.md and index.md, then answer: what Bluetooth versions are covered?`

**Answers lack spec citations:**
- The seed wiki pages have general citations; full citations require ingesting spec PDFs
- Run the ingest workflow for the relevant version

**Claude gives outdated information:**
- Check if the wiki has been updated: `git log --oneline wiki/`
- Run a lint check: `python scripts/ingest.py --lint`

**Download script fails:**
- Visit bluetooth.com manually and accept the Terms of Use, then retry
- Or download manually and save to `sources/specs/core-spec-X.Y.pdf`

**OpenDataLoader conversion is slow:**
- Large spec PDFs (5.0 is 2800+ pages) take several minutes even at 60 pages/sec
- Use `--hybrid` mode for better table quality at similar speed
- Consider converting one version at a time
