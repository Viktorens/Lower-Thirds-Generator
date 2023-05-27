class Speaker:
    def __init__(self, name, familyName, title):
        self.__name = name
        self.__familyName = familyName
        self.__title = title

    # Name
    @property
    def name(self):
        return self.__name

    @name.setter
    def vorname(self, n):
        self.__name = n

    # Family Name
    @property
    def familyName(self):
        return self.__familyName

    @familyName.setter
    def familyName(self, f):
        self.__familyName = f

    # Title
    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, t):
        self.title = t
