class LowerThird:
    def __init__(self, nameFontSize, namePositionX, namePositionY, titleFontSize, titlePositionX, titlePositionY):
        self.__nameFontSize= nameFontSize
        self.__namePositionX = namePositionX
        self.__namePositionY = namePositionY
        self.__titleFontSize = titleFontSize
        self.__titlePositionX = titlePositionX
        self.__titlePositionY = titlePositionY

    # Name Fontsize
    @property
    def nameFontSize(self):
        return self.__nameFontSize

    # Name PositionX
    @property
    def namePositionX(self):
        return self.__namePositionX
    
    # Name PositionY
    @property
    def namePositionY(self):
        return self.__namePositionY

    # Title Fontsize
    @property
    def titleFontSize(self):
        return self.__titleFontSize
    
    # Title PositionX
    @property
    def titlePositionX(self):
        return self.__titlePositionX

    # Title PositionY
    @property
    def titlePositionY(self):
        return self.__titlePositionY
