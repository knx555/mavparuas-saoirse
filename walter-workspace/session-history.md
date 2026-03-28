# Session History — MAVPARUAS File Tool Project

## Session 2026-03-28 (Naming & Trademark Research)

### 17:00 — Projektkonzept besprochen
- Markus beschreibt ein universelles Datei-Organisations/Sync-Tool
- Privacy-by-Design ABSOLUT (mehr als DSGVO)
- Nur lokale LLMs für Datenanalyse
- MIT-Lizenz geplant
- MCP-steuerbar durch lokale KI
- Datenquellen: Nextcloud/WebDAV, OneDrive, Dropbox, USB, lokale SSDs, Hetzner Storage Box
- Plugin-basiert, modular, universell
- Datenbank lokal mit Hash-basierter Dedup
- Von überall nach überall synchronisieren/normalisieren

### 17:15 — Namensfindung Runde 1 (4 Kandidaten)
| Name | Ergebnis |
|---|---|
| FRIEDA | MITTEL — Frida (frida.re) Reverse-Engineering Toolkit |
| ALMA | HOCH — AlmaLinux (CentOS-Nachfolger, CERN, AWS) |
| DORA | HOCH — EU-Verordnung 2022/2554 + Google DORA Metrics + Nickelodeon |
| SELMA | NIEDRIG — Sauber, aber Akronym "Lokale Medien-Archive" passt nicht zum universellen Konzept |

### 17:35 — SANA Vorschlag von Markus
- SANA = Selfsorting Analytic Normalizing Algorithm
- ERGEBNIS: **RAUS** — NVIDIA NVlabs/Sana (5000+ Stars, ICLR 2025/2026 Oral) + Sana Commerce (Gartner MQ)
- Direkte Kollision im KI-Ökosystem

### 17:45 — Namensfindung Runde 2 (Irische + Deutsche Namen)
- Markus will der Aisling-Tradition folgen (irische Namen)
- Oder schöne altdeutsche Namen (Klara, Paula, Ottilie, Charlotte, etc.)

**Geprüfte Kandidaten:**
| Name | Bedeutung | Risiko |
|---|---|---|
| SAOIRSE | "Freiheit" (irisch) | NIEDRIG — Sauber! |
| ROISIN | "Kleine Rose" (irisch) | NIEDRIG — Sauber! |
| NIAMH | "Die Strahlende" (irisch) | NIEDRIG — Sauber |
| AOIFE | "Schön, Strahlend" (irisch) | NIEDRIG — Sauber |
| LUISE | "Die Weise" (deutsch) | NIEDRIG — Sauber |
| DARA | "Die Eiche" (irisch) | MITTEL-HOCH — causalens/dara (406 Stars) |

### 17:55 — Markus wählt Favoriten
**Top 2 (in Prüfung):**
1. **SAOIRSE** = Synchronizing All Origins with Intelligent Recognition, Sorting & Exchange
2. **ROISIN** = Remote & Onsite Integrated Synchronization, Indexing & Normalization

**Begründung Markus:**
- Aussprache-Charme (wie bei Aisling) — nicht sofort lesbar, aber leicht sprechbar
- SAOIRSE: "Freiheit" passt perfekt zum Konzept (Freiheit von Daten-Silos)
- ROISIN: Persönlicher Favorit-Name
- LUISE schön, passt aber nicht so gut
- SELMA-Akronym passt nicht (zu lokal)

### 18:00 — Tiefe Markenrecherche gestartet

**EUIPO (EU-Markenamt) — ERLEDIGT:**
- SAOIRSE: **0 Marken, 0 Designs** — KOMPLETT FREI
- ROISIN: **0 Ergebnisse** — KOMPLETT FREI

**DPMA (Deutsches Patent- und Markenamt) — ERLEDIGT:**
- SAOIRSE: **0 Marken, 0 Designs** (2 irrelevante Patente) — KOMPLETT FREI
- ROISIN: 12 Treffer, aber NUR Personen-/Firmennamen in Mode/Wein (z.B. "HIRO BY ROISIN", "RÓISÍN PIERCE", "Fleur de Roisin 12"). Keine alleinstehende Marke "ROISIN". 5 davon abgelaufen. — **EFFEKTIV FREI**

**USPTO (US-Markenamt) — ERLEDIGT:**
- SAOIRSE: **"No results found"** — KOMPLETT FREI
- ROISIN: **"No results found"** — KOMPLETT FREI

**DOMAINS — ERLEDIGT:**
| Domain | SAOIRSE | ROISIN |
|---|---|---|
| .io | BESETZT | **FREI** |
| .dev | FREI (keine DNS) | **FREI** |
| .org | BESETZT | BESETZT |
| .com | BESETZT | unklar (SERVFAIL) |

**PACKAGE REGISTRIES — ERLEDIGT:**
| Registry | SAOIRSE | ROISIN |
|---|---|---|
| NPM | BESETZT (abandoned, 0 Downloads, 4J) | **FREI** |
| PyPI | FREI | FREI |
| Crates.io | FREI | FREI |

**APP STORES — ERLEDIGT:**
- Keine relevanten Apps unter SAOIRSE oder ROISIN

**GESAMTBEWERTUNG:**
- ROISIN: Technisch bessere Verfügbarkeit (Domains .io+.dev frei, NPM frei, alles frei)
- SAOIRSE: Sauberste Marken-Situation (null Treffer überall), aber schlechtere Domain/NPM-Lage
- BEIDE markenrechtlich sicher für Software-Nutzung

### 18:16 — FINALE ENTSCHEIDUNG: SAOIRSE

**Markus wählt SAOIRSE.**

**Strategische Begründung (Zitat Markus, 18:16:34):**
> "Ich möchte überhaupt gar keine Markenrechtssituationen herbeiführen und ich werde das
> niemals auf einer einzelnen Domain oder irgendwas bewerben. Sondern es wird immer im
> Kontext von MAVPARUAS eingesetzt werden. Es ist immer nur ein Modul, ein Programm,
> ein Plugin, ein VST, ein VSTFX oder irgendwas. Eine DLL. Es wird immer nur ein Modul
> oder irgendetwas. Ein Konstrukt von etwas großem."

**Konsequenzen dieser Strategie:**
- Domain-Verfügbarkeit IRRELEVANT — kein eigenständiger Webauftritt geplant
- NPM-Besetzung IRRELEVANT — Package wird `@mavparuas/saoirse` oder `mavparuas-saoirse`
- Markenrecht IRRELEVANT — kein eigenständiger Markenauftritt, nur MAVPARUAS-Komponente
- Naming-Pattern: `mavparuas-saoirse`, `MAVPARUAS::SAOIRSE`, `saoirse-plugin` etc.

**SAOIRSE = Synchronizing All Origins with Intelligent Recognition, Sorting & Exchange**

### 18:18 — Marketing-Strategie klargestellt

Markus stellt klar: SAOIRSE wird durchaus namentlich genannt (YouTube, Docs, etc.),
aber IMMER im MAVPARUAS-Kontext. Beispiele:
- "MAVPARUAS SAOIRSE bietet Ihnen..."
- "Hier sehen Sie SAOIRSE im Einsatz"
- Nie ohne Software-Kontext, nie als eigenständige Marke

Aussprache: "Sorsha" (irisch) — so wird es in Videos/Marketing gesprochen.
Markenrechtliche Einordnung: Deskriptiv-Marketing wie "Adobe Photoshop" — Nizza-Klasse Software, keine Kollision mit gleichnamigen Produkten anderer Branchen.

### 18:20 — Leitprotokoll für Markenrechtliche Absicherung

Markus beauftragt die Erstellung eines formalen Trademark Clearance Protocols:

**Zitat Markus (18:20:18):**
> "Lasst uns ein Leitprotokoll ableiten, warum wir diesen Namen gewählt haben.
> Ein rechtssicheres Protokoll, verbatim bei der Formulierung.
> Damit wir einem Richter im schlimmsten Fall sagen können: Wir haben uns
> wirklich bemüht, wir wollten kein Recht brechen."

Erstellt: `docs/legal/TRADEMARK-CLEARANCE-PROTOCOL_SAOIRSE_DE.md`
- 11 Abschnitte, vollständige Good-Faith-Dokumentation
- Verbatim-Zitate aller Markus-Entscheidungen
- Risikobewertung, Nizza-Klassifikation, Nutzungsformen
- 7 Vertiefungs-Tasks (T-001 bis T-007)

### 18:25 — TMView Internationale Markenrecherche (T-001 ERLEDIGT)

Nachträgliche Prüfung über TMView (EUIPO + 70 internationale Ämter):
- **16 Treffer weltweit** für "SAOIRSE"
- **0 Treffer in Nizza-Klasse 9 (Software)**
- **0 aktive Treffer in Klasse 42 (IT-Dienstleistungen)** — 1 erloschen seit 2000
- Alle aktiven Marken in branchenfremden Klassen: Bekleidung (25), Getränke (32/33), Kosmetik (3), Leder (18), Unterhaltung (41)
- Protokoll um Abschnitt 4.8 ergänzt mit vollständiger Analyse aller 16 Treffer

**Ergebnis: SAOIRSE international für Software BESTÄTIGT FREI**

### Offene Tasks aus dem Protokoll
1. ~~T-001: WIPO/TMView~~ → **ERLEDIGT**
2. T-002: Anwaltliche Ähnlichkeitsrecherche (MITTEL)
3. ~~T-003: Benutzungsdokumentation~~ → **ERLEDIGT** (Usage Documentation Template DE+EN erstellt)
4. T-004: Eigene Markenanmeldung prüfen (NIEDRIG)
5. T-005: Markenüberwachung einrichten (NIEDRIG)
6. ~~T-006: Screenshots/Archivierung~~ → **ERLEDIGT** (4 PNGs + Evidence-Index mit SHA-256)
7. ~~T-007: Nizza-Klassifikation~~ → **ERLEDIGT** (Tiefenanalyse DE+EN, 7 Klassen geprüft)

### 18:40 — Evidence-Archivierung (T-006)
- Playwright-basierte Screenshots mit forensischem Evidence-Banner
- Banner enthält: Projekt, Datenbank, Suchbegriff, URL, ISO-Timestamp, GitHub knx555, Quell-IP
- KEINE persönlichen Namen — Privacy-by-Design auch bei Evidence
- TMView (349 KB), DPMA (80 KB), USPTO (166 KB) → alle erfolgreich
- EUIPO erstmal Timeout → Retry-Skript → 175 KB erfolgreich (19:10)
- Evidence-Index mit SHA-256 Hashes erstellt

### 19:00 — Forensische Sauberkeit als Grundprinzip (Markus)
Markus fordert explizit: "forensisch und juristisch extrem sauber arbeiten"
Prinzip in 3 Stellen verankert: project-learning.md, team-profiles.md, User-Memory

### 19:06 — Nizza-Klassifikations-Analyse (T-007)
- Tiefenanalyse basierend auf NCL 12. Ausgabe (2023)
- **Klasse 9**: PRIMÄR — Herunterladbare Software (NCL 090717, 090658, 090949)
- **Klasse 42**: BEDINGT — Nur bei SaaS/gehosteter Version, empfohlen für vorsorgliche Anmeldung
- **Klasse 38**: NICHT ANWENDBAR — SAOIRSE nutzt Netze, stellt keine bereit
- **Klasse 35**: NICHT ANWENDBAR — Selbstbetriebenes Tool, kein Dienst für Dritte
- Klassen 39, 41, 45: Ebenfalls nicht anwendbar
- Empfohlene Anmeldung: Klasse 9 + 42 (DPMA ~290€, EUIPO ~900€)
- Dokumentiert in DE + EN

### 19:10 — Usage Documentation Template (T-003)
- Nutzungsdokumentations-Template erstellt (DE + EN)
- Meilenstein-Checkliste, automatisierte Nachweisquellen
- Erste 4 Einträge bereits dokumentiert (28.03.2026)

### 19:18 — Markus Feedback & Auftrag
Markus ist begeistert von der juristisch-technischen Ableitung.
Auftrag: Enterprise Development Plan + Walter-Workspace Reorganisation.
Markus geht einkaufen.

### 19:20 — GitHub Repository Erstellung
- Markus autorisiert neue Repository-Erstellung auf GitHub
- .gitignore erstellt (.venv, __pycache__, node_modules, etc.)
- README.md (EN) + README_DE.md erstellt
- MIT LICENSE erstellt (Copyright 2026 knx555)
- Git init → Branch main → Initial Commit (24 Dateien, 2.635 Zeilen)
- GitHub Repo: knx555/mavparuas-saoirse (public)
- Push mit -u origin main erfolgreich

### 19:35 — Enterprise Development Plan
- docs/DEVELOPMENT-PLAN.md (EN): 10 Abschnitte, 5 Phasen (Q1 2026 → Q2 2027)
- docs/ENTWICKLUNGSPLAN_DE.md: Deutsche Kurzversion
- Architektur: Rust Core + MAVPARUAS Plugin System + SQLite
- Qualitätsstandards: 80%+ Coverage, cargo audit, cargo deny
- Risikomanagement: 6 Risiken mit Gegenmaßnahmen
- Meilensteine M0-M6 definiert

### 19:45 — Walter-Workspace Reorganisation
- INDEX.md: Zentraler Navigations-Hub mit Status-Dashboard
- backlog.md: Product Backlog (MoSCoW, Phase 0-2, 30+ Items)
- architecture-decisions.md: 6 ADRs (Rust, SQLite, MIT, Tauri, Plugins, SAOIRSE)
- sprint-log.md: Sprint-Tracking (Sprint 0 complete, Sprint 1-2 geplant)

### 19:40 — Repo-Umbenennung zu VERSALIEN-Standard
- Markus bemerkt: Repo-Name war lowercase `mavparuas-saoirse`
- VERSALIEN ist Standard seit KLARA (alle Repos: MAVPARUAS-xxx)
- `gh repo rename MAVPARUAS-SAOIRSE --yes` → erfolgreich
- Git Remote automatisch aktualisiert

### 19:42 — Architektur-Umstellung (Markus-Direktive)
**Rust-First Philosophie:**
- Rust = Primärsprache für ALLE Logik (Backend, Sync, Plugins, CLI, API)
- Python = NUR für KI/ML (nur wenn kein ONNX-Export / kein Rust-Äquivalent)
- TypeScript + Electron = GUI ONLY (reine Präsentationsschicht)
- **Tauri ist RAUS** — Electron bietet bessere Accessibility + reiferes Ökosystem
- Rust Sidecar via IPC (JSON-RPC) für alle Business-Logik hinter der GUI
- `ort` Crate für Rust-nativen ONNX-Inference statt PyO3

### 19:44 — Markus geht einkaufen, Auftrag: Aufwendige Sprint-Planung
**Zitat**: "Lass dir bitte Zeit. Schreib das sehr aufwendig. Mach gleich Milestones.
Mach gleich am besten Sprints. Strukturier das logisch."
**Erlaubnis**: Subagents beauftragen, 20+ Minuten nehmen, alles nutzen

### 19:44 – 20:30 — Systematische Dokumentations-Überarbeitung
Alle Projektdokumente auf Rust-First + Electron Architektur aktualisiert:

1. **DEVELOPMENT-PLAN.md** (EN) → Komplett-Rewrite v1.1 (~700 Zeilen)
   - 21 Sprints (S0.3 → S21), 5 Phasen, 10 Milestones (M0-M10)
   - Rust-First Philosophy mit Sprachhierarchie-Tabelle
   - Detaillierte Sprint-Tasks mit Acceptance Criteria
   - Sprint-Kalender mit Datumsangaben (April 2026 → Jan 2027)
   - 10-Punkte Risiko-Register (inkl. Electron Binary Size, ONNX-Gaps)

2. **ENTWICKLUNGSPLAN_DE.md** (DE) → Komplett-Rewrite v1.1
   - Spiegelt EN-Version in Deutsch, eigene Sprint-Übersichtstabellen
   - "Python-Grenze" und "Grenzregel" Abschnitte

3. **architecture-decisions.md** → Major Update
   - ADR-004: Tauri→Electron komplett umgeschrieben (Akzeptiert)
   - NEU ADR-007: Rust-First Entwicklungsphilosophie
   - NEU ADR-008: Privacy-by-Design & Lokale KI
   - ADR-005: PyO3 → ONNX/Subprocess

4. **README.md + README_DE.md** → Tech-Stack-Tabellen aktualisiert
   - Rust-First, Electron+TypeScript für GUI, Python (AI only)

5. **INDEX.md** → Repo-Link zu VERSALIEN korrigiert

6. **backlog.md** → Komplett-Rewrite (55+ Items mit Sprint-Zuordnung)
   - Phase-Headers mit Architektur-Annotationen
   - Phase 2: PyO3 → ONNX/`ort`, Phase 4: Tauri → Electron

7. **sprint-log.md** → Komplett-Rewrite
   - Sprint-Kalender-Übersicht (21 Sprints)
   - Sprint 0 mit vollständiger Task-Liste (DONE)
   - Sprint 0.3, 1, 2 mit geplanten Tasks

### Phase 0 Status: VOLLSTÄNDIG ABGESCHLOSSEN (inkl. Architektur-Overhaul)

### Kernkonzept des Tools
- Universelle Datei-Organisation über alle Speicherorte hinweg
- Plugin-System für verschiedene Backends (Nextcloud, OneDrive, Dropbox, Hetzner, lokal)
- Lokale Datenbank mit Hash-Dedup
- Lokale KI für intelligente Sortierung (ONNX via `ort`, Rust-nativ)
- Keine Daten fließen nach außen (Privacy-by-Design, ADR-008)
- MCP-steuerbar
- Von-überall-nach-überall Sync/Normalisierung
- **Architektur**: Rust-First, Electron GUI (Präsentation), Python nur KI/ML
