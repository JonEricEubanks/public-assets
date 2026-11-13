# public-assets
Publicly accessible images, icons, screenshots, diagrams, and media assets used across applications, documentation, blogs, and community content.

## Civic Evidence Lab

- [Illustrated vector search, knowledge graphs, and Fabric Graph blog](blogs/vector-search-knowledge-graphs-fabric.html)
- [Tech Community paste-ready HTML with public image URLs](blogs/vector-search-knowledge-graphs-fabric-techcommunity.html)
- [Visual theme, screenshot capture checklist, and publishing guide](blogs/civic-evidence-lab-guide.md)
- [SVG artwork generator](tools/build_civic_evidence_art.py)

The collection includes 11 original animated, scene-led SVG illustrations and matching static PNG fallbacks.
The local blog preview defaults to animated SVGs and provides a still-image switch.
The blog is a local editorial draft; conceptual illustrations are not product screenshots.

## Microsoft Foundry, Minus the Rename Noise

- [Tech Community paste-ready blog](blogs/microsoft-foundry-minus-the-rename-noise.html) with public image URLs
- [Local preview](blogs/microsoft-foundry-minus-the-rename-noise-preview.html) of the same blog, reading the images in this checkout
- [Animated illustration gallery](blogs/municipal-foundry-casebook.html)
- [Artwork builder and exporter](tools/build_municipal_foundry_art.py)
- [Preserved source renders](images/municipal-foundry-sources)

Five light-theme, rendered 3D illustrations share one palette and material
language (pearl white, frosted ice-blue resin, pale sage, graphite) but each
uses its own metaphor for its section:

| Section | Metaphor | Message |
|---|---|---|
| Opening | Two-level municipal service counter; the response is not handed over yet | Better service, clear ownership |
| The rename | Desk nameplate holder with two removed inserts | The name changed; the responsibility did not |
| Figure 1 | Foundry hub connected to a phone, tablet, laptop and desktop, each with its own lock | One hub, many front doors |
| Figure 2 | Marked-up proof on a lightbox beside an empty notice display | Prepared is not approved |
| Closing | Parks planning model with one planted, measured plot | Start with one plot, earn the next |

These are conceptual illustrations, not product screenshots or claims about a
specific community's deployment. The pilot stakes are illustrative, not data.

The look uses PNG source renders with separate HTML typography and an animated
SVG layer drawn in source-image pixels (`tools/municipal_foundry_fx.py`). Each
scene plays a 12-second story: the bell rings and staff gather cited sources
into a draft that waits for approval; name inserts swap while the holder's
responsibilities stay put; signals reach each device, which boots its own app
and lock; a proof is scanned, flagged, corrected and held before posting; one
plot is measured and reviewed before the next is even outlined. Motion never
hands over a response, posts a notice or plants another plot. Still exports and
reduced-motion views show each scene's fully revealed final state. On narrow
screens the in-art labels hide and the cards beneath carry the text.

The paste-ready blog uses static PNG compositions with meaningful alt text and
captions; it requires no scripts. The generated local preview and gallery use
the layered web scenes. Each of the five compositions also has a matching
12-second GIF (960px wide, 10fps, under 10 MB) for hosts that accept animated
images. GIF exports omit camera drift but keep citation trails, review
highlights and chapter indicators, allowing efficient changed-pixel frames. GIFs
cannot honor reduced-motion preferences or offer built-in pause controls;
publish PNGs by default, or offer GIFs as explicitly chosen alternatives.

Regenerate from the repository root. Edit the paste-ready blog for prose,
the builder for scene wording, and the companion CSS/JS for layout and motion.
The source renders are preserved inputs; rebuilding does not invoke an image
model or regenerate the original artwork:

```powershell
python .\tools\build_municipal_foundry_art.py --previews --check
```

Without flags, the command rebuilds the two HTML pages. `--stills` exports PNGs;
`--previews` exports PNGs and GIFs. `--check` checks responsive geometry, local
assets, pause/resume, actual frame differences, reduced motion, no-JavaScript
fallback, and GIF timing when exports exist. Export/check commands require
Pillow and Python Playwright with installed Edge, or Playwright Chromium.

The web scenes honor `prefers-reduced-motion`, offer a still/animation switch,
and pause offscreen. With JavaScript disabled they remain still and readable.
All text is outside the rendered art. Public image URLs target `main`; new
assets will not be available at those URLs until published. Nothing in this
workflow commits, pushes or deploys the files.
