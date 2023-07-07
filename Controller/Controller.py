from UI.Ui import *
from Entities.LowerThird import LowerThird
from Tests.TestName import *

class Controller:
    def __init__(self, repo):
        self.__repo = repo

    '''
    Adds speaker name to image
    @param new speaker to be added
    @return False if input is incorrect, else True
    '''
    def add(self, speaker):
        # try:
        #     assert TestName().speakerName(speaker.name) is True
        #     assert TestName().speakerName(speaker.familyName) is True
        # except AssertionError:
        #     return Error().invalidSpeakerName()
        # else:
        #     return self.__repoSpeaker.addSpeaker(speaker)
        try:
            assert TestName().inputNotEmpty(speaker.name) is True
            assert TestName().inputNotEmpty(speaker.familyName) is True
        except AssertionError:
            return False
        else:
            self.__repo.addSpeaker(speaker)
            return True
    
    '''
    Clears the output folder
    '''
    def clearOutputFolder(self):
        return self.__repo.clearOutputFolder()

    '''
    Gets number of files in output folder
    @return number of files
    '''
    def getNumberOfFiles(self):
        return self.__repo.getNumberOfFiles()
    
    '''
    Saves new lower third values to json file
    @param all new settings
    @return True if successful, else False
    '''
    def saveNewValues(self, nameFontSizeText, namePositionXText, namePositionYText, titleFontSizeText, titlePositionXText, titlePositionYText):
        try:
            nameFontSizeText = int(nameFontSizeText)
            namePositionXText = int(namePositionXText)
            namePositionYText = int(namePositionYText)
            titleFontSizeText = int(titleFontSizeText)
            titlePositionXText = int(titlePositionXText)
            titlePositionYText = int(titlePositionYText)
            lowerThird = LowerThird(nameFontSizeText, namePositionXText, namePositionYText, titleFontSizeText, titlePositionXText, titlePositionYText)
            self.__repo.saveNewValues(lowerThird)
            return True
        except ValueError:
            return False
        
    '''
    Gets settings stored in json file
    @return Settings stored in json
    '''
    def getJsonSettings(self):
        return self.__repo.getJsonData()
