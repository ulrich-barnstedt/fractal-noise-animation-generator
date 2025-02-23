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
        iterationCounter = 0

        for step in self.steps:
            step.initialize()
        logTime("Initialization complete")

        while self.dataSource.dataLeft():
            iterationCounter += 1
            logTime(f"Starting iteration {iterationCounter}")
            data = self.dataSource.next()

            for step in self.steps:
                if self.verbose:
                    logSubTime(f"Step {step.__class__.__name__}")

                data = step.execute(data)
                if data is None:
                    if self.verbose:
                        logSubTime("Break execution, no data")

                    break
                if self.verbose:
                    logSubTime(f"Iteration results: {len(data)}")

        logTime("All iterations complete, running cleanup")
        for step in self.steps:
            step.cleanup()
        self.dataSource.reset()
        logTime("Cleanup complete")
