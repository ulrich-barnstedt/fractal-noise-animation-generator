import numpy as np
from typing import Any
from . import DataStep


class NormalizeValues(DataStep):
    def execute(self, data: Any) -> Any:
        # convert to range 0 - ...
        minValue = np.min(data)
        zeroed = data + abs(minValue)

        # convert to range 0 - 255
        maxValue = np.max(zeroed)
        adjusted= zeroed* (255 / maxValue)

        return adjusted
