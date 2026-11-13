"""Choreographed motion layers drawn in source-image pixels (1774 x 887).

Every element's base style is its fully revealed state, so the motion-free still
and reduced-motion view show the whole story. Keyframes only run under
[data-motion="on"] and start from an idle state.
"""

LOOP = 12.0


def pct(seconds):
    return f"{max(0.0, min(100.0, seconds / LOOP * 100)):.2f}%"


def affine(tl, tr, bl, w, h):
    """SVG matrix mapping a local w x h rectangle onto a screen quad."""
    a = (tr[0] - tl[0]) / w
    b = (tr[1] - tl[1]) / w
    c = (bl[0] - tl[0]) / h
    d = (bl[1] - tl[1]) / h
    return f"matrix({a:.4f} {b:.4f} {c:.4f} {d:.4f} {tl[0]} {tl[1]})"


# Measured from images/municipal-foundry-sources/platform.png
HUB_FACE = ((52, 320), (428, 352), (54, 448), 376, 128)
DEVICES = [
    # name, label, screen (tl, tr, bl, w, h), radius, lock, chip centre, rail segment
    ("phone", "Resident app", ((582, 271), (659, 277), (575, 432), 77, 161), 9,
     (602, 465), (606, 560), ((462, 405), (566, 414))),
    ("tablet", "Field inspections", ((764, 242), (917, 250), (755, 457), 153, 215), 10,
     (814, 487), (830, 585), ((684, 428), (742, 436))),
    ("laptop", "Staff workspace", ((1022, 260), (1268, 276), (1013, 433), 246, 173), 6,
     (1097, 522), (1112, 620), ((930, 470), (984, 477))),
    ("desktop", "Back office", ((1340, 182), (1710, 200), (1338, 400), 370, 218), 8,
     (1502, 558), (1520, 650), ((1268, 494), (1392, 507))),
]
PULSES = [(0.6, 1.4), (2.2, 2.9), (3.8, 4.5), (5.4, 6.3)]
FADE_OUT = (10.8, 11.6)


def phone_ui(w, h):
    return f"""
<rect x="6" y="8" width="{w - 12}" height="12" rx="6" fill="#ffffff" opacity=".9"/>
<g class="pf-bubble pf-b1"><rect x="{w - 52}" y="30" width="44" height="22" rx="10" fill="#4f7fb8"/>
<rect x="{w - 46}" y="37" width="30" height="3" rx="1.5" fill="#fff"/><rect x="{w - 46}" y="43" width="20" height="3" rx="1.5" fill="#fff"/></g>
<g class="pf-bubble pf-b2"><rect x="8" y="60" width="50" height="28" rx="10" fill="#ffffff"/>
<rect x="14" y="67" width="36" height="3" rx="1.5" fill="#7d93a8"/><rect x="14" y="73" width="30" height="3" rx="1.5" fill="#7d93a8"/><rect x="14" y="79" width="22" height="3" rx="1.5" fill="#7d93a8"/></g>
<g class="pf-typing"><rect x="8" y="98" width="30" height="14" rx="7" fill="#ffffff"/>
<circle class="pf-dot pf-d1" cx="16" cy="105" r="2.2" fill="#5f8fb4"/><circle class="pf-dot pf-d2" cx="23" cy="105" r="2.2" fill="#5f8fb4"/><circle class="pf-dot pf-d3" cx="30" cy="105" r="2.2" fill="#5f8fb4"/></g>
<rect x="6" y="{h - 22}" width="{w - 12}" height="14" rx="7" fill="#ffffff" opacity=".85"/>"""


def tablet_ui(w, h):
    return f"""
<clipPath id="pf-photo"><rect x="10" y="12" width="{w - 20}" height="112" rx="6"/></clipPath>
<g clip-path="url(#pf-photo)">
  <rect x="10" y="12" width="{w - 20}" height="112" fill="#dbeaf6"/>
  <path d="M10 80 Q70 62 {w - 10} 74 V124 H10Z" fill="#9cc49a"/>
  <path d="M60 124 Q74 96 92 84 L100 84 Q90 100 96 124Z" fill="#e6e2d6"/>
  <circle cx="40" cy="62" r="16" fill="#7fae86"/><rect x="38" y="70" width="4" height="16" fill="#8a7b67"/>
  <circle cx="{w - 34}" cy="58" r="20" fill="#86b48c"/><rect x="{w - 36}" y="70" width="4" height="18" fill="#8a7b67"/>
  <rect class="pf-scan" x="10" y="12" width="{w - 20}" height="6" fill="#ffffff" opacity=".8"/>
</g>
<path d="M18 22 v-6 h8 M{w - 26} 16 h8 v6 M18 112 v6 h8 M{w - 26} 118 h8 v-6" stroke="#ffffff" stroke-width="2.4" fill="none" stroke-linecap="round"/>
<rect class="pf-flash" x="10" y="12" width="{w - 20}" height="112" rx="6" fill="#ffffff"/>
<g class="pf-row pf-r1"><rect x="10" y="136" width="{w - 20}" height="22" rx="6" fill="#ffffff"/><rect x="18" y="144" width="60" height="5" rx="2.5" fill="#7d93a8"/><rect x="{w - 46}" y="141" width="28" height="12" rx="6" fill="#9ec7c0"/></g>
<g class="pf-row pf-r2"><rect x="10" y="164" width="{w - 20}" height="22" rx="6" fill="#ffffff"/><rect x="18" y="172" width="80" height="5" rx="2.5" fill="#7d93a8"/><rect x="{w - 46}" y="169" width="28" height="12" rx="6" fill="#c9d8ea"/></g>
<rect x="10" y="{h - 22}" width="{w - 20}" height="12" rx="6" fill="#4f7fb8" opacity=".85"/>"""


def laptop_ui(w, h):
    lines = "".join(
        f'<rect x="16" y="{30 + 13 * i}" width="{[120, 132, 104, 128, 90, 118, 110, 70][i]}" height="5" rx="2.5" fill="#8ea3b6"/>'
        for i in range(8)
    )
    return f"""
<rect x="6" y="6" width="{w - 12}" height="12" rx="4" fill="#ffffff" opacity=".9"/>
<rect x="8" y="22" width="150" height="{h - 30}" rx="6" fill="#ffffff"/>
{lines}
<rect class="pf-highlight" x="12" y="54" width="140" height="11" rx="3" fill="#bfe0d8" opacity=".75"/>
<rect x="166" y="22" width="{w - 174}" height="{h - 30}" rx="6" fill="#f3f8fd"/>
<g class="pf-src pf-s1"><rect x="172" y="32" width="{w - 186}" height="30" rx="5" fill="#ffffff"/><rect x="178" y="40" width="10" height="14" rx="2" fill="#4f7fb8"/><rect x="194" y="41" width="40" height="4" rx="2" fill="#7d93a8"/><rect x="194" y="49" width="28" height="4" rx="2" fill="#b3c2d1"/></g>
<g class="pf-src pf-s2"><rect x="172" y="68" width="{w - 186}" height="30" rx="5" fill="#ffffff"/><rect x="178" y="76" width="10" height="14" rx="2" fill="#5f9e95"/><rect x="194" y="77" width="44" height="4" rx="2" fill="#7d93a8"/><rect x="194" y="85" width="24" height="4" rx="2" fill="#b3c2d1"/></g>
<g class="pf-src pf-s3"><rect x="172" y="104" width="{w - 186}" height="30" rx="5" fill="#ffffff"/><rect x="178" y="112" width="10" height="14" rx="2" fill="#8b86c4"/><rect x="194" y="113" width="36" height="4" rx="2" fill="#7d93a8"/><rect x="194" y="121" width="30" height="4" rx="2" fill="#b3c2d1"/></g>"""


def desktop_ui(w, h):
    bars = "".join(
        f'<rect class="pf-bar pf-bar{i}" x="{24 + 26 * i}" y="{150 - v}" width="16" height="{v}" rx="3" fill="{"#4f7fb8" if i % 2 == 0 else "#7fb0d8"}"/>'
        for i, v in enumerate((52, 74, 60, 92, 70, 104, 84))
    )
    return f"""
<rect x="8" y="8" width="{w - 16}" height="14" rx="5" fill="#ffffff" opacity=".9"/>
<rect x="10" y="30" width="200" height="140" rx="8" fill="#ffffff"/>
<rect x="24" y="40" width="70" height="5" rx="2.5" fill="#7d93a8"/>
<g class="pf-bars">{bars}</g>
<line x1="20" y1="151" x2="200" y2="151" stroke="#c9d6e3" stroke-width="2"/>
<g class="pf-kpi pf-k1"><rect x="220" y="30" width="{w - 230}" height="40" rx="8" fill="#ffffff"/><rect x="232" y="40" width="40" height="5" rx="2.5" fill="#9fb0c2"/><rect x="232" y="51" width="70" height="10" rx="4" fill="#4f7fb8"/></g>
<g class="pf-kpi pf-k2"><rect x="220" y="78" width="{w - 230}" height="40" rx="8" fill="#ffffff"/><rect x="232" y="88" width="50" height="5" rx="2.5" fill="#9fb0c2"/><rect x="232" y="99" width="56" height="10" rx="4" fill="#5f9e95"/></g>
<g class="pf-kpi pf-k3"><rect x="220" y="126" width="{w - 230}" height="44" rx="8" fill="#ffffff"/>
<polyline class="pf-spark" points="232,160 250,152 266,156 284,142 300,146 318,134 336,138 350,130" fill="none" stroke="#4f7fb8" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" pathLength="1"/></g>
<rect x="10" y="{h - 40}" width="{w - 20}" height="30" rx="8" fill="#ffffff" opacity=".9"/>
<rect x="22" y="{h - 29}" width="120" height="6" rx="3" fill="#9fb0c2"/>
<rect x="{w - 100}" y="{h - 31}" width="80" height="10" rx="5" fill="#c9d8ea"/>"""


UI = {"phone": phone_ui, "tablet": tablet_ui, "laptop": laptop_ui, "desktop": desktop_ui}


def platform_fx():
    css = [
        '[data-motion="on"] #casebook-platform .pf-sweep{animation:pf-sweep 12s ease-in-out infinite}',
        '@keyframes pf-sweep{0%,30%{transform:translateX(-900px);opacity:0}38%{opacity:.55}70%,100%{transform:translateX(2100px);opacity:0}}',
        '#casebook-platform .pf-sweep{opacity:0}',
        '[data-motion="on"] #casebook-platform .pf-hubglow{animation:pf-hub 12s ease-in-out infinite}',
        f'@keyframes pf-hub{{0%{{opacity:.25}}{pct(0.5)}{{opacity:1}}{pct(1.2)}{{opacity:.55}}{pct(2.1)}{{opacity:.95}}{pct(2.8)}{{opacity:.55}}'
        f'{pct(3.7)}{{opacity:.95}}{pct(4.4)}{{opacity:.55}}{pct(5.3)}{{opacity:1}}{pct(6.2)}{{opacity:.6}}{pct(10.8)}{{opacity:.7}}100%{{opacity:.25}}}}',
        '[data-motion="on"] #casebook-platform .pf-hublabel{animation:pf-label 12s ease-in-out infinite}',
        f'@keyframes pf-label{{0%{{opacity:.35}}{pct(0.6)},{pct(FADE_OUT[0])}{{opacity:1}}100%{{opacity:.35}}}}',
        # micro-interactions inside the screens; 3 s and 6 s loops divide the 12 s export loop
        '[data-motion="on"] #casebook-platform .pf-dot{animation:pf-dot 1.5s ease-in-out infinite}',
        '#casebook-platform .pf-d2{animation-delay:-1.3s!important}#casebook-platform .pf-d3{animation-delay:-1.1s!important}',
        '@keyframes pf-dot{0%,60%,100%{opacity:.35;transform:translateY(0)}30%{opacity:1;transform:translateY(-2px)}}',
        '[data-motion="on"] #casebook-platform .pf-scan{animation:pf-scan 3s linear infinite}',
        '@keyframes pf-scan{0%{transform:translateY(0);opacity:0}10%{opacity:.8}90%{opacity:.8}100%{transform:translateY(106px);opacity:0}}',
        '#casebook-platform .pf-flash{opacity:0}',
        '[data-motion="on"] #casebook-platform .pf-flash{animation:pf-flash 6s ease-out infinite}',
        '@keyframes pf-flash{0%,48%{opacity:0}50%{opacity:.9}58%,100%{opacity:0}}',
        '[data-motion="on"] #casebook-platform .pf-highlight{animation:pf-hl 6s ease-in-out infinite}',
        '@keyframes pf-hl{0%,100%{transform:translateY(-26px)}50%{transform:translateY(39px)}}',
        '[data-motion="on"] #casebook-platform .pf-spark{stroke-dasharray:1;animation:pf-spark 6s ease-in-out infinite}',
        '@keyframes pf-spark{0%{stroke-dashoffset:1}50%,100%{stroke-dashoffset:0}}',
        '#casebook-platform .pf-bar{transform-box:fill-box;transform-origin:bottom}',
        '[data-motion="on"] #casebook-platform .pf-bar{animation:pf-bar 6s ease-in-out infinite}',
        '@keyframes pf-bar{0%,100%{transform:scaleY(.55)}50%{transform:scaleY(1)}}',
    ]
    for i in range(7):
        css.append(f'#casebook-platform .pf-bar{i}{{animation-delay:-{i * 0.35:.2f}s!important}}')

    body = [
        '<defs>'
        '<radialGradient id="pf-glow"><stop offset="0" stop-color="#ffffff" stop-opacity=".95"/>'
        '<stop offset=".45" stop-color="#cfe4ff" stop-opacity=".55"/><stop offset="1" stop-color="#a9cdf7" stop-opacity="0"/></radialGradient>'
        '<radialGradient id="pf-pulse"><stop offset="0" stop-color="#ffffff"/><stop offset=".35" stop-color="#bfe0ff" stop-opacity=".95"/>'
        '<stop offset="1" stop-color="#7fb7f0" stop-opacity="0"/></radialGradient>'
        '<linearGradient id="pf-sweep-g" x1="0" x2="1"><stop offset="0" stop-color="#fff" stop-opacity="0"/>'
        '<stop offset=".5" stop-color="#fff" stop-opacity=".9"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>'
        '<linearGradient id="pf-screen" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#eef6ff"/><stop offset="1" stop-color="#d3e6fb"/></linearGradient>'
        '<linearGradient id="pf-glass" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".45"/>'
        '<stop offset=".4" stop-color="#fff" stop-opacity="0"/></linearGradient>'
        '<filter id="pf-soft" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="6"/></filter>'
        '</defs>',
        '<ellipse class="pf-hubglow" cx="245" cy="398" rx="200" ry="92" fill="url(#pf-glow)"/>',
        f'<g transform="{affine(*HUB_FACE)}"><g class="pf-hublabel">'
        '<text x="32" y="58" font-family="Segoe UI, system-ui, sans-serif" font-size="31" font-weight="600" fill="#1f4b78" fill-opacity=".82">Microsoft Foundry</text>'
        '<text x="33" y="90" font-family="Segoe UI, system-ui, sans-serif" font-size="15.5" letter-spacing="1" fill="#2b5785" fill-opacity=".72">MODELS · AGENTS · FOUNDRY IQ · TOOLS</text>'
        '</g></g>',
    ]

    for idx, (name, label, (tl, tr, bl, w, h), radius, lock, chip, seg) in enumerate(DEVICES):
        p0, p1 = PULSES[idx]
        on = p1
        dx, dy = seg[1][0] - seg[0][0], seg[1][1] - seg[0][1]
        css += [
            f'#casebook-platform .pf-pulse-{name}{{opacity:0}}',
            f'[data-motion="on"] #casebook-platform .pf-pulse-{name}{{animation:pf-pulse-{name} 12s linear infinite}}',
            f'@keyframes pf-pulse-{name}{{0%,{pct(p0 - 0.01)}{{transform:translate(0,0);opacity:0}}{pct(p0)}{{transform:translate(0,0);opacity:1}}'
            f'{pct(p1)}{{transform:translate({dx}px,{dy}px);opacity:1}}{pct(p1 + 0.15)},100%{{transform:translate({dx}px,{dy}px);opacity:0}}}}',
            f'[data-motion="on"] #casebook-platform .pf-trail-{name}{{stroke-dasharray:1;animation:pf-trail-{name} 12s ease-out infinite}}',
            f'@keyframes pf-trail-{name}{{0%,{pct(p0)}{{stroke-dashoffset:1;opacity:0}}{pct(p0 + 0.05)}{{opacity:.9}}{pct(p1)}{{stroke-dashoffset:0;opacity:.9}}'
            f'{pct(FADE_OUT[0])}{{stroke-dashoffset:0;opacity:.45}}{pct(FADE_OUT[1])},100%{{stroke-dashoffset:0;opacity:0}}}}',
            f'[data-motion="on"] #casebook-platform .pf-on-{name}{{animation:pf-on-{name} 12s ease-out infinite}}',
            f'@keyframes pf-on-{name}{{0%,{pct(on)}{{opacity:0}}{pct(on + 0.35)},{pct(FADE_OUT[0])}{{opacity:1}}{pct(FADE_OUT[1])},100%{{opacity:0}}}}',
            f'#casebook-platform .pf-boot-{name}{{opacity:0}}',
            f'[data-motion="on"] #casebook-platform .pf-boot-{name}{{animation:pf-boot-{name} 12s ease-out infinite}}',
            f'@keyframes pf-boot-{name}{{0%,{pct(on - 0.01)}{{opacity:0}}{pct(on)}{{opacity:.95}}{pct(on + 0.6)},100%{{opacity:0}}}}',
            f'#casebook-platform .pf-ring-{name}{{opacity:0;transform-box:fill-box;transform-origin:center}}',
            f'[data-motion="on"] #casebook-platform .pf-ring-{name}{{animation:pf-ring-{name} 12s ease-out infinite}}',
            f'@keyframes pf-ring-{name}{{0%,{pct(on + 0.15)}{{opacity:0;transform:scale(.5)}}{pct(on + 0.25)}{{opacity:1;transform:scale(.7)}}'
            f'{pct(on + 1.1)}{{opacity:0;transform:scale(1.9)}}{pct(7.6 + 0.35 * idx)}{{opacity:0;transform:scale(.5)}}{pct(7.7 + 0.35 * idx)}{{opacity:1;transform:scale(.7)}}'
            f'{pct(8.6 + 0.35 * idx)},100%{{opacity:0;transform:scale(1.9)}}}}',
            f'[data-motion="on"] #casebook-platform .pf-lockglow-{name}{{animation:pf-lock-{name} 12s ease-out infinite}}',
            f'@keyframes pf-lock-{name}{{0%,{pct(on)}{{opacity:0}}{pct(on + 0.3)}{{opacity:.9}}{pct(on + 1.2)}{{opacity:.35}}'
            f'{pct(7.7 + 0.35 * idx)}{{opacity:.35}}{pct(7.9 + 0.35 * idx)}{{opacity:.95}}{pct(8.8 + 0.35 * idx)}{{opacity:.35}}{pct(FADE_OUT[1])},100%{{opacity:0}}}}',
            f'#casebook-platform .pf-chip-{name}{{transform-box:fill-box;transform-origin:center}}',
            f'[data-motion="on"] #casebook-platform .pf-chip-{name}{{animation:pf-chip-{name} 12s cubic-bezier(.2,.8,.2,1) infinite}}',
            f'@keyframes pf-chip-{name}{{0%,{pct(on + 0.2)}{{opacity:0;transform:translateY(14px)}}{pct(on + 0.7)},{pct(FADE_OUT[0])}{{opacity:1;transform:translateY(0)}}'
            f'{pct(FADE_OUT[1])},100%{{opacity:0;transform:translateY(8px)}}}}',
        ]
        # inner elements stagger after their device turns on
        for cls in {"phone": ("pf-b1", "pf-b2", "pf-typing"), "tablet": ("pf-r1", "pf-r2"),
                    "laptop": ("pf-s1", "pf-s2", "pf-s3"), "desktop": ("pf-k1", "pf-k2", "pf-k3")}[name]:
            k = f"pf-in-{cls}"
            delay = {"pf-b1": 0.4, "pf-b2": 1.4, "pf-typing": 2.2, "pf-r1": 0.9, "pf-r2": 1.5,
                     "pf-s1": 0.6, "pf-s2": 1.1, "pf-s3": 1.6, "pf-k1": 0.5, "pf-k2": 0.9, "pf-k3": 1.3}[cls]
            css += [
                f'#casebook-platform .{cls}{{transform-box:fill-box;transform-origin:center}}',
                f'[data-motion="on"] #casebook-platform .{cls}{{animation:{k} 12s cubic-bezier(.2,.8,.2,1) infinite}}',
                f'@keyframes {k}{{0%,{pct(on + delay)}{{opacity:0;transform:translateY(6px) scale(.96)}}'
                f'{pct(on + delay + 0.4)},{pct(FADE_OUT[0])}{{opacity:1;transform:none}}{pct(FADE_OUT[1])},100%{{opacity:0}}}}',
            ]

        x0, y0 = seg[0]
        x1, y1 = seg[1]
        chip_w = 34 + 11.5 * len(label)
        body += [
            f'<line class="pf-trail-{name}" x1="{x0}" y1="{y0}" x2="{x1}" y2="{y1}" pathLength="1" stroke="#9fd0ff" stroke-width="7" stroke-linecap="round" opacity=".55" filter="url(#pf-soft)"/>',
            f'<g class="pf-pulse-{name}"><circle cx="{x0}" cy="{y0}" r="26" fill="url(#pf-pulse)"/><circle cx="{x0}" cy="{y0}" r="5" fill="#fff"/></g>',
            f'<g transform="{affine(tl, tr, bl, w, h)}">'
            f'<rect width="{w}" height="{h}" rx="{radius}" fill="url(#pf-screen)"/>'
            f'<g class="pf-on-{name}">{UI[name](w, h)}</g>'
            f'<rect width="{w}" height="{h}" rx="{radius}" fill="url(#pf-glass)"/>'
            f'<rect class="pf-boot-{name}" width="{w}" height="{h}" rx="{radius}" fill="#ffffff"/>'
            '</g>',
            f'<circle class="pf-lockglow-{name}" cx="{lock[0]}" cy="{lock[1]}" r="16" fill="#9fd0ff" opacity=".35" filter="url(#pf-soft)"/>',
            f'<circle class="pf-ring-{name}" cx="{lock[0]}" cy="{lock[1]}" r="20" fill="none" stroke="#5f97cf" stroke-width="2.5"/>',
            f'<g class="pf-chip-{name} fx-label">'
            f'<line x1="{lock[0]}" y1="{lock[1] + 26}" x2="{chip[0]}" y2="{chip[1] - 22}" stroke="#9db6cd" stroke-width="1.5" stroke-dasharray="3 4"/>'
            f'<rect x="{chip[0] - chip_w / 2:.0f}" y="{chip[1] - 21}" width="{chip_w}" height="42" rx="21" fill="#ffffff" fill-opacity=".92" stroke="#c4d6e6"/>'
            f'<circle cx="{chip[0] - chip_w / 2 + 22:.0f}" cy="{chip[1]}" r="5" fill="#4f7fb8"/>'
            f'<text x="{chip[0] - chip_w / 2 + 36:.0f}" y="{chip[1] + 7}" font-family="Segoe UI, system-ui, sans-serif" font-size="20" font-weight="600" fill="#24435c">{label}</text>'
            '</g>',
        ]

    body.append('<g transform="skewX(-18)"><rect class="pf-sweep" x="0" y="0" width="360" height="887" fill="url(#pf-sweep-g)"/></g>')
    return "<style>" + "".join(css) + "</style>" + "".join(body)



# ---------------------------------------------------------------------------
# Shared builder for the other four scenes.

FONT = 'font-family="Segoe UI, system-ui, sans-serif"'
INK, MUTED, BLUE, SAGE, LILAC = "#24435c", "#5b7489", "#4f7fb8", "#5f9e95", "#8b86c4"


def _qbez(p0, p1, p2, n=8):
    return [
        ((1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0],
         (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1])
        for t in (i / n for i in range(n + 1))
    ]


class FX:
    def __init__(self, sid):
        self.sid, self.css, self.body = sid, [], []
        self.css.append(f'#casebook-{sid} .fx-hide{{opacity:0}}')

    def sel(self, cls):
        return f'#casebook-{self.sid} .{cls}'

    def kf(self, cls, frames, ease="ease-in-out", hidden=False, origin=None):
        sel, name = self.sel(cls), f'{self.sid}-{cls}'
        if hidden:
            self.css.append(f'{sel}{{opacity:0}}')
        if origin:
            self.css.append(f'{sel}{{transform-box:fill-box;transform-origin:{origin}}}')
        self.css.append(f'[data-motion="on"] {sel}{{animation:{name} 12s {ease} infinite}}')
        self.css.append(f'@keyframes {name}{{' + "".join(f'{pct(t)}{{{p}}}' for t, p in frames) + '}')

    def appear(self, cls, t, dy=10, until=FADE_OUT[0], dur=0.45, scale=False):
        start = f'opacity:0;transform:translateY({dy}px)' + (' scale(.9)' if scale else '')
        self.kf(cls, [(0, start), (t, start), (t + dur, 'opacity:1;transform:none'),
                      (until, 'opacity:1;transform:none'), (until + 0.6, 'opacity:0;transform:none'),
                      (12, 'opacity:0;transform:none')],
                ease="cubic-bezier(.2,.8,.2,1)", origin="center" if scale else None)

    def window(self, cls, t0, t1, fade=0.35, hidden=True, peak=1):
        self.kf(cls, [(0, 'opacity:0'), (t0, 'opacity:0'), (t0 + fade, f'opacity:{peak}'),
                      (t1, f'opacity:{peak}'), (t1 + fade, 'opacity:0'), (12, 'opacity:0')], hidden=hidden)

    def ping(self, cls, t, dur=1.0, start=.5, end=2.1):
        self.kf(cls, [(0, f'opacity:0;transform:scale({start})'), (t, f'opacity:0;transform:scale({start})'),
                      (t + 0.08, f'opacity:1;transform:scale({start + .1})'),
                      (t + dur, f'opacity:0;transform:scale({end})'), (12, f'opacity:0;transform:scale({end})')],
                ease="ease-out", hidden=True, origin="center")

    def draw(self, cls, t0, t1, rest=.55):
        self.css.append(f'{self.sel(cls)}{{stroke-dasharray:1;opacity:{rest}}}')
        self.kf(cls, [(0, 'stroke-dashoffset:1;opacity:0'), (t0, 'stroke-dashoffset:1;opacity:0'),
                      (t0 + .05, 'opacity:.95'), (t1, 'stroke-dashoffset:0;opacity:.95'),
                      (FADE_OUT[0], f'stroke-dashoffset:0;opacity:{rest}'),
                      (FADE_OUT[1], 'stroke-dashoffset:0;opacity:0'), (12, 'stroke-dashoffset:0;opacity:0')],
                ease="ease-out")

    def travel(self, cls, t0, t1, pts, r=24):
        x0, y0 = pts[0]
        self.body.append(
            f'<g class="{cls}"><circle cx="{x0:.0f}" cy="{y0:.0f}" r="{r}" fill="url(#{self.sid}-pulse)"/>'
            f'<circle cx="{x0:.0f}" cy="{y0:.0f}" r="5" fill="#fff"/></g>')
        frames = [(0, 'opacity:0;transform:translate(0,0)'), (t0 - .01, 'opacity:0;transform:translate(0,0)')]
        for i, (x, y) in enumerate(pts):
            frames.append((t0 + (t1 - t0) * i / (len(pts) - 1),
                           f'opacity:1;transform:translate({x - x0:.1f}px,{y - y0:.1f}px)'))
        x, y = pts[-1]
        frames += [(t1 + .2, f'opacity:0;transform:translate({x - x0:.1f}px,{y - y0:.1f}px)'),
                   (12, f'opacity:0;transform:translate({x - x0:.1f}px,{y - y0:.1f}px)')]
        self.kf(cls, frames, ease="linear", hidden=True)

    def chip(self, cls, x, y, label, num=None, size=21, sub=None, leader=None):
        w = 40 + 0.58 * size * max(len(label), 0.82 * len(sub or "")) + (34 if num else 0)
        h = 44 if not sub else 70
        x0 = x - w / 2
        parts = []
        if leader:
            parts.append(f'<path d="M{leader[0]} {leader[1]} L{x:.0f} {y - h / 2 if leader[1] < y else y + h / 2:.0f}" '
                         'stroke="#9db6cd" stroke-width="1.6" stroke-dasharray="3 5" fill="none"/>')
        parts.append(f'<rect x="{x0:.0f}" y="{y - h / 2:.0f}" width="{w:.0f}" height="{h}" rx="{min(22, h / 2):.0f}" '
                     'fill="#ffffff" fill-opacity=".94" stroke="#c4d6e6"/>')
        tx = x0 + 20
        if num:
            parts.append(f'<circle cx="{tx + 12:.0f}" cy="{y - (13 if sub else 0):.0f}" r="13" fill="{BLUE}"/>'
                         f'<text x="{tx + 12:.0f}" y="{y - (13 if sub else 0) + 6:.0f}" text-anchor="middle" {FONT} '
                         f'font-size="16" font-weight="700" fill="#fff">{num}</text>')
            tx += 34
        else:
            parts.append(f'<circle cx="{tx + 3:.0f}" cy="{y - (13 if sub else 0):.0f}" r="5" fill="{BLUE}"/>')
            tx += 16
        parts.append(f'<text x="{tx:.0f}" y="{y + 7 - (13 if sub else 0):.0f}" {FONT} font-size="{size}" '
                     f'font-weight="600" fill="{INK}">{label}</text>')
        if sub:
            parts.append(f'<text x="{tx:.0f}" y="{y + 22:.0f}" {FONT} font-size="17" fill="{MUTED}">{sub}</text>')
        self.body.append(f'<g class="{cls} fx-label">' + "".join(parts) + '</g>')

    def sweep(self):
        self.body.append(f'<g transform="skewX(-18)"><rect class="fx-sweep" x="0" y="0" width="340" height="887" '
                         f'fill="url(#{self.sid}-sweep)"/></g>')
        self.kf("fx-sweep", [(0, 'transform:translateX(-700px);opacity:0'), (FADE_OUT[0] - 3.2, 'transform:translateX(-700px);opacity:0'),
                             (FADE_OUT[0] - 2.4, 'opacity:.5'), (FADE_OUT[0], 'transform:translateX(2200px);opacity:0'),
                             (12, 'transform:translateX(2200px);opacity:0')], hidden=True)

    def render(self):
        s = self.sid
        defs = (f'<defs><radialGradient id="{s}-pulse"><stop offset="0" stop-color="#fff"/>'
                f'<stop offset=".35" stop-color="#bfe0ff" stop-opacity=".95"/><stop offset="1" stop-color="#7fb7f0" stop-opacity="0"/></radialGradient>'
                f'<radialGradient id="{s}-glow"><stop offset="0" stop-color="#d9ecff" stop-opacity=".95"/>'
                f'<stop offset="1" stop-color="#bcd7f5" stop-opacity="0"/></radialGradient>'
                f'<radialGradient id="{s}-sage"><stop offset="0" stop-color="#d6ece6" stop-opacity=".95"/>'
                f'<stop offset="1" stop-color="#b6d8cf" stop-opacity="0"/></radialGradient>'
                f'<linearGradient id="{s}-sweep" x1="0" x2="1"><stop offset="0" stop-color="#fff" stop-opacity="0"/>'
                f'<stop offset=".5" stop-color="#fff" stop-opacity=".85"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>'
                f'<filter id="{s}-soft" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="6"/></filter>'
                + getattr(self, "extra_defs", "") + '</defs>')
        return "<style>" + "".join(self.css) + "</style>" + defs + "".join(self.body)


def ring(fx, cls, x, y, r, color=BLUE, width=3, t=0.0, dur=1.0, start=.5, end=2.1):
    fx.body.append(f'<circle class="{cls}" cx="{x}" cy="{y}" r="{r}" fill="none" stroke="{color}" stroke-width="{width}"/>')
    fx.ping(cls, t, dur, start, end)


# ---------------------------------------------------------------------------
# Opening: a request arrives, staff gather support, the response waits.

def hero_fx():
    fx = FX("hero")
    response = ((764, 436), (905, 377), (999, 560), 153, 266)
    # 1. the bell rings
    for i, t in enumerate((0.25, 0.55, 0.85)):
        fx.body.append(f'<ellipse class="hr-ring{i}" cx="418" cy="352" rx="40" ry="20" fill="none" stroke="{BLUE}" stroke-width="3"/>')
        fx.ping(f"hr-ring{i}", t, 1.1, .6, 2.4)
    fx.body.append(f'<ellipse class="hr-reqglow" cx="309" cy="437" rx="110" ry="52" fill="url(#hero-glow)"/>')
    fx.window("hr-reqglow", 0.2, 1.6, hidden=False, peak=.9)
    fx.css.append(f'{fx.sel("hr-reqglow")}{{opacity:.35}}')
    fx.chip("hr-c-req", 300, 535, "Resident request", num=1, leader=(309, 470))
    fx.appear("hr-c-req", 0.5)
    # 2. the request reaches the staff side
    path = _qbez((309, 437), (600, 330), (900, 440))
    fx.body.append(f'<path class="hr-tr-req" d="M309 437 Q600 330 900 440" pathLength="1" fill="none" stroke="#9fd0ff" '
                   f'stroke-width="6" stroke-linecap="round" filter="url(#hero-soft)"/>')
    fx.draw("hr-tr-req", 1.1, 2.0, rest=.35)
    fx.travel("hr-p-req", 1.1, 2.0, path)
    # 3. staff gather three sources
    sources = [
        ("guide", "Guidance", (1115, 318), (240, 130), (1080, 200), 2.3, (1000, 425)),
        ("photo", "Site photo", (1357, 212), (210, 100), (1357, 105), 3.3, (1020, 425)),
        ("notes", "Notes", (1552, 148), (120, 64), (1600, 70), 4.3, (1040, 432)),
    ]
    for key, label, (cx, cy), (rw, rh), (chx, chy), t, dest in sources:
        fx.body.append(f'<ellipse class="hr-g-{key}" cx="{cx}" cy="{cy}" rx="{rw / 2 + 40:.0f}" ry="{rh / 2 + 30:.0f}" fill="url(#hero-glow)"/>')
        fx.window(f"hr-g-{key}", t - .1, t + 1.0, hidden=True, peak=.95)
        fx.body.append(f'<rect class="hr-f-{key}" x="{cx - rw / 2 - 14:.0f}" y="{cy - rh / 2 - 12:.0f}" width="{rw + 28}" '
                       f'height="{rh + 24}" rx="14" fill="none" stroke="{BLUE}" stroke-width="3" stroke-dasharray="10 8"/>')
        fx.window(f"hr-f-{key}", t, t + 1.1, hidden=True, peak=.9)
        fx.chip(f"hr-c-{key}", chx, chy, label, leader=(cx, cy - rh / 2 - 12))
        fx.appear(f"hr-c-{key}", t + .1)
        mid = ((cx + dest[0]) / 2, min(cy, dest[1]) - 60)
        d = f"M{cx} {cy} Q{mid[0]:.0f} {mid[1]:.0f} {dest[0]} {dest[1]}"
        fx.body.append(f'<path class="hr-tr-{key}" d="{d}" pathLength="1" fill="none" stroke="#a9d3c9" stroke-width="5" '
                       f'stroke-linecap="round" filter="url(#hero-soft)"/>')
        fx.draw(f"hr-tr-{key}", t + .5, t + 1.3, rest=.3)
        fx.travel(f"hr-p-{key}", t + .5, t + 1.3, _qbez((cx, cy), mid, dest))
    # 4. the draft response writes itself, with citations
    lines = []
    for i, (y, w) in enumerate(((70, 112), (88, 124), (106, 98), (130, 118), (148, 104), (172, 120), (190, 86))):
        lines.append(f'<rect class="hr-ln{i}" x="16" y="{y}" width="{w}" height="5" rx="2.5" fill="#7d93a8"/>')
        fx.appear(f"hr-ln{i}", 5.0 + i * .28, dy=0, dur=.3)
    cites = []
    for i, (y, x, col) in enumerate(((106, 122, BLUE), (148, 128, SAGE), (190, 110, LILAC))):
        cites.append(f'<g class="hr-ct{i}"><circle cx="{x}" cy="{y + 2}" r="7" fill="{col}"/>'
                     f'<text x="{x}" y="{y + 6}" text-anchor="middle" {FONT} font-size="10" font-weight="700" fill="#fff">{i + 1}</text></g>')
        fx.appear(f"hr-ct{i}", 5.6 + i * .55, dy=0, scale=True, dur=.3)
    fx.body.append(f'<g transform="{affine(*response)}">' + "".join(lines) + "".join(cites) + '</g>')
    fx.chip("hr-c-draft", 1250, 545, "Draft response", num=2, sub="cited, not yet sent", leader=(1117, 490))
    fx.appear("hr-c-draft", 5.4)
    # 5. staff review; nothing crosses the ledge on its own
    fx.body.append('<path class="hr-review" d="M764 436 L905 377 L1117 490 L999 560Z" fill="none" stroke="#5f9e95" '
                   'stroke-width="4" stroke-linejoin="round"/>')
    fx.kf("hr-review", [(0, 'opacity:0'), (7.6, 'opacity:0'), (7.9, 'opacity:1'), (8.4, 'opacity:.45'),
                        (8.9, 'opacity:1'), (9.4, 'opacity:.45'), (9.9, 'opacity:1'), (FADE_OUT[0], 'opacity:1'),
                        (FADE_OUT[1], 'opacity:0'), (12, 'opacity:0')])
    fx.chip("hr-c-review", 1250, 655, "Awaiting staff approval", num=3, leader=(1250, 580))
    fx.appear("hr-c-review", 7.8)
    fx.body.append('<rect class="hr-hand" x="610" y="610" width="200" height="86" rx="18" fill="#ffffff" fill-opacity=".25" '
                   'stroke="#ffffff" stroke-width="3" stroke-dasharray="10 9" transform="rotate(-27 710 653)"/>')
    fx.kf("hr-hand", [(0, 'opacity:0'), (8.2, 'opacity:0'), (8.6, 'opacity:1'), (9.2, 'opacity:.5'), (9.8, 'opacity:1'),
                      (FADE_OUT[0], 'opacity:1'), (FADE_OUT[1], 'opacity:0'), (12, 'opacity:0')])
    fx.chip("hr-c-hand", 560, 800, "Handed over only after approval", leader=(690, 700))
    fx.appear("hr-c-hand", 8.5)
    fx.sweep()
    return fx.render()


# ---------------------------------------------------------------------------
# The rename: inserts change, the holder (responsibility) never moves.

def rename_fx():
    fx = FX("rename")
    insert = ((948, 158), (1552, 272), (948, 345), 604, 187)
    fx.extra_defs = '<clipPath id="rename-slot"><rect width="604" height="187" rx="12"/></clipPath>'
    names = [("rn-n1", "Azure AI Studio", "EARLIER NAME"),
             ("rn-n2", "Azure AI Foundry", "IGNITE ? NOVEMBER 2024"),
             ("rn-n3", "Microsoft Foundry", "IGNITE 2025 ? CURRENT NAME")]
    groups = "".join(
        f'<g class="{cls}"><text x="302" y="98" text-anchor="middle" {FONT} font-size="52" font-weight="600" '
        f'fill="#1f4b78" fill-opacity=".86">{n}</text><text x="302" y="140" text-anchor="middle" {FONT} font-size="19" '
        f'letter-spacing="3" fill="#2b5785" fill-opacity=".72">{sub}</text></g>' for cls, n, sub in names)
    fx.body.append(f'<g transform="{affine(*insert)}"><g clip-path="url(#rename-slot)">{groups}</g></g>')
    up, none = 'transform:translateY(-200px);opacity:0', 'transform:none;opacity:1'
    fx.css.append(f'{fx.sel("rn-n1")},{fx.sel("rn-n2")}{{opacity:0}}')
    fx.kf("rn-n1", [(0, none), (3.0, none), (3.5, up), (11.3, up), (11.9, none), (12, none)])
    fx.kf("rn-n2", [(0, up), (3.6, up), (4.1, none), (6.9, none), (7.4, up), (12, up)])
    fx.kf("rn-n3", [(0, up), (7.5, up), (8.0, none), (11.2, none), (11.7, 'transform:none;opacity:0'), (12, 'transform:none;opacity:0')])
    # the removed name travels to its insert on the desk
    for i, (t, dest, chip, label, sub) in enumerate((
            (3.2, (470, 600), (300, 805), "Azure AI Studio", "set aside"),
            (7.1, (700, 560), (720, 805), "Azure AI Foundry", "set aside"))):
        pts = _qbez((1150, 250), ((1150 + dest[0]) / 2, 230), dest)
        fx.travel(f"rn-p{i}", t, t + .9, pts)
        fx.body.append(f'<ellipse class="rn-land{i}" cx="{dest[0]}" cy="{dest[1]}" rx="150" ry="70" fill="url(#rename-glow)"/>')
        fx.window(f"rn-land{i}", t + .8, t + 1.6, peak=.9)
        fx.chip(f"rn-c{i}", *chip, label, sub=sub, leader=(dest[0], dest[1] + 60))
        fx.appear(f"rn-c{i}", t + 1.0)
    # the holder: responsibilities that never move
    fx.body.append(f'<text class="rn-head fx-label" x="1010" y="735" {FONT} font-size="18" font-weight="700" '
                   f'letter-spacing="2.6" fill="{MUTED}">STAYS WITH YOUR MUNICIPALITY</text>')
    x = 1010
    for i, item in enumerate(("Identity", "Data", "Records", "Decisions", "Cost")):
        w = 34 + 11.2 * len(item)
        fx.body.append(f'<g class="rn-r{i} fx-label"><rect x="{x:.0f}" y="757" width="{w:.0f}" height="42" rx="21" '
                       f'fill="#ffffff" fill-opacity=".95" stroke="#9cc4bb" stroke-width="1.6"/>'
                       f'<text x="{x + w / 2:.0f}" y="785" text-anchor="middle" {FONT} font-size="19" font-weight="600" '
                       f'fill="{INK}">{item}</text></g>')
        fx.body.append(f'<rect class="rn-k{i}" x="{x - 4:.0f}" y="753" width="{w + 8:.0f}" height="50" rx="25" fill="none" '
                       f'stroke="{SAGE}" stroke-width="3"/>')
        fx.kf(f"rn-k{i}", [(0, 'opacity:0'), (3.7 + i * .08, 'opacity:0'), (3.9 + i * .08, 'opacity:1'), (4.6 + i * .08, 'opacity:0'),
                           (7.7 + i * .08, 'opacity:0'), (7.9 + i * .08, 'opacity:1'), (8.6 + i * .08, 'opacity:0'),
                           (12, 'opacity:0')], hidden=True)
        x += w + 10
    fx.body.append('<path class="rn-bracket fx-label" d="M1010 712 L1010 700 Q1010 690 1020 690 L1250 690" fill="none" '
                   'stroke="#9cc4bb" stroke-width="2" stroke-dasharray="4 5"/>')
    fx.body.append('<ellipse class="rn-holder" cx="1250" cy="560" rx="380" ry="120" fill="url(#rename-sage)"/>')
    fx.kf("rn-holder", [(0, 'opacity:.25'), (3.7, 'opacity:.25'), (4.1, 'opacity:.8'), (4.9, 'opacity:.25'),
                        (7.8, 'opacity:.25'), (8.2, 'opacity:.8'), (9.0, 'opacity:.25'), (12, 'opacity:.25')])
    fx.css.append(f'{fx.sel("rn-holder")}{{opacity:.25}}')
    fx.sweep()
    return fx.render()


# ---------------------------------------------------------------------------
# Review: the proof is checked and corrected; nothing posts by itself.

ROWS = [(377 + 7 * i, 352 + 17 * i) for i in range(14)]
STRUCK = 6


def review_fx():
    fx = FX("review")
    fx.extra_defs = ('<clipPath id="review-sheet"><path d="M300 325 L795 300 L905 610 L430 652Z"/></clipPath>'
                     '<linearGradient id="review-scan" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#bfe0ff" stop-opacity="0"/>'
                     '<stop offset=".7" stop-color="#9fd0ff" stop-opacity=".55"/><stop offset="1" stop-color="#ffffff" stop-opacity=".9"/></linearGradient>')
    fx.chip("rv-c-ai", 470, 250, "AI-prepared draft", num=1)
    fx.appear("rv-c-ai", 0.2)
    fx.body.append('<g clip-path="url(#review-sheet)"><g transform="rotate(-3 600 470)"><rect class="rv-scan" x="260" y="250" '
                   'width="700" height="60" fill="url(#review-scan)"/></g></g>')
    fx.kf("rv-scan", [(0, 'transform:translateY(0);opacity:0'), (0.3, 'transform:translateY(0);opacity:1'),
                      (2.3, 'transform:translateY(390px);opacity:1'), (2.6, 'transform:translateY(390px);opacity:0'),
                      (12, 'transform:translateY(390px);opacity:0')], ease="linear", hidden=True)
    # staff review pass
    x0, y0 = ROWS[0]
    fx.body.append(f'<g transform="rotate(-3 {x0} {y0})"><rect class="rv-hl" x="{x0 - 10}" y="{y0 - 11}" width="360" height="20" '
                   f'rx="6" fill="#bfe0d8" fill-opacity=".55"/></g>')
    frames, t = [(0, 'opacity:0;transform:translate(0,0)'), (2.6, 'opacity:0;transform:translate(0,0)')], 2.7
    for i, (x, y) in enumerate(ROWS):
        frames.append((t, f'opacity:1;transform:translate({x - x0}px,{y - y0}px)'))
        t += 1.9 if i == STRUCK else .26
    frames += [(t, f'opacity:0;transform:translate({ROWS[-1][0] - x0}px,{ROWS[-1][1] - y0}px)'),
               (12, f'opacity:0;transform:translate({ROWS[-1][0] - x0}px,{ROWS[-1][1] - y0}px)')]
    fx.kf("rv-hl", frames, ease="linear", hidden=True)
    t = 2.7
    for i, (x, y) in enumerate(ROWS):
        if i != STRUCK:
            fx.body.append(f'<circle class="rv-d{i}" cx="{x - 24}" cy="{y + 1}" r="5.5" fill="{SAGE}"/>')
            fx.appear(f"rv-d{i}", t + .1, dy=0, dur=.2, scale=True)
        t += 1.9 if i == STRUCK else .26
    sx, sy = ROWS[STRUCK]
    flag_t = 2.7 + .26 * STRUCK
    fx.body.append(f'<g transform="rotate(-3 {sx} {sy})"><rect class="rv-flagbar" x="{sx - 10}" y="{sy - 11}" width="360" '
                   f'height="22" rx="6" fill="{LILAC}" fill-opacity=".3" stroke="{LILAC}" stroke-width="2"/>'
                   f'<rect class="rv-fixbar" x="{sx - 10}" y="{sy - 11}" width="360" height="22" rx="6" fill="#bfe0d8" '
                   f'fill-opacity=".45" stroke="{SAGE}" stroke-width="2"/></g>')
    fx.window("rv-flagbar", flag_t, flag_t + 1.9)
    fx.appear("rv-fixbar", flag_t + 1.9, dy=0)
    ring(fx, "rv-flagring", 850, 432, 34, LILAC, 3, flag_t, 1.0)
    ring(fx, "rv-flagring2", 850, 432, 34, LILAC, 3, flag_t + .5, 1.0)
    fx.chip("rv-c-flag", 1020, 360, "Flagged: needs a source", num=2, leader=(860, 420))
    fx.window("rv-c-flag", flag_t + .1, flag_t + 1.9)
    fx.css.append(f'{fx.sel("rv-c-flag")}{{opacity:0}}')
    fx.chip("rv-c-fix", 1020, 360, "Corrected by staff", num=2, leader=(860, 420))
    fx.appear("rv-c-fix", flag_t + 2.0)
    # the gate: posting requires approval
    gt = 8.3
    fx.body.append('<path class="rv-path" d="M905 540 C990 545 1050 480 1120 455" pathLength="1" fill="none" stroke="#9fb9d1" '
                   'stroke-width="4" stroke-dasharray="1" stroke-linecap="round"/>')
    fx.draw("rv-path", gt, gt + .8, rest=.8)
    fx.body.append(f'<g class="rv-stop"><circle cx="1132" cy="452" r="22" fill="#ffffff" stroke="{BLUE}" stroke-width="3"/>'
                   f'<rect x="1124" y="442" width="5" height="20" rx="2" fill="{BLUE}"/><rect x="1135" y="442" width="5" height="20" rx="2" fill="{BLUE}"/></g>')
    fx.appear("rv-stop", gt + .7, dy=0, scale=True)
    ring(fx, "rv-stopring", 1132, 452, 24, BLUE, 3, gt + .9, 1.0)
    fx.chip("rv-c-gate", 1180, 650, "Posts only after approval", num=3, leader=(1132, 476))
    fx.appear("rv-c-gate", gt + .9)
    fx.body.append('<rect class="rv-empty" x="1228" y="108" width="340" height="392" rx="10" fill="none" stroke="#9fb9d1" '
                   'stroke-width="2.5" stroke-dasharray="9 9"/>')
    fx.body.append(f'<text class="rv-nothing fx-label" x="1398" y="310" text-anchor="middle" {FONT} font-size="26" '
                   f'font-weight="600" fill="#5b7489">Nothing posted yet</text>')
    for cls in ("rv-empty", "rv-nothing"):
        fx.kf(cls, [(0, 'opacity:.35'), (gt + 1.0, 'opacity:.35'), (gt + 1.4, 'opacity:1'), (gt + 1.9, 'opacity:.55'),
                    (gt + 2.4, 'opacity:1'), (12, 'opacity:.35')])
    fx.sweep()
    return fx.render()


# ---------------------------------------------------------------------------
# Footer: plant one plot, measure it, review the evidence, then decide.

PLOT2 = ((575, 360), (889, 322), (1024, 490), (690, 540))
PLOT3 = ((899, 320), (1190, 282), (1340, 445), (1034, 490))
PLOT4 = ((1200, 280), (1470, 240), (1630, 410), (1350, 445))
BEADS = ((220, 236), (197, 327), (240, 392))
METRICS = (("Accuracy", .82), ("Staff time", .64), ("Failures", .28), ("Cost", .52))


def _poly(points):
    return "M" + " L".join(f"{x} {y}" for x, y in points) + "Z"


def pilot_fx():
    fx = FX("pilot")
    # 1. one bounded plot
    fx.body.append(f'<path class="pl-plot" d="M212 408 L568 362 L645 548 L292 604Z" pathLength="1" fill="none" '
                   f'stroke="{SAGE}" stroke-width="4" stroke-linejoin="round"/>')
    fx.draw("pl-plot", 0.2, 1.3, rest=.9)
    fx.body.append('<ellipse class="pl-plotglow" cx="430" cy="490" rx="260" ry="130" fill="url(#pilot-sage)"/>')
    fx.window("pl-plotglow", 0.3, 1.6, peak=.7)
    fx.chip("pl-c-1", 440, 770, "Pilot one process", num=1, leader=(440, 640))
    fx.appear("pl-c-1", 0.6)
    # living plot: drifting pollen
    for i in range(9):
        x, y = 290 + (i * 37) % 300, 470 + (i * 29) % 90
        fx.body.append(f'<circle class="pl-pol pl-pol{i}" cx="{x}" cy="{y}" r="{2.5 + i % 3}" fill="#ffffff"/>')
        fx.css.append(f'{fx.sel(f"pl-pol{i}")}{{animation-delay:-{i * .37:.2f}s!important}}')
    fx.css.append(f'{fx.sel("pl-pol")}{{opacity:0}}')
    fx.css.append(f'[data-motion="on"] {fx.sel("pl-pol")}{{animation:pilot-pol 3s ease-out infinite}}')
    fx.css.append('@keyframes pilot-pol{0%{opacity:0;transform:translate(0,0)}25%{opacity:.9}100%{opacity:0;transform:translate(14px,-120px)}}')
    # 2. measure: stakes ping, metrics fill
    for i, t in enumerate((1.6, 2.4, 3.2, 4.0)):
        bx, by = BEADS[i % 3]
        ring(fx, f"pl-bead{i}", bx, by, 16, BLUE, 3, t, 1.0, .6, 2.6)
        fx.body.append(f'<circle class="pl-beadg{i}" cx="{bx}" cy="{by}" r="26" fill="url(#pilot-pulse)"/>')
        fx.window(f"pl-beadg{i}", t, t + .5, fade=.2)
    fx.body.append('<path class="pl-lead" d="M232 230 Q262 170 300 150" fill="none" stroke="#9db6cd" stroke-width="1.6" '
                   'stroke-dasharray="3 5"/>')
    rows = [f'<rect x="300" y="28" width="410" height="190" rx="18" fill="#ffffff" fill-opacity=".93" stroke="#c4d6e6"/>',
            f'<circle cx="332" cy="60" r="13" fill="{BLUE}"/><text x="332" y="66" text-anchor="middle" {FONT} font-size="16" '
            f'font-weight="700" fill="#fff">2</text>',
            f'<text x="356" y="67" {FONT} font-size="19" font-weight="700" letter-spacing="2" fill="{INK}">MEASURE IT</text>']
    for i, (name, v) in enumerate(METRICS):
        y = 104 + i * 32
        rows.append(f'<text x="324" y="{y + 6}" {FONT} font-size="18" fill="{INK}">{name}</text>')
        rows.append(f'<rect x="452" y="{y - 6}" width="200" height="12" rx="6" fill="#e3ecf4"/>')
        rows.append(f'<rect class="pl-bar{i}" x="452" y="{y - 6}" width="{200 * v:.0f}" height="12" rx="6" '
                    f'fill="{SAGE if name == "Failures" else BLUE}"/>')
        rows.append(f'<circle class="pl-ok{i}" cx="680" cy="{y}" r="7" fill="{SAGE}"/>')
        t = 1.7 + i * .8
        fx.kf(f"pl-bar{i}", [(0, 'transform:scaleX(0)'), (t, 'transform:scaleX(0)'), (t + .7, 'transform:scaleX(1)'),
                             (FADE_OUT[0], 'transform:scaleX(1)'), (FADE_OUT[1], 'transform:scaleX(0)'), (12, 'transform:scaleX(0)')],
              ease="cubic-bezier(.2,.8,.2,1)", origin="left center")
        fx.appear(f"pl-ok{i}", t + .7, dy=0, dur=.25, scale=True)
    fx.body.append('<g class="pl-panel fx-label">' + "".join(rows) + '</g>')
    fx.appear("pl-panel", 1.2)
    fx.body.append('<rect class="pl-panelring" x="296" y="24" width="418" height="198" rx="21" fill="none" '
                   f'stroke="{SAGE}" stroke-width="3"/>')
    fx.window("pl-panelring", 5.0, 6.4)
    # 3. review the evidence
    fx.chip("pl-c-3", 900, 125, "Review the evidence", num=3, leader=(712, 125))
    fx.appear("pl-c-3", 5.3)
    # 4. the next plot is considered, not planted
    fx.body.append(f'<path class="pl-next" d="{_poly(PLOT2)}" pathLength="1" fill="#e9f4f0" fill-opacity=".55" '
                   f'stroke="{SAGE}" stroke-width="3.5" stroke-dasharray="1" stroke-linejoin="round"/>')
    fx.draw("pl-next", 7.0, 8.2, rest=.95)
    for i, (x, y) in enumerate(((700, 430), (790, 470), (880, 410), (760, 390))):
        fx.body.append(f'<g class="pl-seed{i}"><circle cx="{x}" cy="{y}" r="18" fill="none" stroke="{SAGE}" stroke-width="2.5" '
                       f'stroke-dasharray="5 5"/><circle cx="{x}" cy="{y}" r="4" fill="{SAGE}" fill-opacity=".6"/></g>')
        fx.appear(f"pl-seed{i}", 8.0 + i * .2, dy=0, scale=True)
    fx.chip("pl-c-4", 820, 600, "Next plot", num=4, sub="only if the evidence supports it", leader=(820, 520))
    fx.appear("pl-c-4", 8.3)
    for i, pts in enumerate((PLOT3, PLOT4)):
        cx = sum(p[0] for p in pts) / 4
        cy = sum(p[1] for p in pts) / 4
        fx.body.append(f'<text class="pl-later{i} fx-label" x="{cx:.0f}" y="{cy + 8:.0f}" text-anchor="middle" {FONT} '
                       f'font-size="24" font-weight="600" letter-spacing="2" fill="#7f95a8">NOT YET</text>')
        fx.appear(f"pl-later{i}", 9.0 + i * .3, dy=6)
    fx.sweep()
    return fx.render()
