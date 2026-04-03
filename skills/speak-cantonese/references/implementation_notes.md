# Implementation Notes — speak-cantonese

## Voice

Uses Microsoft edge-tts with the Hong Kong Cantonese voice:
- Voice: `zh-HK-HiuMaanNeural`
- Language: Cantonese (Hong Kong)
- No API key required — edge-tts is free and runs locally

## How It Works

1. `edge_tts.Communicate(text, voice)` sends the text to Microsoft's TTS service and streams back audio
2. Audio is saved as `.mp3` to `speeches/cantonese_{YYYYMMDD_HHMMSS}.mp3`
3. `pygame.mixer` loads and plays the mp3 file
4. File is kept after playback for the user to reuse

## Dependencies

```bash
pip install edge-tts pygame
```

- `edge-tts` — Microsoft TTS client (free, no API key)
- `pygame` — cross-platform audio playback

## Output File

- Folder: `speeches/`
- Filename: `cantonese_{YYYYMMDD_HHMMSS}.mp3`
- Format: mp3

## Limitations

- Requires internet connection (edge-tts calls Microsoft's service)
- Cantonese only — for Putonghua use `speak-putonghua`, for English use `speak-english`
- Playback requires audio output device
