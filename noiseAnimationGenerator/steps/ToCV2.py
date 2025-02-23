import cv2
import numpy as np
from noiseAnimationGenerator.steps import DataStep
from typing import Any


class ToCV2(DataStep):
    def execute(self, data: Any) -> Any:
        return [cv2.cvtColor(np.array(i), cv2.COLOR_RGB2BGR) for i in data]
