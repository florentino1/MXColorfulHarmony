from enum import Enum
class ColorAngle(Enum):
    _45 = 0
    _90 = 1
    _110 = 2
    _270 = 3

class BasicColorInfo:
    def __init__(self, a: int, b: int, l: int):
        self.aValue = a
        self.bValue = b
        self.lValue = l


class ColorInfo:
    def __init__(self, angle: ColorAngle, color: BasicColorInfo):
        self.angle = angle
        self.colorData = color
        