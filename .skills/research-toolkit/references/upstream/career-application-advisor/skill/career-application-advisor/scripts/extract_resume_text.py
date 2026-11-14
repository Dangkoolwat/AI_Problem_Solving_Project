#!/usr/bin/env python3
"""Extract text from PDF or DOCX resumes without modifying the source file."""

from __future__ import annotations

import argparse
from pathlib import Path
import sys


def extract_pdf(path: Path) -> str:
    try:
        import pdfplumber
    except ImportError as exc:
        raise RuntimeError("PDF extraction requires pdfplumber") from exc

    with pdfplumber.open(str(path)) as document:
        return "\n\n".join(page.extract_text() or "" for page in document.pages)


def extract_docx(path: Path) -> str:
    try:
        from docx import Document
    except ImportError as exc:
        raise RuntimeError("DOCX extraction requires python-docx") from exc

    document = Document(str(path))
    blocks = [paragraph.text for paragraph in document.paragraphs]
    for table in document.tables:
        for row in table.rows:
            blocks.append("\t".join(cell.text for cell in row.cells))
    return "\n".join(blocks)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="PDF or DOCX source file")
    parser.add_argument("--output", type=Path, help="Optional UTF-8 text output")
    parser.add_argument("--max-chars", type=int, default=0, help="Limit stdout only; 0 means unlimited")
    args = parser.parse_args()

    source = args.input.expanduser().resolve()
    if not source.is_file():
        parser.error(f"file not found: {source}")

    suffix = source.suffix.lower()
    if suffix == ".pdf":
        text = extract_pdf(source)
    elif suffix == ".docx":
        text = extract_docx(source)
    else:
        parser.error("supported formats: .pdf and .docx")

    if args.output:
        destination = args.output.expanduser().resolve()
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(text, encoding="utf-8")

    stdout_text = text[: args.max_chars] if args.max_chars > 0 else text
    sys.stdout.buffer.write(stdout_text.encode("utf-8", errors="replace"))
    if text.strip():
        return 0
    print("\nWarning: no text extracted; the file may require OCR.", file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
