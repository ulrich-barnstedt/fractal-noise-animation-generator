from typing import Any
from PIL import ImageOps
from . import DataStep


class Posterize(DataStep):
    bits: int

    def __init__(self, bits: int):
        self.bits = bits

    def execute(self, data: Any) -> Any:
        return [ImageOps.posterize(i, self.bits) for i in data]
