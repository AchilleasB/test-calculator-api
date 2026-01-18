from typing import List
from app.repository.history_repository import HistoryRepository

class InMemoryHistoryRepository(HistoryRepository):
    def __init__(self):
        self._storage = []

    def save(self, entry: dict) -> None:
        self._storage.append(entry)

    def list_history(self) -> List[dict]:
        return self._storage

    def clear(self) -> None:
        self._storage = []

