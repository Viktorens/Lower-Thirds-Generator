from tkinter import messagebox
from Entities.LowerThird import LowerThird
from PIL import Image, ImageDraw, ImageFont
import os, shutil, subprocess, platform, json


class Repository:
    '''
    Adds speaker name to image
    @param new speaker to be added
    @return Speaker
    '''
    def addSpeaker(self, speaker):
        lowerThirdSettings = self.getJsonData()
        lowerThird = LowerThird(lowerThirdSettings['lowerThirdConfig']['nameFontSize'], lowerThirdSettings['lowerThirdConfig']['namePositionX'], lowerThirdSettings['lowerThirdConfig']['namePositionY'], lowerThirdSettings['lowerThirdConfig']['titleFontSize'], lowerThirdSettings['lowerThirdConfig']['titlePositionX'], lowerThirdSettings['lowerThirdConfig']['titlePositionY'])
        text = speaker.name + ' ' + speaker.familyName
        image = Image.open('Assets/img/default.png')
        draw = ImageDraw.Draw(image)
        nameFontSize = ImageFont.truetype('Assets/fonts/Montserrat-Bold.ttf', lowerThird.nameFontSize)
        titleFontSize = ImageFont.truetype('Assets/fonts/Montserrat-Thin.ttf', lowerThird.titleFontSize)

        if speaker.title == '':
            draw.text((lowerThird.namePositionX, lowerThird.namePositionY), text, font=nameFontSize, fill=(1, 1, 1))
        else:
            draw.text((lowerThird.titlePositionX, lowerThird.titlePositionY), text, font=nameFontSize, fill=(1, 1, 1))

        draw.text((470, 955), speaker.title, font=titleFontSize, fill=(1, 1, 1))
        image.save('Output/' + text + '.png')
        
        if platform.system() == 'Windows':
            os.startfile('Output')
        elif platform.system() == 'Darwin':
            subprocess.Popen(['open', 'Output'])
        else:
            subprocess.Popen(['xdg-open', 'Output'])    
        return speaker
    
    '''
    Clears the output folder
    '''
    def clearOutputFolder(self):
        folder = './Output'
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                return messagebox.showerror('Delete Output Folder', 'Failed to delete %s. Reason: %s' % (file_path, e))

    '''
    Gets number of files in output folder
    @return number of files
    '''
    def getNumberOfFiles(self):
        dir_path = r'./Output'
        count = 0
        for path in os.listdir(dir_path):
            if os.path.isfile(os.path.join(dir_path, path)):
                count += 1
        return count
    
    '''
    Gets settings stored in json file
    @return Settings stored in json
    '''
    def getJsonData(self):
        with open('config.json') as config_file:
            data = json.load(config_file)
            config_file.close()
            return data
    
    '''
    Stores settings in json file
    '''
    def storeJsonData(self, data):
        with open("config.json", "w") as config_file:
            myJSON = json.dump(data, config_file)
            config_file.close()

    '''
    Saves new lower third values to json file
    @param all new settings
    '''
    def saveNewValues(self, newLowerThirdSettings):
        data = self.getJsonData()
        data['lowerThirdConfig']['nameFontSize'] = newLowerThirdSettings.nameFontSize
        data['lowerThirdConfig']['namePositionX'] = newLowerThirdSettings.namePositionX
        data['lowerThirdConfig']['namePositionY'] = newLowerThirdSettings.namePositionY
        data['lowerThirdConfig']['titleFontSize'] = newLowerThirdSettings.titleFontSize
        data['lowerThirdConfig']['titlePositionX'] = newLowerThirdSettings.titlePositionX
        data['lowerThirdConfig']['titlePositionY'] = newLowerThirdSettings.titlePositionY
        self.storeJsonData(data)