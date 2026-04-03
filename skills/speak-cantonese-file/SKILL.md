---
name: speak-cantonese-file
description: Read a text file line by line, save all lines as mp3 files, join them into one combined mp3, then play it once with no gaps between sentences. Use ONLY when the user explicitly says "use skill speak-cantonese-file" followed by a filename. Requires ffmpeg for joining.
---

# Speak Cantonese File

Read a text file, save each line as an mp3, join all into one combined mp3, then play it once — no gaps between sentences.

## Workflow

1. Extract the filename from the user's message
2. Create a subfolder using the filename without extension (e.g. `cantonese-challenge-1` from `cantonese-challenge-1.txt`)
3. Read each line — skip blank lines and markdown formatting (headings, bullets, numbered lists)
4. **Phase 1 — Save all lines as mp3 files into the subfolder:**
   For each line, run `scripts/speak_cantonese_save.py {line}` from the `speak-cantonese-save` skill, saving into the subfolder. Complete ALL lines before moving on.
5. **Phase 2 — Join all mp3 files into one:**
   Run `scripts/join_mp3.py {subfolder}` from the `join-mp3` skill. This creates a single `joined_{timestamp}.mp3` in the current directory.
6. **Phase 3 — Play the combined mp3 once:**
   Run `scripts/play_mp3.py {joined_mp3_filepath}` from the `play-mp3` skill.
7. Report the result to the user.

## Trigger Examples

- `use skill speak-cantonese-file cantonese-challenge-1.txt`
- `use skill speak-cantonese-file speech-Cantonese.txt`

## Output Format

```
Saving N lines to {subfolder}/...
Joining mp3 files...
✅ Joined N files → {joined_filename}
🔊 Playing...
✅ Done
```

## Important

- Complete ALL saves (Phase 1) before joining (Phase 2)
- Complete joining (Phase 2) before playing (Phase 3)
- Do NOT retry any step if it exits with code 0
- Requires ffmpeg: `brew install ffmpeg`
