from dataclasses import dataclass


@dataclass
class UrlDTO:
    """
    Url information
    """
    url_id: int
    title: str
    original_url: str
    short_url: str
    