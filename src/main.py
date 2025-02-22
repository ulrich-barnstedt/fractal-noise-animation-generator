import math
import time
import numpy as np
from perlin_numpy import generate_fractal_noise_3d
from PIL import Image, ImageOps, ImageFilter

def generateNoiseFrames(frameCount, resolution, generationResolution):
    np.random.seed(math.floor(time.time()))
    noise = generate_fractal_noise_3d(
        (frameCount, resolution, resolution), (1, generationResolution, generationResolution), 4, tileable=(True, False, False)
    )

    adjustedNoise = (noise + 100) * 127.5  # somewhat 0 - 255

    return adjustedNoise

def smoothFrames(frames, steps):
    outputNoise = []
    frameCount = len(frames)

    for idx in range(0, frameCount - 1):
        spaced = np.linspace(frames[idx], frames[idx + 1], steps, False)
        for newFrame in spaced:
            outputNoise.append(newFrame)

    returnSpacing = np.linspace(frames[frameCount - 1], frames[0], steps, False)
    for newFrame in returnSpacing:
        outputNoise.append(newFrame)

    return np.uint8(np.array(outputNoise))

def filters(frames):
    image = [Image.fromarray(x, "L") for x in frames]
    posterizedImage = [ImageOps.posterize(i, 4) for i in image]

    edgeImage = [i.filter(ImageFilter.FIND_EDGES) for i in posterizedImage]
    coloredEdgeImage = [ImageOps.colorize(i, black="black", white="blue") for i in edgeImage]

    return coloredEdgeImage

noise = generateNoiseFrames(16, 1024, 4)
smoothed = smoothFrames(noise, 8)
images = filters(smoothed)
images[0].save("gif.gif", format="GIF", append_images=images[1:], save_all=True, duration=50, loop=0)
