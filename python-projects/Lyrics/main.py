#!/usr/bin/env python3
import os, sys, re, shutil, difflib, tempfile, requests
import numpy as np
import sounddevice as sd
import soundfile as sf

# === CONFIG ===
AUDIO_FILE   = "I Wanna Be Yours.mp3"   # tumhara song file
START_TIME   = 0                      # kis second se start ho
LRC_FOLDER   = os.path.expanduser("lyrics")  # local lyrics folder
BLOCKSIZE    = 2048
LYRIC_OFFSET = -1.5                     # lyrics sync fix (try -1.5 se -2 tak)

# === FETCH LYRICS ONLINE ===
def fetch_lrc_from_lrclib(title: str, artist: str = "") -> str | None:
    try:
        r = requests.get("https://lrclib.net/api/search",
                         params={"q": f"{title} {artist}".strip()},
                         timeout=10)
        r.raise_for_status()
        for item in r.json():
            if item.get("syncedLyrics"):
                return item["syncedLyrics"]
    except Exception as e:
        print("⚠️  LRCLIB fetch failed:", e)
    return None

# === FIND LOCAL LRC IF AVAILABLE ===
def find_closest_lrc(song_title: str, folder: str) -> str | None:
    if not os.path.isdir(folder):
        return None
    bases = [os.path.splitext(f)[0] for f in os.listdir(folder)
             if f.lower().endswith(".lrc")]
    closest = difflib.get_close_matches(song_title, bases, n=1, cutoff=0.4)
    return os.path.join(folder, closest[0] + ".lrc") if closest else None

# === PARSE LRC FILE ===
def parse_lrc(path: str):
    pattern = re.compile(r"\[(\d+):(\d+(?:\.\d+)?)\](.*)")
    out = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            m = pattern.match(line.strip())
            if m:
                mins, secs, txt = m.groups()
                t = int(mins)*60 + float(secs) + LYRIC_OFFSET
                out.append((max(0.0, t), txt.strip()))
    return sorted(out)

# === MAIN PREPARATION ===
base = os.path.splitext(os.path.basename(AUDIO_FILE))[0]
artist_guess, title_guess = ("", base)
if "-" in base:
    artist_guess, title_guess = [x.strip() for x in base.split("-", 1)]

lyrics_path = None
lrc_text = fetch_lrc_from_lrclib(title_guess, artist_guess)
if lrc_text:
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".lrc")
    tmp.write(lrc_text.encode("utf-8")); tmp.close()
    lyrics_path = tmp.name
    print("🎵 Synced lyrics fetched from LRCLIB!")
else:
    match = find_closest_lrc(title_guess, LRC_FOLDER)
    if match:
        lyrics_path = match
        print(f"📂 Using local lyrics: {match}")
    else:
        print("❌ No lyrics found online or locally.")

lyrics = parse_lrc(lyrics_path) if lyrics_path else []

# === LOAD AUDIO ===
data, samplerate = sf.read(AUDIO_FILE, dtype="float32")
if data.ndim > 1:
    data = np.mean(data, axis=1)
data = data / np.max(np.abs(data))
start_idx = int(START_TIME * samplerate)

term_columns, _ = shutil.get_terminal_size((100, 40))
columns = min(80, term_columns)
center  = 6
lyric_index = 0
for i, (t, _) in enumerate(lyrics):
    if t >= START_TIME:
        lyric_index = max(0, i - 1)
        break

def smooth(vals, window=5):
    if len(vals) < window: return vals
    k = np.ones(window)/window
    return np.convolve(vals, k, mode="same")

def hsv_to_rgb(h,s,v):
    i = int(h*6); f = h*6 - i
    p = int(255*v*(1-s)); q = int(255*v*(1-f*s)); t = int(255*v*(1-(1-f)*s))
    v = int(255*v); i = i % 6
    return [(v,t,p),(q,v,p),(p,v,t),(p,q,v),(t,p,v),(v,p,q)][i]

def colorize(text, r,g,b):
    return f"\033[38;2;{r};{g};{b}m{text}\033[0m"

def dim_color(text, r, g, b, factor=0.4):
    rr = int(r*factor); gg = int(g*factor); bb = int(b*factor)
    return f"\033[38;2;{rr};{gg};{bb}m{text}\033[0m"

def render_lyrics_block(idx, r, g, b):
    lines = []
    if idx < len(lyrics):
        lines.append(colorize(lyrics[idx][1], r, g, b))
    for n in range(1, 3):
        if idx + n < len(lyrics):
            lines.append("")
            lines.append(dim_color(lyrics[idx + n][1], r, g, b, 0.4))
    return "\n".join(lines)

def callback(outdata, frames, time_info, status):
    global start_idx, lyric_index
    if status: print(status, file=sys.stderr)

    chunk = data[start_idx:start_idx+frames]
    if len(chunk) < frames:
        outdata[:len(chunk),0] = chunk
        outdata[len(chunk):] = 0
        raise sd.CallbackStop
    else:
        outdata[:,0] = chunk

    play_time = start_idx / samplerate
    if lyrics:
        while lyric_index + 1 < len(lyrics) and play_time >= lyrics[lyric_index + 1][0]:
            lyric_index += 1

    step   = max(1, len(chunk)//columns)
    levels = np.abs(chunk[::step])
    levels = smooth(levels, window=6)
    levels = np.interp(np.clip(levels,0,1), [0,1], [0,center-1]).astype(int)

    hue = [0.15,0.3,0.6,0.8][int((play_time*0.2)%4)]
    r,g,b = hsv_to_rgb(hue,0.5,0.9)

    screen=[]
    for row in range(center*2):
        line=[]
        for lvl in levels:
            if row==center:
                line.append(colorize("─",r,g,b))
            elif row<center and (center-row)<=lvl:
                line.append(colorize("█",r,g,b))
            elif row>center and (row-center)<=lvl:
                line.append(colorize("█",r,g,b))
            else:
                line.append(" ")
        screen.append("".join(line))

    if lyrics:
        screen.append("")
        screen.append(render_lyrics_block(lyric_index, r, g, b))

    sys.stdout.write("\033[H\033[J" + "\n".join(screen))
    sys.stdout.flush()
    start_idx += frames

with sd.OutputStream(channels=1, samplerate=samplerate,
                     callback=callback, blocksize=BLOCKSIZE, latency="low"):
    sd.sleep(int((len(data) - start_idx) / samplerate * 1000))
