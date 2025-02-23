from .sources import DataSource
from .steps import DataStep
from .utils import logTime, logSubTime


class Pipeline:
    steps: list[DataStep]
    dataSource: DataSource
    verbose: bool

    def __init__(self, verbose: bool = False):
        self.steps = []
        self.verbose = verbose

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
        logTime("Starting pipeline")
        counter = 0

        while self.dataSource.dataLeft():
            counter += 1
            logTime(f"Starting iteration {counter}")
            data = self.dataSource.next()

            for step in self.steps:
                if self.verbose:
                    logSubTime(f"Step {step.__class__.__name__}")
                data = step.execute(data)

        self.dataSource.reset()
        logTime("All iterations complete")
