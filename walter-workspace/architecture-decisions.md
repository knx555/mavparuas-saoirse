# Architecture Decision Records — MAVPARUAS SAOIRSE

> Format: Lightweight ADR | Aktualisiert: 2026-03-28

## ADR-001: Rust als Core-Sprache

- **Status**: Akzeptiert
- **Datum**: 2026-03-28
- **Kontext**: Core Engine braucht hohe I/O-Performance für Dateisystem-Operationen, Speichersicherheit ohne GC, und Cross-Platform-Kompilierung.
- **Entscheidung**: Rust für die Core Engine.
- **Begründung**: Speichersicherheit ohne GC, Performance auf C-Niveau, starkes Typsystem, MIT/Apache-2.0 dual-lizenziert, exzellentes Async-Ökosystem (Tokio).
- **Alternativen**: Go (GC-Pausen, weniger kontrolle über Memory), C++ (keine Memory Safety), Python (zu langsam für Core).

## ADR-002: SQLite als Standard-Datenbank

- **Status**: Akzeptiert
- **Datum**: 2026-03-28
- **Kontext**: Lokale Datei-Metadaten, Kategorien und Sync-Status müssen persistent gespeichert werden. Kein externer Service für Einzelbenutzer-Szenarien.
- **Entscheidung**: SQLite als Default, konfigurierbare Backends.
- **Begründung**: Zero-Config, einzelne Datei, Public Domain, ausreichend für lokale Nutzung.
- **Alternativen**: Redis (In-Memory, braucht Service), PostgreSQL (Overkill für lokal).

## ADR-003: MIT-Lizenz

- **Status**: Akzeptiert
- **Datum**: 2026-03-28
- **Kontext**: Maximale Freiheit für kommerzielle und nicht-kommerzielle Nutzung. Keine Copyleft-Kontamination.
- **Entscheidung**: MIT License. Nur permissive Dependencies erlaubt.
- **Begründung**: Einfachste permissive Lizenz, maximale Kompatibilität, keine Verpflichtung zur Quellcode-Offenlegung bei Derivaten.
- **Enforcement**: `cargo deny` in CI-Pipeline.

## ADR-004: Electron + TypeScript für Desktop-GUI

- **Status**: Akzeptiert (ersetzt Tauri-Vorschlag)
- **Datum**: 2026-03-28
- **Kontext**: Desktop-Anwendung für Phase 4 benötigt Cross-Platform UI mit exzellenter Barrierefreiheit (Screen-Reader-Unterstützung ist nicht verhandelbar).
- **Entscheidung**: Electron (TypeScript Frontend) + Rust-Sidecar (Backend via IPC).
- **Begründung**: TypeScript als reine Präsentationsschicht, ALLE Geschäftslogik im Rust-Sidecar. Electron bietet: (1) Überlegene Accessibility via Chromium, (2) Reifes Ökosystem für komplexe UIs, (3) Bewährtes Debugging-Toolkit, (4) MIT-lizenziert.
- **Architektur**: Renderer Process (TS) ↔ IPC JSON-RPC ↔ Main Process (Rust Sidecar). Kein Business-Code im Frontend.
- **Grenzregel**: Wenn es als Rust-Funktion ausgedrückt werden kann → muss es in Rust sein.
- **Alternativen abgelehnt**: Tauri (weniger reife Accessibility), GTK4-rs (nur Linux nativ), Iced (zu jung für Produktion).
- **Supersedes**: Ursprünglicher ADR-004 "Tauri für Desktop-GUI" (Vorgeschlagen → Abgelehnt).

## ADR-005: Plugin-Kommunikation via FFI + HTTP Hybrid

- **Status**: Vorgeschlagen (Phase 2)
- **Datum**: 2026-03-28
- **Kontext**: MAVPARUAS-Ökosystem nutzt Perl, Python, C/C++, Rust. Plugins müssen in verschiedenen Sprachen funktionieren.
- **Entscheidung**: Hierarchisches System — Dynamic Loading für Rust, FFI für C/C++, ONNX/Subprocess für Python-KI, HTTP für externe Plugins.
- **Begründung**: Optimale Latenz pro Sprache, HTTP als universeller Fallback. Python nur für KI/ML via isoliertem Subprocess.
- **Trade-offs**: Komplexere Plugin-Registry, aber maximale Sprachflexibilität.

## ADR-006: Projektname SAOIRSE

- **Status**: Akzeptiert
- **Datum**: 2026-03-28
- **Kontext**: Universelles File-Tool braucht einen einprägsamen, markenrechtlich freien Namen.
- **Entscheidung**: SAOIRSE (irisch: "Freiheit").
- **Begründung**: TMView (0 Treffer in Klasse 9/42), EUIPO/DPMA/USPTO alle frei. Irische Namenstradition (Markus' Präferenz). Forensische Beweissicherung abgeschlossen.
- **Referenz**: [Trademark Clearance Protocol](../docs/legal/TRADEMARK-CLEARANCE-PROTOCOL_SAOIRSE_EN.md)

## ADR-007: Rust-First Entwicklungsphilosophie

- **Status**: Akzeptiert
- **Datum**: 2026-03-28
- **Kontext**: Klare Sprachhierarchie nötig, um Tech-Stack-Zersplitterung zu verhindern. Markus' Vorgabe: Rust für alles was möglich ist, Python nur für KI wo es nicht anders geht, TypeScript nur Bedien-Schicht.
- **Entscheidung**: Strikte Rust-First Entwicklungsphilosophie mit dokumentierten Ausnahmen.
- **Sprachhierarchie**:
  - Priorität 1 (Primär): **Rust** — Core Engine, Geschäftslogik, Routing, API, Sync, Plugins, CLI
  - Priorität 2 (Nur KI): **Python** — NUR wenn kein Rust-Crate existiert (z.B. kein ONNX-Export für bestimmtes Modell)
  - Priorität 3 (Nur GUI): **TypeScript** — NUR Rendering und Benutzerinteraktion in Electron
- **Begründung**: Einheitlicher Tech-Stack, minimale Deployment-Komplexität, maximale Performance, Single-Binary für Core.
- **Enforcement**: Code-Review prüft Sprachgrenzen. Python-Code nur in `plugins/ai/`. TypeScript nur in `gui/`.

## ADR-008: Privacy-by-Design & Lokale KI

- **Status**: Akzeptiert
- **Datum**: 2026-03-28
- **Kontext**: MAVPARUAS SAOIRSE verarbeitet persönliche Dateien. Datenschutz ist ABSOLUT — mehr als DSGVO-Compliance.
- **Entscheidung**: Keine Daten verlassen den Rechner des Nutzers ohne explizite Zustimmung. KI-Modelle laufen ausschließlich lokal.
- **Begründung**: Privacy-by-Design ist Markus' fundamentale Anforderung. Kein Cloud-Inference, kein Telemetrie, kein Tracking. Sync nur bei expliziter Nutzer-Konfiguration.
- **Technische Umsetzung**: Lokale ONNX-Modelle via `ort`, kein Netzwerk-Default, Firewall-freundlich.

---

Nächster ADR: ADR-009 (verfügbar für Phase 1 Architektur-Entscheidungen)
