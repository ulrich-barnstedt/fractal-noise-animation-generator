from .Pipeline import Pipeline
from .sources import NoiseSource
from .steps import Brighten, CollectVideo, Colorize, FindEdges, Interpolate, Posterize, ToImages

print("running main")

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

