# MAVPARUAS SAOIRSE — Enterprise-Entwicklungsplan

> Version 1.1 | 28.03.2026 | Autor: Walter Codecraft (knx555)

## 1. Zusammenfassung

**SAOIRSE** = **S**ynchronizing **A**ll **O**rigins with **I**ntelligent **R**ecognition, **S**orting & **E**xchange

MAVPARUAS SAOIRSE ist ein universelles Werkzeug zur Datei-Organisation, -Kategorisierung und -Synchronisation. Dieses Dokument definiert den phasenweisen Entwicklungsfahrplan von der rechtlichen Grundlage bis zum Produktionsrelease unter MIT-Lizenz.

**Zentrale Architektur-Prinzipien:**

1. **Rust-First** — ALLE Logik, Routing, Geschäftslogik und Backend in Rust
2. **Python** — NUR wenn unbedingt nötig (KI/ML-Bibliotheken ohne Rust-Äquivalent)
3. **Electron + TypeScript** — GUI-Präsentationsschicht AUSSCHLIESSLICH (keine Geschäftslogik im Frontend)
4. Plugin-Architektur kompatibel mit **MAVPARUAS-Ökosystem** (Perl, Python, C/C++, Rust)
5. **SQLite** als Standard-Datenbank, konfigurierbare Backends
6. **MIT-Lizenz** — keine Copyleft-Abhängigkeiten erlaubt
7. Plattformübergreifend: Linux (primär), Windows, macOS

## 2. Entwicklungsphilosophie: Rust-First

### 2.1 Sprachhierarchie

SAOIRSE folgt einer strikten **Rust-First** Entwicklungsphilosophie. Jede Komponente wird in Rust implementiert, es sei denn es gibt einen nachgewiesenen, dokumentierten Grund dagegen.

| Priorität | Sprache | Rolle | Grenze |
| --- | --- | --- | --- |
| 1 (Primär) | **Rust** | Core Engine, Geschäftslogik, Routing, API, Sync, Plugins, CLI | Alles standardmäßig |
| 2 (Nur KI) | **Python** | KI/ML-Inferenz, Modell-Loading, NLP-Pipelines | NUR wenn kein Rust-Crate existiert |
| 3 (Nur GUI) | **TypeScript** | Electron GUI — Präsentationsschicht | NUR Rendering & Benutzerinteraktion |

### 2.2 Entscheidungskriterien für Nicht-Rust-Code

Bevor IRGENDEIN Nicht-Rust-Code geschrieben wird, muss dokumentiert werden:

1. **Python**: Welche spezifische KI/ML-Bibliothek wird benötigt? Gibt es ein Rust-Äquivalent (`candle`, `burn`, `ort`)? Wenn ja → Rust verwenden. Wenn nein → Python via Subprocess, isoliert.
2. **TypeScript**: Handelt es sich rein um UI-Rendering oder Benutzerinteraktion? Wenn ja → TypeScript in Electron. Bei JEGLICHER Logik, Validierung, Routing oder Datentransformation → muss in Rust-Backend.

### 2.3 Grenzregel

Wenn es als Rust-Funktion ausgedrückt werden kann → MUSS es in Rust sein. Die TypeScript-Schicht ist eine dünne Präsentationshülle, die Daten rendert und Benutzeraktionen via IPC an Rust sendet.

## 3. Architekturübersicht

```text
┌──────────────────────────────────────────────────────────┐
│                  Benutzeroberflächen                       │
│  ┌──────────┐  ┌───────────────────┐  ┌───────────────┐  │
│  │   CLI    │  │       GUI         │  │   REST API    │  │
│  │  (Rust)  │  │  (Electron + TS)  │  │ (Axum/Rust)   │  │
│  │          │  │  Nur Präsentation │  │               │  │
│  └────┬─────┘  └───────┬───────────┘  └──────┬────────┘  │
│       │                │ IPC                  │           │
│       └────────────────┼──────────────────────┘           │
│                        ▼                                  │
│  ┌────────────────────────────────────────────────────┐   │
│  │              Core Engine (Rust)                     │   │
│  │  Scanner · Rule Engine · Sync · Kategorien         │   │
│  │  Watch Service · Konfiguration · MCP Server        │   │
│  │  KI-Orchestrator (Rust → Python nur bei Bedarf)    │   │
│  └───────────────────┬────────────────────────────────┘   │
│                      ▼                                    │
│  ┌────────────────────────────────────────────────────┐   │
│  │           Plugin-System (FFI/HTTP)                 │   │
│  │  Rust (nativ) · Python (nur KI) · C++ (FFI)       │   │
│  │  HTTP/Extern (beliebige Sprache)                   │   │
│  └───────────────────┬────────────────────────────────┘   │
│                      ▼                                    │
│  ┌────────────────────────────────────────────────────┐   │
│  │           Speicherschicht                          │   │
│  │  SQLite (Standard) · Redis (optional)              │   │
│  │  Cloud (WebDAV/S3/Hetzner Storage Box)             │   │
│  └────────────────────────────────────────────────────┘   │
└──────────────────────────────────────────────────────────┘
```

## 4. Entwicklungsphasen & Sprint-Übersicht

### Phase 0: Grundlagen (Q1 2026) — ABGESCHLOSSEN

| Sprint | Aufgabe | Status |
| --- | --- | --- |
| S0.1 | Markenrecherche (TMView, EUIPO, DPMA, USPTO) | ERLEDIGT |
| S0.1 | Nizza-Klassifikations-Analyse | ERLEDIGT |
| S0.1 | Forensische Beweissicherung (SHA-256) | ERLEDIGT |
| S0.1 | Nutzungsdokumentation | ERLEDIGT |
| S0.2 | MIT-Lizenz + README (bilingual EN/DE) | ERLEDIGT |
| S0.2 | GitHub-Repository | ERLEDIGT |
| S0.2 | Enterprise-Entwicklungsplan (EN/DE) | ERLEDIGT |
| S0.2 | Walter-Workspace Reorganisation | ERLEDIGT |
| S0.3 | CI/CD-Pipeline (GitHub Actions) | OFFEN |
| S0.3 | CONTRIBUTING.md + Verhaltenskodex | OFFEN |
| S0.3 | Sicherheitsrichtlinie (SECURITY.md) | OFFEN |

### Phase 1: Core Engine (Q2 2026) — 6 Sprints

**Ziel**: Produktionsreifer Datei-Scanner, Rule Engine und CLI — 100% Rust.

| Sprint | Wochen | Fokus | Ergebnis |
| --- | --- | --- | --- |
| S1 | W1-2 | Cargo Workspace + Konfiguration | Multi-Crate Projektstruktur |
| S2 | W3-4 | Datei-Scanner + Hashing | Async-Scanner, BLAKE3-Dedup |
| S3 | W5-6 | Rule Engine | TOML-basiert, 15+ Regeltypen |
| S4 | W7-8 | Speicher + Kategorien | SQLite, Tags, Suche |
| S5 | W9-10 | CLI + Testing | clap-Subcommands, 80%+ Coverage |
| S6 | W11-12 | Watch-Modus + MCP + Polish | inotify, MCP-Interface |

**Ergebnis**: CLI-Werkzeug das Verzeichnisse scannt, Regeln anwendet, kategorisiert und überwacht.

### Phase 2: Plugin-System & KI-Integration (Q3 2026) — 4 Sprints

**Ziel**: MAVPARUAS-kompatible Plugin-Architektur + lokale KI-Klassifikation.

| Sprint | Wochen | Fokus | Ergebnis |
| --- | --- | --- | --- |
| S7 | W13-14 | Plugin-Architektur | Trait, Sandboxing, SDK |
| S8 | W15-16 | KI-Klassifikation (Rust) | ONNX via `ort`, Embeddings |
| S9 | W17-18 | Externe Plugin-Bridges | HTTP, Perl, C/C++ FFI |
| S10 | W19-20 | KI-Plugins + Integration | Auto-Kategorisierung, Duplikate |

**Python-Grenze**: Python wird NUR eingesetzt wenn ein spezifisches KI-Modell keinen ONNX-Export hat und nicht via Rust's `ort` oder `candle` laufen kann.

**Ergebnis**: Plugin-System mit Rust-nativer KI-Klassifikation und MAVPARUAS-Kompatibilität.

### Phase 3: Synchronisation (Q4 2026) — 4 Sprints

**Ziel**: Geräteübergreifende Datei-Synchronisation — alle Logik in Rust.

| Sprint | Wochen | Fokus | Ergebnis |
| --- | --- | --- | --- |
| S11 | W21-22 | Sync-Protokoll | Spezifikation, Konfliktstrategie |
| S12 | W23-24 | Lokale + LAN-Sync | mDNS, TLS, Peer-to-Peer |
| S13 | W25-26 | Cloud-Backends | WebDAV, S3, Hetzner |
| S14 | W27-28 | Sync-Härtung | E2E-Verschlüsselung, Multi-Remote |

**Ergebnis**: Zuverlässige lokale + LAN + Cloud Dateisynchronisation mit Verschlüsselung.

### Phase 4: Desktop-GUI & REST-API (Q1 2027) — 4 Sprints

**Ziel**: Electron Desktop-App (TypeScript Frontend, Rust Backend via IPC) + öffentliche REST-API.

| Sprint | Wochen | Fokus | Ergebnis |
| --- | --- | --- | --- |
| S15 | W29-30 | REST-API | OpenAPI 3.1, Axum, JWT |
| S16 | W31-32 | Electron-Scaffold | Rust-Sidecar, IPC-Bridge |
| S17 | W33-34 | Kern-GUI-Views | Dateibrowser, Regel-Editor |
| S18 | W35-36 | Cross-Platform + Polish | Accessibility, Installer |

**Ergebnis**: Plattformübergreifende Electron Desktop-App mit barrierefreier UI + dokumentierte REST-API.

### Phase 5: Produktionsrelease (Q2 2027) — 3 Sprints

**Ziel**: v1.0 — sicherheitsgeprüft, optimiert, verteilt.

| Sprint | Wochen | Fokus | Ergebnis |
| --- | --- | --- | --- |
| S19 | W37-38 | Sicherheit + Performance | OWASP-Audit, Fuzzing |
| S20 | W39-40 | Dokumentation + Distribution | crates.io, AUR, Homebrew |
| S21 | W41-42 | Release Engineering | v1.0.0 Final |

## 5. Technologie-Entscheidungen

### 5.1 Warum Rust für den Core (und fast alles andere)

1. **Speichersicherheit** ohne Garbage Collection
2. **Performance** auf C/C++-Niveau
3. **Plattformübergreifende** Kompilierung
4. **Starkes Typsystem** erkennt Fehler zur Kompilierzeit
5. **Single-Binary** Deployment — keine Runtime-Abhängigkeiten
6. **MIT/Apache-2.0** dual-lizenziert — kompatibel mit Projektlizenz

### 5.2 Warum Electron + TypeScript für GUI (nicht Tauri)

1. **Reifes Ökosystem** — bewährt für komplexe Desktop-Anwendungen
2. **TypeScript** — Typsicherheit für die Präsentationsschicht
3. **Rust-Sidecar** — ALLE Geschäftslogik als separater Rust-Prozess
4. **Barrierefreiheit** — exzellente Screen-Reader-Unterstützung via Chromium
5. **Cross-Platform** — konsistentes Rendering auf Linux/Windows/macOS
6. **MIT-Lizenz** — vollständig kompatibel

### 5.3 Warum SQLite als Standard

1. **Zero Configuration** — einzelne Datenbankdatei
2. **Eingebettet** — kein externer Service erforderlich
3. **Public Domain** — keine Lizenzbedenken

### 5.4 Python: Strikt nur für KI/ML

| Erlaubt | Verboten |
| --- | --- |
| KI-Modell-Inferenz (kein ONNX-Export verfügbar) | Geschäftslogik |
| NLP-Pipelines (spaCy, transformers) | Dateioperationen |
| Benutzerdefinierte Trainings-Skripte | Konfiguration |
| ML-Experiment-Notebooks | API-Endpunkte |

**Durchsetzung**: Python-Code lebt NUR im `plugins/ai/`-Verzeichnis.

## 6. Qualitätsstandards

| Ebene | Werkzeug | Ziel |
| --- | --- | --- |
| Unit Tests | `cargo test` | 80%+ Abdeckung |
| Integration Tests | `cargo test --test` | Kritische Pfade |
| Property-Based | `proptest` | Parser + Rule Engine |
| Performance | `criterion` Benchmarks | Regressionsschutz |
| Fuzzing | `cargo fuzz` | Datei-Parsing, Regel-Parsing |
| Sicherheit | `cargo audit` + `cargo deny` | Null Schwachstellen |
| Linting | `clippy` + `rustfmt` | Null Warnungen |
| GUI Tests | Playwright | Kritische User-Flows |

## 7. Lizenz-Compliance

| Erlaubt | Verboten (ohne Genehmigung) |
| --- | --- |
| MIT, BSD, Apache 2.0, MPL 2.0, ISC | GPL, AGPL, LGPL, SSPL |

## 8. Meilensteine

| ID | Meilenstein | Phase | Sprint | Zieldatum | Status |
| --- | --- | --- | --- | --- | --- |
| M0 | Rechtliche Grundlage | 0 | S0.1-S0.2 | 28.03.2026 | ERLEDIGT |
| M0.5 | CI/CD + Community | 0 | S0.3 | 04.04.2026 | OFFEN |
| M1 | Erster Scan | 1 | S1-S2 | 25.04.2026 | OFFEN |
| M2 | Rule Engine komplett | 1 | S3-S4 | 23.05.2026 | OFFEN |
| M3 | CLI v0.1 Release | 1 | S5-S6 | 20.06.2026 | OFFEN |
| M4 | Plugin MVP | 2 | S7-S8 | 18.07.2026 | OFFEN |
| M5 | KI-Klassifikation | 2 | S9-S10 | 15.08.2026 | OFFEN |
| M6 | Lokale Sync | 3 | S11-S12 | 12.09.2026 | OFFEN |
| M7 | Cloud Sync | 3 | S13-S14 | 10.10.2026 | OFFEN |
| M8 | REST API | 4 | S15 | 24.10.2026 | OFFEN |
| M9 | Desktop-App (Electron) | 4 | S16-S18 | 05.12.2026 | OFFEN |
| M10 | v1.0 Release | 5 | S19-S21 | 30.01.2027 | OFFEN |

## 9. Risikomanagement

| ID | Risiko | Auswirkung | Wahrscheinlichkeit | Gegenmaßnahme |
| --- | --- | --- | --- | --- |
| R1 | Rust-Lernkurve | Mittel | Hoch | Umfassende Doku, Beispielcode |
| R2 | Plugin-Sandboxing-Komplexität | Hoch | Mittel | Start mit Subprocess-Isolation |
| R3 | Plattformübergreifende FS-Unterschiede | Mittel | Hoch | Abstraktion via Platform Layer |
| R4 | Scope Creep | Hoch | Mittel | Strikte Phasengates, MVP-Fokus |
| R5 | Copyleft-Kontamination | Kritisch | Niedrig | `cargo deny` in CI |
| R6 | Electron Binary-Größe | Mittel | Mittel | Tree-Shaking, Lazy Loading |
| R7 | ONNX-Modell Kompatibilitätslücken | Mittel | Mittel | Python-Fallback verfügbar |
| R8 | KI-Genauigkeit bei Kategorisierung | Mittel | Hoch | Konfigurierbarer Schwellenwert |

---

## Dokumentenhistorie

| Version | Datum | Autor | Änderungen |
| --- | --- | --- | --- |
| 1.0 | 28.03.2026 | Walter Codecraft | Initialplan |
| 1.1 | 28.03.2026 | Walter Codecraft | Rust-First Architektur, Electron GUI (ersetzt Tauri), detaillierte Sprint-Aufgliederung, KI-Strategie, erweiterte Meilensteine |

---

*Detaillierte englische Version: [DEVELOPMENT-PLAN.md](DEVELOPMENT-PLAN.md)*
