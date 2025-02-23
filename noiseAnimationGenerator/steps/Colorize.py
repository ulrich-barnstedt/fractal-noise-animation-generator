from typing import Any
from PIL import ImageOps
from . import DataStep


class Colorize(DataStep):
    def execute(self, data: Any) -> Any:
        return [ImageOps.colorize(i, black="blue", white="black") for i in data]
