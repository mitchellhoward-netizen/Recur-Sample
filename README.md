# Recur-Sample: a simulated eQMS product repo

> **SIMULATION.** This is not Cognidox's code. It is a stand-in product repo built for a demo.
> Module names mirror the modules Cognidox lists publicly at cognidox.com; everything else
> (code, versions, changelog) is invented.

**What it is for.** Pushes to this repo are the *internal clock* in a two-clock signal:

- **External clock:** a prospect's own dated regulatory events, from public FDA data (openFDA
  recalls with FDA-assigned root causes, 510(k) clearances) and the QMSR changeover.
- **Internal clock:** what the product team just shipped, here.

A Clay workflow tags every release to the quality-system requirements it addresses
(e.g. ISO 13485 §7.3.9 design change control, 21 CFR Part 11 records and e-signatures) and joins it to
every prospect's clock. The rep gets an alert only when both clocks point at the same requirement
inside its window.

## How a change is tagged

Code, not a model, reads three things in every commit:

| Signal | Example | Requirement |
|---|---|---|
| Conventional-commit scope | `feat(change-control): ...` | DCC: design and process change control |
| Module path | `modules/software_validation/...` | SWV: software validation |
| Regulatory terms | "Part 11 audit trail" | REC: records and e-signatures |

## Modules

| Path | Module | Requirement |
|---|---|---|
| `modules/document_management` | Document Management | ISO 13485 §4.2.4 |
| `modules/esignatures` | e-Signatures | §4.2.5, 21 CFR Part 11 |
| `modules/design_controls` | Design Controls | §7.3 |
| `modules/change_management` | Change Management | §7.3.9, §4.1.4 |
| `modules/software_validation` | Software Validation | §4.1.6, §7.5.6, IEC 62304 |
| `modules/capa` | CAPAs & Non-conformance | §8.5.2–8.5.3 |
| `modules/learning_management` | Learning Management | §6.2 |
| `modules/supplier_management` | Supplier Management | §7.4 |
| `modules/labelling` | Labelling (in Change Management) | §7.5.1 |
