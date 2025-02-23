from typing import Any
import numpy as np
from PIL import Image
from . import DataStep


class ToImages(DataStep):
    def execute(self, data: Any) -> Any:
        return [Image.fromarray(np.uint8(x), "L") for x in data]
