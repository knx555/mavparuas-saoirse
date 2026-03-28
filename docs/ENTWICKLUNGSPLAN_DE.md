# MAVPARUAS SAOIRSE — Enterprise-Entwicklungsplan

> Version 1.0 | 28.03.2026 | Autor: Walter Codecraft (knx555)

## 1. Zusammenfassung

**SAOIRSE** = **S**ynchronizing **A**ll **O**rigins with **I**ntelligent **R**ecognition, **S**orting & **E**xchange

MAVPARUAS SAOIRSE ist ein universelles Werkzeug zur Datei-Organisation, -Kategorisierung und -Synchronisation. Dieses Dokument definiert den phasenweisen Entwicklungsfahrplan von der rechtlichen Grundlage bis zum Produktionsrelease unter MIT-Lizenz.

**Kerntechnische Entscheidungen:**

1. Core Engine in **Rust** für Performance und Speichersicherheit
2. Plugin-Architektur kompatibel mit **MAVPARUAS-Ökosystem** (Perl, Python, C/C++, Rust)
3. **SQLite** als Standard-Datenbank, konfigurierbare Backends
4. **MIT-Lizenz** — keine Copyleft-Abhängigkeiten erlaubt
5. Plattformübergreifend: Linux (primär), Windows, macOS

## 2. Architekturübersicht

```text
┌─────────────────────────────────────────────────────┐
│                  Benutzeroberflächen                  │
│  ┌──────────┐  ┌──────────┐  ┌───────────────────┐  │
│  │   CLI    │  │   GUI    │  │    REST API       │  │
│  │ (Rust)   │  │ (Tauri)  │  │ (Actix-Web/Axum) │  │
│  └────┬─────┘  └────┬─────┘  └────────┬──────────┘  │
│       └──────────────┼─────────────────┘             │
│                      ▼                               │
│  ┌───────────────────────────────────────────────┐   │
│  │            Core Engine (Rust)                  │   │
│  │  Scanner · Rule Engine · Sync · Kategorien    │   │
│  │  Watch Service · Konfiguration                │   │
│  └───────────────────┬───────────────────────────┘   │
│                      ▼                               │
│  ┌───────────────────────────────────────────────┐   │
│  │          Plugin-System (FFI/HTTP)             │   │
│  │  Perl · Python · Rust · C++ · HTTP-Extern     │   │
│  └───────────────────┬───────────────────────────┘   │
│                      ▼                               │
│  ┌───────────────────────────────────────────────┐   │
│  │           Speicherschicht                     │   │
│  │  SQLite (Standard) · Redis · Cloud (S3/WebDAV)│   │
│  └───────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────┘
```

## 3. Entwicklungsphasen

### Phase 0: Grundlagen (Aktuell — Q1 2026)

| Aufgabe | Status | Anmerkungen |
| --- | --- | --- |
| Markenrecherche (TMView, EUIPO, DPMA, USPTO) | ERLEDIGT | Alle Datenbanken frei |
| Nizza-Klassifikations-Analyse | ERLEDIGT | Klasse 9 primär |
| Forensische Beweissicherung | ERLEDIGT | SHA-256 verifiziert |
| Nutzungsdokumentation | ERLEDIGT | Erste Einträge erfasst |
| MIT-Lizenz + README | ERLEDIGT | Zweisprachig EN/DE |
| GitHub-Repository | ERLEDIGT | knx555/mavparuas-saoirse |
| Entwicklungsplan | ERLEDIGT | Dieses Dokument |
| CI/CD-Pipeline | OFFEN | GitHub Actions |
| CONTRIBUTING.md + Verhaltenskodex | OFFEN | — |
| Sicherheitsrichtlinie (SECURITY.md) | OFFEN | — |

### Phase 1: Core Engine (Q2 2026)

**Ziel**: Minimaler funktionsfähiger Datei-Scanner + Rule Engine in Rust.

**Ergebnis**: CLI-Werkzeug das Verzeichnisse scannt, Regeln anwendet und Dateien kategorisiert.

### Phase 2: Plugin-System (Q3 2026)

**Ziel**: MAVPARUAS-kompatible Plugin-Architektur.

**Ergebnis**: Funktionierendes Plugin-System mit mindestens Rust + Python Plugins.

### Phase 3: Synchronisation (Q4 2026)

**Ziel**: Geräteübergreifende Datei-Synchronisation.

**Ergebnis**: Zuverlässige lokale + LAN-Dateisynchronisation.

### Phase 4: GUI & API (Q1 2027)

**Ziel**: Desktop-GUI + REST-API für Drittanbieter-Integration.

**Ergebnis**: Desktop-Anwendung + dokumentierte REST-API.

### Phase 5: Produktionsrelease (Q2 2027)

**Ziel**: v1.0 Release mit Sicherheitsaudit, Performance-Optimierung und Distributionspaketen.

## 4. Technologie-Entscheidungen

### Warum Rust für den Core

1. **Speichersicherheit** ohne Garbage Collection — kritisch für Dateioperationen
2. **Performance** vergleichbar mit C/C++ für I/O-intensive Workloads
3. **Plattformübergreifende** Kompilierung
4. **Starkes Typsystem** erkennt Fehler zur Kompilierzeit
5. **MIT/Apache-2.0 dual-lizenziert** — kompatibel mit Projektlizenz

### Warum SQLite als Standard

1. **Zero Configuration** — einzelne Datenbankdatei
2. **Eingebettet** — kein externer Service erforderlich
3. **Public Domain** — keine Lizenzbedenken

### GUI-Framework: Tauri

1. **Rust-Backend** — native Integration mit Core Engine
2. **Web-Frontend** — HTML/CSS/JS (kompatibel mit MAVPARUAS-Standards)
3. **MIT-Lizenz** — vollständig kompatibel

## 5. Qualitätsstandards

| Ebene | Werkzeug | Ziel |
| --- | --- | --- |
| Unit Tests | `cargo test` | 80%+ Abdeckung |
| Integration Tests | `cargo test --test` | Kritische Pfade |
| Performance | `criterion` Benchmarks | Regressionsschutz |
| Sicherheit | `cargo audit` + `cargo deny` | Null bekannte Schwachstellen |
| Linting | `clippy` + `rustfmt` | Null Warnungen |

## 6. Lizenz-Compliance

| Erlaubt | Verboten (ohne Genehmigung) |
| --- | --- |
| MIT, BSD, Apache 2.0, MPL 2.0, ISC | GPL, AGPL, LGPL, SSPL |

**Durchsetzung**: `cargo deny` in CI-Pipeline prüft alle Abhängigkeitslizenzen.

## 7. Risikomanagement

| Risiko | Auswirkung | Wahrscheinlichkeit | Gegenmaßnahme |
| --- | --- | --- | --- |
| Rust-Lernkurve für Beitragende | Mittel | Hoch | Gute Doku, Beispielcode |
| Plugin-Sandboxing-Komplexität | Hoch | Mittel | Start mit Subprocess-Isolation |
| Plattformübergreifende FS-Unterschiede | Mittel | Hoch | Abstraktion via Platform Layer |
| Scope Creep | Hoch | Mittel | Strikte Phasengates, MVP-Fokus |
| Copyleft-Kontamination | Kritisch | Niedrig | Automatische Lizenzprüfung in CI |

## 8. Meilensteine

| Meilenstein | Phase | Erfolgskriterium |
| --- | --- | --- |
| M0: Rechtliche Grundlage | 0 | Marke frei, Repo live, Plan dokumentiert |
| M1: Erster Scan | 1 | CLI scannt 10k Dateien in < 5s |
| M2: Rule Engine | 1 | 20+ Regeltypen, TOML-Konfiguration |
| M3: Plugin MVP | 2 | Rust + Python Plugin funktionsfähig |
| M4: Lokale Sync | 3 | Bidirektionale LAN-Sync |
| M5: Desktop-App | 4 | Tauri-App auf Linux |
| M6: v1.0 Release | 5 | Alle Tests bestanden, Doku komplett |

---

## Dokumentenhistorie

| Version | Datum | Autor | Änderungen |
| --- | --- | --- | --- |
| 1.0 | 28.03.2026 | Walter Codecraft | Initialplan |

---

*Detaillierte englische Version: [DEVELOPMENT-PLAN.md](DEVELOPMENT-PLAN.md)*
