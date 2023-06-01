class ControllerSpeaker:
    def __init__(self, repoSpeaker):
        self.__repoSpeaker = repoSpeaker

    def add(self, speaker):
        return self.__repoSpeaker.addSpeaker(speaker)

    def clearOutputFolder(self):
        return self.__repoSpeaker.clearOutputFolder()

    def getNumberOfFiles(self):
        return self.__repoSpeaker.getNumberOfFiles()