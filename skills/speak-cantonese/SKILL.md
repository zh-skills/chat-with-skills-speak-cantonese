---
name: speak-cantonese
description: Speak a Cantonese sentence aloud using text-to-speech. Use ONLY when the user explicitly says "use skill speak-cantonese" followed by a Cantonese sentence. The script speaks the audio directly — do NOT search for or expect any mp3 file to be saved.
---

# Speak Cantonese

> 中文版本：[SKILL.zh.md](SKILL.zh.md)

Speak a Cantonese sentence aloud using edge-tts (Microsoft zh-HK-HiuMaanNeural voice).

## Workflow

1. Extract the sentence from the user's message (everything after "use skill speak-cantonese")
2. Run `scripts/speak_cantonese.py {sentence}` — the script speaks the audio and exits
3. Report the result to the user
4. Do NOT search for mp3 files. Do NOT retry. The task is complete when the script exits.

## Trigger Examples

- `use skill speak-cantonese 各個國家有各個國家嘅國歌`
- `use skill speak-cantonese 一蚊一隻雞，一蚊一隻龜`

## Output Format

```
🔊 Spoke: {sentence}
```

## Important

- Run `scripts/speak_cantonese.py` only once per request
- The script plays audio directly and exits — no mp3 file is saved
- Do NOT search for mp3 files after running
- Do NOT retry if the script exits with code 0

## Setup

```bash
pip install edge-tts    # auto-installed if missing
```

## Reference

For implementation details see [references/implementation_notes.md](references/implementation_notes.md).
