#!/usr/bin/env python3
"""
speak_cantonese.py — Speak a Cantonese sentence aloud using edge-tts.

Usage:
    python speak_cantonese.py {sentence}

Examples:
    python speak_cantonese.py 各個國家都有各個國家嘅國歌
    python speak_cantonese.py 一蚊一隻雞，一蚊一隻龜
"""

import sys
import asyncio
import subprocess
import tempfile
import os
import platform


VOICE = 'zh-HK-HiuMaanNeural'


def speak(sentence: str) -> str:
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
        with tempfile.NamedTemporaryFile(suffix='.mp3', delete=False) as f:
            tmp = f.name
        asyncio.run(edge_tts.Communicate(sentence, VOICE).save(tmp))

        system = platform.system()
        if system == 'Darwin':
            subprocess.run(['afplay', tmp])
        elif system == 'Windows':
            subprocess.run(['start', '', tmp], shell=True)
            import time; time.sleep(3)
        else:
            subprocess.run(['aplay', tmp])

        os.unlink(tmp)
        return f"🔊 Spoke: {sentence}"
    except Exception as e:
        return f"❌ Failed: {e}"


def speak_nonblocking(sentence: str) -> str:
    """Synthesise and play audio without blocking the caller (for server use)."""
    try:
        import edge_tts
    except ImportError:
        subprocess.run([sys.executable, '-m', 'pip', 'install', 'edge-tts'],
                       capture_output=True)
        try:
            import edge_tts
        except ImportError:
            return "❌ edge-tts install failed. Run: pip install edge-tts"

    try:
        with tempfile.NamedTemporaryFile(suffix='.mp3', delete=False) as f:
            tmp = f.name
        asyncio.run(edge_tts.Communicate(sentence, VOICE).save(tmp))

        system = platform.system()
        if system == 'Darwin':
            subprocess.Popen(['afplay', tmp],
                             stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        elif system == 'Windows':
            subprocess.Popen(['start', '', tmp], shell=True)
        else:
            subprocess.Popen(['aplay', tmp],
                             stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        return f"🔊 Speaking: {sentence}"
    except Exception as e:
        return f"❌ Failed: {e}"


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: speak_cantonese.py {sentence}")
        sys.exit(1)

    sentence = ' '.join(sys.argv[1:])
    print(speak(sentence))
