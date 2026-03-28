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

## ADR-004: Tauri für Desktop-GUI

- **Status**: Vorgeschlagen (Phase 4)
- **Datum**: 2026-03-28
- **Kontext**: Desktop-Anwendung für Phase 4 benötigt Cross-Platform UI.
- **Entscheidung**: Tauri (Rust-Backend + Web-Frontend).
- **Begründung**: Rust-native, kleiner Binary-Footprint, nutzt System-WebView, MIT-lizenziert.
- **Alternativen**: GTK4-rs (nur Linux nativ), Electron (zu groß), Iced (zu jung).

## ADR-005: Plugin-Kommunikation via FFI + HTTP Hybrid

- **Status**: Vorgeschlagen (Phase 2)
- **Datum**: 2026-03-28
- **Kontext**: MAVPARUAS-Ökosystem nutzt Perl, Python, C/C++, Rust. Plugins müssen in verschiedenen Sprachen funktionieren.
- **Entscheidung**: Hierarchisches System — FFI für Rust/C/C++, PyO3 für Python, HTTP für externe Plugins.
- **Begründung**: Optimale Latenz pro Sprache, HTTP als universeller Fallback.
- **Trade-offs**: Komplexere Plugin-Registry, aber maximale Sprachflexibilität.

## ADR-006: Projektname SAOIRSE

- **Status**: Akzeptiert
- **Datum**: 2026-03-28
- **Kontext**: Universelles File-Tool braucht einen einprägsamen, markenrechtlich freien Namen.
- **Entscheidung**: SAOIRSE (irisch: "Freiheit").
- **Begründung**: TMView (0 Treffer in Klasse 9/42), EUIPO/DPMA/USPTO alle frei. Irische Namenstradition (Markus' Präferenz). Forensische Beweissicherung abgeschlossen.
- **Referenz**: [Trademark Clearance Protocol](../docs/legal/TRADEMARK-CLEARANCE-PROTOCOL_SAOIRSE_EN.md)

---

Nächster ADR: ADR-007 (verfügbar für Phase 1 Architektur-Entscheidungen)
