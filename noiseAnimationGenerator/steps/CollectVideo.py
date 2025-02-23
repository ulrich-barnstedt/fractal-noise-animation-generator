import cv2
from . import DataStep
from typing import Any


class CollectVideo(DataStep):
    destination: str
    format: str
    writer: cv2.VideoWriter = None

    def __init__(self, destination: str, format: str = "mp4v"):
        self.destination = destination
        self.format = format

    def createWriter(self, image):
        height, width = image.shape[:2]
        self.writer = cv2.VideoWriter(
            self.destination,
            cv2.VideoWriter_fourcc(*self.format),
            60,
            (width, height)
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

