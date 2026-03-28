# MAVPARUAS SAOIRSE

> Universelles Datei-Organisations- und Synchronisations-Werkzeug

[![Lizenz: MIT](https://img.shields.io/badge/Lizenz-MIT-blue.svg)](LICENSE)

## Überblick

MAVPARUAS SAOIRSE ist ein universelles Werkzeug zur Datei-Organisation, -Kategorisierung und -Synchronisation für Power-User und Enterprise-Umgebungen. Als Teil des [MAVPARUAS](https://github.com/knx555)-Ökosystems bringt SAOIRSE intelligentes Dateimanagement auf den Desktop — mit geplanter Unterstützung für geräteübergreifende Synchronisation und Plugin-basierte Erweiterbarkeit.

> **SAOIRSE** (Irisch: „Freiheit") — Benannt in irischer Tradition, als Ausdruck der Philosophie, Nutzern die volle Kontrolle und Freiheit über ihre Datei-Organisation zu geben.

## Projektstatus

### Phase: Rechtliche Grundlagen & Architekturplanung

Das Projekt befindet sich in der Initialisierungsphase mit Aufbau der rechtlichen und architektonischen Basis:

1. **Markenrecherche** — Vollständige internationale Markenrecherche (TMView, EUIPO, DPMA, USPTO) mit forensischer Beweissicherung
2. **Nizza-Klassifikations-Analyse** — Klasse 9 (primär), Klasse 42 (bedingt für SaaS)
3. **Architekturplanung** — Enterprise-Entwicklungsplan in Arbeit

## Geplante Funktionen

- Intelligente Datei-Kategorisierung mit regelbasierter und ML-unterstützter Sortierung
- Plattformübergreifende Synchronisation (Linux, Windows, macOS)
- Plugin-Architektur (Perl, Python, Rust, C/C++)
- Echtzeit-Dateisystem-Überwachung
- Konfigurierbare Storage-Backends (lokal, Cloud, hybrid)
- CLI- und GUI-Oberflächen
- REST-API für Drittanbieter-Integration

## Technologie-Stack

| Schicht | Technologie |
| --- | --- |
| Core Engine | Rust (performanzkritisch) |
| Plugin-System | MAVPARUAS Plugin-Architektur |
| Plugin-Sprachen | Perl, Python, C, C++, Rust |
| Kommunikation | HTTP APIs, FFI, IPC |
| Frontend (CLI) | Rust / Python |
| Frontend (GUI) | TBD (Tauri / GTK geplant) |
| Datenbank | Konfigurierbar (SQLite Standard) |

## Projektstruktur

```text
mavparuas-file-tool/
├── docs/
│   └── legal/                  # Markenrecherche & rechtliche Docs
│       ├── evidence/           # Forensische Beweise (Screenshots, Hashes)
│       ├── TRADEMARK-CLEARANCE-PROTOCOL_SAOIRSE_DE.md
│       ├── NIZZA-KLASSIFIKATIONS-ANALYSE_SAOIRSE_DE.md
│       └── NUTZUNGSDOKUMENTATION_SAOIRSE_DE.md
├── scripts/                    # Entwicklungs- & Hilfs-Skripte
├── walter-workspace/           # Projektmanagement (Walter Codecraft)
├── .gitignore
├── LICENSE                     # MIT-Lizenz
├── README.md                   # Englische Version
└── README_DE.md                # Diese Datei (Deutsch)
```

## Lizenz

Dieses Projekt steht unter der **MIT-Lizenz** — siehe [LICENSE](LICENSE) für Details.

**Lizenz-Philosophie**: MAVPARUAS SAOIRSE verwendet ausschließlich permissive Lizenzen (MIT, BSD, Apache 2.0). Copyleft-Abhängigkeiten (GPL, AGPL) sind ohne explizite Genehmigung nicht gestattet.

## Mitwirken

Beitragsrichtlinien werden veröffentlicht, sobald die initiale Architektur feststeht. Das Projekt folgt:

- Clean-Code-Standards mit aussagekräftiger Benennung
- Umfassendes Testing (Unit, Integration, Performance)
- Feature-Branch-Workflow mit strukturierten Commit-Messages
- Zweisprachige Dokumentation (Englisch + Deutsch)

## Autor

**knx555** — [GitHub-Profil](https://github.com/knx555)

Teil des **MAVPARUAS**-Projekt-Ökosystems.

---

*SAOIRSE — Freiheit im Dateimanagement.*
