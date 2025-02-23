import abc
from abc import ABC


class DataSource(ABC):
    @abc.abstractmethod
    def dataLeft(self) -> bool:
        pass

    @abc.abstractmethod
    def reset(self):
        pass

    @abc.abstractmethod
    def next(self):
        pass
