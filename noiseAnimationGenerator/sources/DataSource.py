import abc
from noiseAnimationGenerator.StatefulBase import StatefulBase


class DataSource(StatefulBase):
    @abc.abstractmethod
    def dataLeft(self) -> bool:
        pass

    @abc.abstractmethod
    def next(self):
        pass
