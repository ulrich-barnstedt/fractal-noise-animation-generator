from typing import Any
from PIL import ImageOps
from . import DataStep


class Colorize(DataStep):
    blackTo: str
    whiteTo: str

    def __init__(self, whiteTo: str, blackTo: str):
        self.blackTo = blackTo
        self.whiteTo = whiteTo

    def execute(self, data: Any) -> Any:
        return [ImageOps.colorize(i, black=self.blackTo, white=self.whiteTo) for i in data]
