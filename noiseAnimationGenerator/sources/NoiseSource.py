from . import DataSource

# import math
# import time
# import matplotlib.pyplot as plt
# import numpy as np
# from perlin_noise import PerlinNoise

# noise1 = PerlinNoise(octaves=3)
# noise2 = PerlinNoise(octaves=6)
# noise3 = PerlinNoise(octaves=12)
# noise4 = PerlinNoise(octaves=24)
#
# xpix, ypix = 200, 200
# pic = []
# for i in range(xpix):
#     row = []
#     for j in range(ypix):
#         noise_val = noise1([i/xpix, j/ypix])
#         noise_val += 0.5 * noise2([i/xpix, j/ypix])
#         noise_val += 0.25 * noise3([i/xpix, j/ypix])
#         noise_val += 0.125 * noise4([i/xpix, j/ypix])
#
#         row.append(noise_val)
#     pic.append(row)
#
# plt.imshow(pic, cmap='gray')
# plt.show()

class NoiseSource(DataSource):
    loop: bool
    frameCount: int

    counter: int

    def __init__(self, frameCount: int, loop: bool):
        self.loop = loop
        self.frameCount = frameCount
        self.counter = 0

    def dataLeft(self) -> bool:
        return self.counter >= self.frameCount

    def reset(self):
        self.counter = 0

    def next(self):
        self.counter += 1

        return [self.frameCount, 1, 2, 3]
