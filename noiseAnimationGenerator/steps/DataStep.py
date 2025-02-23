import abc
from typing import Any
from noiseAnimationGenerator.StatefulBase import StatefulBase


class DataStep(StatefulBase):
    @abc.abstractmethod
    def execute(self, data: Any) -> Any:
        pass
