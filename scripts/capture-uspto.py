#!/usr/bin/env python3
"""Capture USPTO screenshot for SAOIRSE trademark evidence."""
from playwright.sync_api import sync_playwright
import os

evidence_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "docs", "legal", "evidence")
os.makedirs(evidence_dir, exist_ok=True)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={"width": 1920, "height": 1200}, locale="en-US")
    print("Navigating to USPTO...")
    page.goto("https://tmsearch.uspto.gov/search/search-results?query=saoirse&section=form", wait_until="domcontentloaded", timeout=30000)
    try:
        page.wait_for_selector("text=No results found", timeout=15000)
        print("'No results found' confirmed")
    except Exception:
        print("Selector timeout, capturing anyway")
    page.wait_for_timeout(3000)
    filepath = os.path.join(evidence_dir, "SCREENSHOT-004_USPTO_SAOIRSE_2026-03-28.png")
    page.screenshot(path=filepath, full_page=True)
    size = os.path.getsize(filepath)
    print(f"Saved: {filepath} ({size:,} bytes)")
    browser.close()
print("Done.")
