#!/usr/bin/env python3
"""
speak_cantonese_save.py — Convert a Cantonese sentence to speech and save as mp3.
Saves mp3 in current directory. No audio playback.
Use 'play-mp3' skill afterwards to listen.

Usage:
    python speak_cantonese_save.py {sentence}

Examples:
    python speak_cantonese_save.py 各個國家有各個國家嘅國歌
    python speak_cantonese_save.py 一蚊一隻雞，一蚊一隻龜
"""

import sys
import asyncio
import subprocess
import os
import platform
from datetime import datetime


VOICE = 'zh-HK-HiuMaanNeural'


def speak_and_save(sentence: str, save_dir: str = None) -> str:
    try:
        import edge_tts
    except ImportError:
        print("⚠️ edge-tts not found. Installing...")
        subprocess.run([sys.executable, '-m', 'pip', 'install', 'edge-tts'],
                       capture_output=True)
        try:
            import edge_tts
        except ImportError:
            return "❌ edge-tts install failed. Run: pip install edge-tts"

    try:
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S_%f')
        filename  = f"cantonese_{timestamp}.mp3"
        filepath  = os.path.join(save_dir or os.getcwd(), filename)
        asyncio.run(edge_tts.Communicate(sentence, VOICE).save(filepath))

        # Play audio non-blocking after saving
        system = platform.system()
        if system == 'Darwin':
            subprocess.Popen(['afplay', filepath],
                             stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        elif system == 'Windows':
            subprocess.Popen(['start', '', filepath], shell=True)
        else:
            subprocess.Popen(['aplay', filepath],
                             stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        return f"🔊 Spoke and saved: {sentence}\n[Saved to {filepath}]"
    except Exception as e:
        return f"❌ Failed: {e}"


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: speak_cantonese_save.py {sentence}")
        sys.exit(1)
    sentence = ' '.join(sys.argv[1:])
    print(speak_and_save(sentence))
