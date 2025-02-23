from typing import Any
from src.DataStep import DataStep


class Posterize(DataStep):
    bits: int

    def __init__(self, bits: int):
        self.bits = bits

    def execute(self, data: Any) -> Any:
        pass
