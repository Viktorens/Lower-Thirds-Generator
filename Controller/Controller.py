from UI.Error import *
from UI.ui import *
from Entities.LowerThird import LowerThird
from Tests.TestName import *
import json

class Controller:
    def __init__(self, repoSpeaker):
        self.__repoSpeaker = repoSpeaker

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
            Error().emptyInput()
            return False
        else:
            self.__repoSpeaker.addSpeaker(speaker)
            return True
    
    '''
    Clears the output folder
    '''
    def clearOutputFolder(self):
        return self.__repoSpeaker.clearOutputFolder()

    '''
    Gets number of files in output folder
    @return number of files
    '''
    def getNumberOfFiles(self):
        return self.__repoSpeaker.getNumberOfFiles()
    
    def getJsonData ():
        with open('config.json') as config_file:
            data = json.load(config_file)
            return LowerThird(data['lowerThirdConfig']['nameFontSize'], data['lowerThirdConfig']['titleFontSize'], data['lowerThirdConfig']['namePositionX'], data['lowerThirdConfig']['namePositonY'], data['lowerThirdConfig']['titlePositionX'], data['lowerThirdConfig']['titlePositonY'])
    