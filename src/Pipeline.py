from src.DataSource import DataSource
from src.DataStep import DataStep


class Pipeline:
    steps: list[DataStep]
    dataSource: DataSource

    def __init__(self):
        self.steps = []

    def source(self, sourceInstance: DataSource):
        self.dataSource = sourceInstance
        return self

    def addStep(self, step: DataStep):
        self.steps.append(step)
        return self

    def addSteps(self, steps: list[DataStep]):
        self.steps.extend(steps)
        return self

    def execute(self):
        while self.dataSource.dataLeft():
            data = self.dataSource.next()

            for step in self.steps:
                data = step.execute(data)

        self.dataSource.reset()


    # @staticmethod
    # def fromNoise(frameCount: int, loop: bool):
    #     def noiseSource():
    #         # return true or false depending on if data is left
    #         return True
    #
    #     newPipeline = Pipeline(noiseSource)
    #     return newPipeline

