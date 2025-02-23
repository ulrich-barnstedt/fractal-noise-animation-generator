from typing import Any
import cv2
import numpy as np
from noiseAnimationGenerator.steps import DataStep


class Dilate(DataStep):
    kernel: np.ndarray
    iterations: int

    def __init__(self, width: int, iterations: int):
        self.kernel = np.ones((width, width), np.uint8)
        self.iterations = iterations

    def execute(self, data: Any) -> Any:
        return [cv2.dilate(i, self.kernel, iterations=self.iterations) for i in data]
