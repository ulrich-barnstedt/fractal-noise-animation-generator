from typing import Any
from . import DataStep


class Interpolate(DataStep):
    newFrames: int

    def __init__(self, newFrames: int):
        self.newFrames = newFrames

    def execute(self, data: Any) -> Any:
        pass

