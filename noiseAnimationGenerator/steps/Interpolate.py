import numpy as np
from typing import Any
from . import DataStep


class Interpolate(DataStep):
    newFrames: int
    lastFrame: Any = None

    def __init__(self, newFrames: int):
        self.newFrames = newFrames

    def execute(self, data: Any) -> Any:
        data = data[0]

        if self.lastFrame is None:
            self.lastFrame = data
            return None

        interpolated = np.linspace(self.lastFrame, data, self.newFrames, False)
        self.lastFrame = data

        return interpolated

    def cleanup(self):
        self.lastFrame = None
