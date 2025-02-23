from src.DataSource import DataSource


class NoiseSource(DataSource):
    loop: bool
    frameCount: int

    def __init__(self, frameCount: int, loop: bool):
        self.loop = loop
        self.frameCount = frameCount

    def dataLeft(self) -> bool:
        pass

    def reset(self):
        pass

    def next(self):
        pass
