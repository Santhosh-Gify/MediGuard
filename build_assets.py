import os
FONT = "'Poppins','Segoe UI',system-ui,-apple-system,Helvetica,Arial,sans-serif"
A = "assets"

# ---------------- HEADER ----------------
header = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 420" width="1200" height="420" role="img" aria-label="MediGuard">
<defs>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#F6EEF6"/><stop offset="1" stop-color="#E6D3E8"/></linearGradient>
<radialGradient id="b1"><stop offset="0" stop-color="#D9788F" stop-opacity=".55"/><stop offset="1" stop-color="#D9788F" stop-opacity="0"/></radialGradient>
<radialGradient id="b2"><stop offset="0" stop-color="#8A2A56" stop-opacity=".35"/><stop offset="1" stop-color="#8A2A56" stop-opacity="0"/></radialGradient>
<linearGradient id="cross" gradientUnits="userSpaceOnUse" x1="-62" y1="0" x2="62" y2="0">
<stop offset="0" stop-color="#6E1A42"/><stop offset=".5" stop-color="#8E2A58"/><stop offset=".5" stop-color="#D9788F"/><stop offset="1" stop-color="#EFA9B8"/></linearGradient>
<linearGradient id="ring" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#7A1E48"/><stop offset="1" stop-color="#E79AAC"/></linearGradient>
<linearGradient id="ecg" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#B04468" stop-opacity="0"/><stop offset=".5" stop-color="#B04468"/><stop offset="1" stop-color="#B04468" stop-opacity="0"/></linearGradient>
<clipPath id="r"><rect width="1200" height="420" rx="28"/></clipPath>
</defs>
<style>
.t{font-family:FONT}
@keyframes rise{from{opacity:0;transform:translateY(16px)}to{opacity:1;transform:translateY(0)}}
@keyframes d1{0%,100%{transform:translate(0,0)}50%{transform:translate(70px,30px)}}
@keyframes d2{0%,100%{transform:translate(0,0)}50%{transform:translate(-60px,-25px)}}
@keyframes flow{to{stroke-dashoffset:-730}}
@keyframes flow2{to{stroke-dashoffset:482}}
@keyframes float{0%,100%{transform:translateY(0)}50%{transform:translateY(-9px)}}
@keyframes ecg{0%{stroke-dashoffset:1400;opacity:1}65%{stroke-dashoffset:0;opacity:1}90%,100%{stroke-dashoffset:0;opacity:0}}
@keyframes tw{0%,100%{opacity:.2}50%{opacity:.9}}
.rise{animation:rise 1s cubic-bezier(.2,.8,.2,1) both}
</style>
<g clip-path="url(#r)">
<rect width="1200" height="420" fill="url(#bg)"/>
<circle cx="180" cy="90" r="230" fill="url(#b1)" style="animation:d1 12s ease-in-out infinite"/>
<circle cx="1050" cy="330" r="260" fill="url(#b2)" style="animation:d2 14s ease-in-out infinite"/>
<g fill="#B04468">
<circle cx="130" cy="300" r="4" style="animation:tw 3s infinite"/><circle cx="260" cy="120" r="3" style="animation:tw 4s .8s infinite"/>
<circle cx="980" cy="110" r="4" style="animation:tw 3.5s .3s infinite"/><circle cx="1090" cy="230" r="3" style="animation:tw 4.5s 1.2s infinite"/>
<circle cx="880" cy="60" r="2.5" style="animation:tw 3s 1.6s infinite"/><circle cx="330" cy="330" r="2.5" style="animation:tw 5s .5s infinite"/>
</g>
<g transform="translate(600,132)"><g style="animation:float 6s ease-in-out infinite">
<g transform="translate(14,28) rotate(-32)" fill="none" stroke-linecap="round">
<ellipse rx="118" ry="52" stroke="url(#ring)" stroke-width="13" stroke-dasharray="430 300" style="animation:flow 6s linear infinite"/>
<ellipse rx="102" ry="42" stroke="#C8577A" stroke-opacity=".7" stroke-width="5" stroke-dasharray="220 262" style="animation:flow2 7s linear infinite"/>
</g>
<g transform="translate(-22,-28)"><rect x="-26" y="-62" width="52" height="124" rx="11" fill="url(#cross)"/><rect x="-62" y="-26" width="124" height="52" rx="11" fill="url(#cross)"/></g>
</g></g>
<text class="t rise" x="600" y="322" text-anchor="middle" font-size="66" font-weight="700" style="animation-delay:.3s"><tspan fill="#6E1A42">Medi</tspan><tspan fill="#C8577A" dx="14">guard</tspan></text>
<text class="t rise" x="600" y="360" text-anchor="middle" font-size="19" font-weight="500" fill="#8A2A56" letter-spacing="1.5" style="animation-delay:.9s">Caretaker manages  ·  Patient taps  ·  Doctor understands</text>
<path d="M0,396 H420 L440,396 L456,372 L474,414 L494,352 L512,396 L532,396 H1200" fill="none" stroke="url(#ecg)" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="1400" style="animation:ecg 5s ease-in-out infinite"/>
</g></svg>""".replace("FONT", FONT)
open(f"{A}/header.svg","w").write(header)

# ---------------- DIVIDER ----------------
divider = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 50" width="1200" height="50">
<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#B04468" stop-opacity="0"/><stop offset=".5" stop-color="#B04468"/><stop offset="1" stop-color="#B04468" stop-opacity="0"/></linearGradient></defs>
<style>
@keyframes beat{0%,100%{transform:scale(1)}15%{transform:scale(1.25)}30%{transform:scale(1)}45%{transform:scale(1.15)}}
@keyframes trace{0%{stroke-dashoffset:300}60%,100%{stroke-dashoffset:0}}
.c{transform-box:fill-box;transform-origin:center;animation:beat 2.4s ease-in-out infinite}
</style>
<path d="M0,25 H520 L540,25 L552,12 L566,38 L580,25 H600" fill="none" stroke="url(#g)" stroke-width="2" opacity=".35"/>
<path d="M600,25 H620 L634,25 L646,12 L660,38 L672,25 H1200" fill="none" stroke="url(#g)" stroke-width="2" opacity=".35"/>
<path d="M0,25 H520 L540,25 L552,12 L566,38 L580,25 H620 L634,25 L646,12 L660,38 L672,25 H1200" fill="none" stroke="#C8577A" stroke-width="2.5" stroke-linecap="round" stroke-dasharray="300 900" style="animation:trace 0s"/>
<g class="c"><rect x="594" y="13" width="12" height="24" rx="3" fill="#8A2A56"/><rect x="588" y="19" width="24" height="12" rx="3" fill="#D9788F"/></g>
</svg>"""
open(f"{A}/divider.svg","w").write(divider)

# ---------------- NAV PILLS ----------------
items = ["Overview","Roles","Features","Workflow","Architecture","Roadmap","Setup"]
for i,name in enumerate(items):
    w = int(34 + len(name)*10.5); h = 42
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
<defs><linearGradient id="p" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#7A1E48"/><stop offset="1" stop-color="#B84F72"/></linearGradient>
<clipPath id="c"><rect x="1" y="1" width="{w-2}" height="{h-2}" rx="{(h-2)//2}"/></clipPath></defs>
<style>@keyframes sh{{0%{{transform:translateX(-50px) skewX(-20deg)}}55%,100%{{transform:translateX({w+50}px) skewX(-20deg)}}}}
.s{{animation:sh {3.6+i*0.25:.2f}s ease-in-out {i*0.35:.2f}s infinite}}</style>
<rect x="1" y="1" width="{w-2}" height="{h-2}" rx="{(h-2)//2}" fill="url(#p)"/>
<g clip-path="url(#c)"><rect class="s" x="0" y="0" width="26" height="{h}" fill="#fff" opacity=".28"/></g>
<text x="{w/2}" y="{h/2+5.5}" text-anchor="middle" font-family="{FONT}" font-size="15" font-weight="600" fill="#fff">{name}</text></svg>"""
    open(f"{A}/nav-{name.lower()}.svg","w").write(svg)

# ---------------- WORKFLOW ----------------
xs = [100,300,500,700,900]
labels = ["Caretaker sets up","Alarm rings","Patient taps","Everything syncs","Doctor sees it"]
subs = ["photo · dose · schedule","photo + message + voice","tick or voice reply","offline-first, nothing lost","calendar · charts · trends"]
icons = [
 lambda x: f'<circle cx="{x}" cy="92" r="8" fill="#7A1E48"/><path d="M{x-15},118 a15,15 0 0 1 30,0 z" fill="#7A1E48"/>',
 lambda x: f'<circle cx="{x}" cy="100" r="16" fill="none" stroke="#7A1E48" stroke-width="3"/><line x1="{x}" y1="100" x2="{x}" y2="89" stroke="#7A1E48" stroke-width="3" stroke-linecap="round"/><line x1="{x}" y1="100" x2="{x+8}" y2="105" stroke="#C8577A" stroke-width="3" stroke-linecap="round"><animateTransform attributeName="transform" type="rotate" from="0 {x} 100" to="360 {x} 100" dur="6s" repeatCount="indefinite"/></line>',
 lambda x: f'<path d="M{x-16},101 l11,11 l21,-24" fill="none" stroke="#7A1E48" stroke-width="7" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="60" class="tick"/>',
 lambda x: f'<g><path d="M{x+15},100 a15,15 0 1 1 -6,-12" fill="none" stroke="#7A1E48" stroke-width="4" stroke-linecap="round"/><path d="M{x+2},84 l10,2 l-4,9 z" fill="#7A1E48"/><animateTransform attributeName="transform" type="rotate" from="0 {x} 100" to="360 {x} 100" dur="5s" repeatCount="indefinite"/></g>',
 lambda x: f'<g fill="#7A1E48"><rect class="bar" style="animation-delay:0s" x="{x-17}" y="106" width="9" height="12" rx="2"/><rect class="bar" style="animation-delay:.4s" x="{x-4}" y="94" width="9" height="24" rx="2" fill="#C8577A"/><rect class="bar" style="animation-delay:.8s" x="{x+9}" y="82" width="9" height="36" rx="2"/></g>',
]
nodes = ""
for i,x in enumerate(xs):
    nodes += f"""<g>
<circle class="ping" style="animation-delay:{i*1.2}s" cx="{x}" cy="100" r="40" fill="none" stroke="#C8577A" stroke-width="3"/>
<circle cx="{x}" cy="100" r="40" fill="#FBF5FB" stroke="#A63D62" stroke-width="3"/>
{icons[i](x)}
<text x="{x}" y="176" text-anchor="middle" class="t" font-size="17" font-weight="700" fill="#6E1A42">{labels[i]}</text>
<text x="{x}" y="199" text-anchor="middle" class="t" font-size="13" fill="#8A2A56">{subs[i]}</text></g>"""
workflow = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 250" width="1000" height="250" role="img" aria-label="MediGuard workflow">
<defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#F6EEF6"/><stop offset="1" stop-color="#E9D8EA"/></linearGradient></defs>
<style>
.t{{font-family:{FONT}}}
@keyframes flow{{to{{stroke-dashoffset:-36}}}}
@keyframes ping{{0%{{opacity:.85;transform:scale(1)}}16%{{opacity:0;transform:scale(1.7)}}100%{{opacity:0;transform:scale(1.7)}}}}
@keyframes bar{{0%,100%{{transform:scaleY(1)}}50%{{transform:scaleY(.45)}}}}
@keyframes tick{{0%{{stroke-dashoffset:60}}40%,100%{{stroke-dashoffset:0}}}}
.ping{{opacity:0;transform-box:fill-box;transform-origin:center;animation:ping 6s ease-out infinite}}
.bar{{transform-box:fill-box;transform-origin:50% 100%;animation:bar 2.4s ease-in-out infinite}}
.tick{{animation:tick 2.4s ease-in-out infinite}}
</style>
<rect width="1000" height="250" rx="24" fill="url(#bg)"/>
<line x1="140" y1="100" x2="860" y2="100" stroke="#C8577A" stroke-width="3" stroke-dasharray="8 10" stroke-linecap="round" style="animation:flow 1.2s linear infinite"/>
{nodes}
</svg>"""
open(f"{A}/workflow.svg","w").write(workflow)
print("ok")
