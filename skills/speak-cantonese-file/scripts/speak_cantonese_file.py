#!/usr/bin/env python3
"""
speak_cantonese_file.py — Read a text file, display all lines, speak each line,
then join all mp3 files into one combined mp3.

Usage:
    python speak_cantonese_file.py {filename}

Examples:
    python speak_cantonese_file.py cantonese-challenge-1.txt
    python speak_cantonese_file.py speech-Cantonese.txt
"""

import sys
import asyncio
import subprocess
import os
import re
import platform
from datetime import datetime


VOICE = 'zh-HK-HiuMaanNeural'


def ensure_edge_tts():
    try:
        import edge_tts  # noqa
        return True
    except ImportError:
        print("⚠️ edge-tts not found. Installing...")
        subprocess.run([sys.executable, '-m', 'pip', 'install', 'edge-tts'],
                       capture_output=True)
        try:
            import edge_tts  # noqa
            return True
        except ImportError:
            print("❌ edge-tts install failed. Run: pip install edge-tts")
            return False


def clean_line(line: str) -> str:
    """Strip markdown formatting."""
    line = re.sub(r'^#{1,6}\s*', '', line)
    line = re.sub(r'\*{1,2}([^*]+)\*{1,2}', r'\1', line)
    line = re.sub(r'^\d+\.\s*', '', line)
    line = re.sub(r'^[-*•]\s*', '', line)
    line = re.sub(r'\(.*?\)', '', line)
    return line.strip()


def play_blocking(filepath: str):
    """Play audio and wait for it to finish."""
    system = platform.system()
    try:
        if system == 'Darwin':
            subprocess.run(['afplay', filepath], timeout=60)
        elif system == 'Windows':
            # Use playsound for blocking playback on Windows
            try:
                from playsound import playsound
                playsound(filepath)
            except ImportError:
                # Fallback: install playsound then retry
                subprocess.run([sys.executable, '-m', 'pip', 'install', 'playsound==1.2.2'],
                               capture_output=True)
                try:
                    from playsound import playsound
                    playsound(filepath)
                except Exception:
                    # Last resort: use start /wait (opens media player)
                    subprocess.run(['start', '/wait', '', filepath], shell=True, timeout=60)
        else:
            subprocess.run(['aplay', filepath], timeout=60)
    except Exception:
        pass


def join_mp3(files: list, output: str) -> bool:
    """Join mp3 files using ffmpeg. Returns True on success."""
    list_file = output + '_list.txt'
    try:
        with open(list_file, 'w') as f:
            for fp in files:
                f.write(f"file '{os.path.abspath(fp)}'\n")
        result = subprocess.run(
            ['ffmpeg', '-y', '-f', 'concat', '-safe', '0', '-i', list_file, '-c', 'copy', output],
            capture_output=True
        )
        return result.returncode == 0
    except Exception:
        return False
    finally:
        if os.path.exists(list_file):
            os.remove(list_file)


def speak_cantonese_file(filepath: str, save_dir: str = None) -> str:
    if not os.path.isfile(filepath):
        return f"❌ File not found: {filepath}"

    if not ensure_edge_tts():
        return "❌ edge-tts not available."

    import edge_tts

    with open(filepath, 'r', encoding='utf-8') as f:
        raw_lines = f.readlines()

    lines = [clean_line(l) for l in raw_lines]
    lines = [l for l in lines if len(l) >= 1 and re.search(r'\w', l)]

    if not lines:
        return f"❌ No speakable content found in: {filepath}"

    # ── Phase 1: Display all lines ────────────────────────────────────────────
    display = '\n'.join(f"[{i+1}/{len(lines)}] {l}" for i, l in enumerate(lines))
    print(f"\n📄 Content of {filepath}:\n{display}\n")

    # ── Phase 2: Speak each line and save mp3 ────────────────────────────────
    save_to   = save_dir or os.getcwd()
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    saved     = []

    for i, line in enumerate(lines):
        print(f"🔊 [{i+1}/{len(lines)}] {line}")
        filename = f"cantonese_{timestamp}_{i+1:03d}.mp3"
        fp       = os.path.join(save_to, filename)
        try:
            asyncio.run(edge_tts.Communicate(line, VOICE).save(fp))
            play_blocking(fp)
            saved.append(fp)
        except Exception as e:
            print(f"   ⚠️ Skipped: {e}")

    if not saved:
        return "❌ No lines were spoken."

    # ── Phase 3: Join all mp3 files into one ─────────────────────────────────
    combined_name = f"cantonese_{timestamp}_combined.mp3"
    combined_path = os.path.join(save_to, combined_name)
    if join_mp3(saved, combined_path):
        combined_msg = f"Combined: {combined_name}"
    else:
        combined_msg = "Combined mp3 skipped (ffmpeg not found). Install: brew install ffmpeg"

    return (f"📄 {filepath} — {len(lines)} lines\n"
            f"🔊 Spoke {len(saved)}/{len(lines)} lines\n"
            f"[{combined_msg}]")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: speak_cantonese_file.py {filename}")
        sys.exit(1)
    filename = ' '.join(sys.argv[1:])
    print(speak_cantonese_file(filename))
