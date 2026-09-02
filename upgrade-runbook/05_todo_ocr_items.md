# OCR TODO Items — ENOVIA V6 -> 3DEXPERIENCE R2026x

This file lists the items that could not be extracted from the PDF text stream because they appear inside images (screenshots, diagrams, tables saved as images). I could not perform OCR in this environment, so please either run OCR on the PDF and paste the results here, or give me access to the OCR output and I will merge the verbatim commands/flags into the runbook files.

How to produce OCR text (recommended):
- Use any OCR tool that handles PDF images, for example:
  - `ocrmypdf --skip-text --deskew --rotate-pages input.pdf output.pdf` (Linux)
  - Adobe Acrobat Pro "Recognize Text"
  - Tesseract via `tesseract page.png out -l eng+fra` for each page
- Export the OCR text and provide me with a plain text file or paste the relevant verbatim commands into this file.

What I need from OCR output (for each image-only item):
- Exact command-line syntax (including flags and parameter names)
- Exact JVM/DB parameter names and recommended values
- Any tables that list supported versions or compatibility matrices (copy full table text)
- Diagrams that show ordered steps or stop/start sequences (transcribe steps in order)

Suggested pages/figures to OCR
- Any page that contains a screenshot of CLI commands or a table — these often include the only authoritative command syntax.
- Any figure or table labelled "Upgrade steps", "Compatibility matrix", "Database export/import command", "JVM settings", or similar.

Where I will insert OCR results
- I will merge verbatim commands/flags into:
  - upgrade-runbook/01_runbook_structured.md (exact step locations and Appendix)
  - upgrade-runbook/03_validation_and_tests.md (exact validation SQL/commands)
  - upgrade-runbook/05_todo_ocr_items.md will be cleared as items are merged.

If you want me to run OCR for you
- Provide OCR output files, or
- Grant me access to an OCR service or provide the OCRed text here.

Until OCR output is provided this file remains the authoritative TODO list for image-only content.
