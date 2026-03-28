# Project Learning — MAVPARUAS File Tool

---

## GRUNDPRINZIPIEN (UNVERRÜCKBAR)

### Prinzip 1: Forensische und juristische Sauberkeit

> **Markus, 28.03.2026 18:59:**
> *"Ich möchte, dass wir forensisch und juristisch extrem sauber arbeiten.
> Das ist unser Prinzip, sonst können wir uns die ganze Recherche
> von vorneherein sparen."*

**Was das konkret bedeutet:**

1. **Jeder Evidence-Screenshot MUSS enthalten:**
   - Sichtbarer Suchbegriff (im Suchfeld ODER als injiziertes Banner)
   - Vollständige URL der Datenbank
   - Exaktes Datum und Uhrzeit der Erfassung (mit Zeitzone)
   - Name der durchsuchten Datenbank
   - Projektkontext (MAVPARUAS SAOIRSE)
   - GitHub-Account (knx555) und öffentliche Quell-IP
   - KEINE persönlichen Namen in Evidence-Dateien

2. **Keine Screenshots ohne Kontext** — ein Bild mit "No Results" ohne
   sichtbaren Suchbegriff ist WERTLOS als Beweis

3. **Vollständige Evidence Chain** — jedes Beweismittel wird:
   - Als PNG mit Evidence-Banner gespeichert
   - In einem Evidence-Index mit SHA-256 Hash referenziert
   - Mit Metadaten (Datum, URL, Suchbegriff, Ergebnis) dokumentiert

4. **Reproduzierbarkeit** — Suchen müssen nachvollziehbar beschrieben sein,
   damit ein Dritter sie unabhängig wiederholen kann

5. **Timestamps** — IMMER ISO 8601 mit Zeitzone (z.B. 2026-03-28T18:59:30+0100)

### Prinzip 2: Privacy-by-Design (ABSOLUT)

Mehr als DSGVO. Keine Daten an externe Services. Nur lokale LLMs.
Nicht verhandelbar.

### Prinzip 3: Lizenz-Sicherheit

Nur permissive Lizenzen (MIT, BSD, Apache 2.0, MPL 2.0).
Strikte Vermeidung von Copyleft (GPL, AGPL) ohne explizite Freigabe.

---

## 2026-03-28 — Naming Research

### Trademark Research Methodology
1. GitHub-Suche (breite Projektname-Kollisionen)
2. Wikipedia (bekannte Marken, Produkte, Regulierungen)
3. EUIPO eSearch (EU-Markenregister)
4. DPMA (deutsches Markenamt) — ausstehend
5. USPTO (US-Patentamt) — ausstehend
6. Domain-Checks — ausstehend
7. Package Registry Checks (NPM, PyPI, Crates.io) — ausstehend

### Naming Lessons Learned
- **SANA** war zu schön — NVIDIA hat den Namen für ihr KI-Image/Video-Gen-Framework
- **ALMA** — AlmaLinux ist riesig (Enterprise Linux, CERN)
- **DORA** — EU-Verordnung 2022/2554 für Finanzsektor IT-Resilience
- **FRIEDA** — Frida.re Reverse-Engineering ist gut bekannt in Security-Community
- Irische Namen sind sicherer — weniger Tech-Kollisionen
- Akronyme müssen den universellen Charakter abbilden (nicht "lokal")

### Technical Architecture Notes
- Privacy-by-Design: ABSOLUTE Priorität
- Nur lokale LLMs (kein Datenabfluss)
- Plugin-basiert für Storage-Backends
- Lokale Datenbank mit Hash-Dedup
- MCP-Integration für KI-Steuerung
- Muss auf Raspberry Pi laufen können (leichtgewichtig)
