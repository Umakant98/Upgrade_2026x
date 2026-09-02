# Validation and Test Plan — ENOVIA V6 -> 3DEXPERIENCE R2026x

This file contains the validation checks, test cases, sample queries, and pass/fail criteria extracted from the PDF text stream.

1) Validation categories
- Functional smoke tests
- Data integrity tests
- Performance sanity checks
- Integration/end-to-end flows

2) Functional smoke tests (minimum)
- Admin login: verify single sign-on and local admin login succeed.
- Create/Edit/Save/Retrieve: perform CRUD on 3 representative objects in each major module (PLM, BOM, Document, Change Management).
- Search: global search returns results and pagination works.
- Attachment handling: upload and download a 10MB file, verify checksum.

3) Data integrity tests
- Row counts: compare pre-upgrade export row counts to post-upgrade counts for key tables. Example SQL (replace schema/table):
  - SELECT COUNT(*) FROM <SCHEMA>.<TABLE>;
- Checksums: compute checksum (MD5 or vendor-specified) over concatenated key columns; compare pre/post.
- Referential integrity: run queries to detect orphaned child rows.

4) Integration tests
- For each external integration (CAD connectors, ERP links): run the standard integration job and verify expected artifacts appear.
- API tests: run a subset of REST/SOAP calls; verify response codes and payloads.

5) Performance sanity checks
- Baseline: run representative queries used in production monitoring and capture response times before upgrade.
- Post-upgrade: run same queries and ensure median response time within acceptable threshold (e.g., < 25% degradation) — adjust threshold per customer SLA.

6) Automated test harness
- Where possible run automated test suites (unit + integration) against sandbox after rehearsal.
- Collect logs and attach to the runbook for auditing.

7) Pass/fail criteria (example)
- Critical functional tests: 100% pass
- Non-critical functional tests: >= 95% pass
- Data integrity: row counts and checksums must match; if mismatch, classify severity and follow rollback or remediation plan.

8) Evidence collection
- For each test case capture: test name, tester, timestamp, log file path, result (pass/fail), artifacts (screenshots, query output files).

---

End of file.