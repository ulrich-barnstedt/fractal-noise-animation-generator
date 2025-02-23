import math
import time
import numpy as np
from typing import Any
from perlin_numpy import generate_fractal_noise_2d
from . import DataSource


class NoiseSource(DataSource):
    loop: bool
    frameCount: int
    size: tuple[int, int]
    generationSize: tuple[int, int]
    octaves: int

    counter: int
    initialFrame: Any

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
        self.counter = 0

    def dataLeft(self) -> bool:
        return self.counter < self.frameCount + (1 if self.loop else 0)

    def reset(self):
        self.counter = 0

    def next(self):
        self.counter += 1
        if self.counter > self.frameCount:
            return self.initialFrame

        np.random.seed(math.floor(time.time()))
        noise = generate_fractal_noise_2d(
            self.size,
            self.generationSize,
            self.octaves
        )
        generatedNoise = np.array([noise])

        if self.counter == 1:
            self.initialFrame = generatedNoise

        return generatedNoise
