# Nizza-Klassifikations-Analyse — MAVPARUAS SAOIRSE

> **Dokumenttyp**: Nizza-Klassifikation Tiefenanalyse (T-007)
> **Projekt**: MAVPARUAS SAOIRSE — Universelles Datei-Organisations- und Synchronisations-Tool
> **Datum**: 28. März 2026
> **Referenz**: Nizza-Klassifikation, 12. Ausgabe (2023), WIPO NCL(12-2023)
> **Quelle**: <https://www.wipo.int/classifications/nice/nclpub/>
> **Erstellt von**: Walter Codecraft (KI-Projektmanager, MAVPARUAS)

---

## 1. Produktprofil

**MAVPARUAS SAOIRSE** ist ein herunterladbares, lokal installiertes Software-Tool, das:

1. Dateien **intelligent organisiert** mittels lokaler KI/LLM-Modelle
2. Dateien über heterogene Speicher **synchronisiert** (Nextcloud/WebDAV, OneDrive, Dropbox, Hetzner Storage Box, USB, lokale SSD, Raspberry Pi)
3. **Lokal läuft** — Privacy-by-Design, keine Cloud-Verarbeitung
4. **Verteilt wird als**: Desktop-Anwendung, CLI-Tool, potenziell Mobile-App
5. **Paketnamen**: `@mavparuas/saoirse` (NPM), `mavparuas-saoirse` (PyPI/Crates.io)
6. **Lizenz**: MIT (Open Source)
7. **Nutzung**: Immer als Modul/Plugin innerhalb des MAVPARUAS-Ökosystems

---

## 2. Primäre Klassen

### 2.1 Klasse 9 — Wissenschaftliche und technische Apparate; Software

**Offizielle Klassenüberschrift (NCL 12)**: *Wissenschaftliche, Forschungs-, Navigations-, Vermessungs-, fotografische, Film-, audiovisuelle, optische, Wäge-, Mess-, Signal-, Detektions-, Prüf-, Inspektions-, Rettungs- und Lehrmittel und -instrumente; [...] aufgezeichnete und herunterladbare Medien, Computersoftware, unbeschriebene digitale oder analoge Aufnahme- und Speichermedien; [...]*

**Relevanz**: **JA — PRIMÄRE KLASSE**

**Anwendbare Waren-/Dienstleistungsbegriffe** (aus NCL 12 Alphabetischer Liste):

| NCL-Begriff | Nizza-ID | Anwendbarkeit auf SAOIRSE |
| --- | --- | --- |
| Computerprogramme, herunterladbar | 090717 | **DIREKTE PASSUNG** — SAOIRSE wird als herunterladbare Software vertrieben |
| Computerprogramme, gespeichert | 090658 | **DIREKTE PASSUNG** — SAOIRSE auf physischen/digitalen Medien |
| Computersoftware-Anwendungen, herunterladbar | 090949 | **DIREKTE PASSUNG** — Desktop/Mobile-Apps |
| Computersoftware-Plattformen, gespeichert oder herunterladbar | 090971 | **TEILWEISE** — SAOIRSE als Teil der MAVPARUAS-Plattform |

**Empfohlener Anmeldungswortlaut** (für DPMA/EUIPO-Anmeldung):

> *"Herunterladbare Computersoftware zum Organisieren, Sortieren, Synchronisieren und Verwalten digitaler Dateien auf lokalen und entfernten Speichergeräten und -diensten; herunterladbare Computersoftware zur intelligenten Dateierkennung, Kategorisierung und Organisation mittels künstlicher Intelligenz; herunterladbare Computerprogramme zur Datensynchronisation zwischen Cloud-Speicherdiensten, lokalen Speichergeräten und netzwerkgebundenen Speichern"*

**Kernunterscheidung**: Klasse 9 erfasst Software **als Produkt** (herunterladbar/aufgezeichnet). Dies ist SAOIRSEs primäre Vertriebsform.

---

### 2.2 Klasse 42 — Wissenschaftliche und technologische Dienstleistungen

**Relevanz**: **BEDINGT — SEKUNDÄRE KLASSE (nur bei SaaS-/gehosteter Version)**

**Bewertung**: Klasse 42 ist **aktuell NICHT anwendbar**, da SAOIRSE:

1. Als herunterladbare Software vertrieben wird (→ Klasse 9)
2. Privacy-by-Design mit lokaler Verarbeitung nutzt (kein Cloud-Processing)
3. Nicht als Dienst (SaaS/PaaS) angeboten wird

**Strategischer Hinweis**: Sollte MAVPARUAS jemals eine **gehostete Version** von SAOIRSE anbieten (Web-Interface, API-Endpunkt, verwalteter Sync-Service), wird Klasse 42 relevant. Für eine zukünftige Markenanmeldung könnte die vorsorgliche Einbeziehung von Klasse 42 breiteren Schutz bieten.

---

## 3. Sekundäre Klassen

### 3.1 Klasse 38 — Telekommunikation

**Relevanz**: **NEIN — NICHT ANWENDBAR**

**Kritische Unterscheidung**: Klasse 38 ist für Unternehmen, die **Kommunikationsinfrastruktur bereitstellen** (Telekommunikationsanbieter, ISPs, Messaging-Plattformen). SAOIRSE **nutzt** Telekommunikation (WebDAV, HTTP, Cloud-APIs), **stellt** aber keine Telekommunikationsdienstleistung **bereit**.

### 3.2 Klasse 35 — Werbung und Geschäftsführung

**Relevanz**: **NEIN — NICHT ANWENDBAR**

**Kritische Unterscheidung**: Klasse-35-Dienstleistungen sind **Geschäftsdienstleistungen, die eine Partei der anderen erbringt**. SAOIRSE ist ein **selbstbetriebenes Tool**, das Benutzer lokal installieren und ausführen — es erbringt keine Organisationsdienstleistungen für Dritte.

---

## 4. Zusammenfassende Klassifikationsmatrix

| Nizza-Klasse | Klassenname | Relevanz | Begründung |
| --- | --- | --- | --- |
| **9** | Software / Apparate | **PRIMÄR** | SAOIRSE ist herunterladbare Software — direkte Passung |
| **42** | IT-Dienstleistungen / SaaS | **BEDINGT** | Nur bei gehosteter/SaaS-Version. Sinnvoll als vorsorgliche Anmeldung. |
| 38 | Telekommunikation | **NICHT ANWENDBAR** | SAOIRSE nutzt Netzwerke, stellt aber keine bereit |
| 35 | Geschäftsdienstleistungen | **NICHT ANWENDBAR** | SAOIRSE ist ein selbstbetriebenes Tool, kein Datenverwaltungsdienst |
| 45 | Persönliche Dienstleistungen | **NICHT ANWENDBAR** | Kein Zusammenhang |
| 39 | Transport/Lagerhaltung | **NICHT ANWENDBAR** | Physische Lagerhaltung, nicht digital |
| 41 | Bildung | **NICHT ANWENDBAR** | Keine Bildungsdienstleistungen |

---

## 5. Strategische Implikationen

### 5.1 Für den Umfang der Markenrecherche

Die aktuelle Markenrecherche (T-001, abgeschlossen) hat korrekt auf **Klasse 9 und 42** fokussiert. Die Analyse bestätigt: Klasse 38 und 35 sind **nicht relevant** für SAOIRSE.

**Ergebnis**: Die bestehende Markenrecherche ist **vollständig und ausreichend**.

### 5.2 Für eine potenzielle Markenanmeldung (T-004)

**Minimale Anmeldung** (kostenoptimal):

- **Nur Klasse 9** — Deckt das tatsächliche Produkt ab
- DPMA: ~290 € (beinhaltet bis zu 3 Klassen)
- EUIPO: ~850 € (1 Klasse)

**Empfohlene Anmeldung** (breiterer Schutz):

- **Klasse 9 + Klasse 42** — Deckt sowohl herunterladbare Software ALS AUCH potenzielles zukünftiges SaaS-Angebot ab
- DPMA: ~290 € (immer noch innerhalb der 3-Klassen-Grenze)
- EUIPO: ~900 € (850 € + 50 € für 2. Klasse)

### 5.3 Verwechslungsgefahr-Bewertung

Unter dem **Grundsatz der Spezialität** (§ 14 Abs. 2 Nr. 2 MarkenG / Art. 8 Abs. 1 lit. b EUTMR) besteht **keine Verwechslungsgefahr**, da keine aktive "SAOIRSE"-Marke in Klasse 9 oder 42 existiert.

---

## Querverweise

- [Trademark Clearance Protocol (EN)](TRADEMARK-CLEARANCE-PROTOCOL_SAOIRSE_EN.md) — Abschnitt 4.8 (TMView-Analyse), Abschnitt 9 (T-007)
- [Trademark Clearance Protocol (DE)](TRADEMARK-CLEARANCE-PROTOCOL_SAOIRSE_DE.md)
- [Evidence Index](evidence/EVIDENCE-INDEX.md)

---

Dokumentversion: 1.0 | Erstellt: 28.03.2026 | MAVPARUAS Projekt
