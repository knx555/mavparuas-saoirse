#!/usr/bin/env python3
"""
take-evidence-screenshots.py — Capture trademark search evidence as PNG screenshots.

Uses Playwright (headless Chromium) to render JavaScript-heavy SPAs
and saves full-page screenshots to docs/legal/evidence/.

Usage: python3 scripts/take-evidence-screenshots.py
"""

import sys
import os
import urllib.request
import json
from datetime import datetime

# Ensure we can import playwright
try:
    from playwright.sync_api import sync_playwright
except ImportError:
    print("ERROR: Playwright is not installed.")
    print("Run: pip install playwright && playwright install chromium")
    sys.exit(1)


def get_public_ip():
    """Retrieve the public outgoing IP address."""
    try:
        req = urllib.request.Request(
            "https://api.ipify.org?format=json",
            headers={"User-Agent": "evidence-capture/1.0"}
        )
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read().decode())
            return data.get("ip", "unknown")
    except Exception:
        return "unknown"

# Configuration
EVIDENCE_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "docs", "legal", "evidence"
)
TODAY = datetime.now().strftime("%Y-%m-%d")
SEARCH_TERM = "SAOIRSE"
PROJECT = "MAVPARUAS SAOIRSE — Trademark Clearance Research"
GITHUB_ACCOUNT = "knx555"
PUBLIC_IP = get_public_ip()

TARGETS = [
    {
        "id": "001",
        "name": "TMView",
        "desc": "TMView International (70+ IP Offices, EUIPO/TMDN)",
        "url": "https://www.tmdn.org/tmview/#/tmview/results?1&page=1&pageSize=30&criteria=C&basicSearch=saoirse",
        "wait_selector": "table",
        "wait_timeout": 15000,
    },
    {
        "id": "002",
        "name": "EUIPO",
        "desc": "EUIPO eSearch Plus (EU Trade Mark Registry)",
        "url": "https://euipo.europa.eu/eSearch/#basic/1+1+1+1/100+100+100+100/saoirse",
        "wait_selector": "text=No results",
        "wait_timeout": 15000,
    },
    {
        "id": "003",
        "name": "DPMA",
        "desc": "DPMA Register (Deutsches Patent- und Markenamt)",
        "url": "https://register.dpma.de/DPMAregister/marke/trefferliste?searchMode=simple&query=saoirse",
        "wait_selector": "body",
        "wait_timeout": 15000,
    },
    {
        "id": "004",
        "name": "USPTO",
        "desc": "USPTO Trademark Search (United States Patent and Trademark Office)",
        "url": "https://tmsearch.uspto.gov/search/search-results?query=saoirse&section=form",
        "wait_selector": "text=No results found",
        "wait_timeout": 15000,
    },
]


def inject_evidence_banner(page, target):
    """Inject a visible evidence banner at the top of the page showing
    URL, search term, date/time, database name, GitHub account and source IP.
    No personal names — only knx555 account ID and outgoing IP for forensic traceability."""

    now_str = datetime.now().strftime("%Y-%m-%dT%H:%M:%S%z")
    url = target["url"]
    desc = target["desc"]

    # Escape for JS string literal
    url_escaped = url.replace("'", "\\'")
    desc_escaped = desc.replace("'", "\\'")
    now_escaped = now_str.replace("'", "\\'")

    js_code = f"""
    (() => {{
        const banner = document.createElement('div');
        banner.id = 'evidence-banner';
        banner.style.cssText = `
            position: fixed; top: 0; left: 0; right: 0; z-index: 999999;
            background: #1a1a2e; color: #e0e0e0; padding: 12px 20px;
            font-family: 'Courier New', monospace; font-size: 13px;
            line-height: 1.6; border-bottom: 3px solid #e94560;
            box-shadow: 0 2px 10px rgba(0,0,0,0.3);
        `;
        banner.innerHTML = `
            <div style="display:flex; justify-content:space-between; align-items:flex-start;">
                <div>
                    <div style="color:#e94560; font-weight:bold; font-size:15px; margin-bottom:4px;">
                        EVIDENCE SCREENSHOT &mdash; TRADEMARK CLEARANCE
                    </div>
                    <div><strong style="color:#0f3460;">Project:</strong> {PROJECT}</div>
                    <div><strong style="color:#0f3460;">Database:</strong> {desc_escaped}</div>
                    <div><strong style="color:#0f3460;">Search Term:</strong>
                        <span style="background:#e94560;color:#fff;padding:2px 8px;border-radius:3px;font-weight:bold;">
                            {SEARCH_TERM}
                        </span>
                    </div>
                    <div><strong style="color:#0f3460;">URL:</strong>
                        <span style="color:#16c79a; word-break:break-all;">{url_escaped}</span>
                    </div>
                </div>
                <div style="text-align:right; min-width:220px;">
                    <div style="color:#e94560; font-weight:bold; font-size:14px;">{now_escaped}</div>
                    <div style="color:#888; font-size:12px;">GitHub: {GITHUB_ACCOUNT}</div>
                    <div style="color:#888; font-size:12px;">Source IP: {PUBLIC_IP}</div>
                </div>
            </div>
        `;
        document.body.insertBefore(banner, document.body.firstChild);

        // Push page content down so banner doesn't overlap
        document.body.style.marginTop = (banner.offsetHeight + 10) + 'px';
    }})();
    """
    page.evaluate(js_code)
    # Short wait for the DOM injection to render
    page.wait_for_timeout(500)


def main():
    os.makedirs(EVIDENCE_DIR, exist_ok=True)
    print(f"Evidence directory: {EVIDENCE_DIR}")
    print(f"Date: {TODAY}")
    print(f"Search term: {SEARCH_TERM}")
    print(f"Targets: {len(TARGETS)}")
    print()

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            viewport={"width": 1920, "height": 1200},
            locale="de-DE",
        )

        for target in TARGETS:
            filename = f"SCREENSHOT-{target['id']}_{target['name']}_SAOIRSE_{TODAY}.png"
            filepath = os.path.join(EVIDENCE_DIR, filename)

            print(f"[{target['id']}] {target['name']}...")
            print(f"     URL: {target['url']}")

            try:
                page = context.new_page()
                page.goto(target["url"], wait_until="domcontentloaded", timeout=30000)

                # Wait for content to render (JS SPAs need this)
                try:
                    page.wait_for_selector(
                        target["wait_selector"],
                        timeout=target["wait_timeout"]
                    )
                except Exception:
                    print(f"     (selector timeout, capturing anyway)")

                # Additional wait for JS rendering
                page.wait_for_timeout(3000)

                # Inject evidence banner with URL, search term, date
                inject_evidence_banner(page, target)

                # Take screenshot
                page.screenshot(path=filepath, full_page=True)
                size = os.path.getsize(filepath)
                print(f"     -> {filepath}")
                print(f"     -> {size:,} bytes")
                page.close()

            except Exception as e:
                print(f"     ERROR: {e}")

        browser.close()

    print()
    print("Done! Evidence screenshots saved.")
    print(f"Directory: {EVIDENCE_DIR}")

    # List saved files
    files = sorted(f for f in os.listdir(EVIDENCE_DIR) if f.endswith(".png"))
    for f in files:
        size = os.path.getsize(os.path.join(EVIDENCE_DIR, f))
        print(f"  {f} ({size:,} bytes)")


if __name__ == "__main__":
    main()
