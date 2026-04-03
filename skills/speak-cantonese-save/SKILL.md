---
name: speak-cantonese-save
description: Convert a Cantonese sentence to speech and save as an mp3 file in the current directory. No audio playback. Use ONLY when the user explicitly says "use skill speak-cantonese-save" followed by a Cantonese sentence. After saving, suggest using play-mp3 skill to listen.
---

# Speak Cantonese Save

> 中文版本：[SKILL.zh.md](SKILL.zh.md)

Convert a Cantonese sentence to speech using edge-tts and save as an mp3 file. No audio playback — use the `play-mp3` skill to listen.

## Workflow

1. Extract the sentence from the user's message (everything after "use skill speak-cantonese-save")
2. Run `scripts/speak_cantonese_save.py {sentence}` — saves mp3 to current directory
3. Report the saved filename and suggest using `play-mp3` to listen

## Trigger Examples

- `use skill speak-cantonese-save 各個國家有各個國家嘅國歌`
- `use skill speak-cantonese-save 一蚊一隻雞，一蚊一隻龜`

## Output Format

```
✅ Saved: {filepath}
To listen: use skill play-mp3 {filename}
```

## Important

- Run `scripts/speak_cantonese_save.py` only once per request
- The mp3 is saved in the current directory — no audio playback, no subdirectory
- Do NOT retry if the script exits with code 0
- Do NOT open, play, or search for the mp3 file — report the filepath and STOP
- To listen, use the `play-mp3` skill: `use skill play-mp3 {filename}`
