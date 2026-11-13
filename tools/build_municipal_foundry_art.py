"""Build the rendered civic casebook gallery, blog preview, and PNG/GIF exports.

python .\\tools\\build_municipal_foundry_art.py --previews --check

Source renders are preserved in images/municipal-foundry-sources. Rebuilding
does not call an image model. Browser export requires Pillow and Playwright.
"""

import argparse
import io
import re
from html import escape
from pathlib import Path

from municipal_foundry_fx import hero_fx, pilot_fx, platform_fx, rename_fx, review_fx

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "images"
BLOG = ROOT / "blogs" / "microsoft-foundry-minus-the-rename-noise.html"
PREVIEW = BLOG.with_name(BLOG.stem + "-preview.html")
GALLERY = BLOG.with_name("municipal-foundry-casebook.html")
PUBLIC_IMAGES = "https://raw.githubusercontent.com/JonEricEubanks/public-assets/main/images/"
LOOP_MS = 12000
STILL_MS = 9000

SCENES = [
    {
        "id": "hero", "name": "municipal-foundry-daylight-hero",
        "eyebrow": "MICROSOFT FOUNDRY FOR LOCAL GOVERNMENT",
        "title": "Better service. Clear ownership.",
        "intro": "AI helps staff behind the counter. The municipality decides what goes back over it.",
        "alt": "A two-level municipal service counter. A resident's request card and service bell sit on the frosted-blue public ledge. On the staff surface behind it, guidance, a park photo and a note sit beside a partly written response that has not been handed over.",
        "cards": [
            ("The request", "One resident question arrives at the public counter."),
            ("The support", "Foundry capabilities help staff gather guidance and evidence."),
            ("The response", "It stays on the staff side until someone accountable approves it."),
        ],
        "note": "Illustrative scene. The public ledge stays empty in every frame: nothing is handed over automatically.",
        "path": "M765 125 C700 150 660 170 629 185 S560 240 540 258",
        "focus": (420, 352),
        "fx": hero_fx,
    },
    {
        "id": "rename", "name": "municipal-foundry-rename-path",
        "eyebrow": "FIRST: WHAT HAPPENED TO AZURE AI FOUNDRY?",
        "title": "Same seat. New nameplate.",
        "intro": "The insert changed twice. The holder, your responsibility, never moved.",
        "alt": "Two removed frosted-blue name inserts lie beside a solid desk nameplate holder that now holds a third, identical insert.",
        "cards": [
            ("Azure AI Studio", "The earlier name."),
            ("Azure AI Foundry", "Introduced at Ignite 2024."),
            ("Microsoft Foundry", "The name used by Ignite 2025."),
        ],
        "note": "The holder is your accountability, not the architecture: check classic hub-based versus newer project types.",
        "path": "M360 330 C440 320 540 260 600 220 S680 185 700 180",
        "focus": (700, 308),
        "fx": rename_fx,
    },
    {
        "id": "platform", "name": "municipal-foundry-service-pavilion",
        "eyebrow": "FIGURE 1 / WHO OWNS WHAT",
        "title": "One hub. Many front doors.",
        "intro": "Foundry sits behind the services your team builds. Each keeps its own lock.",
        "alt": "A frosted-blue hub connects along one rail to a phone, a tablet, a laptop and a desktop monitor. Each device has its own lock.",
        "cards": [
            ("Foundry, the hub", "Models, Agent Service, Foundry IQ and Tools, shared behind every experience."),
            ("Your experiences", "Resident app, field tablet, staff laptop, back-office desktop: built and owned by your team."),
            ("Each with its own lock", "Sign-in, permissions, accessibility and support stay with each service."),
        ],
        "note": "Search, Storage, Key Vault and systems of record also stay separately governed, with their own meters. Foundry IQ is not Azure AI Search renamed.",
        "path": "M273 231 C330 238 360 242 395 245 S490 258 538 262 S680 272 733 276",
        "focus": (847, 313),
        "fx": platform_fx,
    },
    {
        "id": "review", "name": "municipal-foundry-review-bridge",
        "eyebrow": "FIGURE 2 / A SAFE MUNICIPAL AI PATTERN",
        "title": "Prepared is not approved.",
        "intro": "AI can produce the proof. Staff mark it up before anything is posted.",
        "alt": "A draft notice on a proofing lightbox has one line struck through and flagged for correction. A separate public notice display case is still empty.",
        "cards": [
            ("Proof the draft", "Check sources, citations and missing information."),
            ("Mark corrections", "Clarify, correct or escalate before acting."),
            ("Post deliberately", "Only approved outcomes reach the official record or the public."),
        ],
        "note": "The display stays empty in every frame. The animation highlights review, never automatic publishing.",
        "path": "M239 264 C300 260 380 254 424 251 S460 244 476 241",
        "focus": (786, 169),
        "fx": review_fx,
    },
    {
        "id": "pilot", "name": "municipal-foundry-evidence-footer",
        "eyebrow": "WHERE I WOULD START",
        "title": "Start with one plot. Earn the next.",
        "intro": "One bounded process, measured before anything expands.",
        "alt": "A parks planning model with one planted plot, measured by three stakes, beside empty plots awaiting a decision.",
        "cards": [
            ("Plant one plot", "Give AI only the information and tools this process needs."),
            ("Measure it", "Accuracy, staff time, failures and cost under realistic use."),
            ("Then decide", "The empty plots wait for evidence, not enthusiasm."),
        ],
        "note": "The stakes are illustrative measurements, not performance data.",
        "path": "M135 221 C130 205 115 195 111 183 S118 145 123 134",
        "focus": (123, 180),
        "fx": pilot_fx,
    },
]


def scene_html(scene):
    sid = scene["id"]
    cards = "".join(
        f'<li class="cb-card" style="--step:{i}"><span class="cb-number" aria-hidden="true">0{i + 1}</span>'
        f'<div><h4>{escape(title)}</h4><p>{escape(body)}</p></div></li>'
        for i, (title, body) in enumerate(scene["cards"])
    )
    cx, cy = scene["focus"]
    if "fx" in scene:
        layer = (
            '<svg class="cb-light-layer cb-fx" viewBox="0 0 1774 887" aria-hidden="true" focusable="false">'
            + scene["fx"]() + "</svg>"
        )
    else:
        layer = f"""      <svg class="cb-light-layer" viewBox="0 0 1000 500" aria-hidden="true" focusable="false">
        <defs>
          <linearGradient id="{sid}-trail" x1="0" x2="1">
            <stop stop-color="#527fa0" stop-opacity=".12"/>
            <stop offset="1" stop-color="#447a86" stop-opacity=".7"/>
          </linearGradient>
          <radialGradient id="{sid}-glow">
            <stop stop-color="#bcd7cf" stop-opacity=".4"/>
            <stop offset="1" stop-color="#bcd7cf" stop-opacity="0"/>
          </radialGradient>
        </defs>
        <path class="cb-trail" d="{scene["path"]}" pathLength="1" stroke="url(#{sid}-trail)"/>
        <path class="cb-traveller" d="{scene["path"]}" pathLength="1"/>
        <g class="cb-focus" style="transform-origin:{cx}px {cy}px">
          <ellipse cx="{cx}" cy="{cy}" rx="60" ry="28" fill="url(#{sid}-glow)"/>
          <ellipse cx="{cx}" cy="{cy}" rx="34" ry="14" fill="none" stroke="#59817b"
            stroke-width="1.2" stroke-opacity=".55" stroke-dasharray="2 6"/>
        </g>
      </svg>
"""
    return f"""
<section class="casebook-scene" id="casebook-{sid}" aria-labelledby="{sid}-title">
  <header class="cb-heading">
    <p class="cb-eyebrow">{escape(scene["eyebrow"])}</p>
    <h3 id="{sid}-title">{escape(scene["title"])}</h3>
    <p class="cb-intro">{escape(scene["intro"])}</p>
  </header>
  <div class="cb-art">
    <div class="cb-render-layer">
      <img src="../images/municipal-foundry-sources/{sid}.png" width="1774" height="887"
        alt="{escape(scene["alt"], quote=True)}" decoding="async"/>
{layer}    </div>
  </div>
  <ol class="cb-cards">{cards}</ol>
  <p class="cb-note">{escape(scene["note"])}</p>
</section>"""


TOOLBAR = """
<div class="cb-toolbar">
  <p>Rendered artwork + layered web motion <span>/ 12-second chapters</span></p>
  <button type="button" id="casebook-motion" hidden>Show stills</button>
  <noscript><p>Still artwork shown. JavaScript is required for animation controls.</p></noscript>
</div>"""


def document(body, title):
    return (
        '<!doctype html>\n<!-- Generated by tools/build_municipal_foundry_art.py. -->\n'
        '<html lang="en" data-motion="off"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width, initial-scale=1">'
        f'<title>{escape(title)}</title>'
        '<link rel="stylesheet" href="municipal-foundry-casebook.css">'
        '<script src="municipal-foundry-casebook.js" defer></script>'
        f'</head><body><main><h1>{escape(title)}</h1>{TOOLBAR}{body}</main></body></html>\n'
    )


def build():
    for scene in SCENES:
        source = OUT / "municipal-foundry-sources" / f'{scene["id"]}.png'
        if not source.is_file():
            raise FileNotFoundError(f"Missing preserved render: {source}")
    gallery = "".join(
        f'<figure>{scene_html(s)}<figcaption>'
        f'<a href="../images/{s["name"]}.png" download>Download PNG still</a>'
        f' &middot; <a href="../images/{s["name"]}.gif" download>Download animated GIF</a>'
        '</figcaption></figure>'
        for s in SCENES
    )
    GALLERY.write_text(document(gallery, "Microsoft Foundry blog illustrations"), encoding="utf-8")
    body = BLOG.read_text(encoding="utf-8").replace(PUBLIC_IMAGES, "../images/")
    for scene in SCENES:
        pattern = rf'<img\b[^>]*src="\.\./images/{re.escape(scene["name"])}\.png"[^>]*/>'
        body, count = re.subn(pattern, lambda _: scene_html(scene), body)
        if count != 1:
            raise ValueError(f'Expected exactly one blog image for {scene["name"]}, found {count}')
    PREVIEW.write_text(
        document(body, "Microsoft Foundry, Minus the Rename Noise"), encoding="utf-8",
    )
    print(f"Wrote {GALLERY.name} and {PREVIEW.name}")


def launch_browser(playwright):
    edge = Path(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")
    if edge.is_file():
        return playwright.chromium.launch(executable_path=str(edge))
    return playwright.chromium.launch()


def export(stills, gifs):
    from PIL import Image, ImageChops, ImageStat
    from playwright.sync_api import sync_playwright

    css = (BLOG.parent / "municipal-foundry-casebook.css").read_text(encoding="utf-8")
    with sync_playwright() as playwright:
        browser = launch_browser(playwright)
        try:
            # Lay out at publishing width so GIF/PNG text is not reduced to tiny labels.
            page = browser.new_page(viewport={"width": 960, "height": 1400}, device_scale_factor=2)
            page.emulate_media(reduced_motion="no-preference")
            for scene in SCENES:
                markup = scene_html(scene).replace(
                    "../images/", OUT.as_uri() + "/",
                )
                # Navigate to a local origin before embedding local image resources.
                page.goto(GALLERY.as_uri())
                page.set_content(
                    f'<html data-motion="on"><head><style>{css}'
                    'body{background:#fff}.casebook-scene{border:0;border-radius:0}'
                    f'</style></head><body>{markup}</body></html>'
                )
                page.wait_for_function(
                    "[...document.images].every(i => i.complete && i.naturalWidth > 0)"
                )
                page.evaluate("document.fonts.ready")
                box = page.locator(".casebook-scene").bounding_box()
                if not box or box["height"] > 1400:
                    raise RuntimeError(f'Export viewport does not fit {scene["id"]}: {box}')

                def frame(ms, scale="css"):
                    page.evaluate("""ms => document.getAnimations().forEach(a => {
                        a.pause(); a.currentTime = ms;
                    })""", ms)
                    return Image.open(io.BytesIO(page.screenshot(clip=box, scale=scale))).convert("RGB")

                if stills:
                    # The PNG is the fully legible, motion-free composition, not a mid-transition frame.
                    page.locator("html").evaluate("el => el.dataset.motion = 'off'")
                    frame(STILL_MS, scale="device").save(OUT / f'{scene["name"]}.png', optimize=True)
                    page.locator("html").evaluate("el => el.dataset.motion = 'on'")
                if gifs:
                    # Keep the photographic layer stable so GIF delta frames stay small.
                    # Citation trails, review highlights and chapter indicators still animate.
                    page.add_style_tag(content=".cb-render-layer{animation:none !important}")
                    size = (960, round(960 * box["height"] / box["width"]))
                    frames = [
                        frame(ms).resize(size, Image.Resampling.LANCZOS)
                        for ms in range(0, LOOP_MS, 100)
                    ]
                    difference = ImageStat.Stat(ImageChops.difference(frames[0], frames[40]))
                    if max(difference.mean) < 0.1:
                        raise RuntimeError(f'No measurable exported motion: {scene["id"]}')
                    # One palette across the loop avoids frame-to-frame color flicker.
                    strip = Image.new("RGB", (size[0], size[1] * 4))
                    for i in range(4):
                        strip.paste(frames[i * len(frames) // 4], (0, size[1] * i))
                    palette = strip.quantize(colors=255, method=Image.Quantize.MEDIANCUT)
                    colours = palette.getpalette()
                    palette.putpalette(colours[:765] + colours[:3])
                    indexed = [
                        im.quantize(palette=palette, dither=Image.Dither.NONE).point(
                            [0 if i == 255 else i for i in range(256)]
                        )
                        for im in frames
                    ]
                    # Reserve index 255 for unchanged pixels; older Pillow versions
                    # crop delta rectangles but do not make their interiors transparent.
                    deltas = [indexed[0]]
                    for previous, current in zip(indexed, indexed[1:]):
                        before = Image.frombytes("L", size, previous.tobytes())
                        after = Image.frombytes("L", size, current.tobytes())
                        unchanged = ImageChops.difference(before, after).point(
                            [255] + [0] * 255
                        )
                        delta = current.copy()
                        delta.paste(255, mask=unchanged)
                        deltas.append(delta)
                    dest = OUT / f'{scene["name"]}.gif'
                    deltas[0].save(
                        dest, save_all=True, append_images=deltas[1:],
                        duration=100, loop=0, optimize=False, disposal=1, transparency=255,
                    )
                    with Image.open(dest) as result:
                        duration = 0
                        for i in range(result.n_frames):
                            result.seek(i)
                            duration += result.info["duration"]
                            if duration in (100, 4100, 8100):
                                expected = indexed[(duration - 100) // 100].convert("RGB")
                                if ImageChops.difference(result.convert("RGB"), expected).getbbox():
                                    raise RuntimeError(f"GIF delta reconstruction failed: {dest}, {duration}ms")
                        if duration != LOOP_MS or result.n_frames < 2:
                            raise RuntimeError(f"Invalid GIF timing: {dest}, {duration}ms")
                    print(f'{dest.name}: {len(frames)} frames, {LOOP_MS}ms, {dest.stat().st_size:,} bytes')
                    if dest.stat().st_size > 10_000_000:
                        raise RuntimeError(f"GIF exceeds the 10 MB publishing budget: {dest}")
        finally:
            browser.close()


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--stills", action="store_true")
    parser.add_argument("--previews", action="store_true", help="export PNGs and 12-second GIFs")
    parser.add_argument("--check", action="store_true", help="run browser regression checks")
    args = parser.parse_args()
    build()
    if args.stills or args.previews:
        export(True, args.previews)
    if args.check:
        from check_municipal_foundry_art import check
        check()


if __name__ == "__main__":
    main()
