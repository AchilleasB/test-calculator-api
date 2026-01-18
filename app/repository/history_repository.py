from typing import Protocol, List

class HistoryRepository(Protocol):
    def save(self, entry: dict) -> None:
        ...

    def list_history(self) -> List[dict]:
        ...
