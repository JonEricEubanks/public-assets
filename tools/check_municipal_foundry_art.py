"""Browser checks for the casebook's layout, motion, accessibility and exports."""

import io
import re

from build_municipal_foundry_art import (
    BLOG, GALLERY, LOOP_MS, OUT, PREVIEW, PUBLIC_IMAGES, SCENES, launch_browser,
)

SEEK = """ms => document.getAnimations().forEach(a => {
    a.pause(); a.currentTime = ms;
})"""

GEOMETRY = """() => {
  const issues = [];
  if (document.documentElement.scrollWidth > innerWidth + 1) issues.push("horizontal overflow");
  const overlap = (a, b) => a.left < b.right - .5 && b.left < a.right - .5
    && a.top < b.bottom - .5 && b.top < a.bottom - .5;
  document.querySelectorAll(".casebook-scene").forEach(scene => {
    const frame = scene.getBoundingClientRect();
    const art = scene.querySelector(".cb-art").getBoundingClientRect();
    const texts = [...scene.querySelectorAll("h3,h4,p,.cb-number")];
    const boxes = texts.flatMap(el => {
      const range = document.createRange();
      range.selectNodeContents(el);
      return [...range.getClientRects()].map(rect => ({el, rect}));
    });
    boxes.forEach(({el, rect}, i) => {
      if (rect.left < frame.left || rect.right > frame.right ||
          rect.top < frame.top || rect.bottom > frame.bottom)
        issues.push(scene.id + " clipped text: " + el.textContent);
      if (overlap(rect, art)) issues.push(scene.id + " text overlays artwork: " + el.textContent);
      boxes.slice(i + 1).forEach(other => {
        if (el !== other.el && overlap(rect, other.rect))
          issues.push(scene.id + " text collision: " + el.textContent + " / " + other.el.textContent);
      });
    });
    const cards = [...scene.querySelectorAll(".cb-card")];
    cards.forEach(card => {
      const bounds = card.getBoundingClientRect();
      card.querySelectorAll("h4,p").forEach(el => {
        const rect = el.getBoundingClientRect();
        if (rect.left < bounds.left || rect.right > bounds.right ||
            rect.top < bounds.top || rect.bottom > bounds.bottom)
          issues.push(scene.id + " card content overflow: " + el.textContent);
      });
    });
  });
  return issues;
}"""

CONTRAST = """() => {
  const luminance = rgb => rgb.map(v => {
    v /= 255;
    return v <= .04045 ? v / 12.92 : ((v + .055) / 1.055) ** 2.4;
  }).reduce((sum, v, i) => sum + v * [.2126, .7152, .0722][i], 0);
  const parse = css => css.match(/[\\d.]+/g).map(Number);
  return [...document.querySelectorAll(".casebook-scene h3,.casebook-scene h4,.casebook-scene p,.cb-number")]
    .flatMap(el => {
      const text = luminance(parse(getComputedStyle(el).color).slice(0, 3));
      let parent = el, bg;
      while (parent) {
        bg = parse(getComputedStyle(parent).backgroundColor);
        if (bg.length === 3 || bg[3] === 1) break;
        parent = parent.parentElement;
      }
      const background = luminance(bg.slice(0, 3));
      const ratio = (Math.max(text, background) + .05) / (Math.min(text, background) + .05);
      return ratio < 4.5 ? [el.textContent + ": " + ratio.toFixed(2)] : [];
    });
}"""


def ready(page, path):
    page.goto(path.as_uri())
    page.wait_for_function("[...document.images].every(i => i.complete && i.naturalWidth > 0)")
    page.evaluate("document.fonts.ready")


def check():
    from PIL import Image, ImageChops, ImageStat
    from playwright.sync_api import sync_playwright

    urls = re.findall(r'<img\b[^>]*src="([^"]+)"', BLOG.read_text(encoding="utf-8"))
    expected = {PUBLIC_IMAGES + s["name"] + ".png" for s in SCENES}
    assert len(urls) == len(expected) and set(urls) == expected, "Blog references differ from the five PNG exports"
    for url in urls:
        assert (OUT / url.removeprefix(PUBLIC_IMAGES)).is_file(), f"Missing blog image: {url}"

    with sync_playwright() as playwright:
        browser = launch_browser(playwright)
        try:
            page = browser.new_page(viewport={"width": 1440, "height": 1400})
            errors = []
            page.on("pageerror", lambda error: errors.append(str(error)))
            page.on("requestfailed", lambda request: errors.append(request.url + ": " + request.failure))
            page.emulate_media(reduced_motion="no-preference")
            for width in (320, 390, 700, 701, 960, 1440):
                page.set_viewport_size({"width": width, "height": 1400})
                ready(page, PREVIEW)
                for ms in (0, 4000, 8000, 11900):
                    page.evaluate(SEEK, ms)
                    assert not (issues := page.evaluate(GEOMETRY)), f"{width}px/{ms}ms: {issues}"
                    assert not (issues := page.evaluate(CONTRAST)), f"Text contrast: {issues}"
            print("PASS: full text bounds and 4.5:1 contrast; six widths, four animation times.")

            page.set_viewport_size({"width": 1200, "height": 1400})
            ready(page, GALLERY)

            def capture(selector):
                box = page.locator(selector).bounding_box()
                assert box, f"Missing screenshot target: {selector}"
                return Image.open(io.BytesIO(page.screenshot(clip=box))).convert("RGB")

            for scene in SCENES:
                selector = "#casebook-" + scene["id"]
                page.locator(selector).scroll_into_view_if_needed()
                page.wait_for_function(
                    "id => document.querySelector(id).dataset.paused === 'false'", arg=selector,
                )
                page.evaluate(SEEK, 0)
                first = capture(selector + " .cb-art")
                page.evaluate(SEEK, 4000)
                later = capture(selector + " .cb-art")
                assert max(ImageStat.Stat(ImageChops.difference(first, later)).mean) > .1, (
                    f'Artwork itself has no measurable motion: {scene["id"]}'
                )
            print("PASS: all five artwork regions animate, independently of text indicators.")

            # Reload clears deterministic test pauses before exercising real controls.
            ready(page, GALLERY)
            page.evaluate("window.scrollTo(0, 0)")
            page.wait_for_timeout(300)
            button = page.locator("#casebook-motion")
            button.click()
            assert page.locator("html").get_attribute("data-motion") == "off"
            assert page.evaluate("document.getAnimations().length") == 0
            first = capture("#casebook-hero")
            page.wait_for_timeout(350)
            assert ImageChops.difference(first, capture("#casebook-hero")).getbbox() is None
            button.click()
            assert page.locator("html").get_attribute("data-motion") == "on"
            assert page.evaluate("document.getAnimations().length") > 0

            page.emulate_media(reduced_motion="reduce")
            page.wait_for_function("document.documentElement.dataset.motion === 'off'")
            assert button.is_disabled()
            assert page.evaluate("document.getAnimations().length") == 0
            first = capture("#casebook-hero")
            page.wait_for_timeout(350)
            assert ImageChops.difference(first, capture("#casebook-hero")).getbbox() is None
            page.emulate_media(reduced_motion="no-preference")
            page.wait_for_function("document.documentElement.dataset.motion === 'on'")
            page.locator("#casebook-pilot").scroll_into_view_if_needed()
            page.wait_for_function("document.querySelector('#casebook-hero').dataset.paused === 'true'")
            assert page.locator("#casebook-hero").evaluate(
                "el => el.getAnimations({subtree:true}).every(a => a.playState === 'paused')"
            )
            assert not errors, errors
            print("PASS: still/resume controls, live reduced-motion changes, and offscreen pause.")

            no_js = browser.new_context(java_script_enabled=False)
            try:
                static_page = no_js.new_page()
                ready(static_page, PREVIEW)
                assert static_page.locator(".casebook-scene").count() == 5
                assert static_page.evaluate("document.getAnimations().length") == 0
                assert not static_page.locator("#casebook-motion").is_visible()
            finally:
                no_js.close()
            print("PASS: no-JavaScript fallback keeps five readable static scenes.")
        finally:
            browser.close()

    gifs = [OUT / (s["name"] + ".gif") for s in SCENES]
    if any(path.exists() for path in gifs):
        assert all(path.exists() for path in gifs), "Incomplete GIF export set"
        for path in gifs:
            assert path.stat().st_size <= 10_000_000, f"GIF exceeds 10 MB: {path}"
            with Image.open(path) as image:
                assert image.width == 960 and image.n_frames > 1 and image.info["loop"] == 0, path
                total = 0
                for i in range(image.n_frames):
                    image.seek(i)
                    total += image.info["duration"]
                assert total == LOOP_MS, f"{path}: {total}ms"
        print("PASS: all five GIFs loop for exactly 12,000ms at 960px wide, under 10 MB each.")
    print("Casebook checks passed.")


if __name__ == "__main__":
    check()
