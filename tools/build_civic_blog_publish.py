"""Build a script-free Tech Community HTML fragment with public image URLs."""

from html import escape
from html.parser import HTMLParser
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "blogs" / "vector-search-knowledge-graphs-fabric.html"
OUTPUT = ROOT / "blogs" / "vector-search-knowledge-graphs-fabric-techcommunity.html"
PUBLIC_IMAGES = "https://raw.githubusercontent.com/JonEricEubanks/public-assets/main/images/"


class PublishedImages(HTMLParser):
    def __init__(self):
        super().__init__()
        self.images = []
        self.tags = []

    def handle_starttag(self, tag, attrs):
        self.tags.append(tag)
        if tag == "img":
            self.images.append(dict(attrs))


def build():
    source = SOURCE.read_text(encoding="utf-8")
    article = re.search(r"<article>\s*(.*?)\s*</article>", source, re.DOTALL)
    if article is None:
        raise ValueError("The preview must contain an article.")
    body = article.group(1)
    body, captures = re.subn(
        r'\s*<aside class="capture">.*?</aside>', "", body, flags=re.DOTALL
    )
    if captures != 5:
        raise ValueError(f"Expected five capture notes, found {captures}.")
    body = re.sub(r"\s*<h1>.*?</h1>", "", body, count=1, flags=re.DOTALL)
    body = re.sub(
        r'\s*<p class="meta">JonEricEubanks.*?</p>', "", body, count=1,
        flags=re.DOTALL,
    )
    body = re.sub(
        r'\s*<p class="eyebrow">.*?</p>', "", body, count=1, flags=re.DOTALL
    )

    def publish_image(match):
        filename = match.group(1)
        if not (ROOT / "images" / filename).is_file():
            raise FileNotFoundError(filename)
        alt = match.group(2)
        svg_url = escape(PUBLIC_IMAGES + filename, quote=True)
        return (
            '<img\n'
            '        style="width: 100%; max-width: 960px; height: auto"\n'
            f'        src="{svg_url}"\n'
            f'        alt="{alt}"\n'
            '        loading="lazy"\n'
            '      />'
        )

    body, images = re.subn(
        r'<img data-civic-art src="\.\./images/([^"]+\.svg)"[^>]*?alt="([^"]*)"[^>]*>',
        publish_image, body,
    )
    if images != 11:
        raise ValueError(f"Expected eleven images, found {images}.")
    body = re.sub(r' class="(?:eyebrow|meta)"', "", body)
    result = body.strip() + "\n"
    parser = PublishedImages()
    parser.feed(result)
    if any(tag in parser.tags for tag in ["script", "object", "style", "aside", "h1"]):
        raise ValueError("Publishing output contains preview-only markup.")
    if len(parser.images) != 11 or any(
        not image["src"].startswith(PUBLIC_IMAGES)
        or not image["src"].endswith(".svg") for image in parser.images
    ):
        raise ValueError("Publishing images must use absolute public SVG URLs.")
    OUTPUT.write_text(result, encoding="utf-8")
    print(f"Built Tech Community fragment with 11 public SVG images: {OUTPUT}")


if __name__ == "__main__":
    build()
