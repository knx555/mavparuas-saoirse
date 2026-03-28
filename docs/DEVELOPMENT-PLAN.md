# MAVPARUAS SAOIRSE — Enterprise Development Plan

> Version 1.0 | 2026-03-28 | Author: Walter Codecraft (knx555)

## 1. Executive Summary

MAVPARUAS SAOIRSE is a universal file organization, categorization, and synchronization tool. This document defines the phased development roadmap from legal foundation through production release under MIT License.

**Key Decisions:**

1. Core engine in **Rust** for performance and memory safety
2. Plugin architecture compatible with **MAVPARUAS ecosystem** (Perl, Python, C/C++, Rust)
3. **SQLite** as default database, configurable backends
4. **MIT License** — no copyleft dependencies permitted
5. Cross-platform: Linux (primary), Windows, macOS

## 2. Architecture Overview

```text
┌─────────────────────────────────────────────────────┐
│                    User Interfaces                   │
│  ┌──────────┐  ┌──────────┐  ┌───────────────────┐  │
│  │   CLI    │  │   GUI    │  │    REST API       │  │
│  │ (Rust)   │  │ (Tauri)  │  │ (Actix-Web/Axum) │  │
│  └────┬─────┘  └────┬─────┘  └────────┬──────────┘  │
│       └──────────────┼─────────────────┘             │
│                      ▼                               │
│  ┌───────────────────────────────────────────────┐   │
│  │              Core Engine (Rust)                │   │
│  │  ┌──────────┐ ┌──────────┐ ┌───────────────┐ │   │
│  │  │ File     │ │ Rule     │ │ Sync          │ │   │
│  │  │ Scanner  │ │ Engine   │ │ Manager       │ │   │
│  │  └──────────┘ └──────────┘ └───────────────┘ │   │
│  │  ┌──────────┐ ┌──────────┐ ┌───────────────┐ │   │
│  │  │ Category │ │ Watch    │ │ Config        │ │   │
│  │  │ Manager  │ │ Service  │ │ Manager       │ │   │
│  │  └──────────┘ └──────────┘ └───────────────┘ │   │
│  └───────────────────┬───────────────────────────┘   │
│                      ▼                               │
│  ┌───────────────────────────────────────────────┐   │
│  │           Plugin System (FFI/HTTP)            │   │
│  │  ┌────┐ ┌────────┐ ┌────┐ ┌─────┐ ┌──────┐  │   │
│  │  │Perl│ │ Python │ │Rust│ │ C++ │ │ HTTP │  │   │
│  │  └────┘ └────────┘ └────┘ └─────┘ └──────┘  │   │
│  └───────────────────┬───────────────────────────┘   │
│                      ▼                               │
│  ┌───────────────────────────────────────────────┐   │
│  │           Storage Layer                       │   │
│  │  ┌────────┐ ┌──────────┐ ┌─────────────────┐ │   │
│  │  │ SQLite │ │ Redis    │ │ Cloud Backends  │ │   │
│  │  │(default)│ │(optional)│ │ (S3/WebDAV)    │ │   │
│  │  └────────┘ └──────────┘ └─────────────────┘ │   │
│  └───────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────┘
```

## 3. Development Phases

### Phase 0: Foundation (Current — Q1 2026)

**Status: IN PROGRESS**

| Task | Status | Notes |
| --- | --- | --- |
| Trademark clearance (TMView, EUIPO, DPMA, USPTO) | DONE | All databases clear |
| Nice Classification analysis | DONE | Class 9 primary |
| Forensic evidence archival | DONE | SHA-256 verified |
| Usage documentation setup | DONE | First entries logged |
| MIT License + README | DONE | Bilingual EN/DE |
| GitHub repository | DONE | knx555/mavparuas-saoirse |
| Enterprise development plan | DONE | This document |
| CI/CD pipeline setup | TODO | GitHub Actions |
| CONTRIBUTING.md + Code of Conduct | TODO | — |
| Security policy (SECURITY.md) | TODO | — |

### Phase 1: Core Engine (Q2 2026)

**Goal**: Minimal viable file scanner + rule engine in Rust.

| Task | Priority | Estimate |
| --- | --- | --- |
| Rust project scaffold (Cargo workspace) | HIGH | — |
| File scanner module (recursive, async) | HIGH | — |
| Rule engine (TOML/YAML-based rules) | HIGH | — |
| Category manager (tagging, metadata) | HIGH | — |
| SQLite storage backend | HIGH | — |
| CLI interface (clap-based) | HIGH | — |
| Configuration system (TOML) | MEDIUM | — |
| Unit + integration test suite | HIGH | — |
| Linux filesystem event monitoring (inotify) | MEDIUM | — |
| Performance benchmarks | MEDIUM | — |

**Deliverable**: CLI tool that scans directories, applies rules, categorizes files.

### Phase 2: Plugin System (Q3 2026)

**Goal**: MAVPARUAS-compatible plugin architecture.

| Task | Priority | Estimate |
| --- | --- | --- |
| Plugin trait/interface definition | HIGH | — |
| Rust native plugin loading | HIGH | — |
| Python plugin bridge (PyO3 or subprocess) | HIGH | — |
| Perl plugin bridge (FFI or HTTP) | MEDIUM | — |
| C/C++ plugin bridge (FFI) | MEDIUM | — |
| HTTP-based external plugin protocol | MEDIUM | — |
| Plugin discovery + registration | HIGH | — |
| Plugin sandboxing (security) | HIGH | — |
| Example plugins (3+ languages) | MEDIUM | — |
| Plugin development documentation | HIGH | — |

**Deliverable**: Working plugin system with at least Rust + Python plugins.

### Phase 3: Synchronization (Q4 2026)

**Goal**: Cross-device file synchronization.

| Task | Priority | Estimate |
| --- | --- | --- |
| Sync protocol design | HIGH | — |
| Local-to-local sync (LAN) | HIGH | — |
| Conflict resolution strategy | HIGH | — |
| Change detection (hash-based) | HIGH | — |
| Incremental sync (delta) | MEDIUM | — |
| Cloud backend: WebDAV | MEDIUM | — |
| Cloud backend: S3-compatible | LOW | — |
| Sync status UI (CLI) | MEDIUM | — |
| End-to-end encryption (optional) | HIGH | — |
| Sync performance testing | HIGH | — |

**Deliverable**: Reliable local + LAN file synchronization.

### Phase 4: GUI & API (Q1 2027)

**Goal**: Desktop GUI + REST API for third-party integration.

| Task | Priority | Estimate |
| --- | --- | --- |
| REST API design (OpenAPI spec) | HIGH | — |
| API implementation (Actix-Web or Axum) | HIGH | — |
| API authentication (token-based) | HIGH | — |
| Tauri desktop application scaffold | HIGH | — |
| File browser view | HIGH | — |
| Rule editor UI | MEDIUM | — |
| Sync status dashboard | MEDIUM | — |
| Plugin management UI | MEDIUM | — |
| Accessibility (WCAG 2.1 AA) | HIGH | — |
| Cross-platform testing (Win/Mac/Linux) | HIGH | — |

**Deliverable**: Desktop application + documented REST API.

### Phase 5: Production Release (Q2 2027)

**Goal**: v1.0 release.

| Task | Priority | Estimate |
| --- | --- | --- |
| Security audit | HIGH | — |
| Performance optimization | HIGH | — |
| Documentation finalization | HIGH | — |
| Package distribution (crates.io, AUR, Homebrew) | HIGH | — |
| Release automation | MEDIUM | — |
| Community contribution workflow | MEDIUM | — |

## 4. Technology Decisions

### 4.1 Why Rust for Core

1. **Memory safety** without garbage collection — critical for file operations
2. **Performance** comparable to C/C++ for I/O-heavy workloads
3. **Cross-platform** compilation (Linux, Windows, macOS)
4. **Strong type system** catches bugs at compile time
5. **Ecosystem** (Tokio for async, Serde for serialization, Clap for CLI)
6. **MIT/Apache-2.0 dual-licensed** — compatible with project license

### 4.2 Why SQLite as Default

1. **Zero configuration** — single file database
2. **Embedded** — no external service required
3. **Battle-tested** — most widely deployed database engine
4. **Public domain** — no license concerns
5. **Sufficient for single-user** file management scenarios

### 4.3 Plugin Communication Hierarchy

| Method | Use Case | Latency |
| --- | --- | --- |
| FFI (direct) | Rust, C, C++ plugins | Lowest |
| PyO3 (embedded) | Python plugins (bundled) | Low |
| Subprocess + IPC | Python/Perl plugins (isolated) | Medium |
| HTTP/REST | External plugins (any language) | Highest |

### 4.4 GUI Framework: Tauri

1. **Rust backend** — native integration with core engine
2. **Web frontend** — HTML/CSS/JS (aligns with MAVPARUAS frontend standards)
3. **Small binary size** — uses system webview
4. **MIT License** — fully compatible
5. **Cross-platform** — Linux, Windows, macOS

## 5. Quality Standards

### 5.1 Testing Strategy

| Level | Tool | Coverage Target |
| --- | --- | --- |
| Unit Tests | `cargo test` | 80%+ |
| Integration Tests | `cargo test --test` | Critical paths |
| Plugin Tests | Per-language test frameworks | All plugin types |
| Performance | `criterion` benchmarks | Regression detection |
| Security | `cargo audit` + `cargo deny` | Zero known vulns |
| Linting | `clippy` + `rustfmt` | Zero warnings |

### 5.2 CI/CD Pipeline (GitHub Actions)

```yaml
# Planned pipeline stages
stages:
  - lint        # clippy, rustfmt, markdownlint
  - test        # unit + integration tests
  - security    # cargo audit, cargo deny, license check
  - build       # cross-platform compilation
  - release     # tagged releases → GitHub Releases
```

### 5.3 Code Standards

1. **Rust**: `rustfmt` + `clippy` with strict settings
2. **Python plugins**: `ruff` + `mypy`
3. **Documentation**: All public APIs documented
4. **Commits**: Conventional Commits (`feat:`, `fix:`, `docs:`, `refactor:`)
5. **Reviews**: All PRs require review before merge

## 6. Security Framework

### 6.1 Principles

1. **Least privilege** — plugins run sandboxed
2. **No network by default** — sync is opt-in
3. **Encryption at rest** — optional for sensitive metadata
4. **Encryption in transit** — TLS for all sync connections
5. **Dependency auditing** — automated via `cargo audit`

### 6.2 License Compliance

| Allowed | Forbidden (without approval) |
| --- | --- |
| MIT | GPL |
| BSD (2/3-clause) | AGPL |
| Apache 2.0 | LGPL (case-by-case) |
| MPL 2.0 | SSPL |
| ISC | — |
| Unlicense / CC0 | — |

**Enforcement**: `cargo deny` in CI pipeline checks all dependency licenses.

## 7. Repository Structure (Target)

```text
mavparuas-saoirse/
├── .github/
│   ├── workflows/          # CI/CD pipelines
│   ├── ISSUE_TEMPLATE/     # Bug/feature templates
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── copilot-instructions.md
├── crates/
│   ├── saoirse-core/       # Core engine library
│   ├── saoirse-cli/        # CLI binary
│   ├── saoirse-api/        # REST API server
│   ├── saoirse-plugins/    # Plugin system
│   └── saoirse-sync/       # Synchronization engine
├── plugins/
│   ├── examples/           # Example plugins
│   └── sdk/                # Plugin SDK
├── docs/
│   ├── legal/              # Trademark & legal (existing)
│   ├── architecture/       # Architecture Decision Records
│   ├── api/                # API documentation
│   └── guides/             # User & developer guides
├── scripts/                # Development scripts
├── walter-workspace/       # Project management
├── Cargo.toml              # Workspace manifest
├── LICENSE
├── README.md
├── README_DE.md
├── CONTRIBUTING.md
├── SECURITY.md
└── CODE_OF_CONDUCT.md
```

## 8. Milestones & Success Criteria

| Milestone | Phase | Success Criteria |
| --- | --- | --- |
| M0: Legal Foundation | 0 | Trademark clear, repo live, plan documented |
| M1: First Scan | 1 | CLI scans 10k files in < 5s |
| M2: Rule Engine | 1 | 20+ rule types, TOML config |
| M3: Plugin MVP | 2 | Rust + Python plugin working |
| M4: Local Sync | 3 | Bidirectional LAN sync, conflict resolution |
| M5: Desktop App | 4 | Tauri app on Linux, basic file browser |
| M6: v1.0 Release | 5 | All tests pass, docs complete, packages published |

## 9. Risk Register

| Risk | Impact | Likelihood | Mitigation |
| --- | --- | --- | --- |
| Rust learning curve for contributors | Medium | High | Good docs, example code, mentoring |
| Plugin sandboxing complexity | High | Medium | Start with subprocess isolation |
| Cross-platform filesystem differences | Medium | High | Abstract via platform layer |
| Scope creep | High | Medium | Strict phase gates, MVP focus |
| Copyleft dependency contamination | Critical | Low | Automated license checks in CI |
| Trademark conflict (post-registration) | High | Very Low | Monitoring + legal counsel |

## 10. Contribution Model

### Pre-v1.0 (Current)

- **Core contributors only** (knx555 + invited collaborators)
- Feature branches → PR → Review → Merge to `main`
- Conventional Commits enforced

### Post-v1.0

- Open to community contributions
- CONTRIBUTING.md with DCO (Developer Certificate of Origin)
- Issue labels: `good-first-issue`, `help-wanted`, `plugin-idea`
- Plugin contributions encouraged through SDK + examples

---

## Document History

| Version | Date | Author | Changes |
| --- | --- | --- | --- |
| 1.0 | 2026-03-28 | Walter Codecraft | Initial plan |

---

*This document is the living roadmap for MAVPARUAS SAOIRSE. Updated as the project evolves.*
