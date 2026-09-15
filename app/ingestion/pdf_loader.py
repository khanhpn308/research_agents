from pathlib import Path
from typing import TypedDict

import pymupdf


class LoadedPaper(TypedDict):
    path: str
    filename: str
    page_count: int
    char_count: int
    text: str


def load_pdf(
    pdf_path: str | Path,
) -> LoadedPaper:

    path = Path(pdf_path)

    if not path.exists():
        raise FileNotFoundError(
            f"PDF not found: {path}"
        )

    if path.suffix.lower() != ".pdf":
        raise ValueError(
            f"Not a PDF file: {path}"
        )

    document = pymupdf.open(path)

    pages: list[str] = []

    try:
        for page_number, page in enumerate(
            document,
            start=1,
        ):
            text = page.get_text("text").strip()

            pages.append(
                f"\n\n===== PAGE {page_number} =====\n\n"
                f"{text}"
            )

    finally:
        document.close()

    full_text = "".join(pages).strip()

    if len(full_text) < 500:
        raise RuntimeError(
            f"Very little machine-readable text was "
            f"extracted from {path.name}. "
            "The PDF may be scanned or image-based."
        )

    return {
        "path": str(path.resolve()),
        "filename": path.name,
        "page_count": len(pages),
        "char_count": len(full_text),
        "text": full_text,
    }