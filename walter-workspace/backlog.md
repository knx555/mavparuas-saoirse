# Product Backlog — MAVPARUAS SAOIRSE

> Priorisiert nach MoSCoW | Aktualisiert: 2026-03-28

## Phase 0: Foundation (Aktuell)

| ID | Priorität | Titel | Status |
| --- | --- | --- | --- |
| B-001 | MUST | Trademark Clearance (4 Datenbanken) | DONE |
| B-002 | MUST | Nice Classification Analysis | DONE |
| B-003 | MUST | Evidence Archival (forensisch) | DONE |
| B-004 | MUST | Usage Documentation Template | DONE |
| B-005 | MUST | GitHub Repository + MIT License | DONE |
| B-006 | MUST | Enterprise Development Plan | DONE |
| B-007 | SHOULD | CI/CD Pipeline (GitHub Actions) | OPEN |
| B-008 | SHOULD | CONTRIBUTING.md | OPEN |
| B-009 | SHOULD | SECURITY.md | OPEN |
| B-010 | SHOULD | CODE_OF_CONDUCT.md | OPEN |
| B-011 | COULD | GitHub Issue Templates | OPEN |
| B-012 | COULD | PR Template | OPEN |

## Phase 1: Core Engine (Q2 2026)

| ID | Priorität | Titel | Status |
| --- | --- | --- | --- |
| B-100 | MUST | Rust Cargo workspace scaffold | OPEN |
| B-101 | MUST | Async file scanner (tokio) | OPEN |
| B-102 | MUST | Rule engine (TOML-Konfiguration) | OPEN |
| B-103 | MUST | Category manager (Tags, Metadata) | OPEN |
| B-104 | MUST | SQLite storage backend | OPEN |
| B-105 | MUST | CLI (clap) | OPEN |
| B-106 | MUST | Unit + integration tests | OPEN |
| B-107 | SHOULD | Configuration system (TOML) | OPEN |
| B-108 | SHOULD | inotify filesystem monitoring | OPEN |
| B-109 | COULD | Performance benchmarks (criterion) | OPEN |

## Phase 2: Plugin System (Q3 2026)

| ID | Priorität | Titel | Status |
| --- | --- | --- | --- |
| B-200 | MUST | Plugin trait/interface | OPEN |
| B-201 | MUST | Rust native plugin loading | OPEN |
| B-202 | MUST | Python plugin bridge (PyO3) | OPEN |
| B-203 | SHOULD | Perl plugin bridge | OPEN |
| B-204 | SHOULD | C/C++ FFI bridge | OPEN |
| B-205 | SHOULD | HTTP external plugin protocol | OPEN |
| B-206 | MUST | Plugin sandboxing | OPEN |
| B-207 | SHOULD | Example plugins (3+ Sprachen) | OPEN |

## Phase 3-5: Sync, GUI, Release

Detailliert im [Development Plan](../docs/DEVELOPMENT-PLAN.md).

---

*Legende: MUST = Muss für MVP, SHOULD = Wichtig, COULD = Optional, WONT = Nicht in dieser Phase*
