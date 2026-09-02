# Risk Register — ENOVIA V6 -> 3DEXPERIENCE R2026x

This risk register enumerates the technical risks and suggested mitigations based on the PDF text-stream extraction and typical ENOVIA upgrade projects. Items that were image-only in the PDF are listed in 05_todo_ocr_items.md and may contain additional vendor-specific risks once OCRed.

Columns: Risk ID | Area | Risk Description | Likelihood | Impact | Mitigation / Action Owner

R-001 | Database | Unsupported database version or missing intermediate upgrade path causing failed migration | Medium | High | Verify DB version compatibility against vendor matrix; apply required intermediate upgrades in sandbox first. Owner: DBA

R-002 | Data Integrity | Row-count or checksum mismatches after import leading to data loss | Low-Medium | High | Take full logical exports and physical snapshots; validate checksums and row counts in rehearsal; have rollback snapshot ready. Owner: DBA/PLM Lead

R-003 | Customizations | Custom code not compatible with R2026x APIs causing runtime errors | High | High | Inventory all customizations; recompile/test against R2026x API in sandbox; schedule remediation tasks with owners. Owner: Dev Lead

R-004 | Performance | Post-upgrade performance degradation due to config or JVM settings | Medium | High | Capture baseline performance metrics; tune JVM and DB parameters in sandbox; have rollback plan if SLAs not met. Owner: Ops

R-005 | Middleware | App server incompatibilities or misconfigured JVM flags causing outages | Medium | High | Validate supported app server versions; apply recommended JVM options; rehearse stop/start orders. Owner: Middleware Admin

R-006 | Backup/Restore | Backup fails or restore time exceeds acceptable window during rollback | Low | High | Test backup and restore procedures in rehearsal; optimize dump strategies and snapshots. Owner: Backup Admin

R-007 | Integrations | External integrations (CAD/ERP) fail due to protocol or payload changes | Medium | High | Validate integrations in sandbox; schedule integration stakeholders during cutover; keep fallback integration mode. Owner: Integration Lead

R-008 | Security | Credential rotation, expired certs, or permissions blocking upgrade scripts | Low | High | Verify all credentials, certificates and SSO tokens; ensure service accounts are active and not expiring during cutover. Owner: Security

R-009 | Cutover Window | Cutover taking longer than allocated causing business impact | Medium | High | Run timed rehearsals; prepare a prioritized rollback decision matrix and stagger tasks to allow partial rollbacks. Owner: PM/Release Lead

R-010 | Vendor Support | Vendor support not available during cutover window | Low | Critical | Confirm vendor on-call and escalation contacts for cutover; get written availability. Owner: PM

---

Instructions: Each risk should be tracked in the Excel tracker (Risk Register sheet) with owner, mitigation status, and residual risk. Update this file after each rehearsal and before production cutover.