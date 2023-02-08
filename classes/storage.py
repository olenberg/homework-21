from abc import ABC, abstractmethod


class Storage(ABC):
    @property
    @abstractmethod
    def items(self) -> dict[str, int]:
        pass

    @property
    @abstractmethod
    def capacity(self) -> int:
        pass

    @abstractmethod
    def add(self, title: str, count: int) -> None:
        pass

    @abstractmethod
    def remove(self, title: str, count: int) -> None:
        pass

    @abstractmethod
    def get_free_space(self) -> int:
        pass

    @abstractmethod
    def get_items(self) -> dict[str, int]:
        pass

    @abstractmethod
    def get_unique_items_count(self) -> int:
        pass
