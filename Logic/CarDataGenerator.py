
from Model.ColorType import ColorType
from Model.CarInfo import CarInfo
from Model.ColorInfo import ColorAngle, BasicColorInfo, ColorInfo

def generateCarData():
    vin = "88899990"
    colorType = ColorType.pureWhite
    b = BasicColorInfo(a=0.3, b=0.6, l=1.5)
    a = ColorInfo(angle= ColorAngle._45, color= b)

    carSingleAngleData = CarInfo(VIN= vin, colorName= colorType)
    carSingleAngleData.carData = [a]



if __name__ == '__main__':
    generateCarData()