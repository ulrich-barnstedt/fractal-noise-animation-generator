from typing import Any
from PIL import ImageFilter
from noiseAnimationGenerator.steps import DataStep


class Dilate(DataStep):
    width: int

    def __init__(self, width: int):
        self.width = width

    def execute(self, data: Any) -> Any:
        return [i.filter(ImageFilter.MaxFilter(self.width)) for i in data]
