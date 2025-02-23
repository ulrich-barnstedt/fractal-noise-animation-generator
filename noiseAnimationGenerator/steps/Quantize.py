from typing import Any
from PIL import Image
from .import DataStep


class Quantize(DataStep):
    def execute(self, data: Any) -> Any:
        quantized = [i.quantize(2, method=Image.Quantize.MAXCOVERAGE) for i in data]
        return [i.convert("RGB") for i in quantized]
