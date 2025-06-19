from enum import Enum
class ColorType(Enum):
    pureWhite = 0
    pearlWhite = 1
    bogendiRed = 2
    stoneGrey = 3

    def __str__(self):
        if self.value == 0:
            return "雅典娜白"
        elif self.value == 1:
            return "珍珠白"
        elif self.value == 2:
            return "勃艮第红"
        elif self.value == 3:
            return "岩石灰"