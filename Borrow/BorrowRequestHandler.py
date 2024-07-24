from abc import ABC, abstractmethod
from typing import Optional


class BorrowRequestHandler(ABC):
    def __init__(self, successor: Optional['BorrowRequestHandler'] = None) -> None:
        self.successor = successor

    @abstractmethod
    def handle_request(self, user_id: int, book_title: str) -> bool:
        pass
