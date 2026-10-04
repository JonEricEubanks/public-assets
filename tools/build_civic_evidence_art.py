"""Render the original, scene-led Civic Evidence Lab animated SVG collection."""

from html import escape
from math import cos, sin, pi
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "images"
NAVY, PURPLE, GREEN = "#94bee8", "#c6a4ff", "#8de4bd"
GOLD, MAGENTA, BLUE = "#f1ca85", "#f4a7d7", "#88d4ef"

DEFS = """
<defs>
 <linearGradient id="sky" x2="0" y2="1"><stop stop-color="#121c30"/><stop offset=".7" stop-color="#253949"/><stop offset="1" stop-color="#815249"/></linearGradient>
 <linearGradient id="desk" x2="0" y2="1"><stop stop-color="#263843"/><stop offset="1" stop-color="#09151e"/></linearGradient>
 <linearGradient id="paper" x2=".2" y2="1"><stop stop-color="#f7efdb"/><stop offset=".6" stop-color="#e8d8b4"/><stop offset="1" stop-color="#b69d76"/></linearGradient>
 <linearGradient id="bronze" x2="1" y2=".3"><stop stop-color="#6d4b32"/><stop offset=".25" stop-color="#e8c68b"/><stop offset=".5" stop-color="#9b7148"/><stop offset=".75" stop-color="#f8ddb0"/><stop offset="1" stop-color="#765236"/></linearGradient>
 <linearGradient id="stone" x2="1" y2="1"><stop stop-color="#d1c1a2"/><stop offset=".55" stop-color="#9c8c75"/><stop offset="1" stop-color="#665e57"/></linearGradient>
 <linearGradient id="roof" x2="0" y2="1"><stop stop-color="#4c6f76"/><stop offset="1" stop-color="#1e373f"/></linearGradient>
 <linearGradient id="cover" x2="1" y2="1"><stop stop-color="#364d68"/><stop offset="1" stop-color="#152335"/></linearGradient>
 <linearGradient id="beam" x2="0" y2="1"><stop stop-color="#ffe7ad" stop-opacity=".3"/><stop offset="1" stop-color="#ffe7ad" stop-opacity="0"/></linearGradient>
 <radialGradient id="aura"><stop stop-color="#d2a575" stop-opacity=".22"/><stop offset="1" stop-color="#d2a575" stop-opacity="0"/></radialGradient>
 <radialGradient id="radar"><stop stop-color="#2c2948"/><stop offset="1" stop-color="#101c29"/></radialGradient>
 <pattern id="grain" width="6" height="6" patternUnits="userSpaceOnUse"><path d="M0 1H6M1 0V6" stroke="#fff" stroke-opacity=".025"/></pattern>
 <pattern id="mapgrid" width="38" height="38" patternUnits="userSpaceOnUse"><path d="M38 0H0V38" fill="none" stroke="#526f75" stroke-opacity=".24"/></pattern>
 <filter id="shadow" x="-30%" y="-30%" width="170%" height="190%"><feDropShadow dx="0" dy="10" stdDeviation="9" flood-color="#000" flood-opacity=".45"/></filter>
 <filter id="glow" x="-80%" y="-80%" width="260%" height="260%"><feGaussianBlur stdDeviation="4" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
 <marker id="edge-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path d="M1 1L9 5L1 9" fill="none" stroke="#2e7b63" stroke-width="1.5"/></marker>
 <clipPath id="mapclip"><path d="M0 16L30 0H760L790 18V325L755 344H24L0 326Z"/></clipPath>
 <g id="tree"><path d="M0 0V27" stroke="#897864" stroke-width="5"/><path d="M-22 5L0 -42L22 5ZM-17 -14L0 -55L17 -14Z" fill="#315c54"/><path d="M0 -55V5" stroke="#739881" opacity=".4"/></g>
</defs>
<style>
 text{font-family:'Segoe UI',Arial,sans-serif;fill:#f3eee3}
 .mono{font-family:Consolas,'Courier New',monospace;letter-spacing:2px}
 .twinkle{animation:twinkle 8s ease-in-out infinite}
 .windows{animation:windows 7s ease-in-out infinite}
 .flag{animation:flag 4s ease-in-out infinite}
 .float{animation:float 6s ease-in-out infinite}
 .ripples{transform-box:fill-box;transform-origin:center;animation:ripples 4s ease-out infinite}
 .sweep{animation:sweep 12s linear infinite;transform-origin:0 0}
 .needle{animation:needle 8s ease-in-out infinite;transform-origin:0 0}
 .stamp{animation:stamp 7s ease-in-out infinite}
 .drawer{animation:drawer 9s ease-in-out infinite}
 .pull{animation:pull 9s ease-in-out infinite}
 .draft{stroke-dasharray:18 250;animation:draft 8s linear infinite}
 .flow{stroke-dasharray:10 24;animation:flow 4s linear infinite}
 .traveler{offset-rotate:0deg;animation:travel 14s linear infinite}
 .water{animation:water 6s ease-in-out infinite}
 .lamp{animation:lamp 9s ease-in-out infinite}
 @keyframes twinkle{0%,100%{opacity:.25}50%{opacity:.9}}
 @keyframes windows{0%,100%{opacity:.65}50%{opacity:1}}
 @keyframes flag{0%,100%{transform:skewY(-4deg)}50%{transform:skewY(6deg)}}
 @keyframes float{0%,100%{transform:translateY(0)}50%{transform:translateY(-10px)}}
 @keyframes ripples{0%{transform:scale(.72);opacity:.8}100%{transform:scale(1.2);opacity:.05}}
 @keyframes sweep{to{transform:rotate(360deg)}}
 @keyframes needle{0%,100%{transform:rotate(-12deg)}50%{transform:rotate(16deg)}}
 @keyframes stamp{0%,25%,100%{transform:translateY(-16px)}35%,55%{transform:translateY(0)}}
 @keyframes pull{0%,20%,100%{transform:translate(0,0)}35%,65%{transform:translate(-5px,9px)}}
 @keyframes drawer{0%,20%,100%{transform:translateX(0)}35%,65%{transform:translateX(18px)}}
 @keyframes draft{to{stroke-dashoffset:-268}}
 @keyframes flow{to{stroke-dashoffset:-68}}
 @keyframes travel{to{offset-distance:100%}}
 @keyframes water{0%,100%{opacity:.55}50%{opacity:.95}}
 @keyframes lamp{0%,100%{opacity:.6}50%{opacity:.9}}
</style>
"""


def text(x, y, value, size=24, color=None, extra=""):
    style = f' style="fill:{color}"' if color else ""
    return f'<text x="{x}" y="{y}" font-size="{size}"{style} {extra}>{escape(value)}</text>'


def transformed(x, y, scale, body):
    return f'<g transform="translate({x} {y}) scale({scale})">{body}</g>'


def label(x, y, title, subtitle="", color=GOLD):
    result = text(x, y, title, 23, color, 'font-weight="600"')
    if subtitle:
        result += text(x, y+32, subtitle, 19, "#becbd0")
    return result


def townhall(x, y, scale=1):
    body = """<ellipse cx="0" cy="18" rx="147" ry="24" fill="#07131d" opacity=".45"/>
<path d="M-120 -120H120V0H-120Z" fill="url(#stone)" stroke="#e1cfac"/>
<path d="M-143 -119L0 -207L143 -119Z" fill="url(#roof)" stroke="#a8beb6" stroke-width="2"/>
<path d="M-110 -123L0 -187L110 -123Z" fill="none" stroke="#728e89"/>
<rect x="-32" y="-128" width="64" height="128" fill="#253645"/>
<path d="M-150 0H150M-140 10H140M-126 20H126" stroke="#c6b99f" stroke-width="8"/>
<g fill="url(#paper)" stroke="#706e63"><path d="M-96 -112H-78V-3H-96ZM-58 -112H-40V-3H-58ZM40 -112H58V-3H40ZM78 -112H96V-3H78Z"/></g>
<g class="windows" fill="#f1ca85"><path d="M-113 -82H-103V-50H-113ZM103 -82H113V-50H103Z"/><path d="M-19 -90H19V-61H-19Z" opacity=".5"/></g>
<circle cx="0" cy="-146" r="18" fill="#132b37" stroke="#d7c499" stroke-width="3"/><path d="M0 -158V-146L9 -139" stroke="#f1ca85" stroke-width="2" fill="none"/>
<path d="M0 -208V-261" stroke="#cfb98c" stroke-width="3"/>
<g transform="translate(2 -258)"><path class="flag" d="M0 0Q20 -8 42 0V22Q20 13 0 22Z" fill="#c9a06e"/></g>"""
    return transformed(x, y, scale, body)


def tower(x, y, scale=1):
    body = """<ellipse cy="20" rx="72" ry="17" fill="#061421" opacity=".5"/>
<path d="M-36 -110L-52 15M36 -110L52 15M-36 -87L44 -7M36 -87L-44 -7M-44 -8H44" stroke="#90a9b1" stroke-width="6" fill="none"/>
<path d="M-58 -167Q0 -188 58 -167V-109Q0 -87 -58 -109Z" fill="url(#roof)" stroke="#b7c5bd" stroke-width="2"/>
<ellipse cy="-167" rx="58" ry="17" fill="#789398" stroke="#b7c5bd"/>
<path d="M-48 -159V-117" stroke="#d0dfd7" stroke-width="5" opacity=".35"/>
<path d="M-59 -100H59M-63 -94V-109M63 -94V-109" stroke="#d5bb88" fill="none" stroke-width="3"/>
<path d="M-8 -178V-204H8V-178" fill="#729298"/>
<circle class="windows" cy="-207" r="5" fill="#f1ca85" filter="url(#glow)"/>"""
    return transformed(x, y, scale, body)


def house(x, y, scale=1):
    body = """<ellipse cy="10" rx="63" ry="13" fill="#07121b" opacity=".4"/>
<path d="M-50 -68H50V0H-50Z" fill="#957a62"/><path d="M-66 -65L0 -117L66 -65Z" fill="#334f59" stroke="#8ca2a1"/>
<path d="M-43 -60H43" stroke="#d1b58f"/><path d="M-8 -36H14V0H-8Z" fill="#223c49"/>
<g class="windows" fill="#f1ca85"><path d="M-34 -43H-16V-22H-34ZM23 -43H41V-22H23Z"/></g>
<path d="M-25 -43V-22M32 -43V-22" stroke="#705c4d" stroke-width="2"/>"""
    return transformed(x, y, scale, body)


def truck(x, y, scale=1):
    body = """<ellipse cx="4" cy="18" rx="98" ry="12" fill="#07131c" opacity=".45"/>
<path d="M-91 -45H20V-71H62L91 -39V4H-91Z" fill="#bb8860" stroke="#f1ca85" stroke-width="2"/>
<path d="M29 -63H56L75 -40H29Z" fill="#18394c" stroke="#9ab9bf"/>
<path d="M-80 -35H10M-80 -24H10M19 -37V-4" stroke="#704d39" stroke-width="2"/>
<g fill="#0a1721" stroke="#7f969f" stroke-width="4"><circle cx="-53" cy="6" r="18"/><circle cx="58" cy="6" r="18"/></g>
<g fill="#b8bdb2"><circle cx="-53" cy="6" r="7"/><circle cx="58" cy="6" r="7"/></g>
<path class="lamp" d="M87 -31L190 -54V13L87 -15Z" fill="url(#beam)"/>
<rect class="windows" x="81" y="-30" width="9" height="14" fill="#ffe4a3"/>
<path d="M37 -78H53" stroke="#f1ca85" stroke-width="6"/>"""
    return transformed(x, y, scale, body)


def skyline(y, scale=1):
    body = f'<path d="M0 {y}H1400V800H0Z" fill="#101d29"/>'
    for x in range(40, 1400, 130):
        h = 35+(x % 7)*9
        body += f'<path d="M{x} {y}V{y-h}H{x+72}V{y}Z" fill="#192b37"/>'
    body += townhall(720, y, scale*.43) + tower(1130, y, scale*.48)
    return body


def stars(height):
    body = ""
    for i in range(22):
        x = 390+(i*137)%970
        y = 24+(i*43)%max(35, min(height//3, 150))
        body += f'<circle class="twinkle" style="animation-delay:-{i%7}s" cx="{x}" cy="{y}" r="{1+i%3*.35}" fill="#e4d8c3"/>'
    return body


def book(x, y, scale=1, title="ASSET FILES"):
    body = """<ellipse cx="135" cy="209" rx="150" ry="17" fill="#07111b" opacity=".5"/>
<path d="M250 -10L268 -21V181L250 200Z" fill="#0f1b2a" stroke="#5f788d"/>
<path d="M10 -10L28 -21H268L250 -10Z" fill="#587189" stroke="#7b9bb3"/>
<rect x="10" y="-10" width="240" height="210" rx="3" fill="url(#cover)" stroke="#7b9bb3" stroke-width="2"/>"""
    labels = [title, "WM-481 / ACTIVE", "MUNICIPAL RECORD"]
    for i, name in enumerate(labels):
        top = -2 + i*67
        cls = 'class="pull"' if i == 1 else ""
        body += f'<g {cls}><rect x="20" y="{top}" width="220" height="61" rx="2" fill="#2a3f54" stroke="#7c96a5"/>'
        body += f'<rect x="52" y="{top+8}" width="156" height="21" rx="2" fill="#e3d3a8" stroke="#a89776"/>'
        body += text(130, top+23, name, 12, "#2d3d44", 'class="mono" text-anchor="middle"')
        body += f'<path d="M98 {top+44}H162" stroke="url(#bronze)" stroke-width="7" stroke-linecap="round"/></g>'
    return transformed(x, y, scale, body)

def charter(x, y, scale=1):
    body = """<path d="M0 4Q120 -8 234 4L247 217Q120 232 -12 217Z" fill="url(#paper)" stroke="#a89776" filter="url(#shadow)"/>
<path d="M12 21H215M20 170H217" stroke="#8f805f"/>
<path d="M23 82H207M23 105H189M23 127H203M23 150H167" stroke="#63767a" stroke-width="3" opacity=".55"/>"""
    body += text(22, 51, "THE CIVIC CHARTER", 18, "#34484c", 'font-weight="600"')
    body += text(25, 200, "SOURCE / OWNER / DATE", 12, "#34484c", 'class="mono"')
    body += seal(195, 213, .6)
    return transformed(x, y, scale, body)


def seal(x, y, scale=1):
    body = """<circle r="34" fill="url(#bronze)" stroke="#efcf95" stroke-width="2"/>
<circle r="26" fill="#836045" stroke="#efcf95" stroke-width="1.5" stroke-dasharray="2 4"/>
<path d="M-15 -14H15V0Q15 15 0 21Q-15 15 -15 0Z" fill="none" stroke="#ffe4b0" stroke-width="2"/>
<path class="windows" d="M-8 0L-1 7L10 -7" fill="none" stroke="#ffe4b0" stroke-width="3"/>"""
    return transformed(x, y, scale, body)


def compass(x, y, scale=1):
    body = '<circle r="73" fill="url(#bronze)" stroke="#e9c893" stroke-width="2" filter="url(#shadow)"/><circle r="62" fill="#132c36" stroke="#dcc496"/>'
    for i in range(24):
        angle = i*pi/12
        body += f'<path d="M{cos(angle)*52:.2f} {sin(angle)*52:.2f}L{cos(angle)*58:.2f} {sin(angle)*58:.2f}" stroke="#d7c29b"/>'
    body += text(0,-34,"N",16,GOLD,'text-anchor="middle"')
    body += '<g class="needle"><path d="M0 -29L12 24L0 14L-12 24Z" fill="#f1ca85"/><path d="M0 -29V14L-12 24Z" fill="#9e7155"/></g><circle r="5" fill="#e5c58d"/>'
    return transformed(x, y, scale, body)


def atlas(x, y, scale=1, relations=False):
    body = """<path d="M0 16L30 0H760L790 18V325L755 344H24L0 326Z" fill="url(#paper)" stroke="#d7c8a6" filter="url(#shadow)"/>
<g clip-path="url(#mapclip)"><rect width="790" height="344" fill="url(#mapgrid)"/>
<path d="M0 78Q210 114 340 72T790 90M0 125Q230 166 400 127T790 145M0 274Q240 230 420 280T790 260" stroke="#bfae83" stroke-width="2" fill="none" opacity=".6"/>
<path d="M515 -15Q459 70 553 150T508 360" fill="none" stroke="#668994" stroke-width="38" opacity=".7"/>
<path class="flow" d="M515 -15Q459 70 553 150T508 360" fill="none" stroke="#d0e5df" stroke-width="2" opacity=".7"/>
<path d="M24 191H750M168 24V314M370 24V314M653 24V314" stroke="#718077" stroke-width="14" fill="none"/>
<path d="M24 191H750M168 24V314M370 24V314M653 24V314" stroke="#dcd4b9" stroke-width="8" fill="none"/>
<path d="M40 28H288V128H40ZM218 225H421V314H218ZM580 29H745V136H580Z" fill="none" stroke="#73877a" stroke-width="1.5"/>
<g fill="#748d69" opacity=".6"><path d="M46 230H143V315H46Z"/><path d="M588 224H740V313H588Z"/></g>
<path d="M269 0V344M526 0V344" stroke="#a89c79" opacity=".6"/>
</g>"""
    body += townhall(370,173,.38) + tower(655,178,.42) + house(171,177,.5)
    body += truck(385,281,.4)
    for tx,ty in [(70,275),(108,290),(610,277),(700,286)]:
        body += transformed(tx,ty,.45,'<use href="#tree"/>')
    if relations:
        for path in ["M171 191H370", "M171 191V71H653V191", "M653 191V279H385"]:
            body += f'<path d="{path}" fill="none" stroke="#2e7b63" stroke-width="3" marker-end="url(#edge-arrow)"/>'
            body += f'<path class="draft" d="{path}" fill="none" stroke="#8de4bd" stroke-width="2"/>'
        body += text(240,215,"located at",15,"#27594e")
        body += text(400,61,"concerns",15,"#27594e")
        body += text(475,302,"maintained by",15,"#27594e")
        for px,py,caption in [(131,246,"Complaint"),(331,246,"Address"),(608,226,"Water Main"),(330,328,"Public Works")]:
            body += text(px,py,caption,15,"#27594e",'font-weight="600"')
    return transformed(x,y,scale,body)


def scanner(x, y, radius):
    body = f'<circle r="{radius+15}" fill="url(#bronze)" stroke="#e7cda3" stroke-width="2" filter="url(#shadow)"/><circle r="{radius}" fill="url(#radar)" stroke="{PURPLE}" stroke-width="2"/>'
    for fraction in [.25,.5,.75]:
        body += f'<circle r="{radius*fraction}" fill="none" stroke="{PURPLE}" stroke-opacity=".3"/>'
    body += f'<path d="M{-radius} 0H{radius}M0 {-radius}V{radius}" stroke="{PURPLE}" stroke-opacity=".25"/>'
    body += f'<g class="sweep"><path d="M0 0L{radius*.87} {-radius*.5}A{radius} {radius} 0 0 1 {radius} 0Z" fill="{PURPLE}" fill-opacity=".17"/><path d="M0 0H{radius}" stroke="{PURPLE}" stroke-width="2"/></g>'
    for i,(dx,dy) in enumerate([(-.45,-.3),(.33,-.24),(.52,.2),(-.21,.47)]):
        body += f'<circle class="windows" style="animation-delay:-{i}s" cx="{dx*radius}" cy="{dy*radius}" r="5" fill="{PURPLE}"/>'
    return transformed(x,y,1,body)


def report(x,y,scale=1,title="WATER AT THE CURB"):
    body = """<g class="float"><path d="M0 0H154L182 28V116H0Z" fill="url(#paper)" stroke="#b59b7d" filter="url(#shadow)"/>
<path d="M154 0V28H182" fill="#a89374"/><path d="M17 60H164M17 79H146M17 98H118" stroke="#856f83" stroke-width="3"/>"""
    body += text(15,37,title,12,"#443b55",'font-weight="600"')
    body += '</g>'
    return transformed(x,y,scale,body)


def traveler(path, color=MAGENTA, duration=14):
    return (
        f'<path d="{path}" fill="none" stroke="{color}" stroke-width="2" opacity=".4"/>'
        f'<circle class="traveler" r="6" fill="{color}" filter="url(#glow)" '
        f'style="offset-path:path(\'{path}\');animation-duration:{duration}s"/>'
    )


def puddle(x,y,scale=1):
    body = '<ellipse rx="72" ry="14" fill="#689bad" opacity=".5"/>'
    for i in range(3):
        body += f'<ellipse class="ripples" style="animation-delay:-{i*1.3}s" rx="{32+i*12}" ry="{6+i*2}" fill="none" stroke="{BLUE}" stroke-width="2"/>'
    body += '<path class="water" d="M-5 -4Q-13 -25 -4 -40Q4 -18 12 -6" stroke="#a4dded" stroke-width="3" fill="none"/>'
    return transformed(x,y,scale,body)


def write(name,title,description,body,height=680,subtitle="",compact=False):
    header = text(54,34 if compact else 46,"CIVIC EVIDENCE LAB / A CITY READ FOUR WAYS",16,GOLD,'class="mono"')
    if compact:
        header += text(52,84,title,38,extra='font-weight="700"')
        header += text(54,114,subtitle,20,"#c6d3d5")
    elif height>300:
        header += text(52,107,title,44,extra='font-weight="700"')
        header += text(54,148,subtitle,23,"#c6d3d5")
    footer = text(54,height-22,"CONCEPTUAL MUNICIPAL SCENE / NOT PRODUCT UI",14,"#b0c2c9",'class="mono"')
    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="1400" height="{height}" viewBox="0 0 1400 {height}" role="img" aria-labelledby="title desc">'
        f'<title id="title">{escape(title)}</title><desc id="desc">{escape(description)}</desc>{DEFS}'
        f'<defs><clipPath id="frame"><rect width="1400" height="{height}" rx="22"/></clipPath></defs>'
        f'<g clip-path="url(#frame)"><rect width="1400" height="{height}" fill="url(#sky)"/>'
        f'<ellipse cx="870" cy="{height*.5}" rx="740" ry="340" fill="url(#aura)"/>'
        f'{stars(height)}{body}<rect width="1400" height="{height}" fill="url(#grain)"/>{header}{footer}</g>'
        f'<rect x="1" y="1" width="1398" height="{height-2}" rx="21" fill="none" stroke="#66818d" stroke-opacity=".5"/>'
        '</svg>\n'
    )
    (OUT/f"{name}.svg").write_text(svg,encoding="utf-8")


def build():
    OUT.mkdir(exist_ok=True)
    body = skyline(306)
    body += '<path d="M0 374L1400 347V800H0Z" fill="url(#desk)"/><path d="M0 727L1400 704" stroke="#ac8862" stroke-opacity=".6" stroke-width="6"/>'
    body += atlas(458,347,1.07,True) + book(84,420,1.25)
    body += scanner(1123,350,113) + compass(469,589,.85) + charter(480,664,.42)
    body += '<path class="lamp" d="M105 285L18 688H408L174 285Z" fill="url(#beam)"/><path d="M86 475V271Q86 244 136 244H185" stroke="url(#bronze)" stroke-width="12" fill="none"/><path d="M98 278L139 219L196 276Z" fill="#486565" stroke="#c6b794"/><path d="M96 279H199" stroke="#f1ca85" stroke-width="6"/><ellipse cx="89" cy="493" rx="51" ry="11" fill="url(#bronze)"/>'
    body += label(116,344,"THE MEMORY","The official records",NAVY)
    body += label(956,181,"THE LISTENING","Meaning, not identity",PURPLE)
    body += label(458,196,"THE LEGEND","Governed meaning",GREEN)
    body += traveler("M641 553L855 553L1157 553L1157 645L870 645",MAGENTA)
    body += label(1115,745,"THE JOURNEY","Follow the path",MAGENTA)
    write("municipal-information-city-hero","One city. Four ways to read it.","A lamplit municipal survey desk overlooks a city hall and water tower. A steel file cabinet, floating-report radar, brass compass, charter seal, and parchment city atlas recur throughout the article. A magenta traveler follows a modeled route; it does not create facts.",body,800,"The public record. The listening signal. The governed atlas. The connected journey.")

    body = skyline(201,.75)
    body += text(54,105,"Every connection needs an anchor.",34,extra='font-weight="600"')
    body += text(54,151,"Begin with the public record. Keep similarity separate from fact.",23,"#c6d3d5")
    body += traveler("M54 185L461 185L461 203L1291 203",GOLD,12)
    body += seal(1276,114,1.2)
    write("municipal-information-city-divider","Every connection needs an anchor.","A gold survey light travels toward a municipal seal above a distant city hall and water tower, anchoring the story in the public record.",body,260)

    body = '<path d="M0 550H1400V680H0Z" fill="url(#desk)"/>'
    body += townhall(314,478,1.1)
    body += '<path d="M620 219H1010V516H620Z" fill="url(#cover)" stroke="#859db0" stroke-width="2"/><path d="M620 238H1010M632 227V502M994 227V502" stroke="#354e62" stroke-width="8"/>'
    for i in range(3):
        y=260+i*77
        cls='class="drawer"' if i==1 else ""
        body += f'<g {cls}><path d="M648 {y}H974V{y+58}H648Z" fill="#344a5b" stroke="#7c96a5"/><path d="M761 {y+36}H861" stroke="url(#bronze)" stroke-width="6"/>'
        body += text(666,y+25,["ASSETS / WM-481","WORK ORDERS / WO-204","INSPECTIONS / IN-032"][i],15,GOLD,'class="mono"')+'</g>'
    body += book(1027,385,.92)
    body += label(74,580,"THE CITY'S MEMORY","Keys, constraints, transactions.",NAVY)
    body += label(643,580,"THE RECORD IS EXACT","An identifier is not a similarity score.",NAVY)
    write("municipal-records-office","The memory / Preserve the public record","A stone municipal records office sits beside a brass-handled archive cabinet and a smaller steel file cabinet. The work-order drawer slowly opens and closes while city-hall windows glow. All displayed IDs are fictional.",body,subtitle="Relational records are the city's memory: exact identifiers and protected transactions.")

    body = skyline(568,.9)
    body += scanner(470,378,179)
    body += report(73,257,1.05,"WATER BUBBLING")
    body += report(950,236,1.3,"STANDING WATER")
    body += report(1035,401,.95,"POSSIBLE MAIN BREAK")
    body += '<path class="water" d="M700 317Q725 297 750 317T800 317T850 317T900 317" fill="none" stroke="#c6a4ff" stroke-width="3"/>'
    body += label(54,599,"THE CITY'S LISTENING SIGNAL","Nearby in meaning. Not officially connected.",PURPLE)
    body += text(755,619,"No shared asset or incident is implied.",23,GOLD)
    write("municipal-similarity-radar","The listening / Find related evidence","Three folded complaint sheets float around a rotating brass-rimmed radar over a municipal skyline. A purple wave denotes semantic similarity without any authoritative graph edges.",body,subtitle="Different words can describe similar trouble. The scanner hears the resemblance.")

    body = '<path d="M0 555H1400V680H0Z" fill="url(#desk)"/>'
    body += atlas(78,231,1.07,True) + compass(863,255,.76) + charter(1035,265,1.14)
    body += label(77,623,"THE CITY'S SHARED LEGEND",color=GREEN)
    body += text(470,623,"Defined entities. Sources. Responsibilities.",21,"#becbd0")
    body += text(998,575,"Source. Owner. Effective date.",22,GOLD)
    write("municipal-knowledge-map","The legend / Give connections meaning","A parchment street atlas uses actual municipal landmarks rather than abstract node cards. Labeled green connections cross the map; a moving drafting highlight does not alter their authoritative status. A compass gently settles and a sealed charter represents definitions and provenance.",body,subtitle="A map without a legend is just marks on paper. Governance supplies the vocabulary.")

    body = '<path d="M0 564H1400V680H0Z" fill="url(#desk)"/>'
    body += atlas(295,204,1.08,True)
    body += '<path d="M190 223V194H1301V550H1268" fill="none" stroke="#f4a7d7" stroke-width="2" stroke-dasharray="2 6"/>'
    body += text(54,228,"FABRIC GRAPH",20,MAGENTA,'class="mono"')
    body += traveler("M480 410L695 410L1000 410L1000 505L711 505",MAGENTA,11)
    body += text(54,601,"THE JOURNEY / execution over modeled connections",23,MAGENTA)
    body += '<path d="M54 620H1344" stroke="#88d4ef" stroke-width="12" stroke-opacity=".35"/>'
    body += text(804,643,"ONELAKE / SOURCE DATA FOUNDATION",18,BLUE,'class="mono"')
    write("fabric-graph-route-engine","The journey / Follow the connected path","A magenta traveling light follows a multistep path across a large municipal street atlas. A dotted magenta bracket is labeled as the Fabric Graph execution extent, not an inferred relationship. A blue source-data rail represents OneLake.",body,subtitle="The atlas supplies modeled connections. The engine navigates them.")

    body = '<path d="M0 565H1400V680H0Z" fill="url(#desk)"/>'
    body += charter(111,270,1.3) + compass(544,368,1.14)
    body += atlas(784,294,.68,True)
    body += traveler("M901 424L1035 424L1228 424L1228 484L1045 484",MAGENTA,9)
    body += label(75,226,"THE CHARTER / MEANING","What is it? Who asserted it?",GREEN)
    body += label(806,226,"THE COMPASS / EXECUTION","What is reachable? Which path exists?",MAGENTA)
    body += text(76,616,"The legend defines the map. The engine finds the route.",29,GOLD)
    write("knowledge-versus-execution","The charter is not the compass.","A sealed charter and a large gently moving brass compass sit beside a miniature municipal atlas with a traveling route light. They distinguish designed meaning from path execution without using comparison cards.",body,subtitle="A graph engine can execute connections. It cannot invent their governed meaning.")

    body = '<path d="M0 508H1400V680H0Z" fill="url(#desk)"/><path d="M0 522H1400" stroke="#c6b08a" stroke-width="5"/>'
    body += house(307,473,1.65) + tower(1061,474,1.18) + truck(713,478,1.03) + puddle(472,509,1.2)
    body += '<path d="M0 582H1400" stroke="#344f60" stroke-width="20"/><path class="flow" d="M64 582H1334" stroke="#88d4ef" stroke-width="3"/>'
    body += report(54,233,.98,"COMPLAINT / CR-017") + book(492,216,.8) + compass(913,264,.66) + seal(1245,277,.96)
    body += label(54,621,"ONE LEAK / FOUR QUESTIONS",color=GOLD)
    body += text(474,621,"Recorded? Similar? Defined? Connected?",22,"#becbd0")
    write("water-main-four-views","One incident. Not one universal database.","A dimensional street scene shows a resident's house, a bubbling puddle, a public-works truck, and a water tower. An underground cutaway carries flowing blue water. A complaint sheet, file cabinet, compass, and charter seal illustrate the four questions about the same incident.",body,subtitle="The report starts the investigation. Every capability answers a different question.")

    body = '<path d="M0 552H1400V680H0Z" fill="url(#desk)"/>'
    body += book(63,251,.87) + scanner(498,338,88) + charter(707,243,.94) + compass(1138,338,1.16)
    body += label(62,485,"FILE CABINET / RECORD",color=NAVY)
    body += label(374,485,"RADAR / SIMILARITY",color=PURPLE)
    body += label(708,485,"SEAL / GOVERNANCE",color=GOLD)
    body += label(1050,485,"COMPASS / ROUTE",color=MAGENTA)
    for x,title,dash in [(54,"Authoritative",None),(388,"Inferred","10 8"),(724,"Unverified","2 8")]:
        attr=f' stroke-dasharray="{dash}"' if dash else ""
        body += f'<path d="M{x} 556H{x+245}" fill="none" stroke="{GREEN}" stroke-width="3"{attr}/>'
        body += text(x,591,title,21,GREEN)
    body += '<path class="water" d="M1060 556Q1075 540 1090 556T1120 556T1150 556T1180 556T1210 556T1240 556T1270 556T1300 556" fill="none" stroke="#c6a4ff" stroke-width="3"/>'
    body += text(1060,591,"Similar, not a fact",21,PURPLE)
    write("municipal-data-symbols","The objects are the legend.","Physical civic evidence objects form an animated still life: a steel file cabinet, sweeping radar, charter with a municipal seal, and brass compass. Engraved line samples below distinguish authoritative, inferred, unverified, and similar. Color alone is never the key.",body,subtitle="A recurring visual vocabulary, not a collection of interchangeable glowing nodes.")

    body = '<path d="M0 511H1400V680H0Z" fill="url(#desk)"/>'
    body += townhall(291,470,1.03) + tower(1133,468,1.2)
    body += atlas(448,321,.69,True) + book(87,405,.73) + scanner(625,295,82) + charter(803,244,.71)
    body += traveler("M577 453L703 453L703 514L901 514",MAGENTA,10)
    body += label(54,587,"KEEP THE RECORDS","Preserve integrity.",NAVY)
    body += label(391,587,"LISTEN FOR EVIDENCE","Retrieve by meaning.",PURPLE)
    body += label(750,587,"READ THE LEGEND","Govern relationships.",GREEN)
    body += label(1065,587,"FOLLOW THE ROUTE","Traverse the graph.",MAGENTA)
    write("municipal-information-layers","Compose the city. Do not choose a winner.","City hall and a water tower frame one municipal evidence desk. The archive file cabinet, radar, sealed charter, and city map share the scene as complementary instruments rather than stacked technology boxes. A route light traverses the atlas.",body,subtitle="These are complementary responsibilities, not a required stack or an execution sequence.")

    body = skyline(224,.75) + seal(1290,114,1.2)
    body += text(54,108,"Preserve the record. Understand the evidence.",35,extra='font-weight="600"')
    body += text(54,157,"Listen for meaning. Validate connections. Follow the route. Keep people accountable.",23,"#c6d3d5")
    body += traveler("M54 189L707 189L707 207L1260 207",MAGENTA,13)
    write("municipal-information-city-footer","Preserve the record. Understand the evidence.","The recurring city hall, water tower, charter seal, and traveling magenta light close the municipal story. The destination is accountable understanding, not a universal database.",body,260)
    build_wide_hero()
    print(f"Built 12 animated municipal scenes in {OUT}")


def build_wide_hero():
    """2.4:1 header variant of the city hero (1400x583 scales to 1200x500)."""
    ax, ay, scale = 395, 250, .86
    route = "".join(
        f'{"M" if i == 0 else "L"}{ax+scale*lx:.0f} {ay+scale*ly}'
        for i, (lx, ly) in enumerate([(171, 192), (370, 192), (653, 192), (653, 279), (385, 279)])
    )
    body = skyline(215, .8)
    body += '<path d="M0 262L1400 240V583H0Z" fill="url(#desk)"/><path d="M0 572L1400 556" stroke="#ac8862" stroke-opacity=".6" stroke-width="6"/>'
    body += atlas(ax, ay, scale, True) + book(100, 318, .8)
    body += scanner(1165, 310, 78) + compass(1315, 322, .6) + charter(1288, 408, .3)
    body += '<g transform="translate(3.9 85.1) scale(.72)"><path class="lamp" d="M105 285L18 688H408L174 285Z" fill="url(#beam)"/><path d="M86 475V271Q86 244 136 244H185" stroke="url(#bronze)" stroke-width="12" fill="none"/><path d="M98 278L139 219L196 276Z" fill="#486565" stroke="#c6b794"/><path d="M96 279H199" stroke="#f1ca85" stroke-width="6"/><ellipse cx="89" cy="493" rx="51" ry="11" fill="url(#bronze)"/></g>'
    body += label(160,258,"THE MEMORY","The official records",NAVY)
    body += label(910,160,"THE LISTENING","Meaning, not identity",PURPLE)
    body += label(480,170,"THE LEGEND","Governed meaning",GREEN)
    body += traveler(route,MAGENTA)
    body += label(1115,508,"THE JOURNEY","Follow the path",MAGENTA)
    write("municipal-information-city-hero-wide","One city. Four ways to read it.","A lamplit municipal survey desk overlooks a city hall and water tower. A steel file cabinet, floating-report radar, brass compass, charter seal, and parchment city atlas recur throughout the article. A magenta traveler follows a modeled route; it does not create facts.",body,583,"The public record. The listening signal. The governed atlas. The connected journey.",compact=True)


if __name__ == "__main__":
    build()
