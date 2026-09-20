"""Screenshot a web page (or local built HTML file) with headless Chrome and cut it into tiles.

usage: uv run --with pillow python tools/shoot.py URL OUTPREFIX [--width 1280] [--max-height 16000]
Writes OUTPREFIX-01.png, -02.png ... (each 1600 px tall, trailing blank area trimmed). Read the tiles
with the Read tool. Use --width 400 for the phone layout. Pace requests: one page every few seconds.
"""
import argparse, subprocess, sys, tempfile, os, time
from PIL import Image, ImageChops
Image.MAX_IMAGE_PIXELS = None
ap = argparse.ArgumentParser(); ap.add_argument("url"); ap.add_argument("out")
ap.add_argument("--width", type=int, default=1280); ap.add_argument("--max-height", type=int, default=16000)
ap.add_argument("--tile", type=int, default=1600)
a = ap.parse_args()
tmp = tempfile.mktemp(suffix=".png", dir=os.path.dirname(os.path.abspath(a.out)) or ".")
import shutil, signal
for attempt in range(3):
    prof = tempfile.mkdtemp(prefix="chrome-prof-", dir=os.path.dirname(tmp))
    p = subprocess.Popen(["google-chrome", "--headless=new", "--no-sandbox", "--disable-gpu", "--hide-scrollbars",
                          f"--user-data-dir={prof}", f"--window-size={a.width},{a.max_height}",
                          "--user-agent=sky130-process-tech docs checker", f"--screenshot={tmp}", a.url],
                         stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, start_new_session=True)
    try:
        p.wait(timeout=60)
    except subprocess.TimeoutExpired:
        pass
    try: os.killpg(p.pid, signal.SIGKILL)
    except ProcessLookupError: pass
    shutil.rmtree(prof, ignore_errors=True)
    if os.path.exists(tmp) and os.path.getsize(tmp) > 0: break
    time.sleep(3)
else:
    sys.exit("screenshot failed three times: " + a.url)
im = Image.open(tmp).convert("RGB")
x0 = int(im.width * 0.3) if im.width > 900 else 0   # ignore the full-height sidebar
n = 0; kept = 0
for y in range(0, im.height, a.tile):
    n += 1
    t = im.crop((0, y, im.width, min(y + a.tile, im.height)))
    col = t.crop((x0, 0, t.width, t.height))
    if ImageChops.difference(col, Image.new("RGB", col.size, col.getpixel((col.width - 1, 0)))).getbbox() is None:
        continue                                          # blank filler between content and footer
    kept += 1; t.save(f"{a.out}-{n:02d}.png")
h = f"{kept} tiles kept of {n}" + (" (page may be longer than the capture; the footer is always the last tile)" if kept == n else "")
os.remove(tmp); print(f"{h} -> {a.out}-NN.png")
time.sleep(2)
