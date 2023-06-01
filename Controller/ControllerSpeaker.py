class ControllerSpeaker:
    def __init__(self, repoSpeaker):
        self.__repoSpeaker = repoSpeaker

    '''
    Adds speaker name to image
    @param new speaker to be added
    '''
    def add(self, speaker):
        return self.__repoSpeaker.addSpeaker(speaker)
    
    '''
    Clears the output folder
    '''
    def clearOutputFolder(self):
        return self.__repoSpeaker.clearOutputFolder()

    '''
    Gets number of files in output folder
    return number of files
    '''
    def getNumberOfFiles(self):
        return self.__repoSpeaker.getNumberOfFiles()
    