from typing import Any
from PIL import ImageFilter
from . import DataStep


class FindEdges(DataStep):
    def execute(self, data: Any) -> Any:
        return [i.filter(ImageFilter.FIND_EDGES) for i in data]
