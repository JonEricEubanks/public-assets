# Civic Evidence Lab: visual system and screenshot guide

## Editorial direction

**Theme:** a city read four ways: memory, listening, meaning, and journey.

**Metaphor:** a lamplit public-works survey desk looking out over a living municipality. The file cabinet is the city's memory; a brass radar listens for similar reports; a sealed charter and parchment street atlas supply shared meaning; a compass and magenta traveler navigate modeled connections. A house, public-works truck, bubbling puddle, and water tower make the incident tangible.

The revision follows the **scene-building method** in the Night Shift and sewer CCTV SVGs: an environmental setting, recognizable physical objects, recurring motifs, and animation that expresses the subject. It does not copy their skyline layout, moon motif, camera tunnel, branded marks, or artwork. The municipal scenes and objects are original. The municipal images referenced in the pasted draft were not present locally.

**Design:** a copper-horizon civic evening, lamplit ink-blue desk, steel file cabinets, stone columns, brass instruments, folded complaint sheets, a river-crossed parchment map, and dimensional public-works landmarks. Technical labels annotate the scene rather than filling interchangeable cards. This is atmospheric dimensional vector illustration, not photorealistic photography.

**Recurring symbols:** city hall anchors public accountability; the water tower identifies the municipal service domain; the gold seal denotes provenance and governance; the magenta traveling light denotes execution, never fact creation. A charter expresses designed rules, not automatic enforcement. These are explanatory metaphors, not claims that SQL opens a physical drawer or Fabric dispatches a truck.

**Developer-community emphasis:** show a real query, a real mapping, and a real returned path. The new illustrative candidate-to-validated-edge contract explains the central distinction in an implementable way without pretending to be Fabric API syntax. Credible evidence and clear boundaries matter more than product-logo density. This presentation cannot guarantee Microsoft MVP recognition.

## Symbology

| Responsibility | Symbol | Accent | Meaning |
|---|---|---|---|
| Relational records | File cabinet / archive drawer | Navy `#94bee8` | The city's memory: exact IDs, constraints, transactions |
| Vector retrieval | Brass radar / floating report sheets / wave | Purple `#c6a4ff` | The listening signal: nearby in meaning, not an established fact |
| Knowledge graph | Parchment atlas / labeled connections | Green `#8de4bd` | Shared meaning: typed entities and relationships |
| Governance | Sealed charter / gold shield | Gold `#f1ca85` | Definitions, provenance, ownership, rules |
| Fabric Graph execution | Compass / traveling light / labeled bracket | Magenta `#f4a7d7` | The journey: traversal and pattern matching |
| OneLake sources | Labeled source-data rail | Blue `#88d4ef` | Source-data foundation, not automatic policy enforcement |

Solid = authoritative; dashed = inferred; dotted = proposed/unverified; wavy = semantic similarity. The traveling magenta light is an execution highlight, not an inferred edge. The explicitly labeled magenta perimeter bracket denotes execution extent, not relationship status. Blue flowing water in the street cutaway is physical context, not OneLake. Labels and shapes carry meaning even without color.

## Artwork and placement

All files are under [images](../images). The [illustrated blog](vector-search-knowledge-graphs-fabric.html) already contains all 11 images, captions, alternative text, and five screenshot capture notes.

| File | Position | Visual purpose |
|---|---|---|
| [municipal-information-city-hero.svg](../images/municipal-information-city-hero.svg) | Opening | Four instruments, one incident |
| [municipal-information-city-divider.svg](../images/municipal-information-city-divider.svg) | Introduction | The public record anchors the analysis |
| [municipal-records-office.svg](../images/municipal-records-office.svg) | Relational section | Controlled records and exact identifiers |
| [municipal-similarity-radar.svg](../images/municipal-similarity-radar.svg) | Vector section | Related reports without asserted edges |
| [municipal-knowledge-map.svg](../images/municipal-knowledge-map.svg) | Knowledge section | Typed relationships and a separate legend |
| [fabric-graph-route-engine.svg](../images/fabric-graph-route-engine.svg) | Fabric Graph section | Execution boundary over OneLake sources |
| [knowledge-versus-execution.svg](../images/knowledge-versus-execution.svg) | Terminology distinction | Meaning is not execution |
| [water-main-four-views.svg](../images/water-main-four-views.svg) | Incident walkthrough | Four questions against one demo incident |
| [municipal-data-symbols.svg](../images/municipal-data-symbols.svg) | Visual language | Shape, color, and line-status legend |
| [municipal-information-layers.svg](../images/municipal-information-layers.svg) | Composition section | Responsibilities, not a mandatory stack |
| [municipal-information-city-footer.svg](../images/municipal-information-city-footer.svg) | Closing | Public-record integrity and accountability |

Hero: 1400 x 800. Section diagrams: 1400 x 680. Divider/footer: 1400 x 260.

**All 11 SVGs now animate**, including the divider, footer, records scene, knowledge atlas, symbol legend, and composition scene. The PNGs remain deliberately static fallbacks.

| Scene | Subject-specific motion |
|---|---|
| Hero | Radar sweep, settling compass, drafting highlight, traveling route light, lamplight |
| Divider | Gold anchor light crosses the municipality toward the seal |
| Records | A work-order archive drawer slowly opens and closes |
| Similarity | Radar rotates while folded reports gently float |
| Knowledge | Compass settles; a drafting highlight follows already-modeled links |
| Fabric Graph | A magenta traveler crosses the municipal atlas |
| Meaning vs. execution | Compass needle moves while a route light travels beside the charter |
| Water-main incident | Puddle ripples expand and water flows through the street cutaway |
| Symbol legend | Physical radar and compass animate above stable line-status samples |
| Composition | The recurring civic instruments operate together around one map |
| Footer | The magenta traveler returns to the familiar municipal skyline |

The [blog preview](vector-search-knowledge-graphs-fabric.html) defaults to **Animated SVGs** and includes an explicit **Still PNGs** switch. Its preview script upgrades the artwork to SVG `<object>` documents, with PNG fallback children, so browser playback is visible. Open the HTML in a browser to see motion; an editor thumbnail, PNG, or screenshot cannot demonstrate animation.

**Why the SVGs have no `prefers-reduced-motion` rule:** an earlier build included one, and the tested Chromium browser applied it to SVGs loaded through `<img>` even when the page itself had no reduced-motion preference. Every SVG then rendered still on GitHub and in blog embeds. The rule was removed so the SVGs animate like the existing Night Shift and sewer CCTV artwork. The trade-off is that viewers who request reduced motion will still see movement; the motion is slow and decorative.

Meaning never depends on movement. Every SVG includes a title and description. There is no SVG JavaScript, embedded remote image, or external font dependency.

## Take these five real screenshots

Use **one synthetic incident throughout**, for example asset `WM-481`, complaint `CR-017`, work order `WO-204`, and inspection `IN-032`. These are fictional demo IDs. Create actual records in your authorized demo environment; do not paste fabricated results into product screenshots.

### 01. Exact record — required

- **Where:** your actual SQL editor or Dataverse demo view.
- **Frame:** exact-ID query, asset key, and related open-work-order results in the same crop.
- **Proves:** exact matching and an authoritative identifier.
- **Suggested caption:** “An exact identifier resolves the official asset and its recorded work orders.”
- **Save as:** `screenshots/civic-01-exact-record.png`.
- If the screenshot is a Fabric analytical copy, label it as a copy and identify the transactional source separately.

### 02. Vector retrieval — required

- **Where:** your actual vector-search service, notebook, or application result panel.
- **Frame:** the natural-language query, three or more differently worded retrieved reports, document IDs, and source metadata.
- **Proves:** related meaning despite different wording.
- **Suggested caption:** “Semantically related reports are retrieval candidates, not proof that they describe the same incident.”
- **Save as:** `screenshots/civic-02-vector-retrieval.png`.
- Name the actual retrieval mode (vector-only, hybrid, or another supported mode). Do not label a rank/retrieval score as a confidence probability. Avoid raw embedding arrays: they consume space without explaining the result.

### 03. Governed meaning — required

- **Where:** your actual schema, catalog, graph-modeling tool, or maintained definition document.
- **Frame:** `WaterMain`, `maintainedBy`, source-record reference, business owner, and effective-date fields.
- **Proves:** meaning and provenance have been designed, not inferred from a node's position.
- **Suggested caption:** “The relationship definition carries meaning, source, and ownership independently of the engine that traverses it.”
- **Save as:** `screenshots/civic-03-governed-meaning.png`.
- This is not a request to invent a Microsoft knowledge-graph UI. A real maintained schema is suitable.

### 04. Fabric Graph mapping — required if available

- **Where:** an authorized Fabric Graph demo workspace where the feature is actually available.
- **Frame:** node/edge mapping, source table names, node keys, and relationship direction. Keep enough workspace context to establish the product, but crop irrelevant navigation.
- **Proves:** source records become a deliberate graph model.
- **Suggested caption:** “Demo OneLake source tables are mapped to graph nodes and edges using explicit keys.”
- **Save as:** `screenshots/civic-04-fabric-mapping.png`.
- Verify current feature status, supported source types, permissions, and mapping behavior against current Microsoft documentation. If unavailable, omit the screenshot and call the SVG conceptual; do not fabricate a model screen.

### 05. Fabric Graph traversal result — required if available

- **Where:** the actual query/result experience in the same workspace.
- **Frame:** executed query plus one readable returned complaint-to-inspection path. Include entity labels and either visible source IDs or a companion property-pane crop.
- **Proves:** traversal across several modeled relationships.
- **Suggested caption:** “A multihop query follows modeled connections from the complaint to repair and inspection records.”
- **Save as:** `screenshots/civic-05-traversal-result.png`.
- Use supported syntax from your environment. Do not substitute imagined GQL/Cypher/Gremlin syntax, a mock node diagram, or the illustrative application contract from the blog.

**Optional sixth capture:** your actual relationship-review workflow showing a candidate remaining unverified until source evidence is checked. Include this only if the workflow exists; it would support the candidate-to-validated-edge section particularly well.

## Capture quality and privacy

1. Use demo data from the start. Remove resident names, addresses, emails, phone numbers, confidential contractor details, tenant/subscription IDs, tokens, connection strings, and sensitive URLs.
2. Check query text, browser tabs, navigation, result rows, tooltips, and property panes, not just the center of the screen. Redact irreversibly in an image editor if needed.
3. Capture at 1600-2000 pixels wide. Increase application zoom until queries and result labels remain legible when displayed at approximately 900 pixels wide.
4. Use one consistent UI theme. Crop empty sidebars; retain enough real context to establish the product and execution result.
5. Do not bake long explanations into screenshots. Add numbered callouts sparingly and explain them in the article caption.
6. Add informative alternative text describing the result, not simply “screenshot of Fabric.”
7. Replace each capture note with its real image and caption. Keep the conceptual diagrams as orientation, but do not repeat the hero between every screenshot.

## Preview and publishing

### Tech Community: use the publishing fragment, not the local preview

Use [the Tech Community HTML fragment](vector-search-knowledge-graphs-fabric-techcommunity.html)
in the editor's HTML/source mode. Enter the article title separately. Do not paste
the full local preview document, its script, or its document shell.

The fragment follows the existing sewer CCTV blog's embedding pattern:
`<figure>` containing `<img>` with a public SVG URL, alternative text,
`loading="lazy"`, and `width: 100%; max-width: 960px; height: auto`.
It embeds all 11 original animated SVGs directly, preserving captions without
additional "open SVG" links or display instructions. It removes local preview
controls, draft metadata, and the five capture notes. The fragment starts with
the hero image. Actual inline motion depends on the platform and browser.
If the editor blocks externally hosted images,
upload the PNGs through its image-upload workflow and use the resulting platform
URLs instead.

Relative paths such as `../images/` resolve against the Tech Community page, not
your GitHub repository, so they cannot be used in pasted article HTML.

Regenerate the fragment after editing the preview:

```powershell
python .\tools\build_civic_blog_publish.py
```

- Open [the illustrated blog](vector-search-knowledge-graphs-fabric.html) locally in a browser. All image paths are relative and work from this checkout.
- This is an editorial draft, not an update to the live Tech Community post. No assets have been pushed and no article has been published.
- For a rich-text blog editor, use the content inside `<article>` only. Do not paste the document shell, preview CSS, local publishing notice, artwork-switch controls, or preview script. The SVGs animate independently of the preview script.
- After adding real screenshots, remove every `<aside class="capture">`. Do not publish capture instructions as if screenshots were already supplied.
- Upload or push approved assets first. Replace `../images/` with `https://raw.githubusercontent.com/JonEricEubanks/public-assets/main/images/` only after those files are available there. For screenshots, replace `../screenshots/` with the corresponding hosted prefix after uploading them.
- Verify the target editor accepts SVG and preserves animation; neither support nor sanitization behavior is assumed. The source article uses portable `<img>` markup, while the local preview script uses SVG documents. Test actual motion in the published/draft viewer, not only inside the editor.
- On a site you control, use inline SVG or an allowed SVG-document embed with an accessible name and a static fallback; do not bypass user motion preferences. A platform that allows only image uploads may still render these SVGs statically. If motion is essential there, export a platform-supported animated format (such as GIF or video) from the original SVGs. Animated GIF/video exports are not included in this collection.
- If SVG is unsupported or a static illustration is acceptable, use matching PNG exports from [images](../images). These preserve all labels and the base visual state, but **do not preserve animation**. Upload them through the platform's normal image workflow, switch image extensions to `.png`, and keep the captions and alt text.
- No information requires a moving frame; the static PNG exports show the complete composition.
- Confirm Fabric Graph status and product claims against current official documentation before publishing. This task improves presentation; it is not a product availability audit.

## Regeneration

The original art is reproducible with the standard-library script:

```powershell
python .\tools\build_civic_evidence_art.py
```

Run this from the repository root. It rewrites only the 11 SVG files named above. PNG exports must be refreshed separately if artwork changes.
