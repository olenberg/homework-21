from classes.storage import Storage


class Store(Storage):
    def __init__(self):
        self._items: dict[str, int] = dict()
        self._capacity: int = 100

    @property
    def items(self) -> dict[str, int]:
        return self._items

    @property
    def capacity(self) -> int:
        return self._capacity

    def add(self, title: str, count: int) -> None:
        if title not in self.items.keys():
            self._items[title] = count
        else:
            self._items[title] += count

    def remove(self, title: str, count: int) -> None:
        self._items[title] -= count

    def get_free_space(self) -> int:
        return self.capacity - sum(self._items.values())

    def get_items(self) -> dict[str, int]:
        return self._items

    def get_unique_items_count(self) -> int:
        return len(self._items)
