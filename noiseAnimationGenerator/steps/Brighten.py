from typing import Any
from PIL import ImageEnhance
from . import DataStep


class Brighten(DataStep):
    factor: float

    def __init__(self, factor: float):
        self.factor = factor

    def execute(self, data: Any) -> Any:
        return [ImageEnhance.Brightness(i).enhance(self.factor) for i in data]
