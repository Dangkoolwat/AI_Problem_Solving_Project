---
name: resume-document-qa
description: Export and verify a resume or application document when PDF/DOCX delivery, a hard page count, ATS-safe structure, or visual quality matters. Use only after content and claims are locked.
---

# Resume Document QA

## Procedure

1. Confirm required formats, page count, locale, filename, and chronology before layout work.
2. Export both editable DOCX and PDF when requested. Prefer a restrained single-column design with standard headings and selectable text.
3. Verify the exact PDF page count and page size.
4. Render and inspect every page for clipping, overlap, orphaned headings, broken wrapping, crowded spacing, or unexpected blank pages.
5. Inspect effective text sizes, not only named styles. Check contact information and links.
6. Extract PDF text and confirm reading order. Test DOCX package integrity and run available accessibility checks.
7. Re-render after every content or typography change that can affect pagination.
8. Report each claim as:
   - `executed`: the real path was run and observed;
   - `code-path`: implementation was inspected but not executed;
   - `assumed`: not verified.

## Done criterion

Delivery is complete only when the requested files exist, the real export path was run, the exact page and chronology constraints pass, every page was visually inspected, text extraction is coherent, links and package integrity pass, and no content claim exceeds the evidence ledger.
