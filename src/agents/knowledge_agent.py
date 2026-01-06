from pathlib import Path
from typing import Optional

from src.utils.config_loader import load_config
from src.utils.logger import get_logger

# Optional dependency (prevents crash if not installed)
try:
    from docx import Document
except ImportError:
    Document = None


def _get_docs_base_path() -> Path:
    """
    Safely resolve docs base path from config.
    Falls back to data/docs if not configured.
    """
    config = load_config()
    docs_path = config.get("sharepoint", {}).get("docs_base_path", "data/docs")
    return Path(docs_path)


def search_docs(query: str, trace_id: Optional[str] = None) -> str:
    """
    Search SharePoint-exported documents for relevant content.
    Currently supports .docx files.

    Args:
        query (str): user question
        trace_id (str): trace id for logging

    Returns:
        str: extracted relevant text or fallback message
    """
    logger = get_logger("KNOWLEDGE_AGENT", trace_id)

    def search_docs(query: str):
        config = load_config()
        sp = config.get("sharepoint")

        if not sp:
            return []

        docs_base_path = sp.get("docs_base_path")
   
    logger.info(f"Searching documents in: {docs_base_path}")

    if not docs_base_path.exists():
        logger.warning("Docs base path does not exist")
        return "Knowledge base is not configured yet."

    if not Document:
        logger.warning("python-docx is not installed")
        return "Document search is not available in this environment."

    results = []

    for file_path in docs_base_path.glob("*.docx"):
        try:
            doc = Document(file_path)
            full_text = "\n".join(p.text for p in doc.paragraphs)

            if query.lower() in full_text.lower():
                results.append(full_text[:700])

        except Exception as e:
            logger.error(f"Failed to read {file_path.name}: {e}")

    if not results:
        logger.info("No matching documentation found")
        return "No relevant documentation found."

    logger.info(f"Found {len(results)} relevant document(s)")
    return "\n\n".join(results)
