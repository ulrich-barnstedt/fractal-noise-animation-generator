from typing import Any
from src.DataStep import DataStep


class Brighten(DataStep):
    factor: float

    def __init__(self, factor: float):
        self.factor = factor

    def execute(self, data: Any) -> Any:
        pass

