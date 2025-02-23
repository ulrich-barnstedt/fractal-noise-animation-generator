import cv2
import numpy as np
from . import DataStep
from typing import Any


class CollectVideo(DataStep):
    destination: str
    writer: cv2.VideoWriter = None

    def __init__(self, destination: str):
        self.destination = destination

    def createWriter(self, image):
        self.writer = cv2.VideoWriter(
            self.destination,
            cv2.VideoWriter_fourcc(*"mp4v"),
            60,
            (image.size[0], image.size[1])  # has to be expanded to work
        )

    def cleanup(self):
        self.writer.release()
        self.writer = None

    def execute(self, data: Any) -> Any:
        if self.writer is None:
            self.createWriter(data[0])

        for image in data:
            self.writer.write(image)

        return data

