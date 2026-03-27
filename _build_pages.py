#!/usr/bin/env python3
"""Build all remaining pages for Tallahassee Mobile Mechanic site."""

import os

BASE = "/Users/costa.demetral/Documents/Rank and Rent $/My-RR-Sites/tallahassee-mobile-mechanic"

NAV = """<header id="site-header">
    <nav class="nav-container" aria-label="Main navigation">
      <a href="/" class="nav-logo"><div class="nav-logo-icon" aria-hidden="true"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="3"/><path d="M19.071 4.929a10 10 0 1 0 0 14.142M13 5l-4 7h6l-4 7"/></svg></div><span class="nav-logo-text">Tallahassee Mobile Mechanic</span></a>
      <ul class="nav-links" id="nav-links" role="list">
        <li><a href="/">Home</a></li>
        <li class="nav-dropdown"><a href="/services/" aria-haspopup="true" aria-expanded="false">Services <svg class="nav-chevron" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg></a><ul class="nav-dropdown-menu" role="menu"><li role="none"><a href="/services/brake-repair.html" role="menuitem">Brake Repair</a></li><li role="none"><a href="/services/oil-change.html" role="menuitem">Oil Change</a></li><li role="none"><a href="/services/battery-replacement.html" role="menuitem">Battery Replacement</a></li><li role="none"><a href="/services/diagnostic-service.html" role="menuitem">Diagnostics</a></li><li role="none"><a href="/services/alternator-repair.html" role="menuitem">Alternator Repair</a></li><li role="none"><a href="/services/pre-purchase-inspection.html" role="menuitem">Pre-Purchase Inspection</a></li><li role="none"><a href="/services/ac-recharge.html" role="menuitem">AC Recharge</a></li><li role="none"><a href="/services/tune-up.html" role="menuitem">Tune-Up</a></li></ul></li>
        <li><a href="/locations/">Locations</a></li>
        <li><a href="/about.html">About</a></li>
        <li><a href="/pricing.html">Pricing</a></li>
        <li><a href="/blog/">Blog</a></li>
        <li><a href="/contact.html">Contact</a></li>
      </ul>
      <div class="nav-actions"><a href="tel:XXXXXXXXXX" class="nav-phone">(XXX) 555-XXXX</a><a href="/contact.html" class="nav-cta-btn">Get a Quote</a></div>
      <button class="nav-hamburger" id="nav-hamburger" aria-label="Toggle navigation" aria-expanded="false" aria-controls="nav-links"><span></span><span></span><span></span></button>
    </nav>
  </header>"""

FOOTER = """<footer class="site-footer">
    <div class="container">
      <div class="footer__grid">
        <div class="footer__brand"><a href="/" class="nav-logo"><div class="nav-logo-icon" aria-hidden="true"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="3"/><path d="M19.071 4.929a10 10 0 1 0 0 14.142M13 5l-4 7h6l-4 7"/></svg></div><span class="nav-logo-text">Tallahassee Mobile Mechanic</span></a><p class="footer__tagline">We Come to You — Fast, Fair, and On Your Turf.</p></div>
        <div><p class="footer__heading">Services</p><ul class="footer__links"><li><a href="/services/brake-repair.html">Brake Repair</a></li><li><a href="/services/oil-change.html">Oil Change</a></li><li><a href="/services/battery-replacement.html">Battery Replacement</a></li><li><a href="/services/diagnostic-service.html">Diagnostics</a></li><li><a href="/services/alternator-repair.html">Alternator Repair</a></li><li><a href="/services/ac-recharge.html">AC Recharge</a></li></ul></div>
        <div><p class="footer__heading">Company</p><ul class="footer__links"><li><a href="/about.html">About Us</a></li><li><a href="/pricing.html">Pricing</a></li><li><a href="/faq.html">FAQ</a></li><li><a href="/blog/">Blog</a></li><li><a href="/locations/">Locations</a></li><li><a href="/contact.html">Contact</a></li></ul></div>
        <div><p class="footer__heading">Hours</p><div class="footer__contact-item"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg><span>Mon-Fri: 7am-7pm<br>Sat: 8am-5pm<br>Sun: Emergency only</span></div><a href="tel:XXXXXXXXXX" style="display:inline-flex;align-items:center;gap:0.5rem;background:var(--color-accent);color:#fff;padding:0.6rem 1rem;border-radius:6px;font-weight:700;font-size:0.875rem;text-decoration:none;margin-top:1rem;">Call (XXX) 555-XXXX</a></div>
      </div>
      <div class="footer__bottom"><span>&copy; 2026 Tallahassee Mobile Mechanic. All rights reserved.</span><div class="footer__bottom-links"><a href="/privacy-policy.html">Privacy Policy</a><a href="/terms-of-service.html">Terms of Service</a><a href="/sitemap.html">Sitemap</a></div></div>
    </div>
  </footer>
  <div class="mobile-cta-bar"><a href="tel:XXXXXXXXXX" class="btn btn--primary"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07A19.5 19.5 0 0 1 4.11 15 19.79 19.79 0 0 1 1.04 6.34 2 2 0 0 1 3 4.11h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"/></svg>Call Now</a><a href="/contact.html" class="btn btn--secondary">Get a Quote</a></div>
  <script>(function(){var h=document.getElementById('site-header'),b=document.getElementById('nav-hamburger'),n=document.getElementById('nav-links');window.addEventListener('scroll',function(){h.classList.toggle('scrolled',window.scrollY>60);},{passive:true});if(b){b.addEventListener('click',function(){var o=b.getAttribute('aria-expanded')==='true';b.setAttribute('aria-expanded',!o);n.classList.toggle('is-open',!o);});}document.querySelectorAll('.nav-dropdown > a').forEach(function(l){l.addEventListener('click',function(e){if(window.innerWidth<=1023){e.preventDefault();var p=l.parentElement;p.classList.toggle('is-open');l.setAttribute('aria-expanded',p.classList.contains('is-open'));}});});document.addEventListener('click',function(e){if(!h.contains(e.target)){n.classList.remove('is-open');if(b)b.setAttribute('aria-expanded','false');}});document.querySelectorAll('.faq-item__trigger').forEach(function(btn){btn.addEventListener('click',function(){var item=btn.closest('.faq-item');var isOpen=item.classList.contains('is-open');document.querySelectorAll('.faq-item').forEach(function(i){i.classList.remove('is-open');var t=i.querySelector('.faq-item__trigger');if(t)t.setAttribute('aria-expanded','false');});if(!isOpen){item.classList.add('is-open');btn.setAttribute('aria-expanded','true');}});});})();</script>"""

CSS_ROOT = '<link rel="stylesheet" href="css/styles.v1.css">'
CSS_SUB  = '<link rel="stylesheet" href="../css/styles.v1.css">'
FONTS    = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400;12..96,700;12..96,800&family=Nunito+Sans:wght@400;600;700&display=swap" rel="stylesheet">'

def page(title, desc, canonical, css, body, schema="", is_utility=False):
    robots = '<meta name="robots" content="noindex, nofollow">' if is_utility else '<meta name="robots" content="index, follow">'
    og = "" if is_utility else f'''  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:type" content="website">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{desc}">'''
    canon = "" if is_utility else f'  <link rel="canonical" href="{canonical}">'
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{desc}">
{canon}
{og}
  {robots}
  {FONTS}
  {css}
  {schema}
</head>
<body>
  <a class="skip-link" href="#main-content">Skip to main content</a>
  {NAV}
  <main id="main-content">
{body}
  </main>
  {FOOTER}
</body>
</html>"""

# ── about.html ──────────────────────────────────────────────────
about_body = """
    <div class="inner-hero">
      <div class="container">
        <span class="inner-hero__eyebrow">About Us</span>
        <h1>About Tallahassee Mobile Mechanic</h1>
        <p>We started with a simple mission: make quality auto repair accessible to everyone — at your home, your office, or wherever life takes you.</p>
      </div>
    </div>

    <section class="section">
      <div class="container">
        <div class="about-split">
          <div class="about-split__img-wrap">
            <img src="https://images.unsplash.com/photo-1619642751034-765dfdf7c58e?w=800&q=80" alt="Mobile mechanic working on car engine in Tallahassee FL" width="800" height="600" loading="lazy">
          </div>
          <div class="about-split__content">
            <h2>Why We Started</h2>
            <p>Traditional auto shops have a monopoly on convenience — you drop your car off, you wait, you pay, you get it back. But what if you're a single parent who can't be without a car? What if you're a college student at Florida State University with no way to get to a shop? What if you're just too busy?</p>
            <p>That's why Tallahassee Mobile Mechanic exists. We built a mobile operation specifically to serve Tallahassee's diverse community — FSU students, state government workers, families in the suburbs, and everyone in between. No tow truck. No waiting room. No runaround.</p>
            <p>We come to you with a fully stocked service van, professional-grade diagnostic equipment, and the expertise to handle most repairs right on the spot. Most of our jobs are completed in under two hours.</p>
          </div>
        </div>
      </div>
    </section>

    <section class="section section--surface">
      <div class="container">
        <div class="section__header">
          <h2 class="section__title">Our Commitment to Tallahassee</h2>
          <p class="section__subtitle">We're not just passing through — Tallahassee is our home, and we're committed to this community.</p>
        </div>
        <div class="location-features" style="max-width:960px;margin:0 auto;">
          <div class="location-feature">
            <div class="location-feature__icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="12" cy="8" r="6"/><path d="M15.477 12.89L17 22l-5-3-5 3 1.523-9.11"/></svg></div>
            <div><h3>ASE-Certified Mechanics</h3><p>Every technician on our team holds current ASE (Automotive Service Excellence) certifications and completes ongoing training. You're not getting a shade-tree mechanic — you're getting a professional.</p></div>
          </div>
          <div class="location-feature">
            <div class="location-feature__icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg></div>
            <div><h3>Fully Insured Operation</h3><p>We carry full general liability insurance on every job. Your vehicle and property are protected when we work on your car. We stand behind every repair we make.</p></div>
          </div>
          <div class="location-feature">
            <div class="location-feature__icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><line x1="12" y1="1" x2="12" y2="23"/><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg></div>
            <div><h3>Honest, Upfront Pricing</h3><p>We quote before we wrench. Our $79 diagnostic fee is waived when you book the repair. No surprise charges, no hidden fees, no pressure to approve work you don't need.</p></div>
          </div>
          <div class="location-feature">
            <div class="location-feature__icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M20 10c0 6-8 12-8 12S4 16 4 10a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/></svg></div>
            <div><h3>Local Coverage You Can Count On</h3><p>We cover all of Leon County, plus Gadsden County communities like Quincy, Havana, and Midway, and Wakulla County including Crawfordville and Woodville.</p></div>
          </div>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="section__header">
          <h2 class="section__title">What We Believe</h2>
        </div>
        <div style="max-width:760px;margin:0 auto;" class="prose">
          <h2>Convenience Shouldn't Be a Luxury</h2>
          <p>Big chain shops spend millions making it easy for you to drive in and hand over your keys. But what if your car won't start? What if you can't afford a tow? What if you have kids at home and can't spend four hours at a waiting room?</p>
          <p>We believe that professional auto service should come to you — not the other way around. That's why we've invested in a fully equipped mobile operation capable of handling the majority of common vehicle repairs right where your car is parked.</p>
          <h2>Transparency Builds Trust</h2>
          <p>Auto repair has a reputation problem. Too many shops charge for work that wasn't needed, quote low and bill high, or use parts that don't last. We've built our business on the opposite approach. Before we touch your car, we show you exactly what's wrong and exactly what it will cost to fix it. No surprises.</p>
          <h2>Tallahassee Is Our Home</h2>
          <p>We service Tallahassee because we live here. We care about this community — the FSU and FAMU students, the state workers, the families, the small business owners. When your car breaks down, we want to be the first call you make. We'll be there.</p>
          <h2>Our Service Promise</h2>
          <p>Every job we take comes with our commitment to do it right the first time. We use quality OEM and OEM-equivalent parts. We guarantee our workmanship. And we'll never leave you stranded without a solution. Call us at (XXX) 555-XXXX — we're here Mon–Fri 7am–7pm and Saturday 8am–5pm.</p>
        </div>
      </div>
    </section>

    <section class="cta-banner">
      <div class="container">
        <h2 class="cta-banner__title">Ready to Experience Mobile Mechanic Service?</h2>
        <p class="cta-banner__sub">Call us or request a quote online. Same-day service available across Tallahassee.</p>
        <div class="cta-banner__actions">
          <a href="tel:XXXXXXXXXX" class="btn btn--white btn--lg">Call (XXX) 555-XXXX</a>
          <a href="/contact.html" class="btn btn--outline-white btn--lg">Get a Free Quote</a>
        </div>
      </div>
    </section>"""

write_file("about.html", page(
    "About Tallahassee Mobile Mechanic | ASE-Certified Mobile Auto Repair",
    "Learn about Tallahassee Mobile Mechanic — ASE-certified mechanics, fully insured, serving Tallahassee and Leon County with same-day mobile auto repair.",
    "https://tallahasseemobilemechanic.com/about.html",
    CSS_ROOT,
    about_body,
    '<script type="application/ld+json">{"@context":"https://schema.org","@type":"AboutPage","name":"About Tallahassee Mobile Mechanic","url":"https://tallahasseemobilemechanic.com/about.html"}</script>'
))

# ── faq.html ────────────────────────────────────────────────────
faq_body = """
    <div class="inner-hero">
      <div class="container">
        <span class="inner-hero__eyebrow">FAQ</span>
        <h1>Frequently Asked Questions</h1>
        <p>Everything you need to know about mobile mechanic service in Tallahassee, FL.</p>
      </div>
    </div>

    <section class="section">
      <div class="container">
        <div class="faq-list" role="list" style="max-width:800px;margin:0 auto;">

          <h2 style="text-align:center;margin-bottom:1.5rem;font-size:1.4rem;">General Questions</h2>

          <div class="faq-item" role="listitem">
            <button class="faq-item__trigger" aria-expanded="false" aria-controls="fq-1">What is a mobile mechanic? <svg class="faq-item__icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg></button>
            <div class="faq-item__body" id="fq-1"><p>A mobile mechanic is a certified automotive technician who travels to you instead of requiring you to bring your vehicle to a shop. We arrive in a fully equipped service van with the tools, parts, and diagnostic equipment needed to complete most repairs on-site at your home, workplace, or wherever your car is located.</p></div>
          </div>

          <div class="faq-item" role="listitem">
            <button class="faq-item__trigger" aria-expanded="false" aria-controls="fq-2">How fast can you get to me? <svg class="faq-item__icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg></button>
            <div class="faq-item__body" id="fq-2"><p>In the Tallahassee metro area, our typical response time is 1–2 hours. Same-day appointments are available Monday through Saturday, 7 AM–7 PM. For outlying areas like Quincy, Havana, Crawfordville, or Monticello, we can usually reach you within 2–3 hours or schedule a next-day appointment.</p></div>
          </div>

          <div class="faq-item" role="listitem">
            <button class="faq-item__trigger" aria-expanded="false" aria-controls="fq-3">What areas do you serve? <svg class="faq-item__icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg></button>
            <div class="faq-item__body" id="fq-3"><p>We serve all of Tallahassee, including midtown, northeast, northwest, and south Tallahassee neighborhoods. Our service area extends to Midway, Crawfordville, Quincy, Havana, Monticello, and Woodville. We cover all of Leon County, much of Gadsden County, and parts of Wakulla County. Not sure if we come to you? Just call!</p></div>
          </div>

          <div class="faq-item" role="listitem">
            <button class="faq-item__trigger" aria-expanded="false" aria-controls="fq-4">Is mobile mechanic service more expensive than a shop? <svg class="faq-item__icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg></button>
            <div class="faq-item__body" id="fq-4"><p>Our rates are typically comparable to local independent shops — and often cheaper than dealerships. More importantly, you save on towing costs ($75–$150+), you don't lose half a day sitting at a waiting room, and you don't need to arrange a ride. When you factor in total cost of your time and inconvenience, mobile mechanic service is almost always the better value.</p></div>
          </div>

          <div class="faq-item" role="listitem">
            <button class="faq-item__trigger" aria-expanded="false" aria-controls="fq-5">What forms of payment do you accept? <svg class="faq-item__icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg></button>
            <div class="faq-item__body" id="fq-5"><p>We accept cash, all major credit cards, Venmo, and Zelle. Payment is due when the job is completed. We never require upfront payment before service — you pay after the work is done and you're satisfied.</p></div>
          </div>

          <h2 style="text-align:center;margin:2rem 0 1.5rem;font-size:1.4rem;">Services &amp; Pricing</h2>

          <div class="faq-item" role="listitem">
            <button class="faq-item__trigger" aria-expanded="false" aria-controls="fq-6">How much does a diagnostic cost? <svg class="faq-item__icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg></button>
            <div class="faq-item__body" id="fq-6"><p>Our diagnostic fee is $79. This covers a full OBD-II scan, visual inspection, and written estimate. If you book the repair with us, the diagnostic fee is completely waived — making it free when combined with any service. We believe you deserve to know what's wrong before you pay for anything.</p></div>
          </div>

          <div class="faq-item" role="listitem">
            <button class="faq-item__trigger" aria-expanded="false" aria-controls="fq-7">Can you work in apartment parking lots or garages? <svg class="faq-item__icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg></button>
            <div class="faq-item__body" id="fq-7"><p>Yes, in most cases. We can work in parking lots, apartment complexes, and office parking areas as long as there's sufficient space and the ground is reasonably level. Some repairs like brake jobs or undercarriage work may require a jack stand setup, which needs flat ground. We'll let you know before arriving if there's any concern.</p></div>
          </div>

          <div class="faq-item" role="listitem">
            <button class="faq-item__trigger" aria-expanded="false" aria-controls="fq-8">What types of vehicles do you service? <svg class="faq-item__icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg></button>
            <div class="faq-item__body" id="fq-8"><p>We service most domestic and foreign passenger vehicles including cars, trucks, SUVs, and minivans. We work on Ford, Chevy, GMC, Toyota, Honda, Nissan, Hyundai, Kia, Dodge, Jeep, Chrysler, Subaru, Mazda, Volkswagen, and many others. We do not currently service heavy trucks, diesel engines, or exotic/supercar vehicles. Call us to confirm your vehicle.</p></div>
          </div>

          <div class="faq-item" role="listitem">
            <button class="faq-item__trigger" aria-expanded="false" aria-controls="fq-9">Do you guarantee your work? <svg class="faq-item__icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg></button>
            <div class="faq-item__body" id="fq-9"><p>Yes. We stand behind every repair. If a part we installed fails prematurely or the issue recurs due to our workmanship, we'll make it right at no additional charge. We use quality OEM and OEM-equivalent parts on all repairs. Ask us about the specific warranty on your service when you book.</p></div>
          </div>

          <div class="faq-item" role="listitem">
            <button class="faq-item__trigger" aria-expanded="false" aria-controls="fq-10">What services can't be done mobile? <svg class="faq-item__icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg></button>
            <div class="faq-item__body" id="fq-10"><p>Most common repairs can be completed mobile. However, some jobs genuinely require a lift or specialized shop equipment — these include transmission rebuilds, engine rebuilds, major suspension overhauls, or frame work. For these cases, we'll give you an honest assessment and a referral to a trusted local shop. We'd rather tell you the truth than take money for a job we can't do properly in the field.</p></div>
          </div>
        </div>
      </div>
    </section>

    <section class="cta-banner">
      <div class="container">
        <h2 class="cta-banner__title">Still Have Questions? Just Call Us.</h2>
        <p class="cta-banner__sub">We're happy to talk through your situation and give you honest advice — no commitment required.</p>
        <div class="cta-banner__actions">
          <a href="tel:XXXXXXXXXX" class="btn btn--white btn--lg">Call (XXX) 555-XXXX</a>
          <a href="/contact.html" class="btn btn--outline-white btn--lg">Get a Free Quote</a>
        </div>
      </div>
    </section>"""

write_file("faq.html", page(
    "FAQ | Tallahassee Mobile Mechanic | Common Questions Answered",
    "Answers to the most common questions about mobile mechanic service in Tallahassee FL — pricing, response time, service area, and what to expect.",
    "https://tallahasseemobilemechanic.com/faq.html",
    CSS_ROOT,
    faq_body,
    '<script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":"What is a mobile mechanic?","acceptedAnswer":{"@type":"Answer","text":"A mobile mechanic travels to you with a fully equipped service van to complete most auto repairs on-site at your home, office, or roadside location."}},{"@type":"Question","name":"How much does a diagnostic cost?","acceptedAnswer":{"@type":"Answer","text":"Our diagnostic fee is $79, waived when you book the repair with us."}},{"@type":"Question","name":"What areas do you serve?","acceptedAnswer":{"@type":"Answer","text":"We serve all of Tallahassee plus Midway, Crawfordville, Quincy, Havana, Monticello, Woodville, and surrounding Leon and Gadsden County communities."}}]}</script>'
))

# ── pricing.html ─────────────────────────────────────────────────
pricing_body = """
    <div class="inner-hero">
      <div class="container">
        <span class="inner-hero__eyebrow">Transparent Pricing</span>
        <h1>Mobile Mechanic Pricing in Tallahassee</h1>
        <p>We quote before we wrench. No surprise charges. No hidden fees. Diagnostic fee waived when you book a repair.</p>
      </div>
    </div>

    <section class="section">
      <div class="container">
        <div class="section__header">
          <h2 class="section__title">Service Pricing</h2>
          <p class="section__subtitle">Prices vary by vehicle make, model, and parts cost. These are typical ranges — we provide exact quotes before starting any work.</p>
        </div>

        <div class="pricing-grid">
          <div class="pricing-card">
            <p class="pricing-card__name">Vehicle Diagnostic</p>
            <p class="pricing-card__price">$79 <span>flat fee</span></p>
            <ul class="pricing-card__features">
              <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>Full OBD-II scan</li>
              <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>Visual inspection</li>
              <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>Written estimate</li>
              <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>Waived when repair booked</li>
            </ul>
            <a href="/contact.html" class="btn btn--primary btn--block" style="margin-top:1.5rem;">Book Diagnostic</a>
          </div>

          <div class="pricing-card pricing-card--featured">
            <p class="pricing-card__name">Brake Service</p>
            <p class="pricing-card__price">$149<span>–$350+</span></p>
            <ul class="pricing-card__features">
              <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>Brake pad replacement</li>
              <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>Rotor resurfacing / replacement</li>
              <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>Caliper inspection</li>
              <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>Brake fluid check</li>
            </ul>
            <a href="/contact.html" class="btn btn--primary btn--block" style="margin-top:1.5rem;">Get Brake Quote</a>
          </div>

          <div class="pricing-card">
            <p class="pricing-card__name">Oil Change</p>
            <p class="pricing-card__price">$49<span>–$119</span></p>
            <ul class="pricing-card__features">
              <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>Conventional or synthetic</li>
              <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>Filter replacement included</li>
              <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>Fluid level check</li>
              <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>Done in 30–45 minutes</li>
            </ul>
            <a href="/contact.html" class="btn btn--primary btn--block" style="margin-top:1.5rem;">Book Oil Change</a>
          </div>

          <div class="pricing-card">
            <p class="pricing-card__name">Battery Replacement</p>
            <p class="pricing-card__price">$129<span>–$249</span></p>
            <ul class="pricing-card__features">
              <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>Battery load test included</li>
              <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>OEM-grade replacement battery</li>
              <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>Alternator charging check</li>
              <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>Done in under 1 hour</li>
            </ul>
            <a href="/contact.html" class="btn btn--primary btn--block" style="margin-top:1.5rem;">Book Battery Service</a>
          </div>

          <div class="pricing-card">
            <p class="pricing-card__name">Alternator / Starter</p>
            <p class="pricing-card__price">$299<span>–$850</span></p>
            <ul class="pricing-card__features">
              <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>Charging system diagnosis</li>
              <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>Alternator or starter replacement</li>
              <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>Belt inspection</li>
              <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>Parts + labor included</li>
            </ul>
            <a href="/contact.html" class="btn btn--primary btn--block" style="margin-top:1.5rem;">Get a Quote</a>
          </div>

          <div class="pricing-card">
            <p class="pricing-card__name">Pre-Purchase Inspection</p>
            <p class="pricing-card__price">$99<span>–$149</span></p>
            <ul class="pricing-card__features">
              <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>100+ point inspection</li>
              <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>OBD-II scan included</li>
              <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>Written report provided</li>
              <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>We go to the seller's location</li>
            </ul>
            <a href="/contact.html" class="btn btn--primary btn--block" style="margin-top:1.5rem;">Book Inspection</a>
          </div>
        </div>

        <div style="background:var(--color-surface);border-radius:var(--radius-lg);padding:2rem;margin-top:3rem;border:1px solid var(--color-border);max-width:760px;margin-left:auto;margin-right:auto;margin-top:3rem;">
          <h2 style="font-size:1.3rem;margin-bottom:0.75rem;">Pricing Notes</h2>
          <ul style="color:var(--color-text-muted);line-height:1.8;padding-left:1.25rem;">
            <li>All prices include parts and labor unless noted otherwise</li>
            <li>Exact quote provided before any work begins — no surprises</li>
            <li>Diagnostic fee ($79) is waived when repair is booked</li>
            <li>Prices vary by vehicle make, model, year, and parts availability</li>
            <li>Most jobs completed in 1–3 hours on-site</li>
            <li>We accept Cash, Credit Card, Venmo, and Zelle</li>
          </ul>
        </div>
      </div>
    </section>

    <section class="cta-banner">
      <div class="container">
        <h2 class="cta-banner__title">Get Your Exact Quote Today</h2>
        <p class="cta-banner__sub">Call us or fill out our form and we'll give you a firm quote before scheduling your appointment.</p>
        <div class="cta-banner__actions">
          <a href="tel:XXXXXXXXXX" class="btn btn--white btn--lg">Call (XXX) 555-XXXX</a>
          <a href="/contact.html" class="btn btn--outline-white btn--lg">Request a Quote</a>
        </div>
      </div>
    </section>"""

write_file("pricing.html", page(
    "Mobile Mechanic Pricing Tallahassee FL | Transparent Auto Repair Costs",
    "Honest, upfront mobile mechanic pricing in Tallahassee FL. Brake repair $149+, oil change $49+, battery $129+, diagnostic $79 (waived with repair). Call for exact quote.",
    "https://tallahasseemobilemechanic.com/pricing.html",
    CSS_ROOT,
    pricing_body,
    '<script type="application/ld+json">{"@context":"https://schema.org","@type":"PriceSpecification","name":"Mobile Mechanic Service Pricing","description":"Transparent pricing for mobile auto repair in Tallahassee FL"}</script>'
))

print("Root pages done.")

# ── thank-you.html ──────────────────────────────────────────────
ty_body = """
    <div style="min-height:calc(100vh - 200px);display:flex;align-items:center;justify-content:center;padding:3rem 1.5rem;margin-top:68px;">
      <div style="text-align:center;max-width:520px;">
        <div style="width:80px;height:80px;background:var(--color-accent);border-radius:50%;display:flex;align-items:center;justify-content:center;margin:0 auto 1.5rem;">
          <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        </div>
        <h1 style="font-size:2rem;margin-bottom:0.75rem;color:var(--color-primary);">Thanks — We Got Your Request!</h1>
        <p style="color:var(--color-text-muted);font-size:1.05rem;line-height:1.8;margin-bottom:2rem;">We'll call you back within 1 hour during business hours (Mon–Fri 7am–7pm, Sat 8am–5pm). For faster service, call us directly:</p>
        <a href="tel:XXXXXXXXXX" class="btn btn--primary btn--lg" style="margin-bottom:1rem;"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07A19.5 19.5 0 0 1 4.11 15 19.79 19.79 0 0 1 1.04 6.34 2 2 0 0 1 3 4.11h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"/></svg>Call (XXX) 555-XXXX</a>
        <br>
        <a href="/" style="color:var(--color-text-muted);font-size:0.9rem;">&larr; Back to Home</a>
      </div>
    </div>"""

write_file("thank-you.html", page(
    "Thank You | Tallahassee Mobile Mechanic",
    "Thank you for contacting Tallahassee Mobile Mechanic. We will call you back within one hour.",
    "https://tallahasseemobilemechanic.com/thank-you.html",
    CSS_ROOT,
    ty_body,
    "",
    is_utility=True
))

# ── 404.html ─────────────────────────────────────────────────────
p404_body = """
    <div style="min-height:calc(100vh - 200px);display:flex;align-items:center;justify-content:center;padding:3rem 1.5rem;margin-top:68px;">
      <div style="text-align:center;max-width:520px;">
        <div style="font-family:var(--font-display);font-size:6rem;font-weight:800;color:var(--color-accent);line-height:1;margin-bottom:1rem;">404</div>
        <h1 style="font-size:1.75rem;margin-bottom:0.75rem;">Page Not Found</h1>
        <p style="color:var(--color-text-muted);margin-bottom:2rem;">The page you're looking for doesn't exist or has been moved. Let's get you back on track.</p>
        <div style="display:flex;gap:0.75rem;justify-content:center;flex-wrap:wrap;">
          <a href="/" class="btn btn--primary">Back to Home</a>
          <a href="/contact.html" class="btn btn--outline">Contact Us</a>
        </div>
        <div style="margin-top:3rem;padding:1.5rem;background:var(--color-surface);border-radius:var(--radius-lg);">
          <p style="font-weight:700;margin-bottom:0.5rem;">Need service right now?</p>
          <a href="tel:XXXXXXXXXX" style="color:var(--color-accent);font-weight:700;font-size:1.1rem;text-decoration:none;">Call (XXX) 555-XXXX</a>
        </div>
      </div>
    </div>"""

write_file("404.html", page(
    "404 Page Not Found | Tallahassee Mobile Mechanic",
    "Page not found. Return to the Tallahassee Mobile Mechanic homepage.",
    "https://tallahasseemobilemechanic.com/404.html",
    CSS_ROOT,
    p404_body,
    "",
    is_utility=True
))

# ── sitemap.html ──────────────────────────────────────────────────
sitemap_body = """
    <div class="inner-hero">
      <div class="container">
        <span class="inner-hero__eyebrow">Sitemap</span>
        <h1>Sitemap</h1>
        <p>Find all pages on the Tallahassee Mobile Mechanic website.</p>
      </div>
    </div>
    <section class="section">
      <div class="container" style="max-width:900px;">
        <div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:2rem;">
          <div>
            <h2 style="font-size:1.1rem;color:var(--color-accent);margin-bottom:0.75rem;border-bottom:2px solid var(--color-accent);padding-bottom:0.5rem;">Main Pages</h2>
            <ul style="list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:0.4rem;">
              <li><a href="/">Home</a></li>
              <li><a href="/about.html">About</a></li>
              <li><a href="/contact.html">Contact</a></li>
              <li><a href="/faq.html">FAQ</a></li>
              <li><a href="/pricing.html">Pricing</a></li>
              <li><a href="/privacy-policy.html">Privacy Policy</a></li>
              <li><a href="/terms-of-service.html">Terms of Service</a></li>
            </ul>
          </div>
          <div>
            <h2 style="font-size:1.1rem;color:var(--color-accent);margin-bottom:0.75rem;border-bottom:2px solid var(--color-accent);padding-bottom:0.5rem;">Services</h2>
            <ul style="list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:0.4rem;">
              <li><a href="/services/brake-repair.html">Brake Repair</a></li>
              <li><a href="/services/oil-change.html">Oil Change</a></li>
              <li><a href="/services/battery-replacement.html">Battery Replacement</a></li>
              <li><a href="/services/diagnostic-service.html">Diagnostics</a></li>
              <li><a href="/services/alternator-repair.html">Alternator Repair</a></li>
              <li><a href="/services/pre-purchase-inspection.html">Pre-Purchase Inspection</a></li>
              <li><a href="/services/ac-recharge.html">AC Recharge</a></li>
              <li><a href="/services/tune-up.html">Tune-Up</a></li>
            </ul>
          </div>
          <div>
            <h2 style="font-size:1.1rem;color:var(--color-accent);margin-bottom:0.75rem;border-bottom:2px solid var(--color-accent);padding-bottom:0.5rem;">Locations</h2>
            <ul style="list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:0.4rem;">
              <li><a href="/locations/">All Locations</a></li>
              <li><a href="/locations/midway-fl.html">Midway, FL</a></li>
              <li><a href="/locations/crawfordville-fl.html">Crawfordville, FL</a></li>
              <li><a href="/locations/quincy-fl.html">Quincy, FL</a></li>
              <li><a href="/locations/havana-fl.html">Havana, FL</a></li>
              <li><a href="/locations/monticello-fl.html">Monticello, FL</a></li>
              <li><a href="/locations/woodville-fl.html">Woodville, FL</a></li>
            </ul>
          </div>
          <div>
            <h2 style="font-size:1.1rem;color:var(--color-accent);margin-bottom:0.75rem;border-bottom:2px solid var(--color-accent);padding-bottom:0.5rem;">Blog</h2>
            <ul style="list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:0.4rem;">
              <li><a href="/blog/">All Posts</a></li>
              <li><a href="/blog/how-mobile-mechanic-works.html">How Mobile Mechanics Work</a></li>
              <li><a href="/blog/mobile-mechanic-vs-shop-tallahassee.html">Mobile Mechanic vs Shop</a></li>
              <li><a href="/blog/when-to-call-mobile-mechanic.html">When to Call a Mobile Mechanic</a></li>
              <li><a href="/blog/cost-mobile-mechanic-tallahassee.html">Mobile Mechanic Costs</a></li>
            </ul>
          </div>
        </div>
      </div>
    </section>"""

write_file("sitemap.html", page(
    "Sitemap | Tallahassee Mobile Mechanic",
    "Browse all pages on the Tallahassee Mobile Mechanic website.",
    "https://tallahasseemobilemechanic.com/sitemap.html",
    CSS_ROOT,
    sitemap_body,
    "",
    is_utility=True
))

# ── privacy-policy.html ──────────────────────────────────────────
pp_body = """
    <div class="inner-hero">
      <div class="container"><span class="inner-hero__eyebrow">Legal</span><h1>Privacy Policy</h1><p>Last updated: March 2026</p></div>
    </div>
    <section class="section">
      <div class="container">
        <div class="prose" style="max-width:760px;margin:0 auto;">
          <h2>Introduction</h2>
          <p>Tallahassee Mobile Mechanic ("we," "our," or "us") is committed to protecting your privacy. This Privacy Policy explains how we collect, use, and safeguard your information when you visit our website or use our services.</p>
          <h2>Information We Collect</h2>
          <p>We collect information you voluntarily provide when you contact us, request a quote, or schedule service. This may include your name, phone number, email address, vehicle information, and service location address. We do not collect payment information directly — payments are processed securely through third-party processors.</p>
          <h2>How We Use Your Information</h2>
          <p>We use your information solely to: provide and schedule auto repair services, communicate with you about your service request, send appointment confirmations and follow-ups, and improve our service quality. We do not sell, rent, or share your personal information with third parties for marketing purposes.</p>
          <h2>Contact Forms</h2>
          <p>Our contact form uses Web3Forms to process submissions. Submissions are forwarded to our business email. We retain form submissions for up to 12 months for service records.</p>
          <h2>Cookies</h2>
          <p>Our website may use basic cookies for functionality. We do not use tracking cookies or third-party advertising cookies. You can disable cookies in your browser settings without affecting core site functionality.</p>
          <h2>Data Security</h2>
          <p>We implement reasonable security measures to protect your information. However, no internet transmission is 100% secure. We encourage you to contact us directly at (XXX) 555-XXXX for sensitive matters.</p>
          <h2>Your Rights</h2>
          <p>You may request access to, correction of, or deletion of your personal information at any time by calling (XXX) 555-XXXX. We will respond to your request within 30 days.</p>
          <h2>Changes to This Policy</h2>
          <p>We may update this Privacy Policy occasionally. Changes will be posted on this page with an updated date. Continued use of our services constitutes acceptance of any changes.</p>
          <h2>Contact Us</h2>
          <p>If you have questions about this Privacy Policy, please use our <a href="/contact.html">contact form</a> or call (XXX) 555-XXXX.</p>
        </div>
      </div>
    </section>"""

write_file("privacy-policy.html", page(
    "Privacy Policy | Tallahassee Mobile Mechanic",
    "Privacy Policy for Tallahassee Mobile Mechanic. We protect your personal information and never sell your data.",
    "https://tallahasseemobilemechanic.com/privacy-policy.html",
    CSS_ROOT,
    pp_body,
    "",
    is_utility=True
))

# ── terms-of-service.html ────────────────────────────────────────
tos_body = """
    <div class="inner-hero">
      <div class="container"><span class="inner-hero__eyebrow">Legal</span><h1>Terms of Service</h1><p>Last updated: March 2026</p></div>
    </div>
    <section class="section">
      <div class="container">
        <div class="prose" style="max-width:760px;margin:0 auto;">
          <h2>Agreement to Terms</h2>
          <p>By contacting Tallahassee Mobile Mechanic or using our services, you agree to these Terms of Service. If you do not agree, please do not use our services.</p>
          <h2>Services</h2>
          <p>Tallahassee Mobile Mechanic provides mobile automotive repair and maintenance services in Tallahassee, FL and surrounding areas. We reserve the right to decline any service request at our discretion. Not all repairs can be performed in a mobile setting — we will advise you accordingly before any work begins.</p>
          <h2>Estimates and Pricing</h2>
          <p>All estimates are provided before work begins. Estimates are based on initial assessment and may be revised if additional issues are discovered during repair. We will always notify you of any changes before proceeding. You are not obligated to approve additional work — we will stop and advise you if we discover something beyond the original scope.</p>
          <h2>Payment</h2>
          <p>Payment is due upon completion of service. We accept cash, major credit cards, Venmo, and Zelle. Returned or declined payments will incur applicable fees. We reserve the right to pursue collection for unpaid invoices.</p>
          <h2>Warranty</h2>
          <p>We warrant our workmanship for defects in labor. Parts are subject to manufacturer warranty terms. Warranty does not cover damage caused by subsequent accidents, misuse, neglect, or work performed by others after our service. Contact us promptly if you experience any issues following our service.</p>
          <h2>Limitation of Liability</h2>
          <p>Our liability is limited to the cost of the service performed. We are not liable for pre-existing conditions, vehicle age-related failures, or issues unrelated to the service we performed. We carry general liability insurance — ask for details if needed.</p>
          <h2>Site Access</h2>
          <p>You are responsible for ensuring safe access for our technician to your vehicle at the service location. This includes obtaining any necessary permission from property owners (e.g., apartment complexes, employers) to allow on-site vehicle repair.</p>
          <h2>Contact</h2>
          <p>Questions about these terms? Use our <a href="/contact.html">contact form</a> or call (XXX) 555-XXXX.</p>
        </div>
      </div>
    </section>"""

write_file("terms-of-service.html", page(
    "Terms of Service | Tallahassee Mobile Mechanic",
    "Terms of Service for Tallahassee Mobile Mechanic mobile auto repair services.",
    "https://tallahasseemobilemechanic.com/terms-of-service.html",
    CSS_ROOT,
    tos_body,
    "",
    is_utility=True
))

print("All root pages done.")

# ────────────────────────────────────────────────────────────────
# SERVICES
# ────────────────────────────────────────────────────────────────

def service_page(slug, name, price_range, img_url, intro, sections, faqs, schema_desc):
    faq_schema_items = "".join([
        f'{{"@type":"Question","name":"{q}","acceptedAnswer":{{"@type":"Answer","text":"{a}"}}}}' + ("," if i < len(faqs)-1 else "")
        for i,(q,a) in enumerate(faqs)
    ])
    schema = f'''<script type="application/ld+json">
  {{"@context":"https://schema.org","@type":"Service","name":"{name}","description":"{schema_desc}","provider":{{"@type":"AutoRepair","name":"Tallahassee Mobile Mechanic","url":"https://tallahasseemobilemechanic.com/"}},"areaServed":{{"@type":"City","name":"Tallahassee","addressRegion":"FL"}},"offers":{{"@type":"Offer","priceRange":"{price_range}"}}}}
  </script>
  <script type="application/ld+json">
  {{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{faq_schema_items}]}}
  </script>'''

    faq_html = "".join([f'''
          <div class="faq-item" role="listitem">
            <button class="faq-item__trigger" aria-expanded="false" aria-controls="sfq-{i}">{q} <svg class="faq-item__icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg></button>
            <div class="faq-item__body" id="sfq-{i}"><p>{a}</p></div>
          </div>''' for i,(q,a) in enumerate(faqs)])

    section_html = "".join([f'<h2>{h}</h2><p>{p}</p>' for h,p in sections])

    body = f"""
    <div class="inner-hero">
      <div class="container">
        <nav class="breadcrumb" aria-label="breadcrumb" style="background:transparent;border:none;padding:0;margin-bottom:1rem;"><ol class="breadcrumb__list"><li><a href="/">Home</a></li><li class="breadcrumb__sep" aria-hidden="true">›</li><li><a href="/services/">Services</a></li><li class="breadcrumb__sep" aria-hidden="true">›</li><li aria-current="page">{name}</li></ol></nav>
        <span class="inner-hero__eyebrow">Mobile Auto Service</span>
        <h1>{name} in Tallahassee, FL</h1>
        <p>{intro}</p>
        <div class="inner-hero__ctas">
          <a href="tel:XXXXXXXXXX" class="btn btn--primary"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07A19.5 19.5 0 0 1 4.11 15 19.79 19.79 0 0 1 1.04 6.34 2 2 0 0 1 3 4.11h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"/></svg>Call (XXX) 555-XXXX</a>
          <a href="/contact.html" class="btn btn--outline-light">Request a Quote</a>
        </div>
      </div>
    </div>

    <section class="section">
      <div class="container">
        <div style="display:grid;grid-template-columns:1fr;gap:3rem;max-width:1100px;margin:0 auto;" class="service-content-wrap">
          <div>
            <img src="{img_url}" alt="{name} in Tallahassee FL by mobile mechanic" width="1200" height="600" loading="lazy" style="border-radius:var(--radius-lg);margin-bottom:2rem;width:100%;object-fit:cover;max-height:400px;">
            <div class="prose">
              {section_html}
            </div>
          </div>

          <div style="background:var(--color-surface);border-radius:var(--radius-lg);padding:2rem;border:1px solid var(--color-border);align-self:start;">
            <h2 style="font-size:1.25rem;margin-bottom:1.25rem;">Book This Service</h2>
            <form action="https://api.web3forms.com/submit" method="POST" novalidate>
              <input type="hidden" name="access_key" value="0219881f-13e5-4175-b720-517b8d10c028">
              <input type="hidden" name="subject" value="Service Request - {name}">
              <input type="hidden" name="redirect" value="https://tallahasseemobilemechanic.com/thank-you.html">
              <div class="form-group" style="margin-bottom:0.75rem;"><label for="s-name">Name</label><input type="text" id="s-name" name="name" placeholder="Your name" required></div>
              <div class="form-group" style="margin-bottom:0.75rem;"><label for="s-phone">Phone</label><input type="tel" id="s-phone" name="phone" placeholder="(850) 555-XXXX" required></div>
              <div class="form-group" style="margin-bottom:0.75rem;"><label for="s-email">Email</label><input type="email" id="s-email" name="email" placeholder="your@email.com" required></div>
              <div class="form-group" style="margin-bottom:0.75rem;"><label for="s-address">Service Location</label><input type="text" id="s-address" name="address" placeholder="Your address or location" required></div>
              <div class="form-group" style="margin-bottom:1rem;"><label for="s-msg">Details</label><textarea id="s-msg" name="message" placeholder="Tell us about your vehicle and issue" style="min-height:80px;" required></textarea></div>
              <button type="submit" class="btn btn--primary btn--block">Request Free Quote</button>
            </form>
            <div style="margin-top:1.5rem;padding-top:1.5rem;border-top:1px solid var(--color-border);">
              <p style="font-size:0.875rem;color:var(--color-text-muted);margin-bottom:0.5rem;font-weight:700;">Pricing</p>
              <p style="font-size:1.25rem;font-weight:800;color:var(--color-accent);">{price_range}</p>
              <p style="font-size:0.8rem;color:var(--color-text-muted);">$79 diagnostic fee waived when repair is booked</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="section section--surface">
      <div class="container">
        <div class="section__header">
          <h2 class="section__title">Frequently Asked Questions</h2>
        </div>
        <div class="faq-list" role="list">{faq_html}
        </div>
      </div>
    </section>

    <section class="cta-banner">
      <div class="container">
        <h2 class="cta-banner__title">Need {name} Today?</h2>
        <p class="cta-banner__sub">Don't wait at a shop. We come to you anywhere in Tallahassee and surrounding areas.</p>
        <div class="cta-banner__actions">
          <a href="tel:XXXXXXXXXX" class="btn btn--white btn--lg">Call (XXX) 555-XXXX</a>
          <a href="/contact.html" class="btn btn--outline-white btn--lg">Request a Quote</a>
        </div>
      </div>
    </section>"""

    return page(
        f"{name} Tallahassee FL | Mobile Auto Repair | Tallahassee Mobile Mechanic",
        f"Professional {name.lower()} in Tallahassee FL. {schema_desc} Call (XXX) 555-XXXX for same-day mobile service.",
        f"https://tallahasseemobilemechanic.com/services/{slug}.html",
        CSS_SUB,
        body,
        schema
    )

SERVICES = [
    ("brake-repair", "Mobile Brake Repair", "$149–$450+",
     "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=1200&q=80",
     "Worn brakes are dangerous. Our certified mobile mechanics replace brake pads, rotors, and calipers at your location in Tallahassee — no shop, no tow, no waiting.",
     [
       ("Why Mobile Brake Repair?", "If you notice grinding noises, a spongy brake pedal, or your car pulling to one side when you brake, don't wait. Driving on failing brakes is dangerous — but so is towing a car unnecessarily. That's where Tallahassee Mobile Mechanic comes in. We bring a fully equipped service van directly to your home, office, or roadside location and handle the entire brake job on the spot. No shop drop-off. No waiting room. No tow truck bill."),
       ("What's Included in Our Brake Service", "Our mobile brake service covers everything your brakes need. We start with a complete brake inspection — checking pad thickness, rotor condition, caliper function, brake fluid level, and brake lines. If we find worn pads or damaged rotors, we replace them with quality OEM-equivalent parts. We torque all fasteners to spec, bleed the brake lines if needed, and test the brakes before we leave. Most brake jobs in Tallahassee are completed in 1–2 hours at your location."),
       ("Warning Signs Your Brakes Need Service", "Don't ignore these signals: squealing or squeaking when braking (worn pad indicators), grinding metal-on-metal sound (pads worn down to the backing), soft or spongy brake pedal (air in brake lines or fluid leak), vehicle pulling to one side during braking (uneven caliper or pad wear), vibration or pulsation through the pedal (warped rotors), warning light on dashboard, or longer stopping distance than usual. If you notice any of these, call us immediately."),
       ("Brake Pad vs. Rotor Replacement — What Do You Need?", "Not every brake job requires rotor replacement. If your rotors still have sufficient material thickness and aren't warped, we can often resurface them or simply replace the pads. Our technician will measure rotor thickness and check for runout before recommending the most cost-effective solution. We never recommend work that isn't necessary — if pads alone will fix it, that's what we'll do."),
       ("Brakes on All Vehicle Types", "We service disc brakes on both front and rear axles for most domestic and foreign vehicles. Whether you drive a Toyota Camry, Ford F-150, Honda CR-V, Chevrolet Silverado, or a Hyundai Tucson, our technicians have the experience and parts to handle your brake service right in your driveway. We carry a comprehensive parts inventory in our service van to handle most makes and models same-day."),
       ("Our Service Area for Brake Repair", "We perform mobile brake repair throughout Tallahassee — including midtown, northeast, northwest, and south Tallahassee neighborhoods — as well as Midway, Crawfordville, Quincy, Havana, Monticello, and Woodville. If you're within Leon County or the surrounding area, we can likely reach you the same day.")
     ],
     [
       ("How much does mobile brake repair cost in Tallahassee?", "Brake repair typically ranges from $149 for a basic single-axle pad replacement to $450+ for a full brake job with four-wheel rotor replacement. We provide a written quote before any work begins. Our diagnostic fee is $79 and is waived when you book the repair."),
       ("Can you replace brakes in a parking lot or apartment complex?", "Yes, in most cases. Brake jobs require the vehicle to be on level ground and safely secured on jack stands. We can work in most parking lots and driveways. Let us know your location when you call and we'll confirm viability."),
       ("How long does a mobile brake job take?", "Most brake jobs take 1–2 hours on-site. A full four-wheel brake job with rotors may take up to 3 hours. We'll give you a time estimate when we arrive and assess your specific vehicle.")
     ],
     "Professional mobile brake pad and rotor replacement at your Tallahassee FL location."
    ),

    ("oil-change", "Mobile Oil Change", "$49–$119",
     "https://images.unsplash.com/photo-1607861716497-e65ab29fc7ac?w=1200&q=80",
     "Skip the wait at the shop. Our mobile oil change service comes to your home or office in Tallahassee — conventional, synthetic blend, or full synthetic, done in 30–45 minutes.",
     [
       ("Why Get Your Oil Changed Mobile?", "Regular oil changes are the single most important maintenance item for your vehicle's longevity. Engine oil lubricates moving parts, reduces friction, dissipates heat, and keeps the engine clean. But finding time to sit at a quick-lube shop in Tallahassee can eat up an hour or more of your day. With Tallahassee Mobile Mechanic, you schedule the appointment and we come to you — you stay home, stay at work, or keep doing what you're doing while we handle your oil change in the driveway."),
       ("What's Included in Our Mobile Oil Change", "We perform a complete oil and filter change at your location. Our service includes draining the old oil, replacing the oil drain plug, installing a new OEM-quality oil filter, filling with fresh oil (your choice of conventional, synthetic blend, or full synthetic), resetting the oil life monitor if your vehicle has one, and a quick visual check of other fluids. We bring all necessary equipment including catch pans, ensuring a clean, mess-free service every time."),
       ("How Often Should You Change Your Oil?", "Modern full synthetic oils typically last 7,500–10,000 miles or about 6 months. Conventional oil should be changed every 3,000–5,000 miles. Your vehicle's owner's manual has the manufacturer's recommended interval. If you're unsure, we'll check your oil condition when we arrive and advise accordingly. Florida's hot climate and stop-and-go Tallahassee traffic can accelerate oil degradation, so staying on schedule is especially important here."),
       ("Oil Types: Which One Is Right for Your Car?", "Conventional motor oil is the most economical option and works well in older vehicles or those that don't see extreme driving conditions. Synthetic blend oil offers improved protection over conventional at a moderate price point — a good middle ground for most drivers. Full synthetic oil provides the best performance, longest interval, and is recommended for newer vehicles, turbocharged engines, and high-performance cars. We carry a full range of viscosities (0W-20, 5W-20, 5W-30, 10W-30, and more) to match your vehicle's specifications."),
       ("Florida Summer and Engine Oil", "Tallahassee summers are brutal on engines. Temperatures regularly hit the upper 90s, and under the hood it gets much hotter. High heat accelerates oil oxidation and breakdown. If you're driving in Tallahassee's summer heat with old oil, you're shortening your engine's life. Don't skip that oil change — and consider upgrading to full synthetic for better thermal stability in Florida conditions."),
       ("Convenient Scheduling Across Tallahassee", "We offer mobile oil change service Monday through Friday from 7 AM to 7 PM and Saturday from 8 AM to 5 PM. We serve all Tallahassee neighborhoods and surrounding areas including Midway, Crawfordville, Quincy, Havana, Monticello, and Woodville. Book online or call (XXX) 555-XXXX to schedule your appointment.")
     ],
     [
       ("How much does a mobile oil change cost in Tallahassee?", "Our mobile oil change prices range from $49 for conventional oil to $119 for premium full synthetic on larger engines. The price includes the oil filter and all labor. We provide an exact quote based on your vehicle's make and oil type before we arrive."),
       ("Can you do an oil change in my apartment parking lot?", "Yes. We work in driveways, parking lots, and most apartment complexes. All we need is enough clearance to get under the vehicle and a catch pan for the used oil. We clean up completely and dispose of the old oil properly."),
       ("How long does a mobile oil change take?", "Most oil changes take 30–45 minutes. We also do a quick visual inspection of your other fluids and belts at no extra charge while we're there.")
     ],
     "Quick, clean mobile oil change service at your Tallahassee FL home or office."
    ),

    ("battery-replacement", "Battery Replacement", "$129–$249",
     "https://images.unsplash.com/photo-1561835491-ed2a507c4571?w=1200&q=80",
     "Dead battery? We come to you with a battery test, the right replacement battery for your vehicle, and have you back running in under an hour.",
     [
       ("Don't Get Stranded — We Come to You", "Nothing kills a day faster than turning the key and getting nothing. A dead battery can leave you stranded in your driveway, a parking lot, or even the side of Apalachee Parkway. Jump starts are a temporary fix — if your battery is more than 3–4 years old or failed a load test, it needs to be replaced. Tallahassee Mobile Mechanic responds quickly to get you back on the road, wherever you are."),
       ("Our Battery Replacement Process", "We start with a battery load test using a professional-grade digital tester to confirm the battery is truly the problem (and not the alternator or starter). If replacement is needed, we install a quality OEM-equivalent battery matched to your vehicle's specifications — correct cold cranking amps, reserve capacity, and group size. We also clean any corrosion from the terminals, check charging system voltage, and ensure the battery is properly secured. Most battery replacements are completed in 30–45 minutes."),
       ("How to Tell If Your Battery Is Dying", "Watch for these signs: slow cranking when starting (the engine turns over sluggishly), battery warning light on dashboard, frequent need for jump starts, dim headlights or interior lights especially when idling, bloated or swollen battery case, corrosion buildup on battery terminals, or a battery that's over 4 years old. Florida's heat is especially hard on car batteries — the heat accelerates the internal chemical degradation that causes batteries to fail. Tallahassee drivers often see shorter battery life than drivers in cooler climates."),
       ("Battery Brands and Quality", "We carry trusted battery brands that meet or exceed OEM specifications. The right battery for your vehicle depends on group size, cold cranking amps (CCA), and reserve capacity (RC). We don't install cheap off-brand batteries that fail prematurely — we want your new battery to last 4–6 years, not 18 months. When we give you a quote, we'll tell you exactly which battery we're installing and its specifications."),
       ("Checking Your Alternator Too", "A bad alternator can kill a new battery quickly — if the alternator isn't charging properly, your battery will drain even with a brand-new cell. We always check charging system voltage as part of our battery replacement service. If we find alternator issues, we'll advise you before proceeding and give you options. There's no point replacing a battery if the alternator is going to kill it in a week."),
       ("Battery Service Across All of Tallahassee", "We provide mobile battery replacement throughout Tallahassee and surrounding communities including Midway, Crawfordville, Quincy, Havana, Monticello, and Woodville. We can usually reach you within 1–2 hours. Call (XXX) 555-XXXX for priority service if you're stranded.")
     ],
     [
       ("How much does mobile battery replacement cost in Tallahassee?", "Battery replacement typically costs $129–$249 depending on your vehicle and battery type. This includes the battery, installation, load test, and charging system check. We'll give you an exact price before we come out."),
       ("Can you come to me if my car won't start?", "Absolutely. That's exactly what we're here for. If your battery is completely dead and you can't start the car, call us and we'll come to you — home, parking lot, or roadside. We carry jump-start equipment and replacement batteries in our van."),
       ("How long do car batteries last in Florida?", "In Florida's heat, batteries typically last 3–5 years, compared to 4–6 years in cooler climates. The heat accelerates internal battery degradation. If your battery is over 3 years old and showing any symptoms, it's worth having it load-tested.")
     ],
     "Mobile car battery testing and replacement in Tallahassee FL. We come to you, fast."
    ),

    ("diagnostic-service", "Check Engine Light Diagnostics", "$79 (waived with repair)",
     "https://images.unsplash.com/photo-1509773896068-7fd415d91e2e?w=1200&q=80",
     "Check engine light on? Don't guess. Our mobile diagnostic service uses professional OBD-II scanners to identify the exact problem — and we explain it in plain English before any work begins.",
     [
       ("What Does the Check Engine Light Mean?", "The check engine light (CEL) can indicate anything from a loose gas cap to a misfiring cylinder or a failing catalytic converter. Without a proper diagnostic scan, you're just guessing — and guessing wrong can be expensive. Tallahassee Mobile Mechanic comes to your location with professional-grade OBD-II diagnostic equipment to read every fault code, identify the root cause, and give you a clear, written estimate for the repair. No shop visit required."),
       ("Our Diagnostic Process", "We connect our diagnostic scanner to your vehicle's OBD-II port (located under the dashboard) and pull all stored and pending fault codes. We don't just read codes — we interpret them in the context of your vehicle's symptoms and history. Our technician will explain exactly what the codes mean, what's causing them, and what it will take to fix the problem. You get the full picture before you decide anything. Our diagnostic fee is $79, which is waived entirely if you book the repair with us."),
       ("Common Check Engine Light Causes", "The most common CEL causes we diagnose in Tallahassee include: O2 sensor failure (most common), catalytic converter issues, loose or bad gas cap, MAF (mass airflow) sensor failure, spark plug or ignition coil misfires, EVAP system leaks, EGR valve issues, and thermostat problems. Many of these can be repaired on-site during the same visit as the diagnostic — saving you time and money."),
       ("Why You Shouldn't Ignore the Check Engine Light", "Some drivers clear the code with a cheap scanner and assume the problem is gone. It's not. The underlying issue persists and often worsens — and some problems that start small (like an O2 sensor failure) can lead to major damage (like a ruined catalytic converter) if left untreated. More importantly, a lit CEL will cause you to fail a Florida emissions test. Don't ignore it — let us diagnose it properly."),
       ("Other Warning Lights We Diagnose", "Beyond the check engine light, we can diagnose ABS (anti-lock brake) warning lights, transmission temperature warnings, tire pressure (TPMS) alerts, oil pressure warnings, battery/charging system lights, and more. Our diagnostic equipment communicates with multiple vehicle control modules, not just the powertrain module. This means we can give you a comprehensive picture of what's going on with your vehicle's systems."),
       ("Mobile Diagnostics Across Tallahassee", "We bring the diagnostic equipment to you — your home, office parking lot, shopping center, or roadside. We serve all of Tallahassee and surrounding areas including Midway, Crawfordville, Quincy, Havana, and Monticello. Response time is typically 1–2 hours. Call (XXX) 555-XXXX or book online.")
     ],
     [
       ("How much does a vehicle diagnostic cost?", "Our diagnostic fee is $79. This covers a full OBD-II scan, visual inspection, and written estimate. If you book the repair with us after the diagnostic, the $79 fee is completely waived — making diagnosis free when combined with service."),
       ("Can you clear the check engine light?", "We can clear the codes after the repair is completed. Clearing codes without fixing the underlying problem is not something we recommend — the light will come back on and the problem will continue to worsen."),
       ("What if I need a repair after the diagnostic?", "We carry parts for many common repairs in our service van. If we diagnose the problem and you approve the repair, we can often complete it the same day in the same location. If we need to order parts, we'll schedule a return visit typically within 24–48 hours.")
     ],
     "Professional OBD-II vehicle diagnostics in Tallahassee FL. Know exactly what's wrong before you pay."
    ),

    ("alternator-repair", "Alternator & Starter Repair", "$299–$850",
     "https://images.unsplash.com/photo-1582719478250-c89cae4dc85b?w=1200&q=80",
     "Charging system failure or no-start condition? Our mobile mechanics diagnose and replace alternators and starters on-site across Tallahassee — without towing your vehicle.",
     [
       ("Alternator vs. Starter — What's the Difference?", "These are two distinct components that often get confused. The starter motor cranks the engine when you turn the key — it provides the initial rotation needed to get the engine running. The alternator, on the other hand, keeps the battery charged while the engine is running and powers all your electrical components. Both can fail, and both can leave you stranded, but they fail in different ways. Our mobile technicians can diagnose which component has failed and replace it on-site."),
       ("Signs Your Alternator Is Failing", "Watch for these alternator warning signs: battery warning light on dashboard, dim or flickering headlights and interior lights, dead battery despite being recently replaced, electrical accessories acting erratically (power windows slow, radio cutting out), burning rubber smell from the engine bay, strange whining or grinding noise from the engine, or a battery that keeps dying overnight. The alternator is essentially a generator — when it fails, the battery is the only power source and it drains quickly."),
       ("Signs Your Starter Is Failing", "Starter problems show up differently: clicking noise when you turn the key (especially a rapid-fire clicking, which usually means low battery but can be a bad starter), single loud click and nothing else, engine cranks slowly and struggles to start, starter staying engaged after engine starts (grinding metal sound), or intermittent no-start condition that comes and goes. Sometimes the starter solenoid fails rather than the starter motor itself — we diagnose both."),
       ("Our Alternator and Starter Replacement Process", "We begin with a full charging system test — measuring alternator output voltage (should be 13.5–14.5V), battery voltage, and starter draw. This confirms the failing component before we quote any work. Once diagnosed, we replace the alternator or starter with a quality remanufactured or new OEM-equivalent unit. We also check the drive belt (serpentine belt) since a worn belt can reduce alternator output. Most alternator and starter jobs are completed in 2–3 hours at your location."),
       ("Can These Really Be Done Mobile?", "Yes — for most vehicles. Alternators and starters are external engine components accessible from the top or bottom of the engine bay. Our technicians have replaced these components on hundreds of vehicles from pickup trucks to small sedans, all without a shop lift. The key is having the right tools and the right parts — we carry a large inventory of common alternators and starters for popular Tallahassee vehicle makes and models."),
       ("Serving All of Tallahassee and Beyond", "Alternator and starter failures often happen at the worst possible time — leaving you stranded in a parking lot or unable to start your car in the morning. Don't wait for a tow. Call Tallahassee Mobile Mechanic at (XXX) 555-XXXX. We serve all of Tallahassee plus Midway, Crawfordville, Quincy, Havana, Monticello, and Woodville with typical response times of 1–3 hours.")
     ],
     [
       ("How much does alternator replacement cost in Tallahassee?", "Alternator replacement typically costs $350–$650 depending on your vehicle make and model. Starter replacement runs $299–$500. These prices include the part and labor. We provide an exact quote after our charging system diagnostic."),
       ("Can you replace an alternator in a parking lot?", "Yes, for most vehicles. Alternators are typically accessible from the top of the engine bay. We need adequate space around the vehicle and good lighting. We work in parking lots, driveways, and apartment complexes regularly."),
       ("Is it the alternator or the battery?", "This is the most common question we get with charging issues. A bad alternator will kill a good battery; a bad battery can make an alternator work harder and fail sooner. We always test both before recommending replacement. Our charging system test gives definitive answers.")
     ],
     "Mobile alternator and starter replacement in Tallahassee FL. We diagnose and repair charging system failures on-site."
    ),

    ("pre-purchase-inspection", "Pre-Purchase Inspection", "$99–$149",
     "https://images.unsplash.com/photo-1568772585407-9361f9bf3a87?w=1200&q=80",
     "Buying a used car? Don't sign until you know what you're buying. We inspect any used vehicle at the seller's location — anywhere in Tallahassee — and give you a detailed written report.",
     [
       ("Why You Need a Pre-Purchase Inspection", "Buying a used car is one of the largest financial decisions most people make. Private sellers and even dealerships may not disclose every issue — some out of ignorance, some intentionally. A pre-purchase inspection (PPI) by an independent, certified mechanic gives you the unbiased facts about the car's condition before you hand over any money. Tallahassee Mobile Mechanic performs PPIs anywhere in the Tallahassee metro area — we go to wherever the car is located, including the seller's home or dealership lot."),
       ("What We Inspect", "Our comprehensive pre-purchase inspection covers over 100 check points including: full OBD-II diagnostic scan for stored and pending fault codes, engine compression test (where accessible), visual inspection of all fluid levels and conditions, check for leaks (oil, coolant, transmission fluid, brake fluid), inspection of belts and hoses, brake system check (pad thickness, rotor condition), suspension and steering check, tire condition and tread depth measurement, battery and charging system test, exterior body inspection for rust, accident damage, or mismatched paint, interior check (all electrical components, HVAC function), and a road test if the vehicle is operational. We document everything and provide a written report."),
       ("We Go to the Car — Not You", "The biggest advantage of our mobile pre-purchase inspection is that we come to wherever the car is. Whether it's a private seller's driveway in northeast Tallahassee, a used car lot on North Monroe, or a dealer in Midway — we show up with our equipment and inspect it there. You don't need to arrange transport. The seller doesn't need to bring it anywhere. We give you the full picture on-site."),
       ("What Happens After the Inspection", "After our inspection, we walk you through the findings in person and provide a written report you can keep. If we find significant problems, we'll tell you exactly what they are, how serious they are, and what they'll cost to repair. This gives you the power to negotiate a lower price, ask the seller to fix issues first, or walk away entirely knowing you made an informed decision. Many of our clients have saved $2,000–$5,000 on a purchase price by having leverage from a professional inspection report."),
       ("Common Issues We Find", "In the used car market around Tallahassee, we commonly find: deferred maintenance that wasn't disclosed (dirty oil, worn brakes, bald tires), undisclosed accident damage or frame repairs, salvage or rebuilt title vehicles disguised to look clean, oil leaks or coolant leaks under the vehicle, worn suspension components (ball joints, control arm bushings), and check engine codes that were cleared to hide problems before the sale. These findings can save you from inheriting someone else's problems."),
       ("Inspection Coverage Area", "We perform pre-purchase inspections throughout Tallahassee and the surrounding region — including Midway, Crawfordville, Quincy, Havana, Monticello, and Woodville. Call (XXX) 555-XXXX or request an inspection online. We typically schedule within 24 hours and provide the written report the same day.")
     ],
     [
       ("How much does a pre-purchase inspection cost?", "Our pre-purchase inspection fee is $99–$149 depending on the vehicle type and location. This is one of the best investments you can make when buying a used car — a single finding can save you thousands. We provide a written report the same day."),
       ("Can you inspect a car at a dealership?", "Yes, in most cases. We have the right to inspect any vehicle as a buyer's representative. Most reputable dealerships will allow an independent inspection. If a dealer refuses to allow a third-party inspection, that's a major red flag about the vehicle."),
       ("How long does a pre-purchase inspection take?", "A thorough pre-purchase inspection takes 45–90 minutes on-site. We won't rush it — this is your money and your decision. We take the time to do it right and explain every finding clearly.")
     ],
     "Mobile pre-purchase car inspection in Tallahassee FL. We go to the seller's location and give you a full written report."
    ),

    ("ac-recharge", "AC Recharge & Repair", "$99–$350",
     "https://images.unsplash.com/photo-1549317661-bd32c8ce0db2?w=1200&q=80",
     "Hot Florida summers demand working AC. Our mobile mechanics recharge refrigerant and diagnose AC problems at your location in Tallahassee — stay cool without a shop visit.",
     [
       ("Mobile AC Service in Florida's Heat", "Tallahassee summers are no joke — temperatures routinely hit the upper 90s, and driving without AC isn't just uncomfortable, it can be dangerous. But AC problems don't have to mean a shop visit. Tallahassee Mobile Mechanic brings the diagnostic equipment and refrigerant directly to you for most AC services. Whether you need a simple recharge or a more involved repair, we come to your location and assess the system on-site."),
       ("What We Do for Mobile AC Service", "Our AC service begins with a system pressure test to determine refrigerant levels and check for leaks. We use professional refrigerant identifier equipment and UV dye detection to find even small leaks. If the system is low on refrigerant and there's no significant leak, we recharge it and test performance (measuring vent outlet temperature). If we find a leak or other component failure, we'll diagnose the issue and give you a repair estimate. We service R-134a systems on most passenger vehicles."),
       ("Signs Your AC Needs Service", "Common AC problems we see in Tallahassee include: AC blowing warm or room-temperature air instead of cold, AC cycling on and off frequently, weak airflow from the vents, unusual noises when the AC compressor engages (clicking, rattling, or grinding), AC that only works sometimes but not others, musty or moldy smell from the vents (indicating moisture or mold in the evaporator), and visible refrigerant oil stains around AC fittings. Any of these symptoms warrant a professional inspection before the season gets any hotter."),
       ("Why Florida AC Systems Work Harder", "Your car's AC system runs almost year-round in Tallahassee — and the more it runs, the more wear it accumulates. The AC compressor is the most wear-prone component, but refrigerant leaks are the most common service item. Florida's high humidity also stresses the system. We recommend having your AC system inspected annually, ideally in March or April before summer heat peaks, to catch problems before they leave you sweltering."),
       ("What's Not Included in a Basic Recharge", "A recharge addresses low refrigerant levels but doesn't fix leaks or component failures. If your system has a significant leak, simply recharging will provide temporary relief but the refrigerant will escape again. We'll always tell you if we find a leak and what it will cost to fix properly. For major AC repairs like compressor replacement or condenser repair, we'll quote those separately and give you the option to approve or decline."),
       ("Serving Tallahassee and Surrounding Areas for AC Service", "We provide mobile AC recharge and diagnostic services throughout Tallahassee and the surrounding region. Call (XXX) 555-XXXX to schedule your AC service — we're available Monday through Friday from 7 AM to 7 PM and Saturday from 8 AM to 5 PM. Don't wait until you're sweating in traffic on I-10 to get your AC fixed.")
     ],
     [
       ("How much does AC recharge cost for a mobile mechanic in Tallahassee?", "A basic AC recharge costs $99–$149. This includes a system pressure check, refrigerant recharge, and performance test. If we find leaks or component issues requiring additional parts or labor, we'll quote those separately before proceeding."),
       ("Can you fix an AC compressor mobile?", "AC compressor replacement can often be done mobile for many vehicle makes and models. This is a more involved repair ($250–$600+) that requires recovering the refrigerant, replacing the compressor, and recharging the system. We'll assess your specific vehicle when we arrive."),
       ("Why does my AC smell musty?", "Musty AC smell is typically caused by mold or bacteria growing on the evaporator coil — a common issue in Florida's humid climate. We can treat this with an evaporator cleaner/disinfectant spray during your AC service visit.")
     ],
     "Mobile AC recharge and repair in Tallahassee FL. Stay cool — we bring the service to you."
    ),

    ("tune-up", "Mobile Tune-Up", "$99–$350",
     "https://images.unsplash.com/photo-1632823471406-4c5c7e4c6f24?w=1200&q=80",
     "Spark plugs, filters, belts, and more — our mobile tune-up service restores your engine's performance and fuel efficiency right in your driveway.",
     [
       ("What Is a Tune-Up?", "A tune-up is a comprehensive maintenance service that addresses the components responsible for your engine's ignition, air flow, and fuel delivery. Over time, spark plugs wear out, air filters get clogged, fuel filters restrict flow, and belts crack — all of which reduce engine performance, hurt fuel economy, and can lead to hard starts or misfires. Tallahassee Mobile Mechanic performs complete mobile tune-up services at your location, restoring your engine's efficiency without a shop visit."),
       ("What's Included in a Mobile Tune-Up", "Our standard tune-up covers: spark plug inspection and replacement, air filter replacement, fuel filter replacement (if accessible), serpentine belt and timing belt visual inspection, PCV valve check and replacement, throttle body cleaning (if needed), visual inspection of ignition wires and coil packs, check for vacuum leaks, and a full OBD-II diagnostic scan. We use quality parts that meet or exceed OEM specifications. After the tune-up, most drivers notice improved throttle response, smoother idle, and better fuel economy."),
       ("How Often Does Your Car Need a Tune-Up?", "With modern vehicles, spark plug intervals have extended significantly. Copper spark plugs should be replaced every 30,000 miles. Iridium or platinum plugs can last 60,000–100,000 miles. Air filters typically need replacement every 15,000–30,000 miles (sooner in dusty conditions). Your vehicle's owner's manual has the manufacturer's recommendations — if you're not sure when your last tune-up was, let us check. We'll pull the maintenance history codes and give you an honest assessment."),
       ("Signs Your Engine Needs a Tune-Up", "Watch for these signals that it's time: rough or lumpy idle that wasn't there before, hesitation or stumbling when accelerating from a stop, check engine light with misfire codes (P0300–P0308 range), reduced fuel economy over the past several fill-ups, hard starting especially when cold, surging idle (RPMs hunting up and down), and increased exhaust emissions. Any of these symptoms in a vehicle with high mileage or deferred maintenance is a strong indicator that a tune-up is overdue."),
       ("Tune-Up for All Vehicle Makes and Models", "We perform mobile tune-ups on most domestic and foreign passenger vehicles. Common vehicles we service include Toyota Camry and Corolla, Honda Accord and CR-V, Ford F-150 and Explorer, Chevrolet Silverado and Equinox, Nissan Altima and Rogue, Hyundai Sonata and Tucson, and many more. We carry a comprehensive parts inventory for the most common makes and models in the Tallahassee area."),
       ("Tune-Up Service Throughout Tallahassee and Surrounding Areas", "We bring tune-up service to all Tallahassee neighborhoods and surrounding communities including Midway, Crawfordville, Quincy, Havana, Monticello, and Woodville. Call (XXX) 555-XXXX or request a quote online to schedule your mobile tune-up. Same-day appointments are frequently available Monday through Saturday.")
     ],
     [
       ("How much does a mobile tune-up cost in Tallahassee?", "Tune-up cost depends on your vehicle and which components need replacement. Basic spark plug and air filter service starts around $99–$149 for vehicles with accessible plug designs. Full tune-up with ignition wires, filters, and belts can run $200–$350. We provide a specific quote for your vehicle after we know your make, model, and mileage."),
       ("How long does a mobile tune-up take?", "A standard tune-up takes 1–2 hours on-site. Vehicles with difficult-to-access spark plugs (such as some V6 and V8 engines requiring intake manifold removal) may take longer. We'll give you an accurate time estimate when you book."),
       ("Can a tune-up fix a rough idle?", "Often yes. Worn spark plugs, a clogged air filter, or a dirty throttle body are common causes of rough idle. A proper tune-up addresses all of these. If the rough idle persists after a tune-up, it may indicate a deeper issue that our diagnostic scan will identify.")
     ],
     "Mobile engine tune-up service in Tallahassee FL. Spark plugs, filters, and belts replaced at your location."
    ),
]

for slug, name, price_range, img, intro, sections, faqs, schema_desc in SERVICES:
    write_file(f"services/{slug}.html", service_page(slug, name, price_range, img, intro, sections, faqs, schema_desc))
    print(f"  Created: services/{slug}.html")

print("Service pages done.")

# ────────────────────────────────────────────────────────────────
# LOCATIONS
# ────────────────────────────────────────────────────────────────

def loc_page(city, state_short, slug, desc_short, intro, img1, img2, sections, faqs):
    faq_html = "".join([f'''
          <div class="faq-item" role="listitem">
            <button class="faq-item__trigger" aria-expanded="false" aria-controls="lfq-{i}">{q} <svg class="faq-item__icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg></button>
            <div class="faq-item__body" id="lfq-{i}"><p>{a}</p></div>
          </div>''' for i,(q,a) in enumerate(faqs)])

    section_html = "".join([f'<h2>{h}</h2><p>{p}</p>' for h,p in sections])

    schema = f'''<script type="application/ld+json">
  {{"@context":"https://schema.org","@type":"AutoRepair","name":"Tallahassee Mobile Mechanic - {city}","description":"Mobile auto repair service in {city}, {state_short}. We come to you.","areaServed":{{"@type":"City","name":"{city}","addressRegion":"{state_short}"}},"url":"https://tallahasseemobilemechanic.com/locations/{slug}.html","telephone":"(XXX) 555-XXXX"}}
  </script>'''

    body = f"""
    <div class="inner-hero">
      <div class="container">
        <nav aria-label="breadcrumb" style="margin-bottom:1rem;"><ol class="breadcrumb__list" style="display:flex;gap:0.4rem;list-style:none;padding:0;margin:0;font-size:0.8rem;color:var(--color-text-muted);"><li><a href="/" style="color:inherit;">Home</a></li><li aria-hidden="true">›</li><li><a href="/locations/" style="color:inherit;">Locations</a></li><li aria-hidden="true">›</li><li aria-current="page">{city}</li></ol></nav>
        <span class="inner-hero__eyebrow">Service Area</span>
        <h1>Mobile Mechanic in {city}, {state_short}</h1>
        <p>{intro}</p>
        <div class="inner-hero__ctas">
          <a href="tel:XXXXXXXXXX" class="btn btn--primary"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07A19.5 19.5 0 0 1 4.11 15 19.79 19.79 0 0 1 1.04 6.34 2 2 0 0 1 3 4.11h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"/></svg>Call (XXX) 555-XXXX</a>
          <a href="/contact.html" class="btn btn--outline-light">Request Service</a>
        </div>
      </div>
    </div>

    <section class="section">
      <div class="container">
        <div style="display:grid;grid-template-columns:1fr;gap:2.5rem;max-width:1100px;margin:0 auto;">
          <div>
            <img src="{img1}" alt="Mobile mechanic serving {city} FL" width="1200" height="500" loading="lazy" style="border-radius:var(--radius-lg);margin-bottom:2rem;width:100%;object-fit:cover;max-height:380px;">
            <div class="prose">{section_html}</div>
          </div>
          <div>
            <img src="{img2}" alt="Auto repair service in {city} Florida" width="800" height="500" loading="lazy" style="border-radius:var(--radius-lg);margin-bottom:2rem;width:100%;object-fit:cover;max-height:300px;">
            <div style="background:var(--color-surface);border-radius:var(--radius-lg);padding:1.75rem;border:1px solid var(--color-border);">
              <h2 style="font-size:1.2rem;margin-bottom:1rem;">Services Available in {city}</h2>
              <ul style="list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:0.5rem;">
                <li><a href="/services/brake-repair.html" style="color:var(--color-text-muted);text-decoration:none;font-size:0.9rem;">✓ Mobile Brake Repair</a></li>
                <li><a href="/services/oil-change.html" style="color:var(--color-text-muted);text-decoration:none;font-size:0.9rem;">✓ Oil Change</a></li>
                <li><a href="/services/battery-replacement.html" style="color:var(--color-text-muted);text-decoration:none;font-size:0.9rem;">✓ Battery Replacement</a></li>
                <li><a href="/services/diagnostic-service.html" style="color:var(--color-text-muted);text-decoration:none;font-size:0.9rem;">✓ Check Engine Diagnostics</a></li>
                <li><a href="/services/alternator-repair.html" style="color:var(--color-text-muted);text-decoration:none;font-size:0.9rem;">✓ Alternator &amp; Starter Repair</a></li>
                <li><a href="/services/ac-recharge.html" style="color:var(--color-text-muted);text-decoration:none;font-size:0.9rem;">✓ AC Recharge &amp; Repair</a></li>
                <li><a href="/services/pre-purchase-inspection.html" style="color:var(--color-text-muted);text-decoration:none;font-size:0.9rem;">✓ Pre-Purchase Inspection</a></li>
                <li><a href="/services/tune-up.html" style="color:var(--color-text-muted);text-decoration:none;font-size:0.9rem;">✓ Mobile Tune-Up</a></li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="section section--surface">
      <div class="container">
        <div class="section__header">
          <h2 class="section__title">FAQ — Mobile Mechanic in {city}</h2>
        </div>
        <div class="faq-list" role="list">{faq_html}</div>
      </div>
    </section>

    <section class="cta-banner">
      <div class="container">
        <h2 class="cta-banner__title">Need a Mobile Mechanic in {city}?</h2>
        <p class="cta-banner__sub">We come to you — home, office, or roadside. Same-day service available.</p>
        <div class="cta-banner__actions">
          <a href="tel:XXXXXXXXXX" class="btn btn--white btn--lg">Call (XXX) 555-XXXX</a>
          <a href="/contact.html" class="btn btn--outline-white btn--lg">Request Service</a>
        </div>
      </div>
    </section>"""

    return page(
        f"Mobile Mechanic {city} FL | Same-Day Auto Repair | Tallahassee Mobile Mechanic",
        f"Mobile mechanic serving {city}, FL. {desc_short} Call (XXX) 555-XXXX for same-day service.",
        f"https://tallahasseemobilemechanic.com/locations/{slug}.html",
        CSS_SUB,
        body,
        schema
    )

LOCATIONS = [
    ("Midway", "FL", "midway-fl",
     "We come to your home or office in Midway for brake repair, oil changes, battery replacement, and more.",
     "Tallahassee Mobile Mechanic serves Midway, FL with fast, professional mobile auto repair. Whether you're home in the Midway area or stranded on US-90, we'll come to you.",
     "https://images.unsplash.com/photo-1625047509248-ec889cbff17f?w=1200&q=80",
     "https://images.unsplash.com/photo-1619642751034-765dfdf7c58e?w=800&q=80",
     [
       ("Mobile Auto Repair in Midway, FL", "Midway is a small but growing community in Gadsden County, located just west of Tallahassee along the US-90 corridor. Many Midway residents commute to Tallahassee for work, which means car trouble can disrupt both your home life and your workday. Tallahassee Mobile Mechanic extends its service area to cover Midway, bringing professional mobile auto repair directly to your driveway, workplace, or anywhere your car is located in the Midway area. We typically reach Midway customers within 1–2 hours of your call."),
       ("Services We Provide in Midway", "Our full range of mobile auto services is available to Midway residents: brake pad and rotor replacement, oil changes (conventional, synthetic blend, and full synthetic), battery testing and replacement, check engine light diagnostics with OBD-II scanning, alternator and starter replacement, AC recharge and repair, pre-purchase used car inspections, and complete tune-up services. We carry a well-stocked service van so most repairs can be completed in a single visit."),
       ("Convenient Service for Midway Commuters", "If you drive from Midway to Tallahassee daily on US-90 or I-10, you know how important a reliable vehicle is. Car trouble doesn't just inconvenience you — it can cost you a day of work. Our mobile service is designed for busy people who can't afford downtime. Book an appointment before you leave for work, during your lunch break, or right after you get home — we'll handle the repair while you carry on with your day."),
       ("Local Knowledge of the Midway Area", "We're familiar with the roads and neighborhoods of Midway, including communities along Havana Highway, the US-90 commercial corridor near the Midway community center, and residential areas south toward the Talquin State Forest. Whether you're in a residential neighborhood or a commercial area, we can reach you and work safely at your location."),
       ("Pricing for Midway Customers", "Our pricing is the same for Midway as it is for Tallahassee — we don't charge a travel surcharge for service in the Midway area. Our diagnostic fee is $79, waived when you book a repair. Most jobs run $150–$450. Call (XXX) 555-XXXX or use our online form to get a quote for your specific vehicle and situation.")
     ],
     [
       ("Do you charge extra to come to Midway?", "No. We do not charge a travel surcharge for Midway. Our pricing is the same as Tallahassee — $79 diagnostic (waived with repair), and standard labor and parts rates for all services."),
       ("How quickly can you reach Midway?", "Midway is typically 15–25 minutes from central Tallahassee. We can usually reach Midway customers within 1–2 hours of your call during business hours (Mon–Fri 7am–7pm, Sat 8am–5pm)."),
       ("What parts of Midway do you service?", "We service all of Midway, FL including the US-90 corridor, residential neighborhoods near Midway, and surrounding communities in Gadsden County. If you're not sure whether we cover your specific location, just call and we'll confirm.")
     ]
    ),
    ("Crawfordville", "FL", "crawfordville-fl",
     "Professional mobile mechanic service in Crawfordville FL — brake repair, diagnostics, oil changes, and more at your location.",
     "Tallahassee Mobile Mechanic serves Crawfordville, FL with professional mobile auto repair. Whether you're home in Wakulla County or stranded on Crawfordville Highway, we'll come to you.",
     "https://images.unsplash.com/photo-1487754180451-c456f719a1fc?w=1200&q=80",
     "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=800&q=80",
     [
       ("Mobile Mechanic Serving Crawfordville, FL", "Crawfordville is the county seat of Wakulla County and a rapidly growing community south of Tallahassee along US-319. With new residential developments expanding throughout Wakulla County, more Crawfordville residents than ever are commuting north to Tallahassee for work — and more vehicles than ever need service in the area. Tallahassee Mobile Mechanic extends service to Crawfordville, bringing certified mobile mechanics directly to your home or wherever your car is located."),
       ("Why Crawfordville Residents Choose Mobile Service", "Crawfordville is roughly 20 miles south of Tallahassee. For routine maintenance or an unexpected breakdown, the prospect of driving back into Tallahassee to find a shop — or worse, paying for a tow — is time-consuming and expensive. Our mobile service eliminates that hassle. We come to your Crawfordville address and handle most repairs right in your driveway. Brake jobs, oil changes, battery replacements, AC recharges — all available at your location."),
       ("Common Service Calls in Crawfordville", "We frequently serve Crawfordville residents for: battery replacement after their car won't start in the morning, brake repair when they hear grinding or squealing, AC recharge before the brutal Florida summer heat sets in, oil changes for busy families who can't find time to visit a shop, and pre-purchase inspections when buying a vehicle from a private seller in the area. The Crawfordville area and Wakulla County generally have many older vehicles that benefit from regular maintenance."),
       ("Serving the Wider Wakulla County Area", "Beyond Crawfordville itself, we service surrounding Wakulla County communities including Sopchoppy, Panacea, and Medart. Whether you're near the Wakulla Springs State Park area, near the coast, or anywhere along US-319 between Crawfordville and Tallahassee, we can reach you. Call us and we'll confirm your coverage and schedule a time that works."),
       ("Same-Day Service for Crawfordville Customers", "Same-day service is available for Crawfordville Monday through Saturday. We typically reach Crawfordville within 1.5–2.5 hours of your call. Our pricing is the same as Tallahassee — no surcharge for the drive south. Call (XXX) 555-XXXX for same-day scheduling or fill out our online form to request a quote.")
     ],
     [
       ("How long does it take to get to Crawfordville from Tallahassee?", "Crawfordville is approximately 20 miles south of Tallahassee on US-319. We typically reach Crawfordville customers within 1.5–2.5 hours of scheduling, depending on current appointment availability."),
       ("Do you service all of Wakulla County?", "We primarily serve Crawfordville and communities along US-319 in Wakulla County. For locations further south toward the coast, call us and we'll confirm whether we can reach you same-day or schedule a next-day appointment."),
       ("Is there a travel fee for Crawfordville?", "We do not charge a separate travel fee for Crawfordville. Our standard pricing applies — $79 diagnostic (waived with repair booking) and standard labor and parts rates.")
     ]
    ),
    ("Quincy", "FL", "quincy-fl",
     "Mobile mechanic service in Quincy FL — we travel to Gadsden County for brake repair, diagnostics, oil changes, and more.",
     "Tallahassee Mobile Mechanic serves Quincy, FL and all of Gadsden County with professional mobile auto repair. No tow, no shop — we come to you.",
     "https://images.unsplash.com/photo-1607861716497-e65ab29fc7ac?w=1200&q=80",
     "https://images.unsplash.com/photo-1561835491-ed2a507c4571?w=800&q=80",
     [
       ("Mobile Mechanic in Quincy, FL", "Quincy is the county seat of Gadsden County, located about 20 miles northwest of Tallahassee on US-90. As the largest city in Gadsden County, Quincy has a significant number of commuters traveling into Tallahassee daily — and a community that deserves access to quality, convenient auto repair. Tallahassee Mobile Mechanic extends service to Quincy, offering the same professional mobile mechanics and same-day service that Tallahassee residents enjoy."),
       ("Services Available in Quincy", "Every service we offer in Tallahassee is available in Quincy: mobile brake repair, oil changes, battery replacement and testing, check engine light diagnostics, alternator and starter replacement, AC recharge and repair, pre-purchase vehicle inspections, and tune-up services. We carry a comprehensive parts inventory