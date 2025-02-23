import numpy as np
from typing import Any
from PIL import Image
from . import DataStep


class DebugImage(DataStep):
    def execute(self, data: Any) -> Any:
        image = data[0]

        if isinstance(image, Image.Image):
            image.show()
        else:
            Image.fromarray(np.uint8(image)).show()

        return data
