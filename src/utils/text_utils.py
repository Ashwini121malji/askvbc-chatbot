def clean_text(text: str) -> str:
    """
    Normalizes spacing and punctuation for responses.
    """
    return " ".join(text.split())
