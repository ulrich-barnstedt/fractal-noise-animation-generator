import abc
from abc import ABC
from typing import Any


class DataStep(ABC):
    @abc.abstractmethod
    def execute(self, data: Any) -> Any:
        pass

    def initialize(self):
        pass

    def cleanup(self):
        pass
