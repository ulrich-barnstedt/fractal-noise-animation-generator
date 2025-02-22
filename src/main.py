import math
import time
import numpy as np
from perlin_numpy import generate_fractal_noise_3d
from PIL import Image, ImageOps, ImageFilter

def generateNoiseFrames(frameCount, resolution, generationResolution, octaves):
    np.random.seed(math.floor(time.time()))
    noise = generate_fractal_noise_3d(
        (frameCount, resolution, resolution),
        (1, generationResolution, generationResolution),
        octaves,
        tileable=(True, False, False)
    )

    # convert to range 0 - ...
    minValue = np.min(noise)
    zeroedNoise = noise + abs(minValue)

    # convert to range 0 - 255
    maxValue = np.max(zeroedNoise)
    adjustedNoise = zeroedNoise * (255 / maxValue)

    # TODO: fix why borders sometimes only appear
    # print(np.min(adjustedNoise), np.max(adjustedNoise))
    return adjustedNoise

def interpolateFrames(frames, steps):
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

def frameToImage(frames):
    return [Image.fromarray(x, "L") for x in frames]

def scaleImage(images, newSize):
    return [i.resize(newSize) for i in images]

def filterImages(images, posterizeBits):
    posterizedImages = [ImageOps.posterize(i, posterizeBits) for i in images]
    return posterizedImages
    # edgeImage = [i.filter(ImageFilter.FIND_EDGES) for i in posterizedImages]
    # return edgeImage
    # coloredEdgeImage = [ImageOps.colorize(i, black="black", white="blue") for i in edgeImage]

    # return coloredEdgeImage

startTime = time.time()
def _logTime(message):
    print(f"[{round(time.time() - startTime, 2)}s] {message}")

_logTime("Start noise generation")
noise = generateNoiseFrames(16, 1024, 8, 5)
_logTime("Noise generation done")
smoothed = interpolateFrames(noise, 8)
_logTime("Interpolation done")
rawImages = frameToImage(smoothed)
_logTime("Frame -> Image")
scaledImages = scaleImage(rawImages, (1024, 1024))
_logTime("Scaling done")
images = filterImages(scaledImages, 3)
_logTime("Filters done")
# images = scaledImages
images[0].save("gif.gif", format="GIF", append_images=images[1:], save_all=True, duration=50, loop=0)
_logTime("Result saved")
