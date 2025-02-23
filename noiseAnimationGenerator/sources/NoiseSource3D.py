import math
import time
import numpy as np
from typing import Any
from perlin_numpy import generate_fractal_noise_3d
from . import DataSource


class NoiseSource3D(DataSource):
    loop: bool
    frameCount: int
    size: tuple[int, int]
    generationSize: tuple[int, int]
    octaves: int

    counter: int
    noise3D: Any

    def __init__(
            self,
            frameCount: int,
            size: tuple[int, int],
            generationSize: tuple[int, int],
            loop: bool,
            octaves: int
    ):
        self.loop = loop
        self.frameCount = frameCount
        self.size = size
        self.octaves = octaves
        self.generationSize = generationSize

    def dataLeft(self) -> bool:
        return self.counter < self.frameCount + (1 if self.loop else 0)

    def initialize(self):
        self.counter = 0
        np.random.seed(math.floor(time.time()))

        self.noise3D = generate_fractal_noise_3d(
            (self.frameCount, *self.size),
            (1, *self.generationSize),
            self.octaves,
            tileable=(True, False, False)
        )

    def cleanup(self):
        self.noise3D = None

    def next(self):
        if self.counter >= self.frameCount:
            self.counter += 1
            return np.array([self.noise3D[0]])

        generatedNoise = np.array([self.noise3D[self.counter]])
        self.counter += 1

        return generatedNoise
