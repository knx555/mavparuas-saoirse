# Nice Classification Analysis — MAVPARUAS SAOIRSE

> **Document Type**: Nice Classification Deep Analysis (T-007)
> **Project**: MAVPARUAS SAOIRSE — Universal File Organization and Synchronization Tool
> **Date**: March 28, 2026
> **Reference**: Nice Classification, 12th Edition (2023), WIPO NCL(12-2023)
> **Source**: https://www.wipo.int/classifications/nice/nclpub/
> **Prepared by**: Walter Codecraft (AI Project Manager, MAVPARUAS)

---

## 1. Product Profile

**MAVPARUAS SAOIRSE** is a downloadable, locally-installed software tool that:

1. **Organizes** files intelligently using local AI/LLM models
2. **Synchronizes** files across heterogeneous storage (Nextcloud/WebDAV, OneDrive, Dropbox, Hetzner Storage Box, USB, local SSD, Raspberry Pi)
3. **Runs locally** — privacy-by-design, no cloud processing
4. **Distributed as**: Desktop application, CLI tool, potentially mobile app
5. **Package names**: `@mavparuas/saoirse` (NPM), `mavparuas-saoirse` (PyPI/Crates.io)
6. **License**: MIT (open source)
7. **Usage**: Always as module/plugin within MAVPARUAS ecosystem

---

## 2. Primary Classes

### 2.1 Class 9 — Scientific and Technical Apparatus; Software

**Official Heading (NCL 12)**: *Scientific, research, navigation, surveying, photographic, cinematographic, audiovisual, optical, weighing, measuring, signalling, detecting, testing, inspecting, life-saving and teaching apparatus and instruments; apparatus and instruments for conducting, switching, transforming, accumulating, regulating or controlling the distribution or use of electricity; apparatus and instruments for recording, transmitting, reproducing or processing sound, images or data; recorded and downloadable media, computer software, blank digital or analogue recording and storage media; mechanisms for coin-operated apparatus; cash registers, calculating devices; computers and computer peripheral devices; diving suits, divers' masks, ear plugs for diving, nose clips for divers and swimmers, gloves for divers, breathing apparatus for underwater swimming; fire-extinguishing apparatus.*

**Relevance**: **YES — PRIMARY CLASS**

**Applicable Goods/Services Terms** (from NCL 12 Alphabetical List):

| NCL Term | Nice ID | Applicability to SAOIRSE |
| --- | --- | --- |
| Computer programs, downloadable | 090717 | **DIRECT FIT** — SAOIRSE is distributed as downloadable software |
| Computer programs, recorded | 090658 | **DIRECT FIT** — SAOIRSE on physical/digital media |
| Computer software applications, downloadable | 090949 | **DIRECT FIT** — Desktop/mobile apps |
| Computer software platforms, recorded or downloadable | 090971 | **PARTIAL** — SAOIRSE as part of MAVPARUAS platform |
| Data processing apparatus | 090372 | **PARTIAL** — Only if distributed with hardware (e.g., Raspberry Pi bundle) |
| Computer peripheral devices | 090732 | **NO** — SAOIRSE is software, not hardware |

**Specific Registration Wording** (recommended for DPMA/EUIPO filing):

> *"Downloadable computer software for organizing, sorting, synchronizing and managing digital files across local and remote storage devices and services; downloadable computer software for intelligent file recognition, categorization and organization using artificial intelligence; downloadable computer programs for data synchronization between cloud storage services, local storage devices and network-attached storage"*

**Key Distinction**: Class 9 covers software **as a product** (downloadable/recorded). This is SAOIRSE's primary distribution form.

---

### 2.2 Class 42 — Scientific and Technological Services

**Official Heading (NCL 12)**: *Scientific and technological services and research and design relating thereto; industrial analysis, industrial research and industrial design services; quality control and authentication services; design and development of computer hardware and software.*

**Relevance**: **PARTIAL — SECONDARY CLASS (only if SaaS/hosted version offered)**

**Applicable Goods/Services Terms**:

| NCL Term | Nice ID | Applicability to SAOIRSE |
| --- | --- | --- |
| Computer software design | 420220 | **NO** — SAOIRSE is a product, not a design service |
| Computer programming | 420227 | **NO** — unless MAVPARUAS sells programming services |
| Software as a service (SaaS) | 420263 | **ONLY IF** a hosted/web version of SAOIRSE is ever offered |
| Cloud computing | 420261 | **ONLY IF** cloud processing is offered (contradicts privacy-by-design) |
| Platform as a service (PaaS) | 420264 | **NO** — SAOIRSE is not a platform service |
| Computer software consultancy | 420209 | **NO** — unless consulting is offered around SAOIRSE |
| Providing temporary use of online non-downloadable software | — | **ONLY IF** a web version exists |

**Assessment**: Class 42 is **currently NOT applicable** because SAOIRSE is:

1. Distributed as downloadable software (→ Class 9)
2. Privacy-by-design with local processing (no cloud)
3. Not offered as a service (SaaS/PaaS)

**Strategic Note**: If MAVPARUAS ever offers a **hosted version** of SAOIRSE (web interface, API endpoint, managed sync service), Class 42 would become relevant. For a future trademark registration, including Class 42 preemptively could provide broader protection.

**Recommended Registration Wording** (preemptive, for future-proofing):

> *"Providing temporary use of online non-downloadable software for file organization and synchronization; software as a service (SaaS) services featuring software for file management, synchronization and intelligent organization"*

---

## 3. Secondary Classes

### 3.1 Class 38 — Telecommunications

**Official Heading (NCL 12)**: *Telecommunications services.*

**Relevance**: **NO — NOT APPLICABLE**

**Analysis**:

Class 38 covers the **provision of telecommunications infrastructure and services**:

| NCL Term | Nice ID | Applicability |
| --- | --- | --- |
| Transmission of digital files | 380050 | **MISLEADING** — This covers telecom providers, not software that uses telecom |
| Electronic data interchange | 380044 | **NO** — This is for telecom/EDI service providers |
| Providing access to databases | 380042 | **NO** — SAOIRSE doesn't provide database access as a service |
| Computer aided transmission of messages and images | 380038 | **NO** — Telecom operator service |

**Critical Distinction**: Class 38 is for entities that **provide communication infrastructure** (telcos, ISPs, messaging platforms). SAOIRSE **uses** telecommunications (WebDAV, HTTP, cloud APIs) but does not **provide** telecommunications service. The distinction is analogous to:

- **Class 38**: A company that operates telephone lines (Deutsche Telekom)
- **Class 9**: Software that makes phone calls over existing lines (a VoIP app)

SAOIRSE synchronizes files over existing networks and cloud services. It does not provide the transmission service itself.

**Conclusion**: Class 38 is **NOT relevant** for SAOIRSE. The synchronization feature is a **software function** (Class 9), not a **telecom service** (Class 38).

---

### 3.2 Class 35 — Advertising and Business Management Services

**Official Heading (NCL 12)**: *Advertising; business management, organization and administration; office functions.*

**Relevance**: **NO — NOT APPLICABLE**

**Analysis**:

Class 35 includes some data-related terms:

| NCL Term | Nice ID | Applicability |
| --- | --- | --- |
| Systemization of information into computer databases | 350117 | **MISLEADING** — This covers companies offering this as a SERVICE to clients |
| Compilation of information into computer databases | 350134 | **NO** — Same: a human-provided data entry service |
| Data search in computer files for others | 350127 | **NO** — SAOIRSE searches its own files, not "for others" as a service provider |
| Updating and maintenance of data in computer databases | 350150 | **NO** — Database management services for third parties |

**Critical Distinction**: Class 35 services are **business services provided by one party to another**. A data management consulting firm that organizes client databases registers in Class 35. SAOIRSE is a **self-operated tool** that users install and run locally — it doesn't provide organization services to others.

**Conclusion**: Class 35 is **NOT relevant** for SAOIRSE.

---

## 4. Other Potentially Relevant Classes

### 4.1 Class 45 — Personal and Social Services

**Relevance**: **NO** — Class 45 covers legal services, security services, personal services. No connection to file management software.

### 4.2 Class 37 — Repair and Installation Services

**Relevance**: **NO** — Unless MAVPARUAS offers installation/setup services for SAOIRSE, which is not planned.

### 4.3 Class 41 — Education and Entertainment

**Relevance**: **NO** — Unless MAVPARUAS publishes educational content/tutorials about SAOIRSE as a separate commercial service. YouTube tutorials alone do not create Class 41 services.

### 4.4 Class 36 — Financial Services / Class 39 — Transport and Storage

**Relevance**: **NO** — "Storage" in Class 39 refers to **physical storage of goods** (warehouses), not digital storage. A common misunderstanding.

---

## 5. Summary Classification Matrix

| Nice Class | Class Name | Relevance | Reasoning |
| --- | --- | --- | --- |
| **9** | Software / Apparatus | **PRIMARY** | SAOIRSE is downloadable software — direct fit |
| **42** | IT Services / SaaS | **CONDITIONAL** | Only if hosted/SaaS version is ever offered. Useful as preemptive registration. |
| 38 | Telecommunications | **NOT APPLICABLE** | SAOIRSE uses networks, it doesn't provide networking |
| 35 | Business Services | **NOT APPLICABLE** | SAOIRSE is a self-operated tool, not a data management service for others |
| 45 | Personal Services | **NOT APPLICABLE** | No connection |
| 39 | Transport/Storage | **NOT APPLICABLE** | Physical storage, not digital |
| 41 | Education | **NOT APPLICABLE** | No educational services |

---

## 6. Strategic Implications

### 6.1 For Trademark Search Scope

The current trademark search (T-001, completed) correctly focused on **Class 9 and 42**. The inclusion of Class 38 and 35 in the original scope was conservative and appropriate for due diligence, but the analysis confirms these classes are **not relevant** to SAOIRSE.

**Result**: The existing trademark search is **complete and sufficient** for SAOIRSE's actual use case.

### 6.2 For Potential Registration (T-004)

If Markus decides to register "MAVPARUAS SAOIRSE" as a trademark:

**Minimum Registration** (cost-optimal):
- **Class 9 only** — Covers the actual product (downloadable software)
- DPMA: ~€290 (includes up to 3 classes)
- EUIPO: ~€850 (1 class)

**Recommended Registration** (broader protection):
- **Class 9 + Class 42** — Covers both downloadable software AND potential future SaaS offering
- DPMA: ~€290 (still within 3-class allowance)  
- EUIPO: ~€900 (€850 + €50 for 2nd class)

**Strategic Advantage of Including Class 42**: Even if SAOIRSE is currently local-only, including Class 42 prevents third parties from registering "SAOIRSE" as a SaaS product in the future. The incremental cost is minimal (€50 at EUIPO, free at DPMA up to 3 classes).

### 6.3 For Likelihood of Confusion Assessment

The TMView analysis (Section 4.8 of the Clearance Protocol) found **16 hits** for "SAOIRSE" worldwide. None were in Class 9 or had an active Class 42 registration. The closest was:

- **"SAOIRSE NETWORK"** (India, Class 41) — Different class, different name, different jurisdiction
- **"CUMANN NA SAOIRSE"** (USA, Class 42) — Status: **Dead** since 2000, political organization

Under the **principle of specialty** (Grundsatz der Spezialität / § 14 Abs. 2 Nr. 2 MarkenG / Art. 8 Abs. 1 lit. b EUTMR), likelihood of confusion requires:
1. Identity or similarity of marks **AND**
2. Identity or similarity of goods/services

Since no active "SAOIRSE" trademark exists in Class 9 or 42, condition (2) is not met for any existing mark. **No likelihood of confusion exists.**

---

## 7. Key Distinction: Class 9 vs. Class 42

| Aspect | Class 9 (Software Product) | Class 42 (Software Service) |
| --- | --- | --- |
| **What is protected** | The software itself (downloadable, recorded) | The service of providing software access |
| **Distribution** | Downloaded, installed, run locally | Accessed online, hosted by provider |
| **Revenue model** | One-time purchase, free download | Subscription, pay-per-use |
| **Data location** | User's device | Provider's servers |
| **SAOIRSE fit** | **YES** — Local installation, privacy-by-design | **Only if** hosted version offered |
| **Example** | Microsoft Office (boxed/downloaded) | Google Docs (web-based) |

SAOIRSE currently fits **exclusively in Class 9** due to its local-first, privacy-by-design architecture.

---

## Cross-References

- [Trademark Clearance Protocol (EN)](TRADEMARK-CLEARANCE-PROTOCOL_SAOIRSE_EN.md) — Section 4.8 (TMView Analysis), Section 9 (T-007)
- [Trademark Clearance Protocol (DE)](TRADEMARK-CLEARANCE-PROTOCOL_SAOIRSE_DE.md)
- [Evidence Index](evidence/EVIDENCE-INDEX.md)

---

*Document Version: 1.0 | Generated: 2026-03-28 | MAVPARUAS Project*
