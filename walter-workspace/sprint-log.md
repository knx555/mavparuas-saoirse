# Sprint Log — MAVPARUAS SAOIRSE

> Agile Sprint Tracking | Format: 2-Wochen-Sprints (ab Phase 1)

## Sprint-Kalender Übersicht

| Sprint | Phase | Wochen | Zeitraum (ca.) | Fokus |
| --- | --- | --- | --- | --- |
| S0.1-S0.2 | Phase 0 | — | 28.03.2026 | Foundation (DONE) |
| S0.3 | Phase 0 | W0 | 29.03. – 04.04.2026 | CI/CD + Community |
| S1 | Phase 1 | W1-2 | 05.04. – 18.04.2026 | Cargo Workspace + Config |
| S2 | Phase 1 | W3-4 | 19.04. – 02.05.2026 | File Scanner + Hashing |
| S3 | Phase 1 | W5-6 | 03.05. – 16.05.2026 | Rule Engine |
| S4 | Phase 1 | W7-8 | 17.05. – 30.05.2026 | Storage + Categories |
| S5 | Phase 1 | W9-10 | 31.05. – 13.06.2026 | CLI + Testing |
| S6 | Phase 1 | W11-12 | 14.06. – 27.06.2026 | Watch Mode + MCP |
| S7 | Phase 2 | W13-14 | 28.06. – 11.07.2026 | Plugin Architecture |
| S8 | Phase 2 | W15-16 | 12.07. – 25.07.2026 | AI Classification (Rust) |
| S9 | Phase 2 | W17-18 | 26.07. – 08.08.2026 | External Plugin Bridges |
| S10 | Phase 2 | W19-20 | 09.08. – 22.08.2026 | AI Plugins + Integration |
| S11 | Phase 3 | W21-22 | 23.08. – 05.09.2026 | Sync Protocol |
| S12 | Phase 3 | W23-24 | 06.09. – 19.09.2026 | Local + LAN Sync |
| S13 | Phase 3 | W25-26 | 20.09. – 03.10.2026 | Cloud Backends |
| S14 | Phase 3 | W27-28 | 04.10. – 17.10.2026 | Sync Hardening |
| S15 | Phase 4 | W29-30 | 18.10. – 31.10.2026 | REST API |
| S16 | Phase 4 | W31-32 | 01.11. – 14.11.2026 | Electron Scaffold |
| S17 | Phase 4 | W33-34 | 15.11. – 28.11.2026 | Core GUI Views |
| S18 | Phase 4 | W35-36 | 29.11. – 12.12.2026 | Cross-Platform + Polish |
| S19 | Phase 5 | W37-38 | 13.12. – 26.12.2026 | Security + Performance |
| S20 | Phase 5 | W39-40 | 03.01. – 16.01.2027 | Docs + Distribution |
| S21 | Phase 5 | W41-42 | 17.01. – 30.01.2027 | Release Engineering |

---

## Sprint 0 — Foundation (28.03.2026) — ABGESCHLOSSEN

**Ziel**: Rechtliche Grundlage + Repository + Planung

| Task | Verantwortlich | Status |
| --- | --- | --- |
| Markenrecherche 4 Datenbanken | Walter + Markus | DONE |
| Evidence Screenshots (forensisch) | Walter | DONE |
| Nice Classification Analysis DE/EN | Walter | DONE |
| Usage Documentation DE/EN | Walter | DONE |
| Git Init + GitHub Repo (MAVPARUAS-SAOIRSE) | Walter | DONE |
| README.md EN/DE + LICENSE (MIT) | Walter | DONE |
| Enterprise Development Plan v1.1 EN/DE | Walter | DONE |
| Walter-Workspace Enterprise Reorganisation | Walter | DONE |
| Architektur-Entscheidung: Rust-First | Markus + Walter | DONE |
| Architektur-Entscheidung: Electron statt Tauri | Markus + Walter | DONE |
| ADR-007 (Rust-First) + ADR-008 (Privacy) erstellt | Walter | DONE |

**Sprint Review**: Phase 0 Foundation vollständig abgeschlossen. Alle rechtlichen Dokumente erstellt, Repository live auf GitHub als MAVPARUAS-SAOIRSE (VERSALIEN-Standard). Development Plan v1.1 mit Rust-First Philosophie, 21-Sprint-Kalender, 10 Milestones. Architektur-Entscheidung: Electron + TypeScript für GUI (reine Präsentationsschicht), alle Logik in Rust. Python strikt auf KI/ML begrenzt.

---

## Sprint 0.3 — CI/CD + Community Files (geplant: 29.03. – 04.04.2026)

**Ziel**: GitHub Actions Pipeline + Community-Dateien

| Task | Verantwortlich | Status |
| --- | --- | --- |
| GitHub Actions CI-Workflow (lint + test) | — | PLANNED |
| CONTRIBUTING.md (EN + DE) | — | PLANNED |
| SECURITY.md (Vulnerability Reporting) | — | PLANNED |
| CODE_OF_CONDUCT.md | — | PLANNED |
| Issue Templates (Bug, Feature, Plugin) | — | PLANNED |
| PR Template | — | PLANNED |
| copilot-instructions.md (Projekt-spezifisch) | — | PLANNED |

---

## Sprint 1 — Cargo Workspace + Config (geplant: 05.04. – 18.04.2026)

**Ziel**: Multi-Crate Projektstruktur + Grundlegende Infrastruktur

| Task | Verantwortlich | Status |
| --- | --- | --- |
| Cargo Workspace (saoirse-core, -cli, -api, -plugins, -sync, -ai, -plugin-sdk) | — | PLANNED |
| Error Handling (`thiserror`, Custom Error Types) | — | PLANNED |
| Logging Framework (`tracing`, konfigurierbar) | — | PLANNED |
| Configuration System (TOML via `serde`) | — | PLANNED |
| CI: cargo build + clippy + rustfmt | — | PLANNED |

---

## Sprint 2 — File Scanner + Hashing (geplant: 19.04. – 02.05.2026)

**Ziel**: Async Datei-Scanner mit BLAKE3 Dedup

Noch nicht detailliert geplant — Start nach Sprint 1 Review.

---

*Detaillierte Sprint-Aufgaben: [DEVELOPMENT-PLAN.md](../docs/DEVELOPMENT-PLAN.md)*
*Product Backlog: [backlog.md](backlog.md)*
