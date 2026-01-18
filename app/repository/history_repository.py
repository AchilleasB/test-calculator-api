from typing import Protocol, List


class HistoryRepository(Protocol):
    """Protocol defining the interface for history storage."""
    
    def save(self, entry: dict) -> None:
        """Save a calculation entry to storage."""
        ...

    def list_history(self) -> List[dict]:
        """Retrieve all stored calculation entries."""
        ...

    def clear(self) -> None:
        """Clear all stored entries (used for testing)."""
        ...
