#!/usr/bin/env python3
import time
import re
import os

# === CONFIG ===
LRC_FILE = "lyrics/I Wanna Be Yours.lrc"   # lyrics file ka path
LYRIC_OFFSET = -0.2                         # adjust if delay (e.g., -0.5 or +0.5)

# === PARSE LRC FILE ===
def parse_lrc(path):
    pattern = re.compile(r"\[(\d+):(\d+(?:\.\d+)?)\](.*)")
    lyrics = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            m = pattern.match(line.strip())
            if m:
                mins, secs, text = m.groups()
                t = int(mins)*60 + float(secs) + LYRIC_OFFSET
                lyrics.append((t, text.strip()))
    return sorted(lyrics)

# === DISPLAY LYRICS IN REAL TIME ===
def show_lyrics(lyrics):
    start_time = time.time()
    for t, line in lyrics:
        while time.time() - start_time < t:
            time.sleep(0.01)
        os.system("cls" if os.name == "nt" else "clear")
        print(f"\n🎵 {line}\n")

# === MAIN ===
if __name__ == "__main__":
    if not os.path.exists(LRC_FILE):
        print("❌ Lyrics file not found!")
    else:
        print("✅ Lyrics loaded, starting sync...\n")
        lyrics = parse_lrc(LRC_FILE)
        time.sleep(2)  # small delay before start
        show_lyrics(lyrics)
