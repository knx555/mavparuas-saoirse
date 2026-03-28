# MAVPARUAS SAOIRSE — Enterprise Development Plan

> Version 1.1 | 2026-03-28 | Author: Walter Codecraft (knx555)

## 1. Executive Summary

**SAOIRSE** = **S**ynchronizing **A**ll **O**rigins with **I**ntelligent **R**ecognition, **S**orting & **E**xchange

MAVPARUAS SAOIRSE is a universal file organization, categorization, and synchronization tool. This document defines the phased development roadmap from legal foundation through production release under MIT License.

**Core Architectural Principles:**

1. **Rust-First** — ALL logic, routing, business logic, and backend in Rust
2. **Python** — ONLY when absolutely necessary (AI/ML libraries with no Rust equivalent)
3. **Electron + TypeScript** — GUI presentation layer ONLY (no business logic in frontend)
4. Plugin architecture compatible with **MAVPARUAS ecosystem** (Perl, Python, C/C++, Rust)
5. **SQLite** as default database, configurable backends
6. **MIT License** — no copyleft dependencies permitted
7. Cross-platform: Linux (primary), Windows, macOS

## 2. Development Philosophy: Rust-First

### 2.1 Language Hierarchy

SAOIRSE follows a strict **Rust-First** development philosophy. Every component is implemented in Rust unless there is a proven, documented reason why Rust cannot fulfill the requirement.

| Priority | Language | Role | Boundary |
| --- | --- | --- | --- |
| 1 (Primary) | **Rust** | Core engine, business logic, routing, API, sync, plugins, CLI | Everything by default |
| 2 (AI-Only) | **Python** | AI/ML inference, model loading, NLP pipelines | ONLY when no Rust crate exists |
| 3 (GUI-Only) | **TypeScript** | Electron GUI — presentation layer | ONLY rendering & user interaction |

### 2.2 Decision Criteria for Non-Rust Code

Before writing ANY non-Rust code, the following must be documented:

1. **Python**: Which specific AI/ML library is needed? Is there a Rust equivalent (e.g., `candle`, `burn`, `ort`)? If yes → use Rust. If no → Python via subprocess, isolated.
2. **TypeScript**: Is this purely UI rendering or user interaction? If yes → TypeScript in Electron. If it involves ANY logic, validation, routing, or data transformation → must be in Rust backend.

### 2.3 Rust Ecosystem Strategy

| Domain | Rust Crate | Purpose |
| --- | --- | --- |
| Async Runtime | `tokio` | Async I/O, task scheduling |
| Serialization | `serde` + `serde_json` / `toml` | Config & data serialization |
| CLI | `clap` | Command-line argument parsing |
| HTTP Server | `axum` | REST API & Electron backend |
| Database | `rusqlite` / `sqlx` | SQLite access |
| File Watching | `notify` | Filesystem event monitoring |
| Hashing | `blake3` / `sha2` | File deduplication & integrity |
| Encryption | `ring` / `rustls` | TLS & data encryption |
| AI (Rust-native) | `candle` / `ort` | ONNX inference, embeddings |
| Logging | `tracing` | Structured logging |
| Error Handling | `thiserror` / `anyhow` | Ergonomic error types |
| Testing | `cargo test` + `proptest` | Unit, integration, property-based tests |
| Benchmarks | `criterion` | Performance regression detection |

## 3. Architecture Overview

```text
┌──────────────────────────────────────────────────────────┐
│                    User Interfaces                        │
│  ┌──────────┐  ┌───────────────────┐  ┌───────────────┐  │
│  │   CLI    │  │       GUI         │  │   REST API    │  │
│  │  (Rust)  │  │  (Electron + TS)  │  │ (Axum/Rust)   │  │
│  │          │  │  Presentation     │  │               │  │
│  │          │  │  Layer Only       │  │               │  │
│  └────┬─────┘  └───────┬───────────┘  └──────┬────────┘  │
│       │                │ IPC                  │           │
│       └────────────────┼──────────────────────┘           │
│                        ▼                                  │
│  ┌────────────────────────────────────────────────────┐   │
│  │              Core Engine (Rust)                     │   │
│  │  ┌──────────┐ ┌──────────┐ ┌────────────────────┐ │   │
│  │  │ File     │ │ Rule     │ │ Sync               │ │   │
│  │  │ Scanner  │ │ Engine   │ │ Manager            │ │   │
│  │  └──────────┘ └──────────┘ └────────────────────┘ │   │
│  │  ┌──────────┐ ┌──────────┐ ┌────────────────────┐ │   │
│  │  │ Category │ │ Watch    │ │ Config             │ │   │
│  │  │ Manager  │ │ Service  │ │ Manager            │ │   │
│  │  └──────────┘ └──────────┘ └────────────────────┘ │   │
│  │  ┌──────────┐ ┌──────────┐ ┌────────────────────┐ │   │
│  │  │ MCP      │ │ IPC      │ │ AI Orchestrator    │ │   │
│  │  │ Server   │ │ Bridge   │ │ (Rust → Python)    │ │   │
│  │  └──────────┘ └──────────┘ └────────────────────┘ │   │
│  └───────────────────┬────────────────────────────────┘   │
│                      ▼                                    │
│  ┌────────────────────────────────────────────────────┐   │
│  │           Plugin System (FFI/HTTP)                 │   │
│  │  ┌────────┐ ┌────────┐ ┌──────┐ ┌──────────────┐ │   │
│  │  │  Rust  │ │ Python │ │ C++  │ │ HTTP/Extern  │ │   │
│  │  │(native)│ │(AI/ML) │ │(FFI) │ │ (any lang)   │ │   │
│  │  └────────┘ └────────┘ └──────┘ └──────────────┘ │   │
│  └───────────────────┬────────────────────────────────┘   │
│                      ▼                                    │
│  ┌────────────────────────────────────────────────────┐   │
│  │           Storage Layer                            │   │
│  │  ┌────────┐ ┌──────────┐ ┌──────────────────────┐ │   │
│  │  │ SQLite │ │ Redis    │ │ Cloud Backends       │ │   │
│  │  │(default)│ │(optional)│ │ (WebDAV/S3/Hetzner) │ │   │
│  │  └────────┘ └──────────┘ └──────────────────────┘ │   │
│  └────────────────────────────────────────────────────┘   │
└──────────────────────────────────────────────────────────┘
```

### 3.1 GUI Architecture (Electron + TypeScript)

```text
┌─────────────────────────────────────────────┐
│           Electron Application               │
│  ┌───────────────────────────────────────┐   │
│  │  Renderer Process (TypeScript)        │   │
│  │  - HTML/CSS/TS presentation only      │   │
│  │  - No business logic                  │   │
│  │  - Calls Rust backend via IPC         │   │
│  │  - Accessibility (WCAG 2.1 AA)       │   │
│  └────────────────┬──────────────────────┘   │
│                   │ IPC (JSON-RPC)           │
│  ┌────────────────▼──────────────────────┐   │
│  │  Main Process (Rust sidecar)          │   │
│  │  - ALL business logic                 │   │
│  │  - Routing & validation               │   │
│  │  - Data transformation                │   │
│  │  - Backend communication              │   │
│  └───────────────────────────────────────┘   │
└─────────────────────────────────────────────┘
```

**Boundary Rule**: If you can express it as a Rust function → it MUST be in Rust. The TypeScript layer is a thin presentation shell that renders data and sends user actions to Rust via IPC.

## 4. Development Phases & Sprint Breakdown

### Phase 0: Foundation (Q1 2026) — COMPLETE

**Status: DONE**

| Sprint | Task | Status | Notes |
| --- | --- | --- | --- |
| S0.1 | Trademark clearance (TMView, EUIPO, DPMA, USPTO) | DONE | All databases clear |
| S0.1 | Nice Classification analysis | DONE | Class 9 primary, Class 42 conditional |
| S0.1 | Forensic evidence archival | DONE | SHA-256 verified screenshots |
| S0.1 | Usage documentation setup | DONE | First entries logged |
| S0.2 | MIT License + README (bilingual EN/DE) | DONE | Bilingual documentation standard |
| S0.2 | GitHub repository creation | DONE | knx555/MAVPARUAS-SAOIRSE |
| S0.2 | Enterprise development plan (EN/DE) | DONE | This document |
| S0.2 | Walter-Workspace enterprise reorganisation | DONE | ADRs, Backlog, Sprint-Log |
| S0.3 | CI/CD pipeline setup (GitHub Actions) | TODO | — |
| S0.3 | CONTRIBUTING.md + Code of Conduct | TODO | — |
| S0.3 | Security policy (SECURITY.md) | TODO | — |

**Deliverable**: Legal foundation, repository, and planning infrastructure.

---

### Phase 1: Core Engine (Q2 2026)

**Goal**: Production-quality file scanner, rule engine, and CLI — 100% Rust.

#### Sprint 1 (Week 1-2): Project Scaffold

| ID | Task | Priority | Acceptance Criteria |
| --- | --- | --- | --- |
| S1.1 | Cargo workspace setup (multi-crate) | HIGH | `cargo build` succeeds, CI green |
| S1.2 | `saoirse-core` crate structure | HIGH | Module hierarchy defined, compiles |
| S1.3 | Error handling architecture (`thiserror`) | HIGH | Custom error types, `Result<T>` throughout |
| S1.4 | Logging framework (`tracing`) | HIGH | Structured logs, configurable verbosity |
| S1.5 | Configuration system (TOML via `serde`) | HIGH | Load/save config files, validate schema |

#### Sprint 2 (Week 3-4): File Scanner

| ID | Task | Priority | Acceptance Criteria |
| --- | --- | --- | --- |
| S2.1 | Async recursive directory scanner (`tokio`) | HIGH | Scans 10k files in < 3s |
| S2.2 | File metadata extraction (size, dates, type) | HIGH | MIME detection, hash computation |
| S2.3 | Hash-based deduplication (`blake3`) | HIGH | Detects identical files across directories |
| S2.4 | Symlink handling + permission checks | MEDIUM | Configurable follow/skip symlinks |
| S2.5 | Exclusion patterns (gitignore-style) | MEDIUM | `.saoirse-ignore` file support |

#### Sprint 3 (Week 5-6): Rule Engine

| ID | Task | Priority | Acceptance Criteria |
| --- | --- | --- | --- |
| S3.1 | Rule definition format (TOML) | HIGH | Schema documented, validated on load |
| S3.2 | Rule types: extension, size, date, name pattern | HIGH | 15+ built-in rule predicates |
| S3.3 | Rule actions: move, copy, tag, rename, ignore | HIGH | Safe rollback for destructive actions |
| S3.4 | Rule chaining + priority system | MEDIUM | Ordered execution, conflict resolution |
| S3.5 | Dry-run mode (preview without execution) | HIGH | Shows planned changes, no side effects |

#### Sprint 4 (Week 7-8): Storage & Categories

| ID | Task | Priority | Acceptance Criteria |
| --- | --- | --- | --- |
| S4.1 | SQLite schema design + migrations | HIGH | Schema versioned, auto-migration |
| S4.2 | File index persistence (scan results → DB) | HIGH | Incremental updates, not full rescan |
| S4.3 | Category/tag system (hierarchical) | HIGH | Create, assign, query categories |
| S4.4 | Search/filter API (by tag, rule, date, size) | MEDIUM | Sub-second queries on 100k+ files |
| S4.5 | Export: JSON, CSV report generation | LOW | Summary statistics + detailed reports |

#### Sprint 5 (Week 9-10): CLI & Testing

| ID | Task | Priority | Acceptance Criteria |
| --- | --- | --- | --- |
| S5.1 | CLI framework (`clap` with subcommands) | HIGH | `saoirse scan`, `saoirse rules`, `saoirse sync` |
| S5.2 | Interactive progress display | MEDIUM | Progress bars, file counts, ETA |
| S5.3 | Unit test suite (80%+ coverage) | HIGH | All core modules covered |
| S5.4 | Integration tests (real filesystem) | HIGH | Temp directories, known test fixtures |
| S5.5 | Performance benchmarks (`criterion`) | MEDIUM | Baseline established, CI regression checks |

#### Sprint 6 (Week 11-12): Filesystem Monitoring & Polish

| ID | Task | Priority | Acceptance Criteria |
| --- | --- | --- | --- |
| S6.1 | Filesystem event monitoring (`notify` crate) | MEDIUM | inotify on Linux, FSEvents on macOS |
| S6.2 | Watch mode: auto-apply rules on changes | MEDIUM | Debounced events, configurable delay |
| S6.3 | MCP server interface (basic) | MEDIUM | Local AI can trigger scans via MCP |
| S6.4 | Documentation: CLI usage guide | HIGH | Man page + markdown docs |
| S6.5 | Phase 1 integration testing + release prep | HIGH | All tests pass, `cargo clippy` clean |

**Phase 1 Deliverable**: CLI tool that scans directories, applies rules, categorizes files, monitors changes — all in Rust.

---

### Phase 2: Plugin System & AI Integration (Q3 2026)

**Goal**: MAVPARUAS-compatible plugin architecture + local AI classification.

#### Sprint 7 (Week 13-14): Plugin Architecture

| ID | Task | Priority | Acceptance Criteria |
| --- | --- | --- | --- |
| S7.1 | Plugin trait/interface definition (Rust) | HIGH | Documented trait with lifecycle hooks |
| S7.2 | Rust native plugin loading (dynamic `.so`/`.dll`) | HIGH | Hot-reload support |
| S7.3 | Plugin registry + discovery system | HIGH | Auto-detect plugins in `plugins/` directory |
| S7.4 | Plugin sandboxing (capability-based) | HIGH | Filesystem + network access control |
| S7.5 | Plugin SDK crate (`saoirse-plugin-sdk`) | HIGH | Template + examples for plugin authors |

#### Sprint 8 (Week 15-16): AI Classification (Rust-First)

| ID | Task | Priority | Acceptance Criteria |
| --- | --- | --- | --- |
| S8.1 | AI orchestrator module (Rust) | HIGH | Manages model loading + inference scheduling |
| S8.2 | ONNX inference via `ort` (Rust-native) | HIGH | Run classification models without Python |
| S8.3 | File content analysis (text extraction) | MEDIUM | PDF, Office, plain-text extraction in Rust |
| S8.4 | Embedding generation for semantic search | MEDIUM | Local embeddings, stored in SQLite |
| S8.5 | Python fallback bridge (subprocess only) | LOW | ONLY for models without ONNX export |

**Python Boundary**: Python is used ONLY if a specific AI model has no ONNX export and cannot run via Rust's `ort` or `candle`. This must be documented per-model.

#### Sprint 9 (Week 17-18): External Plugin Bridges

| ID | Task | Priority | Acceptance Criteria |
| --- | --- | --- | --- |
| S9.1 | HTTP plugin protocol (JSON-RPC over HTTP) | MEDIUM | Documented API, schema validation |
| S9.2 | Perl plugin bridge (HTTP) | MEDIUM | MAVPARUAS Perl module can register |
| S9.3 | C/C++ FFI bridge | MEDIUM | ABI-stable C interface |
| S9.4 | Example plugins (Rust, Python-AI, HTTP) | MEDIUM | 3 working examples with tests |
| S9.5 | Plugin development documentation | HIGH | Guide, API reference, troubleshooting |

#### Sprint 10 (Week 19-20): AI Plugins & Integration

| ID | Task | Priority | Acceptance Criteria |
| --- | --- | --- | --- |
| S10.1 | AI-assisted file categorization plugin | HIGH | Auto-categorize by content + metadata |
| S10.2 | Duplicate detection (fuzzy + exact) | MEDIUM | Near-duplicate detection via embeddings |
| S10.3 | Smart rename suggestions | LOW | AI-generated filename proposals |
| S10.4 | Plugin performance monitoring | MEDIUM | Timeout, resource limits per plugin |
| S10.5 | Phase 2 integration testing | HIGH | Plugin system fully tested |

**Phase 2 Deliverable**: Working plugin system with Rust-native AI classification and MAVPARUAS plugin compatibility.

---

### Phase 3: Synchronization Engine (Q4 2026)

**Goal**: Cross-device file synchronization — all logic in Rust.

#### Sprint 11 (Week 21-22): Sync Protocol Design

| ID | Task | Priority | Acceptance Criteria |
| --- | --- | --- | --- |
| S11.1 | Sync protocol specification (internal doc) | HIGH | Reviewed, edge cases documented |
| S11.2 | Change detection engine (hash + timestamp) | HIGH | Detects adds, deletes, moves, renames |
| S11.3 | Conflict resolution strategy | HIGH | 3 modes: manual, newest-wins, merge |
| S11.4 | Sync state persistence (per-remote) | HIGH | Resume after interruption |
| S11.5 | Transfer protocol (chunked, resumable) | HIGH | Handle large files, network interruptions |

#### Sprint 12 (Week 23-24): Local & LAN Sync

| ID | Task | Priority | Acceptance Criteria |
| --- | --- | --- | --- |
| S12.1 | Local-to-local sync (same machine) | HIGH | Between any two directories |
| S12.2 | LAN discovery (mDNS/Zeroconf) | MEDIUM | Auto-discover SAOIRSE peers |
| S12.3 | LAN sync (encrypted, authenticated) | HIGH | TLS mutual auth, `rustls` |
| S12.4 | Incremental/delta sync | MEDIUM | Only transfer changed byte ranges |
| S12.5 | Bandwidth throttling | LOW | Configurable limits |

#### Sprint 13 (Week 25-26): Cloud Backends

| ID | Task | Priority | Acceptance Criteria |
| --- | --- | --- | --- |
| S13.1 | Backend trait definition | HIGH | Swappable storage backends |
| S13.2 | WebDAV backend (Nextcloud, Hetzner) | HIGH | Sync with Nextcloud server |
| S13.3 | S3-compatible backend | MEDIUM | MinIO, Hetzner Object Storage |
| S13.4 | Hetzner Storage Box (SFTP/CIFS) | MEDIUM | Direct Hetzner integration |
| S13.5 | Backend-specific error handling | HIGH | Retry logic, quota management |

#### Sprint 14 (Week 27-28): Sync Hardening

| ID | Task | Priority | Acceptance Criteria |
| --- | --- | --- | --- |
| S14.1 | End-to-end encryption (per-file, optional) | HIGH | Client-side encryption, zero-knowledge |
| S14.2 | Sync conflict UI (CLI) | MEDIUM | Interactive conflict resolver |
| S14.3 | Sync performance testing (10k+ files) | HIGH | Benchmark suite, regression detection |
| S14.4 | Multi-remote sync (fan-out) | MEDIUM | Sync one source to multiple destinations |
| S14.5 | Phase 3 security audit (sync layer) | HIGH | No data leaks, encryption verified |

**Phase 3 Deliverable**: Reliable local + LAN + cloud file synchronization with encryption.

---

### Phase 4: Desktop GUI & REST API (Q1 2027)

**Goal**: Electron desktop app (TypeScript frontend, Rust backend via IPC) + public REST API.

#### Sprint 15 (Week 29-30): REST API

| ID | Task | Priority | Acceptance Criteria |
| --- | --- | --- | --- |
| S15.1 | REST API design (OpenAPI 3.1 spec) | HIGH | Published spec, interactive docs |
| S15.2 | API implementation (`axum`) | HIGH | All core operations exposed |
| S15.3 | Token-based authentication | HIGH | JWT or API keys, rate limiting |
| S15.4 | WebSocket events (file changes, sync status) | MEDIUM | Real-time notifications |
| S15.5 | API test suite + documentation | HIGH | 100% endpoint coverage |

#### Sprint 16 (Week 31-32): Electron Application Scaffold

| ID | Task | Priority | Acceptance Criteria |
| --- | --- | --- | --- |
| S16.1 | Electron + TypeScript project setup | HIGH | Build pipeline, hot-reload dev mode |
| S16.2 | Rust sidecar integration (IPC bridge) | HIGH | Bidirectional JSON-RPC over stdio/pipe |
| S16.3 | Application window + navigation shell | HIGH | Main window, sidebar, routing |
| S16.4 | Theme system (light/dark, high-contrast) | MEDIUM | System preference detection |
| S16.5 | Accessibility foundation (WCAG 2.1 AA) | HIGH | Screen reader compatible from day 1 |

#### Sprint 17 (Week 33-34): Core GUI Views

| ID | Task | Priority | Acceptance Criteria |
| --- | --- | --- | --- |
| S17.1 | File browser view (tree + list) | HIGH | Navigate, preview, context menu |
| S17.2 | Rule editor (visual rule builder) | MEDIUM | Create rules without editing TOML |
| S17.3 | Sync status dashboard | MEDIUM | Progress, conflicts, history |
| S17.4 | Plugin management view | LOW | Install, enable/disable, configure |
| S17.5 | Settings panel | MEDIUM | All CLI config options in GUI |

#### Sprint 18 (Week 35-36): Polish & Cross-Platform

| ID | Task | Priority | Acceptance Criteria |
| --- | --- | --- | --- |
| S18.1 | Accessibility audit (WCAG 2.1 AA) | HIGH | Screen reader tested, keyboard navigation |
| S18.2 | Cross-platform testing (Linux, Windows, macOS) | HIGH | All platforms functional |
| S18.3 | Electron auto-update system | MEDIUM | Update notifications, background download |
| S18.4 | Installer/package generation | HIGH | AppImage (Linux), MSI (Win), DMG (Mac) |
| S18.5 | Phase 4 integration testing | HIGH | GUI ↔ Rust backend fully tested |

**Phase 4 Deliverable**: Cross-platform Electron desktop app with accessible UI + documented REST API.

---

### Phase 5: Production Release (Q2 2027)

**Goal**: v1.0 — security-audited, optimized, distributed.

#### Sprint 19 (Week 37-38): Security & Performance

| ID | Task | Priority | Acceptance Criteria |
| --- | --- | --- | --- |
| S19.1 | Security audit (OWASP Top 10 review) | HIGH | No critical/high findings |
| S19.2 | Performance optimization profiling | HIGH | Target: 100k files < 30s full scan |
| S19.3 | Memory optimization | MEDIUM | < 200MB RSS for 100k file index |
| S19.4 | Fuzzing (`cargo fuzz`) | MEDIUM | Parser + file handling fuzzed |
| S19.5 | Penetration testing (sync + API) | HIGH | No auth bypass, no data leak |

#### Sprint 20 (Week 39-40): Documentation & Distribution

| ID | Task | Priority | Acceptance Criteria |
| --- | --- | --- | --- |
| S20.1 | User guide (EN + DE) | HIGH | Complete workflow documentation |
| S20.2 | Plugin developer guide | HIGH | Tutorial + API reference |
| S20.3 | crates.io publish (`saoirse-core`, SDK) | HIGH | Published, installable |
| S20.4 | AUR package (Arch Linux) | HIGH | `yay -S mavparuas-saoirse` |
| S20.5 | Homebrew formula (macOS) | MEDIUM | `brew install mavparuas-saoirse` |

#### Sprint 21 (Week 41-42): Release Engineering

| ID | Task | Priority | Acceptance Criteria |
| --- | --- | --- | --- |
| S21.1 | Release automation (GitHub Actions) | HIGH | Tag → Build → Release → Publish |
| S21.2 | Changelog generation | MEDIUM | Conventional Commits → CHANGELOG.md |
| S21.3 | v1.0.0 release candidate | HIGH | All tests pass, docs complete |
| S21.4 | Community contribution workflow | MEDIUM | CONTRIBUTING.md, DCO, templates |
| S21.5 | v1.0.0 final release | HIGH | Published on all platforms |

**Phase 5 Deliverable**: v1.0 production release, published and distributed.

## 5. Technology Decisions

### 5.1 Why Rust for Core (and Almost Everything Else)

1. **Memory safety** without garbage collection — critical for file operations
2. **Performance** comparable to C/C++ for I/O-heavy workloads
3. **Cross-platform** compilation (Linux, Windows, macOS)
4. **Strong type system** catches bugs at compile time
5. **Ecosystem** (Tokio for async, Serde for serialization, Clap for CLI)
6. **MIT/Apache-2.0 dual-licensed** — compatible with project license
7. **Single binary** deployment — no runtime dependencies
8. **Fearless concurrency** — safe parallel file processing

### 5.2 Why SQLite as Default

1. **Zero configuration** — single file database
2. **Embedded** — no external service required
3. **Battle-tested** — most widely deployed database engine
4. **Public domain** — no license concerns
5. **Sufficient for single-user** file management scenarios

### 5.3 Why Electron + TypeScript for GUI (not Tauri)

1. **Mature ecosystem** — proven for complex desktop applications
2. **TypeScript** — type safety for the presentation layer
3. **Rust sidecar** — ALL business logic runs as a separate Rust process
4. **Accessibility** — excellent screen reader support via Chromium
5. **Cross-platform** — consistent rendering across Linux/Windows/macOS
6. **MIT License** — fully compatible
7. **Clear separation** — TypeScript handles ONLY rendering, Rust handles ALL logic

**Why not Tauri?** While Tauri is Rust-native, Electron provides superior accessibility infrastructure (critical for MAVPARUAS — screen reader support is non-negotiable) and a more mature debugging toolkit.

### 5.4 Plugin Communication Hierarchy

| Method | Use Case | Language | Latency |
| --- | --- | --- | --- |
| Dynamic loading | Rust native plugins | Rust | Lowest |
| `ort` (ONNX Runtime) | AI inference (Rust-native) | Rust | Low |
| FFI (C ABI) | C/C++ plugins | C, C++ | Low |
| Subprocess + stdio | Python AI models (isolated) | Python | Medium |
| HTTP/JSON-RPC | External plugins (any language) | Any | Highest |

### 5.5 Python: Strictly AI/ML Only

Python is NOT a general-purpose language in this project. Permitted uses:

| Permitted | Forbidden |
| --- | --- |
| AI model inference (no ONNX export available) | Business logic |
| NLP pipeline (spaCy, transformers) | File operations |
| Custom model training scripts | Configuration |
| ML experiment notebooks | API endpoints |

**Enforcement**: Python code lives ONLY in `plugins/ai/` directory. No Python imports in core crates.

## 6. Quality Standards

### 6.1 Testing Strategy

| Level | Tool | Coverage Target |
| --- | --- | --- |
| Unit Tests | `cargo test` | 80%+ |
| Integration Tests | `cargo test --test` | Critical paths |
| Property-Based | `proptest` | Parser + rule engine |
| Plugin Tests | Per-language test frameworks | All plugin types |
| Performance | `criterion` benchmarks | Regression detection |
| Fuzzing | `cargo fuzz` | File parsing, rule parsing |
| Security | `cargo audit` + `cargo deny` | Zero known vulns |
| Linting | `clippy` + `rustfmt` | Zero warnings |
| GUI Tests | Playwright | Critical user flows |

### 6.2 CI/CD Pipeline (GitHub Actions)

```yaml
# Planned pipeline stages
stages:
  - lint        # clippy, rustfmt, markdownlint, eslint (TS)
  - test        # unit + integration + property-based tests
  - security    # cargo audit, cargo deny, license check
  - build       # cross-platform (Linux, Windows, macOS)
  - gui-test    # Playwright e2e (Phase 4+)
  - release     # tagged releases → GitHub Releases + packages
```

### 6.3 Code Standards

1. **Rust**: `rustfmt` + `clippy` with strict settings (deny warnings)
2. **TypeScript** (GUI only): `eslint` + `prettier`, strict mode
3. **Python** (AI only): `ruff` + `mypy` + `pytest`
4. **Documentation**: All public APIs documented with examples
5. **Commits**: Conventional Commits (`feat:`, `fix:`, `docs:`, `refactor:`)
6. **Reviews**: All PRs require review before merge

## 7. Security Framework

### 7.1 Principles

1. **Privacy-by-Design** — no data leaves the user's machine without explicit consent
2. **Least privilege** — plugins run sandboxed with declared capabilities
3. **No network by default** — sync is opt-in, AI is local-only
4. **Encryption at rest** — optional for sensitive metadata
5. **Encryption in transit** — TLS 1.3 for all sync connections
6. **Dependency auditing** — automated via `cargo audit` + `cargo deny`
7. **Local AI only** — no cloud inference, no data exfiltration

### 7.2 License Compliance

| Allowed | Forbidden (without approval) |
| --- | --- |
| MIT | GPL |
| BSD (2/3-clause) | AGPL |
| Apache 2.0 | LGPL (case-by-case) |
| MPL 2.0 | SSPL |
| ISC | — |
| Unlicense / CC0 | — |

**Enforcement**: `cargo deny` in CI pipeline checks all dependency licenses.

## 8. Repository Structure (Target)

```text
MAVPARUAS-SAOIRSE/
├── .github/
│   ├── workflows/              # CI/CD pipelines
│   │   ├── ci.yml              # Lint + test + security
│   │   ├── release.yml         # Cross-platform release
│   │   └── gui-test.yml        # Electron e2e tests
│   ├── ISSUE_TEMPLATE/         # Bug/feature templates
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── copilot-instructions.md
├── crates/
│   ├── saoirse-core/           # Core engine library (Rust)
│   ├── saoirse-cli/            # CLI binary (Rust)
│   ├── saoirse-api/            # REST API server (Rust/Axum)
│   ├── saoirse-plugins/        # Plugin system (Rust)
│   ├── saoirse-sync/           # Synchronization engine (Rust)
│   ├── saoirse-ai/             # AI orchestrator (Rust, ONNX)
│   └── saoirse-plugin-sdk/     # Plugin SDK for authors
├── gui/
│   ├── electron/               # Electron main process
│   ├── src/                    # TypeScript frontend (presentation only)
│   ├── package.json
│   └── tsconfig.json
├── plugins/
│   ├── ai/                     # Python AI plugins (ONLY AI code here)
│   ├── examples/               # Example plugins (multi-language)
│   └── sdk/                    # Plugin SDK documentation
├── docs/
│   ├── legal/                  # Trademark & legal (existing)
│   ├── architecture/           # Architecture Decision Records
│   ├── api/                    # OpenAPI spec + docs
│   └── guides/                 # User & developer guides
├── scripts/                    # Development scripts
├── walter-workspace/           # Project management
├── Cargo.toml                  # Workspace manifest
├── LICENSE
├── README.md
├── README_DE.md
├── CONTRIBUTING.md
├── SECURITY.md
└── CODE_OF_CONDUCT.md
```

## 9. Milestones & Success Criteria

### Milestone Overview

| ID | Milestone | Phase | Sprint | Target Date | Status |
| --- | --- | --- | --- | --- | --- |
| M0 | Legal Foundation | 0 | S0.1-S0.2 | 2026-03-28 | DONE |
| M0.5 | CI/CD + Community Files | 0 | S0.3 | 2026-04-04 | TODO |
| M1 | First Scan | 1 | S1-S2 | 2026-04-25 | TODO |
| M2 | Rule Engine Complete | 1 | S3-S4 | 2026-05-23 | TODO |
| M3 | CLI v0.1 Release | 1 | S5-S6 | 2026-06-20 | TODO |
| M4 | Plugin MVP | 2 | S7-S8 | 2026-07-18 | TODO |
| M5 | AI Classification | 2 | S9-S10 | 2026-08-15 | TODO |
| M6 | Local Sync | 3 | S11-S12 | 2026-09-12 | TODO |
| M7 | Cloud Sync | 3 | S13-S14 | 2026-10-10 | TODO |
| M8 | REST API | 4 | S15 | 2026-10-24 | TODO |
| M9 | Desktop App (Electron) | 4 | S16-S18 | 2026-12-05 | TODO |
| M10 | v1.0 Release | 5 | S19-S21 | 2027-01-30 | TODO |

### Detailed Milestone Acceptance Criteria

**M0: Legal Foundation** — DONE
- Trademark clearance: 4 international databases searched
- Forensic evidence: SHA-256 verified screenshots archived
- Nice Classification: Classe 9 + 42 analyzed
- Repository: Public on GitHub, MIT licensed

**M0.5: CI/CD + Community**
- GitHub Actions: Lint + test + security pipeline running
- CONTRIBUTING.md: Clear contribution guidelines
- SECURITY.md: Vulnerability reporting process
- Issue/PR templates: Standardized workflows

**M1: First Scan**
- CLI scans 10,000 files in < 3 seconds
- File metadata: size, dates, MIME type, BLAKE3 hash
- Deduplication: Detects exact duplicates across directories
- SQLite: Scan results persisted, incremental updates

**M2: Rule Engine Complete**
- 20+ rule predicates (extension, size, date, content type, pattern)
- TOML-based rule configuration with schema validation
- Dry-run mode: Preview changes without execution
- Safe rollback: Undo destructive operations

**M3: CLI v0.1 Release**
- `saoirse scan` — recursive directory scan
- `saoirse rules` — apply/test/list rules
- `saoirse watch` — filesystem monitoring mode
- `saoirse status` — database statistics
- 80%+ test coverage, `clippy` clean, `cargo audit` clean
- Binary published as GitHub Release (Linux x86_64)

**M4: Plugin MVP**
- Plugin trait documented with lifecycle hooks
- Rust native plugins: dynamic loading + hot-reload
- Plugin sandboxing: capability-based security
- Plugin SDK crate published on crates.io

**M5: AI Classification**
- ONNX models run via Rust-native `ort` crate
- Local embeddings for semantic file search
- Auto-categorization by content + metadata
- Python fallback: ONLY for models without ONNX export

**M6: Local Sync**
- Bidirectional sync between local directories
- LAN discovery via mDNS/Zeroconf
- TLS-encrypted peer-to-peer sync
- Conflict detection with 3 resolution modes

**M7: Cloud Sync**
- WebDAV backend (Nextcloud/Hetzner compatible)
- S3-compatible backend (MinIO/Hetzner Object Storage)
- End-to-end client-side encryption (optional)
- Multi-remote fan-out sync

**M8: REST API**
- OpenAPI 3.1 specification published
- Token-based authentication (JWT)
- WebSocket real-time events
- 100% endpoint test coverage

**M9: Desktop App (Electron)**
- Electron app with Rust sidecar (IPC bridge)
- File browser, rule editor, sync dashboard
- WCAG 2.1 AA accessibility (screen reader tested)
- Cross-platform: Linux AppImage, Windows MSI, macOS DMG

**M10: v1.0 Release**
- Security audit passed (OWASP Top 10)
- Performance benchmarks published
- User guide (EN + DE) complete
- Published: crates.io, AUR, Homebrew, GitHub Releases

## 10. Sprint Calendar

| Sprint | Weeks | Dates (approx.) | Phase | Focus |
| --- | --- | --- | --- | --- |
| S0.3 | W0 | 2026-03-29 – 2026-04-04 | Phase 0 | CI/CD + Community Files |
| S1 | W1-2 | 2026-04-05 – 2026-04-18 | Phase 1 | Cargo Workspace + Config |
| S2 | W3-4 | 2026-04-19 – 2026-05-02 | Phase 1 | File Scanner + Hashing |
| S3 | W5-6 | 2026-05-03 – 2026-05-16 | Phase 1 | Rule Engine |
| S4 | W7-8 | 2026-05-17 – 2026-05-30 | Phase 1 | Storage + Categories |
| S5 | W9-10 | 2026-05-31 – 2026-06-13 | Phase 1 | CLI + Testing |
| S6 | W11-12 | 2026-06-14 – 2026-06-27 | Phase 1 | Watch Mode + MCP + Polish |
| S7 | W13-14 | 2026-06-28 – 2026-07-11 | Phase 2 | Plugin Architecture |
| S8 | W15-16 | 2026-07-12 – 2026-07-25 | Phase 2 | AI Classification (Rust) |
| S9 | W17-18 | 2026-07-26 – 2026-08-08 | Phase 2 | External Plugin Bridges |
| S10 | W19-20 | 2026-08-09 – 2026-08-22 | Phase 2 | AI Plugins + Integration |
| S11 | W21-22 | 2026-08-23 – 2026-09-05 | Phase 3 | Sync Protocol |
| S12 | W23-24 | 2026-09-06 – 2026-09-19 | Phase 3 | Local + LAN Sync |
| S13 | W25-26 | 2026-09-20 – 2026-10-03 | Phase 3 | Cloud Backends |
| S14 | W27-28 | 2026-10-04 – 2026-10-17 | Phase 3 | Sync Hardening |
| S15 | W29-30 | 2026-10-18 – 2026-10-31 | Phase 4 | REST API |
| S16 | W31-32 | 2026-11-01 – 2026-11-14 | Phase 4 | Electron Scaffold |
| S17 | W33-34 | 2026-11-15 – 2026-11-28 | Phase 4 | Core GUI Views |
| S18 | W35-36 | 2026-11-29 – 2026-12-12 | Phase 4 | Cross-Platform + Polish |
| S19 | W37-38 | 2026-12-13 – 2026-12-26 | Phase 5 | Security + Performance |
| S20 | W39-40 | 2027-01-03 – 2027-01-16 | Phase 5 | Docs + Distribution |
| S21 | W41-42 | 2027-01-17 – 2027-01-30 | Phase 5 | Release Engineering |

## 11. Risk Register

| ID | Risk | Impact | Likelihood | Mitigation |
| --- | --- | --- | --- | --- |
| R1 | Rust learning curve for contributors | Medium | High | Comprehensive docs, example code, mentoring |
| R2 | Plugin sandboxing complexity | High | Medium | Start with subprocess isolation, iterate |
| R3 | Cross-platform filesystem differences | Medium | High | Abstract via platform layer (`std::fs` + `notify`) |
| R4 | Scope creep | High | Medium | Strict phase gates, MVP focus, sprint reviews |
| R5 | Copyleft dependency contamination | Critical | Low | `cargo deny` in CI, automated license checks |
| R6 | Trademark conflict (post-registration) | High | Very Low | Monitoring + legal counsel on retainer |
| R7 | Electron binary size | Medium | Medium | Tree-shaking, lazy loading, compression |
| R8 | ONNX model compatibility gaps | Medium | Medium | Python fallback available, document per-model |
| R9 | AI model accuracy for categorization | Medium | High | Configurable confidence threshold, manual override |
| R10 | Sync conflict data loss | Critical | Low | 3-way merge, automatic backup before sync |

## 12. Contribution Model

### Pre-v1.0 (Current)

- **Core contributors only** (knx555 + invited collaborators)
- Feature branches → PR → Review → Merge to `main`
- Conventional Commits enforced
- Small, frequent commits (after every logical change)

### Post-v1.0

- Open to community contributions
- CONTRIBUTING.md with DCO (Developer Certificate of Origin)
- Issue labels: `good-first-issue`, `help-wanted`, `plugin-idea`
- Plugin contributions encouraged through SDK + examples
- Bilingual communication welcome (English + German)

---

## Document History

| Version | Date | Author | Changes |
| --- | --- | --- | --- |
| 1.0 | 2026-03-28 | Walter Codecraft | Initial plan |
| 1.1 | 2026-03-28 | Walter Codecraft | Rust-First architecture, Electron GUI (replaces Tauri), detailed Sprint breakdown, AI strategy, expanded milestones |

---

*This document is the living roadmap for MAVPARUAS SAOIRSE. Updated as the project evolves.*
