from typing import Any
from src.DataStep import DataStep


class CollectVideo(DataStep):
    destination: str

    def __init__(self, destination: str):
        self.destination = destination

    def execute(self, data: Any) -> Any:
        pass