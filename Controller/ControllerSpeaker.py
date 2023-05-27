class ControllerSpeaker:
    def __init__(self, repoSpeaker):
        self.__repoSpeaker = repoSpeaker

    def add(self, speaker):
        self.__repoSpeaker.addSpeaker(speaker)

    def clearOutputFolder(self):
        self.__repoSpeaker.clearOutputFolder()
