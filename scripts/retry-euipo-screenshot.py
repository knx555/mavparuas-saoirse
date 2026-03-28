#!/usr/bin/env python3
"""Retry EUIPO screenshot with evidence banner."""
import os, json, urllib.request
from datetime import datetime
from playwright.sync_api import sync_playwright

def get_public_ip():
    try:
        req = urllib.request.Request(
            "https://api.ipify.org?format=json",
            headers={"User-Agent": "evidence-capture/1.0"}
        )
        with urllib.request.urlopen(req, timeout=5) as resp:
            return json.loads(resp.read().decode()).get("ip", "unknown")
    except Exception:
        return "unknown"

PUBLIC_IP = get_public_ip()
print(f"Public IP: {PUBLIC_IP}")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={"width": 1920, "height": 1200})
    print("Loading EUIPO...")
    page.goto(
        "https://euipo.europa.eu/eSearch/#basic/1+1+1+1/100+100+100+100/saoirse",
        wait_until="domcontentloaded",
        timeout=60000
    )
    try:
        page.wait_for_selector("text=No results", timeout=20000)
        print("  Found 'No results' text")
    except Exception:
        print("  (selector timeout, capturing anyway)")

    page.wait_for_timeout(3000)

    now_str = datetime.now().strftime("%Y-%m-%dT%H:%M:%S%z")
    banner_js = """(() => {
        const banner = document.createElement('div');
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
                    <div><strong style="color:#0f3460;">Project:</strong> MAVPARUAS SAOIRSE &mdash; Trademark Clearance Research</div>
                    <div><strong style="color:#0f3460;">Database:</strong> EUIPO eSearch Plus (EU Trade Mark Registry)</div>
                    <div><strong style="color:#0f3460;">Search Term:</strong>
                        <span style="background:#e94560;color:#fff;padding:2px 8px;border-radius:3px;font-weight:bold;">
                            SAOIRSE
                        </span>
                    </div>
                    <div><strong style="color:#0f3460;">URL:</strong>
                        <span style="color:#16c79a; word-break:break-all;">https://euipo.europa.eu/eSearch/#basic/1+1+1+1/100+100+100+100/saoirse</span>
                    </div>
                </div>
                <div style="text-align:right; min-width:220px;">
                    <div style="color:#e94560; font-weight:bold; font-size:14px;">""" + now_str + """</div>
                    <div style="color:#888; font-size:12px;">GitHub: knx555</div>
                    <div style="color:#888; font-size:12px;">Source IP: """ + PUBLIC_IP + """</div>
                </div>
            </div>
        `;
        document.body.insertBefore(banner, document.body.firstChild);
        document.body.style.marginTop = (banner.offsetHeight + 10) + 'px';
    })()"""

    page.evaluate(banner_js)
    page.wait_for_timeout(500)

    filepath = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "docs", "legal", "evidence",
        "SCREENSHOT-002_EUIPO_SAOIRSE_2026-03-28.png"
    )
    page.screenshot(path=filepath, full_page=True)
    size = os.path.getsize(filepath)
    print(f"EUIPO -> {filepath}")
    print(f"  {size:,} bytes")
    browser.close()
    print("Done!")
