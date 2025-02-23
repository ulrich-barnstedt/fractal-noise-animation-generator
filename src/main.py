import math
import time
import matplotlib.pyplot as plt
import numpy as np
from perlin_noise import PerlinNoise
from src.Pipeline import Pipeline
from src.sources import NoiseSource
from src.steps import Brighten, CollectVideo, Colorize, FindEdges, Interpolate, Posterize, ToImages

noise1 = PerlinNoise(octaves=3)
noise2 = PerlinNoise(octaves=6)
noise3 = PerlinNoise(octaves=12)
noise4 = PerlinNoise(octaves=24)

xpix, ypix = 200, 200
pic = []
for i in range(xpix):
    row = []
    for j in range(ypix):
        noise_val = noise1([i/xpix, j/ypix])
        noise_val += 0.5 * noise2([i/xpix, j/ypix])
        noise_val += 0.25 * noise3([i/xpix, j/ypix])
        noise_val += 0.125 * noise4([i/xpix, j/ypix])

        row.append(noise_val)
    pic.append(row)

plt.imshow(pic, cmap='gray')
plt.show()


(Pipeline()
    .source(NoiseSource(12, True))
    .addSteps([
        Interpolate(12),
        ToImages(),
        Colorize(),
        Posterize(3),
        Brighten(2),
        FindEdges(),
        Brighten(3),
        CollectVideo("../out/output.mp4")
    ])
    .execute()
 )

