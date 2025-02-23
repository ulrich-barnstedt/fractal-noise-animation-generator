from typing import Any
from PIL import ImageOps
from . import DataStep


class Colorize(DataStep):
    blackTo: Any
    whiteTo: Any

    def __init__(self, whiteTo: Any, blackTo: Any):
        self.blackTo = blackTo
        self.whiteTo = whiteTo

    def execute(self, data: Any) -> Any:
        return [ImageOps.colorize(i, black=self.blackTo, white=self.whiteTo) for i in data]
