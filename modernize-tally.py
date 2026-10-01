#!/usr/bin/env python3
"""Modernize tallymobilemechanic.com page markup (round 2 redesign, 2026-10-01).

Pairs with css/modern.css (loaded LAST, every rule scoped under body.tm). Presentation only:
titles, meta, canonicals, H1s, JSON-LD, body copy, phone links, form fields and endpoints and
scripts are left as they are. What it does:
  - versions the existing stylesheet links (?v=20261001r2), adds Outfit / DM Sans and css/modern.css
  - body class "tm tm-<kind>" (home, service, location, post, hub, page, util)
  - emoji and dingbat glyphs become solid inline SVG icons (Costa: emoji never allowed)
  - hotlinked Unsplash photos are served locally from /images/site/u-<id>.jpg
  - photo heroes (--hero-img), home hero side image dropped for a full-bleed photo
  - presentational inline styles replaced by classes (display:none styles are kept, they are
    behaviour: form success/error boxes and honeypots)
  - FAQ accordions become native <details>
  - detail pages: feature photo moves into the article column, aside becomes a sticky panel
  - defect fix: the eight service-page forms had a required "Service Needed" select with no
    options (the form could not be submitted); it gets the same options as the contact form
  - nav gains a Service Areas link (/locations/ was only reachable from the footer)
Idempotent: a page whose <body> already carries class "tm" is skipped.
_build_pages.py is the March generator; it is stale (old path, placeholder phones) and the pages
are no longer generated from it. If it is ever rerun, rerun this script after it.

usage: python3 modernize-tally.py [repo-root]
"""
import os, re, sys, glob

ROOT = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.abspath(__file__))
V = '20261001r2'

# solid icons (heroicons 20 solid), inlined so the repo does not depend on the main tools dir
BOLT = '<svg class="tm-i" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true"><path d="M11.983 1.907a.75.75 0 0 0-1.292-.657l-8.5 9.5A.75.75 0 0 0 2.75 12h6.572l-1.305 6.093a.75.75 0 0 0 1.292.657l8.5-9.5A.75.75 0 0 0 17.25 8h-6.572l1.305-6.093Z"/></svg>'
STAR = '<svg class="tm-i" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true"><path fill-rule="evenodd" d="M10.868 2.884c-.321-.772-1.415-.772-1.736 0l-1.83 4.401-4.753.381c-.833.067-1.171 1.107-.536 1.651l3.62 3.102-1.106 4.637c-.194.813.691 1.456 1.405 1.02L10 15.591l4.069 2.485c.713.436 1.598-.207 1.404-1.02l-1.106-4.637 3.62-3.102c.635-.544.297-1.584-.536-1.65l-4.752-.382-1.831-4.401Z" clip-rule="evenodd"/></svg>'
CHECK = '<svg class="tm-i" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true"><path fill-rule="evenodd" d="M10 18a8 8 0 1 0 0-16 8 8 0 0 0 0 16Zm3.857-9.809a.75.75 0 0 0-1.214-.882l-3.483 4.79-1.88-1.88a.75.75 0 1 0-1.06 1.061l2.5 2.5a.75.75 0 0 0 1.137-.089l4-5.5Z" clip-rule="evenodd"/></svg>'
PHONE = '<svg class="tm-i" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true"><path fill-rule="evenodd" d="M2 3.5A1.5 1.5 0 0 1 3.5 2h1.148a1.5 1.5 0 0 1 1.465 1.175l.513 2.31a1.5 1.5 0 0 1-1.02 1.756l-.97.322a11.04 11.04 0 0 0 6.302 6.302l.322-.97a1.5 1.5 0 0 1 1.756-1.02l2.31.513A1.5 1.5 0 0 1 18 12.352V13.5a1.5 1.5 0 0 1-1.5 1.5H15c-7.18 0-13-5.82-13-13V3.5Z" clip-rule="evenodd"/></svg>'
GLYPH = {'\u26a1': BOLT, '\u2605': STAR, '\u2713': CHECK}
ANY_EMOJI = re.compile('[\U0001F000-\U0001FAFF\u2600-\u27bf\u2b00-\u2bff\u2300-\u23ff]\ufe0f?')

SERVICE_OPTIONS = ('<option value="">Select a service…</option><option>Brake Repair</option><option>Oil Change</option>'
                   '<option>Battery Replacement</option><option>Check Engine Light / Diagnostics</option>'
                   '<option>Alternator / Starter Repair</option><option>AC Recharge / Repair</option>'
                   '<option>Pre-Purchase Inspection</option><option>Tune-Up</option><option>Other / Not Sure</option>')

HERO = {
    'index.html': 'home-hero', 'services/index.html': 'area-van', 'locations/index.html': 'rural-road',
    'services/brake-repair.html': 'u-1645445522156-9ac06bc7a767', 'services/oil-change.html': 'u-1487754180451-c456f719a1fc',
    'services/battery-replacement.html': 'svc-battery', 'services/diagnostic-service.html': 'svc-diagnostic',
    'services/alternator-repair.html': 'svc-alternator', 'services/pre-purchase-inspection.html': 'svc-inspection',
    'services/ac-recharge.html': 'svc-ac', 'services/tune-up.html': 'svc-tune-up',
    'locations/crawfordville-fl.html': 'rural-road', 'locations/havana-fl.html': 'area-van',
    'locations/midway-fl.html': 'u-1603175922978-b10e84330c35', 'locations/monticello-fl.html': 'area-van',
    'locations/quincy-fl.html': 'rural-road', 'locations/woodville-fl.html': 'u-1603175922978-b10e84330c35',
    'about.html': 'area-van', 'contact.html': 'u-1603175922978-b10e84330c35', 'faq.html': 'u-1632733711679-529326f6db12',
    'pricing.html': 'u-1486262715619-67b85e0b08d3', 'blog/index.html': 'u-1625047509248-ec889cbff17f',
    'privacy-policy.html': 'u-1486262715619-67b85e0b08d3', 'terms-of-service.html': 'u-1486262715619-67b85e0b08d3',
    'sitemap.html': 'u-1486262715619-67b85e0b08d3',
}

def kind_of(rel):
    if rel == 'index.html': return 'home'
    if rel in ('404.html', 'thank-you.html'): return 'util'
    if rel.endswith('/index.html'): return 'hub'
    if rel.startswith('services/'): return 'service'
    if rel.startswith('locations/'): return 'location'
    if rel.startswith('blog/'): return 'post'
    return 'page'

def add_class(tag, cls):
    if 'class="' in tag: return tag.replace('class="', f'class="{cls} ', 1)
    return tag.replace('>', f' class="{cls}">', 1) if not tag.endswith('/>') else tag[:-2] + f' class="{cls}"/>'

# inline-style signature -> class (matched on the style value), applied before styles are stripped
SIG = [
    (r'display:grid;grid-template-columns:1fr;gap:2\.5rem;', 'tm-detail'),
    (r'display:grid;grid-template-columns:1fr;gap:3rem;max-width:960px', 'tm-contact'),
    (r'display:grid;grid-template-columns:1fr;gap:3rem;$', 'tm-detail'),
    (r'background:var\(--color-surface\);border-radius:var\(--radius-lg\);padding:1\.75rem;margin-top:3rem', 'tm-panel tm-post-cta'),
    (r'background:var\(--color-surface\);border-radius:var\(--radius-lg\);padding:2rem;margin-top:3rem;border:2px solid', 'tm-note'),
    (r'background:var\(--color-surface\);border-radius:var\(--radius-lg\);padding:1\.75rem', 'tm-panel'),
    (r'margin-top:3rem;padding:1\.5rem;background:var\(--color-surface\)', 'tm-panel'),
    (r'max-height:(380|360|340|300)px', 'tm-feature-img'),
    (r'max-height:(280|260)px', 'tm-aside-img'),
    (r'^margin-top:2\.5rem;$', 'tm-more'),
    (r'max-width:800px;margin:0 auto 2\.5rem', 'tm-lede'),
    (r'^max-width:800px;margin:0 auto;$', 'tm-narrow'),
    (r'grid-template-columns:repeat\(auto-fit,minmax\(280px,1fr\)\);gap:24px', 'tm-reviews'),
    (r'^background:white;border-radius:12px;padding:28px', 'tm-review'),
    (r'font-style:italic;color:#374151', 'tm-review__quote'),
    (r'^font-weight:600;color:var\(--primary\);$', 'tm-review__by'),
    (r'^color:#64748b;font-weight:400;$', 'tm-review__place'),
    (r'^background:#f8fafc;$', 'tm-reviews-band'),
    (r'background:var\(--surface,#f8fafc\);border-radius:12px;padding:2rem', 'tm-price-card'),
    (r'list-style:none;padding:0;margin:0;display:grid;gap:0\.65rem', 'tm-price-list'),
    (r'white-space:nowrap;flex-shrink:0;margin-left:1rem', 'tm-price'),
    (r'grid-template-columns:repeat\(auto-fit,minmax\(220px,1fr\)\);gap:1rem', 'tm-mini-grid'),
    (r'background:var\(--surface,#f8fafc\);border-radius:10px;padding:1\.25rem', 'tm-mini'),
    (r'background:var\(--color-dark-bg, #0f172a\)', 'tm-stats-band'),
    (r'minmax\(160px,1fr\)\);gap:2rem;text-align:center', 'tm-stat-grid'),
    (r'font-size:2\.5rem;font-weight:800', 'tm-stat-num'),
    (r'^color:var\(--color-text-muted\);margin:0\.25rem 0 0;font-size:0\.9rem;$', 'tm-stat-label'),
    (r'list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:0\.(5|4)rem', 'tm-links'),
    (r'repeat\(auto-fill,minmax\(200px,1fr\)\);gap:2rem', 'tm-sitemap'),
    (r'^margin-top:1rem;font-size:0\.875rem;color:var\(--color-accent\);font-weight:700;$', 'tm-from'),
    (r'^font-size:0\.78rem;color:var\(--color-text-muted\);$', 'tm-fine'),
    (r'^color:rgba\(255,255,255,0\.6\);font-size:0\.875rem;margin:0;$', 'tm-meta'),
    (r'display:inline-flex;(align-items:center;gap:0\.5rem;)?background:var\(--color-accent\);color:#fff;padding:0\.6rem 1rem', 'tm-footer-call'),
    (r'^max-width:760px;margin:0 auto;$', 'tm-legal'),
]

def classify_and_strip(seg):
    """Add classes for known inline-style signatures, then drop presentational inline styles."""
    def fix(m):
        tag, style = m.group(0), m.group(2)
        if 'display:none' in style.replace(' ', ''):
            return tag  # behaviour, not presentation
        for pat, cls in SIG:
            if re.search(pat, style):
                tag = add_class(tag, cls)
                break
        return re.sub(r'\s+style="[^"]*"', '', tag, count=1)
    return re.sub(r'<([a-z0-9]+)\b[^>]*?\sstyle="([^"]*)"[^>]*>', fix, seg)

def faq_to_details(body):
    pat = re.compile(r'<div class="faq-item"[^>]*>\s*<button class="faq-item__trigger"[^>]*>\s*(.*?)\s*'
                     r'<svg class="faq-item__icon".*?</svg>\s*</button>\s*'
                     r'<div class="faq-item__body"(?: id="([^"]*)")?[^>]*>(.*?)</div>\s*</div>', re.S)
    def rep(m):
        q, fid, a = m.group(1).strip(), m.group(2), m.group(3).strip()
        idattr = f' id="{fid}"' if fid else ''
        return f'<details class="tm-faq"><summary>{q}</summary><div class="tm-faq-a"{idattr}>{a}</div></details>'
    body = pat.sub(rep, body)
    body = re.sub(r'<div class="faq-list" role="list"', '<div class="faq-list"', body)
    return body

def localise_images(s):
    return re.sub(r'https://images\.unsplash\.com/photo-([0-9a-f-]+)\?w=\d+&(?:amp;)?q=\d+', r'/images/site/u-\1.jpg', s)

def transform(path):
    rel = os.path.relpath(path, ROOT)
    html = open(path, encoding='utf-8').read()
    if re.search(r'<body[^>]*class="[^"]*\btm\b', html): return 'skip (already modern)'
    kind = kind_of(rel)
    head, body = html.split('<body', 1)

    # stylesheets: version the old trio, add fonts + modern.css last
    head = re.sub(r'(href="/?(?:\.\./)?css/(?:styles\.v1|style\.v2\.5|site-theme)\.css)(?:\?v=[^"]*)?"', rf'\1?v={V}"', head)
    head = head.replace('</head>', '  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Outfit:wght@600;700;800&family=DM+Sans:wght@400;500;600;700;800&display=swap">\n'
                        f'  <link rel="stylesheet" href="/css/modern.css?v={V}">\n</head>', 1)

    body = re.sub(r'^([^>]*)>', lambda m: (m.group(1).replace('class="', f'class="tm tm-{kind} ') if 'class="' in m.group(1)
                                           else m.group(1) + f' class="tm tm-{kind}"') + '>', body, count=1)
    # split off scripts so nothing inside them is touched
    parts = re.split(r'(<script\b.*?</script>)', body, flags=re.S)
    for i in range(0, len(parts), 2):
        seg = parts[i]
        seg = localise_images(seg)
        for g, svg in GLYPH.items(): seg = seg.replace(g + ' ', svg + ' ').replace(g, svg)
        left = ANY_EMOJI.findall(seg)
        if left: raise SystemExit(f'{rel}: unmapped glyph {set(left)}')
        if kind == 'util':
            # 404 / thank-you: keep their own centred inline layout, only fix the header/footer bits
            seg = re.sub(r'(<footer.*?</footer>)', lambda m: classify_and_strip(m.group(1)), seg, flags=re.S)
        else:
            seg = classify_and_strip(seg)
        parts[i] = seg
    body = ''.join(parts)

    # nav: Service Areas link, phone icon
    body = body.replace('<li><a href="/about.html">About</a></li>', '<li><a href="/locations/">Service Areas</a></li>\n        <li><a href="/about.html">About</a></li>', 1)
    body = body.replace('<a href="tel:8507263411" class="nav-phone">', f'<a href="tel:8507263411" class="nav-phone">{PHONE}', 1)
    # breadcrumbs
    body = body.replace('<nav aria-label="breadcrumb">', '<nav aria-label="breadcrumb" class="tm-crumbs">')

    # heroes
    img = HERO.get(rel)
    if kind == 'home':
        body = re.sub(r'\s*<div class="hero-split__image-wrap".*?<div class="hero-split__image-overlay"></div>\s*</div>', '', body, count=1, flags=re.S)
        body = body.replace('<section class="hero-split"', f'<section class="hero-split" style="--hero-img:url(/images/site/{img}.jpg)"', 1)
        body = re.sub(r'<section aria-hidden="true">\s*<div>', '<section class="tm-strip" aria-hidden="true">\n      <div class="tm-strip__grid">', body, count=1)
    elif kind == 'post':
        m = re.search(r'<img src="/images/site/(u-[0-9a-f-]+)\.jpg"', body)
        img = img or (m.group(1) if m else 'home-hero')
    if img and kind != 'home':
        body = body.replace('<div class="inner-hero">', f'<div class="inner-hero" style="--hero-img:url(/images/site/{img}.jpg)">', 1)

    # FAQ
    body = faq_to_details(body)

    # detail pages: feature photo moves into the article column
    body = re.sub(r'(<img [^>]*class="tm-feature-img"[^>]*>)\s*(<div class="tm-detail">\s*<div class="prose">)', r'\2\1', body)
    # hubs keep the photo above the prose but in a centred column
    body = re.sub(r'<div class="tm-detail">(\s*<div>\s*<img [^>]*tm-feature-img)', r'<div class="tm-hub-intro">\1', body)

    # defect: empty required service select on service-page forms
    body = body.replace('<select id="service" name="service" required><option value="" disabled selected>Select one…</option></select>',
                        f'<select id="service" name="service" required>{SERVICE_OPTIONS}</select>')

    left = ANY_EMOJI.findall(re.sub(r'<script\b.*?</script>', '', body, flags=re.S))
    if left: raise SystemExit(f'{rel}: emoji left {set(left)}')
    open(path, 'w', encoding='utf-8').write(head + '<body' + body)
    return f'ok ({kind})'

SKIP = ('lead/', 'leads/', 'lead-claimed/', 'job/', '.git/', 'estimate/')
for f in sorted(glob.glob(os.path.join(ROOT, '**', '*.html'), recursive=True)):
    rel = os.path.relpath(f, ROOT)
    if rel.startswith(SKIP): continue
    print(rel, transform(f))

# estimate: form page, only glyphs (none at time of writing) and the stylesheet version
EST_CSS = '@media(hover:none){.nav__cta,.nav__logo{min-height:44px;display:inline-flex;align-items:center}.check-item{min-height:48px}.check-item input[type=checkbox]{-webkit-appearance:none;appearance:none;width:22px;min-width:22px;height:40px;border-radius:0;background:url("data:image/svg+xml,%3Csvg xmlns=\'http://www.w3.org/2000/svg\' viewBox=\'0 0 22 22\'%3E%3Crect x=\'1\' y=\'1\' width=\'20\' height=\'20\' rx=\'5\' fill=\'white\' stroke=\'%2394a3b8\' stroke-width=\'1.5\'/%3E%3C/svg%3E") center/22px 22px no-repeat}.check-item input[type=checkbox]:checked{background-image:url("data:image/svg+xml,%3Csvg xmlns=\'http://www.w3.org/2000/svg\' viewBox=\'0 0 22 22\'%3E%3Crect x=\'1\' y=\'1\' width=\'20\' height=\'20\' rx=\'5\' fill=\'%23f97316\' stroke=\'%23f97316\' stroke-width=\'1.5\'/%3E%3Cpath d=\'M6 11.5l3.2 3.2L16 8\' fill=\'none\' stroke=\'white\' stroke-width=\'2.4\' stroke-linecap=\'round\' stroke-linejoin=\'round\'/%3E%3C/svg%3E")}.check-item input[type=checkbox]:focus-visible{outline:2px solid #f97316;outline-offset:2px}.footer a{display:inline-flex;align-items:center;min-height:44px}}@media(max-width:430px){.footer,.footer p{font-size:14px}.check-item span{font-size:.875rem}}\n'
est = os.path.join(ROOT, 'estimate', 'index.html')
if os.path.exists(est):
    h = open(est, encoding='utf-8').read()
    n = h
    for g, svg in GLYPH.items(): n = n.replace(g, svg.replace('class="tm-i"', 'width="16" height="16" style="vertical-align:-3px"'))
    # brand: the logo said "Mobile Pro"; one brand per site
    n = n.replace('<div class="nav__logo">Mobile <span>Pro</span></div>', '<a href="/" class="nav__logo">Tallahassee <span>Mobile Mechanic</span></a>')
    # phone + tablet: 44px tap targets (checkboxes drawn at 22px inside a 40px hit area), 14px minimum text
    if '@media(hover:none){.nav__cta' not in n:
        n = n.replace('</style>', EST_CSS + '\n</style>', 1)
    if n != h: open(est, 'w', encoding='utf-8').write(n); print('estimate/index.html updated')
