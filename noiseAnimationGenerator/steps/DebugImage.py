from typing import Any
import numpy as np
from . import DataStep


class DebugImage(DataStep):
    def execute(self, data: Any) -> Any:
        if isinstance(data, list) or isinstance(data, np.ndarray):
            data[0].show()
        else:
            data.show()

        return data
