from .Pipeline import Pipeline
from .sources import NoiseSource, NoiseSource3D
from .steps import Brighten, CollectVideo, Colorize, FindEdges, Interpolate, Posterize, ToPIL, NormalizeValues, \
    DebugImage, Dilate, ToCV2

(Pipeline(verbose=True)
    .source(NoiseSource3D(
        12,
        (2560, 1392),
        (16, 8),
        True,
        2
    ))
    .addSteps([
        NormalizeValues(),
        Interpolate(18),
        ToPIL(),
        Colorize("black", "blue"),
        Posterize(3),
        Brighten(2),
        FindEdges(),
        Brighten(4),
        ToCV2(),
        Dilate(5, 1),
        CollectVideo("./out/output-pipeline.mp4")
    ])
    .execute()
 )

