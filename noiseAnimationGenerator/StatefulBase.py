from abc import ABC


class StatefulBase(ABC):
    def initialize(self):
        pass

    def cleanup(self):
        pass
