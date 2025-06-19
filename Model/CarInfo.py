
from Model.ColorType import ColorType;
from Model.ColorInfo import ColorInfo;

class CarInfo :
    # 测量日期
    dataStr: str
    # 涂料批次
    paintBatch : str
    # 车辆颜色数据
    colorData: list[ColorInfo]
    def __init__(self, VIN: str, colorName: ColorType):
        self.VIN = VIN
        self.colorName = str(colorName)
        


