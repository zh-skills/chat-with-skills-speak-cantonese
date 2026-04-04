# Chat with speak-cantonese skill

A local AI chat app with built-in Cantonese text-to-speech (TTS) skills. Runs entirely on your computer — no cloud API needed for TTS.

> 本地 AI 聊天应用，内置粤语语音技能，无需云端 API。

---

## Skills

| Skill | Trigger | Description |
|-------|---------|-------------|
| Chat with Local Model | any question | Chat using a local GGUF model (Qwen2.5) |
| Speak Cantonese | `use skill speak-cantonese {sentence}` | Speak a Cantonese sentence aloud |
| Speak Cantonese Save | `use skill speak-cantonese-save {sentence}` | Speak and save as mp3 |
| Speak Cantonese File | `use skill speak-cantonese-file {filename.txt}` | Read a text file and speak each line |

---

## Quick Start — macOS

**Step 1 — Create a folder (first time only):**

Create a folder to keep all your chat-with-skills apps together. The free local AI model (~400MB) will be downloaded into this folder. As long as you use the same folder, you only download the model once.

```bash
mkdir chat-with-skills-folder
cd chat-with-skills-folder
```

**Step 2 — Install uv package manager (one-time, choose one):**

If pip or pip3 works:
```bash
pip install uv
```
```bash
pip3 install uv
```

If pip is blocked (Homebrew Python):
```bash
pipx install uv
```

Without pip (curl):
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```
Then activate uv in your current terminal:
```bash
source $HOME/.local/bin/env
```

**Step 3 — Clone and run:**
```bash
git clone https://github.com/zh-skills/chat-with-skills-speak-cantonese
cd chat-with-skills-speak-cantonese
uv run server.py
```

**Next time (after restarting your computer):**
```bash
cd chat-with-skills-folder/chat-with-skills-speak-cantonese
uv run server.py
```

---

## Quick Start — Windows

**Step 1 — Create a folder (first time only):**
```bash
mkdir chat-with-skills-folder
cd chat-with-skills-folder
```

**Step 2 — Install uv package manager (one-time, choose one):**

If pip works:
```bash
pip install uv
```

Without pip (PowerShell):
```bash
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**Step 3 — Clone and run:**
```bash
git clone https://github.com/zh-skills/chat-with-skills-speak-cantonese
cd chat-with-skills-speak-cantonese
uv run server.py
```

**Next time (after restarting your computer):**
```bash
cd chat-with-skills-folder\chat-with-skills-speak-cantonese
uv run server.py
```

The browser opens automatically at `http://localhost:8114/cantonese01_index.html`.

On first chat, the Qwen2.5-0.5B model (~400MB) downloads automatically to `models/`.

---

## Requirements

- Python 3.11 (pinned via `.python-version` — `uv` downloads it automatically if needed)
- macOS or Windows (TTS playback uses `afplay` on macOS, `start` on Windows)
- Internet connection for first model download and edge-tts synthesis

> **Why Python 3.11?** Key packages like `llama-cpp-python` and `faster-whisper` have the most reliable pre-built wheels for 3.11. Newer versions (3.12+) may require slow C++ compilation.

### Install dependencies

```bash
pip install -r requirements.txt
```

For Apple Silicon GPU acceleration (optional):
```bash
CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python --force-reinstall --no-cache-dir
```

---

## File Structure

```
cantonese01_server.py       — Flask API server
cantonese01_app.js          — Frontend JavaScript
cantonese01_index.html      — UI
cantonese01_marked.min.js   — Markdown renderer
requirements.txt
skills/
  speak-cantonese/scripts/speak_cantonese.py
  speak-cantonese-save/scripts/speak_cantonese_save.py
  speak-cantonese-file/scripts/speak_cantonese_file.py
models/                     — GGUF model files (downloaded on first use)
```

---

## Example Usage

```
What is artificial intelligence?
什么是人工智能？
use skill speak-cantonese 各個國家都有各個國家嘅國歌
use skill speak-cantonese-save 一蚊一隻雞，一蚊一隻龜
use skill speak-cantonese-file cantonese-challenge-1.txt
use skill speak-cantonese-file speech-Cantonese.txt
```

---

## License

MIT
