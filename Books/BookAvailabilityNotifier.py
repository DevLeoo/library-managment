from abc import ABC, abstractmethod
from typing import List


class Observer(ABC):
    @abstractmethod
    def update(self, message: str) -> None:
        pass


class BookAvailabilityNotifier:
    def __init__(self) -> None:
        self._observers: List[Observer] = []

    def subscribe(self, observer: Observer) -> None:
        self._observers.append(observer)

    def unsubscribe(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self, message: str) -> None:
        for observer in self._observers:
            observer.update(message)
