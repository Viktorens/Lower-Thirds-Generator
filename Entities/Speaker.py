class Speaker:
    def __init__(self, name, familyName, title):
        self.__name = name
        self.__familyName = familyName
        self.__title = title

    # Name
    @property
    def name(self):
        return self.__name

    # Family Name
    @property
    def familyName(self):
        return self.__familyName

    # Title
    @property
    def title(self):
        return self.__title
