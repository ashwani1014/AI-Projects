# pyrefly: ignore [missing-import]
import fitz


def extract_text(pdf_path: str) -> str:
    """Extract readable text from a PDF."""

    extracted_pages = []

    with fitz.open(pdf_path) as pdf:
        for page_number, page in enumerate(pdf, start=1):
            text = page.get_text("text")

            if text.strip():
                extracted_pages.append(
                    f"[Page {page_number}]\n{text}"
                )

    return "\n\n".join(extracted_pages)

def chunk_text(
    text: str,
    chunk_size: int = 800,
    overlap: int = 120
) -> list[str]:
    """Split text into overlapping character chunks."""

    if chunk_size <= 0:
        raise ValueError("chunk_size must be positive")

    if overlap < 0 or overlap >= chunk_size:
        raise ValueError(
            "overlap must be non-negative and smaller than chunk_size"
        )

    chunks = []
    start = 0

    while start < len(text):
        end = min(start + chunk_size, len(text))
        chunk = text[start:end].strip()

        if chunk:
            chunks.append(chunk)

        if end == len(text):
            break

        start = end - overlap

    return chunks    