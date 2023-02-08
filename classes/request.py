class Request:
    def __init__(self, request: str):
        data: list[str] = request.strip().split()
        self._location_from: str = data[4]
        self._location_to: str = data[6]
        self._amount: int = int(data[1])
        self._product: str = data[2]

    @property
    def location_from(self):
        return self._location_from

    @property
    def location_to(self):
        return self._location_to

    @property
    def amount(self):
        return self._amount

    @property
    def product(self):
        return self._product
