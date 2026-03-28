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
| B-006 | MUST | Enterprise Development Plan (v1.1 Rust-First) | DONE |
| B-007 | SHOULD | CI/CD Pipeline (GitHub Actions) | OPEN |
| B-008 | SHOULD | CONTRIBUTING.md | OPEN |
| B-009 | SHOULD | SECURITY.md | OPEN |
| B-010 | SHOULD | CODE_OF_CONDUCT.md | OPEN |
| B-011 | COULD | GitHub Issue Templates | OPEN |
| B-012 | COULD | PR Template | OPEN |

## Phase 1: Core Engine (Q2 2026) — Rust Only

| ID | Priorität | Titel | Sprint | Status |
| --- | --- | --- | --- | --- |
| B-100 | MUST | Cargo Workspace Scaffold (Multi-Crate) | S1 | OPEN |
| B-101 | MUST | Error Handling Architecture (`thiserror`) | S1 | OPEN |
| B-102 | MUST | Logging Framework (`tracing`) | S1 | OPEN |
| B-103 | MUST | Configuration System (TOML via `serde`) | S1 | OPEN |
| B-104 | MUST | Async File Scanner (`tokio`) | S2 | OPEN |
| B-105 | MUST | File Metadata + BLAKE3 Hashing | S2 | OPEN |
| B-106 | MUST | Hash-basierte Deduplizierung | S2 | OPEN |
| B-107 | MUST | Rule Engine (TOML-Konfiguration) | S3 | OPEN |
| B-108 | MUST | Regel-Aktionen (Move, Copy, Tag, Rename) | S3 | OPEN |
| B-109 | MUST | Dry-Run Modus | S3 | OPEN |
| B-110 | MUST | SQLite Schema + Migrationen | S4 | OPEN |
| B-111 | MUST | Kategorie-/Tag-System | S4 | OPEN |
| B-112 | MUST | CLI (`clap` mit Subcommands) | S5 | OPEN |
| B-113 | MUST | Unit + Integration Tests (80%+) | S5 | OPEN |
| B-114 | SHOULD | Performance Benchmarks (`criterion`) | S5 | OPEN |
| B-115 | SHOULD | Filesystem Monitoring (`notify`) | S6 | OPEN |
| B-116 | SHOULD | Watch-Modus (auto-apply) | S6 | OPEN |
| B-117 | SHOULD | MCP Server Interface (Basic) | S6 | OPEN |

## Phase 2: Plugin-System & KI (Q3 2026) — Rust-First, Python nur KI

| ID | Priorität | Titel | Sprint | Status |
| --- | --- | --- | --- | --- |
| B-200 | MUST | Plugin Trait/Interface (Rust) | S7 | OPEN |
| B-201 | MUST | Rust Native Plugin Loading | S7 | OPEN |
| B-202 | MUST | Plugin Sandboxing (Capability-based) | S7 | OPEN |
| B-203 | MUST | Plugin SDK Crate | S7 | OPEN |
| B-204 | MUST | KI-Orchestrator (Rust) | S8 | OPEN |
| B-205 | MUST | ONNX Inference via `ort` (Rust-nativ) | S8 | OPEN |
| B-206 | SHOULD | HTTP Plugin Protocol (JSON-RPC) | S9 | OPEN |
| B-207 | SHOULD | Perl Plugin Bridge (HTTP) | S9 | OPEN |
| B-208 | SHOULD | C/C++ FFI Bridge | S9 | OPEN |
| B-209 | SHOULD | KI-Kategorisierungs-Plugin | S10 | OPEN |
| B-210 | LOW | Python Fallback Bridge (nur Nicht-ONNX) | S8 | OPEN |

## Phase 3: Synchronisation (Q4 2026) — Alles Rust

| ID | Priorität | Titel | Sprint | Status |
| --- | --- | --- | --- | --- |
| B-300 | MUST | Sync-Protokoll Spezifikation | S11 | OPEN |
| B-301 | MUST | Change Detection (Hash + Timestamp) | S11 | OPEN |
| B-302 | MUST | Konflikterkennung + Auflösung (3 Modi) | S11 | OPEN |
| B-303 | MUST | Lokale Sync (Verzeichnis → Verzeichnis) | S12 | OPEN |
| B-304 | MUST | LAN-Sync (mDNS, TLS) | S12 | OPEN |
| B-305 | MUST | WebDAV Backend (Nextcloud/Hetzner) | S13 | OPEN |
| B-306 | SHOULD | S3-kompatibles Backend | S13 | OPEN |
| B-307 | SHOULD | Hetzner Storage Box (SFTP) | S13 | OPEN |
| B-308 | MUST | E2E-Verschlüsselung (optional) | S14 | OPEN |
| B-309 | SHOULD | Multi-Remote Sync (Fan-out) | S14 | OPEN |

## Phase 4: Desktop-GUI & REST-API (Q1 2027) — Electron + TypeScript (nur Präsentation)

| ID | Priorität | Titel | Sprint | Status |
| --- | --- | --- | --- | --- |
| B-400 | MUST | REST API (OpenAPI 3.1, Axum) | S15 | OPEN |
| B-401 | MUST | JWT Token-Authentifizierung | S15 | OPEN |
| B-402 | MUST | Electron + TypeScript Setup | S16 | OPEN |
| B-403 | MUST | Rust Sidecar (IPC JSON-RPC Bridge) | S16 | OPEN |
| B-404 | MUST | Dateibrowser-View | S17 | OPEN |
| B-405 | SHOULD | Regel-Editor UI | S17 | OPEN |
| B-406 | SHOULD | Sync-Status-Dashboard | S17 | OPEN |
| B-407 | MUST | Barrierefreiheit (WCAG 2.1 AA) | S18 | OPEN |
| B-408 | MUST | Cross-Platform (Linux, Windows, macOS) | S18 | OPEN |
| B-409 | MUST | Installer (AppImage, MSI, DMG) | S18 | OPEN |

## Phase 5: Produktionsrelease (Q2 2027)

| ID | Priorität | Titel | Sprint | Status |
| --- | --- | --- | --- | --- |
| B-500 | MUST | Security Audit (OWASP Top 10) | S19 | OPEN |
| B-501 | MUST | Performance Optimierung | S19 | OPEN |
| B-502 | MUST | User Guide EN + DE | S20 | OPEN |
| B-503 | MUST | crates.io Publish | S20 | OPEN |
| B-504 | MUST | AUR Package | S20 | OPEN |
| B-505 | MUST | Release Automation | S21 | OPEN |
| B-506 | MUST | v1.0.0 Release | S21 | OPEN |

---

*Legende: MUST = Muss für MVP, SHOULD = Wichtig, COULD = Optional, LOW = Niedrige Priorität*
