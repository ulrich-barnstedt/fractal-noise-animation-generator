from .sources import DataSource
from .steps import DataStep


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
