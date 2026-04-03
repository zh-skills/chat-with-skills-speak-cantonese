# Cantonese01 — Chat with Cantonese Skills

A local AI chat app with built-in Cantonese text-to-speech skills. Runs entirely on your computer — no cloud API needed for TTS.

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

## Quick Start

```bash
git clone https://github.com/zh-skills/chat-with-skills-speak-cantonese
cd chat-with-skills-speak-cantonese
pip3 install -r requirements.txt
python3 cantonese01_server.py
```

The browser opens automatically at `http://localhost:8114/cantonese01_index.html`.

On first chat, the Qwen2.5-0.5B model (~400MB) downloads automatically to `models/`.

---

## Requirements

- Python 3.10+
- macOS or Windows (TTS playback uses `afplay` on macOS, `start` on Windows)
- Internet connection for first model download and edge-tts synthesis

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
use skill speak-cantonese 各個國家有各個國家嘅國歌
use skill speak-cantonese-save 一蚊一隻雞，一蚊一隻龜
use skill speak-cantonese-file cantonese-challenge-1.txt
```

---

## License

MIT
