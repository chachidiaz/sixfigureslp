"""Build the email GIF: an issue page scrolling inside the phone mockup.

usage: python3 email-gif/make_gif.py <capture-dir> <out-dir> <slug> [<slug> ...]

Reads <capture-dir>/<slug>.png and .json from capture.mjs and writes
<out-dir>/<slug>.gif. The scroll holds on the headline, glides to each graphic
(or callout, or section heading when there are no graphics), and returns to the
top so the loop restarts cleanly.
"""
import json
import math
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

HERE = Path(__file__).parent
FRAME = HERE / 'phone-frame.webp'
MASK = HERE / 'phone-screen-mask.png'

OUT_WIDTH = 800        # displays crisply at 600px in an email
FPS = 10
COLORS = 64            # keeps the file around 1.5 MB
DPR = 2                # capture.mjs screenshots at 2x
STATUS_CSS = 56        # phone status bar height, CSS px
ISLAND_Y = 157         # centre of the dynamic island in phone-frame.webp
MAX_STOPS = 6
PAPER = (250, 246, 239)
INK = (36, 16, 26)
FONTS = [
    '/usr/share/fonts/opentype/inter/Inter-SemiBold.otf',
    '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',
]


def font(size):
    for path in FONTS:
        if Path(path).exists():
            return ImageFont.truetype(path, size)
    return ImageFont.load_default(size)


def status_bar(width, height, cy):
    bar = Image.new('RGB', (width, height), PAPER)
    d = ImageDraw.Draw(bar)
    d.text((round(width * 0.17), cy), '9:41', font=font(34), fill=INK, anchor='mm')
    x = round(width * 0.80)
    for i, h in enumerate((10, 15, 20, 25)):  # signal bars
        d.rounded_rectangle((x + i * 9, cy + 12 - h, x + i * 9 + 6, cy + 12), 2, fill=INK)
    x += 52
    d.rounded_rectangle((x, cy - 11, x + 46, cy + 11), 7, outline=INK, width=3)  # battery
    d.rounded_rectangle((x + 5, cy - 6, x + 34, cy + 6), 3, fill=INK)
    d.rounded_rectangle((x + 49, cy - 4, x + 53, cy + 4), 1, fill=INK)
    return bar


def plan_stops(layout, view_css):
    """Return [(offset_css, scroll_secs, hold_secs)] for the scroll."""
    targets = layout['graphics'] or layout['callouts'] or layout['headings']
    if layout['graphics']:
        # Mix callouts in when there's room, in reading order.
        targets = sorted(layout['graphics'] + layout['callouts'], key=lambda b: b['y'])
    picked, last = [], -1e9
    for box in targets:
        if box['y'] - last > view_css * 0.6:
            picked.append(box)
            last = box['y']
    if len(picked) > MAX_STOPS:
        step = len(picked) / MAX_STOPS
        picked = [picked[math.floor(i * step)] for i in range(MAX_STOPS)]

    pad = 24
    max_off = layout['height'] - view_css
    stops = [(0, 0, 1.6)]
    for box in picked:
        stops.append((min(box['y'] - pad, max_off), None, 1.3))
        if box['h'] > view_css * 1.2:  # tall graphic: show its end too
            stops[-1] = (stops[-1][0], None, 0.7)
            stops.append((min(box['y'] + box['h'] - view_css + pad, max_off), None, 1.0))
    stops.append((0, None, 0))

    timed, prev = [], 0
    for off, secs, hold in stops:
        if secs is None:
            dist = abs(off - prev)
            secs = min(1.5, max(0.8, 0.6 + dist / 4000))
        timed.append((off, secs, hold))
        prev = off
    return timed


def build(slug, capture_dir, out_dir):
    frame = Image.open(FRAME).convert('RGB')
    mask_raw = Image.open(MASK).convert('L')
    sx0, sy0, sx1, sy1 = mask_raw.getbbox()
    mask = mask_raw.filter(ImageFilter.GaussianBlur(0.8))
    page = Image.open(capture_dir / f'{slug}.png').convert('RGB')
    layout = json.loads((capture_dir / f'{slug}.json').read_text())

    screen_w, screen_h = sx1 - sx0, sy1 - sy0
    k = screen_w / page.width                  # page px -> frame px
    view_h = math.ceil(screen_h / k)           # page px visible on the screen
    status_h = STATUS_CSS * DPR
    scroll_h = view_h - status_h
    max_off = max(0, page.height - scroll_h)
    bar = status_bar(page.width, status_h, round((ISLAND_Y - sy0) / k))

    s = OUT_WIDTH / frame.width
    out_h = round(frame.height * s)
    frame_s = frame.resize((OUT_WIDTH, out_h), Image.LANCZOS)
    mask_s = mask.resize((OUT_WIDTH, out_h), Image.LANCZOS)
    scr_pos = (round(sx0 * s), round(sy0 * s))
    scr_size = (round(screen_w * s), round(screen_h * s))

    def render(off):
        off = max(0, min(max_off, round(off)))
        content = Image.new('RGB', (page.width, view_h), PAPER)
        content.paste(bar, (0, 0))
        content.paste(page.crop((0, off, page.width, off + scroll_h)), (0, status_h))
        layer = frame_s.copy()
        layer.paste(content.resize(scr_size, Image.LANCZOS), scr_pos)
        return Image.composite(layer, frame_s, mask_s)

    def ease(t):
        return t * t * (3 - 2 * t)

    frames, durations, cur = [], [], 0
    for off_css, secs, hold in plan_stops(layout, scroll_h // DPR):
        target = off_css * DPR
        n = round(secs * FPS) if secs else 0
        for i in range(1, n + 1):
            frames.append(render(cur + (target - cur) * ease(i / n)))
            durations.append(round(1000 / FPS))
        if n == 0:
            frames.append(render(target))
            durations.append(20)
        cur = target
        durations[-1] += round(hold * 1000)

    # One shared palette keeps the colours steady from frame to frame.
    picks = frames[:: max(1, len(frames) // 4)][:4]
    sample = Image.new('RGB', (OUT_WIDTH, out_h * len(picks)))
    for i, f in enumerate(picks):
        sample.paste(f, (0, i * out_h))
    pal = sample.quantize(colors=COLORS, method=Image.Quantize.MEDIANCUT)
    q = [f.quantize(palette=pal, dither=Image.Dither.NONE) for f in frames]
    out = out_dir / f'{slug}.gif'
    q[0].save(out, save_all=True, append_images=q[1:], duration=durations, loop=0, optimize=True, disposal=1)
    print(f'{out}: {len(frames)} frames, {sum(durations) / 1000:.1f}s, {out.stat().st_size / 1e6:.1f} MB')


def main():
    if len(sys.argv) < 4:
        sys.exit(__doc__)
    capture_dir, out_dir = Path(sys.argv[1]), Path(sys.argv[2])
    out_dir.mkdir(parents=True, exist_ok=True)
    for slug in sys.argv[3:]:
        build(slug, capture_dir, out_dir)


if __name__ == '__main__':
    main()
