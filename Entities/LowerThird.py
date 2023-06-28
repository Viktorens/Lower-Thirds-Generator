class LowerThird:
    def __init__(self, nameFontSize, titleFontSize, namePositionX, namePositonY, titlePositionX, titlePositonY):
        self.__nameFontSize= nameFontSize
        self.__titleFontSize = titleFontSize
        self.__namePositionX = namePositionX
        self.__namePositonY = namePositonY
        self.__titlePositionX = titlePositionX
        self.__titlePositonY = titlePositonY

    # Name Fontsize
    @property
    def nameFontSize(self):
        return self.__nameFontSize

    # Title Fontsize
    @property
    def titleFontSize(self):
        return self.__titleFontSize

    # Name PositionX
    @property
    def namePositionX(self):
        return self.__namePositionX
    
    # Name PositonY
    @property
    def namePositonY(self):
        return self.__namePositonY

    # Title PositionX
    @property
    def titlePositionX(self):
        return self.__titlePositionX

    # Title PositionY
    @property
    def titlePositonY(self):
        return self.__titlePositonY
