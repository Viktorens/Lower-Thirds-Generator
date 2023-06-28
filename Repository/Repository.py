from UI.Error import *
from Controller.Controller import Controller
from PIL import Image, ImageDraw, ImageFont
import os, shutil, subprocess, platform


class Repository:
    def addSpeaker(self, speaker):
        lowerThird = Controller.getJsonData()
        text = speaker.name + ' ' + speaker.familyName
        image = Image.open('Assets/img/default.png')
        draw = ImageDraw.Draw(image)
        nameFontSize = ImageFont.truetype('Assets/fonts/Montserrat-Bold.ttf', lowerThird.nameFontSize)
        titleFontSize = ImageFont.truetype('Assets/fonts/Montserrat-Thin.ttf', lowerThird.titleFontSize)

        if speaker.title == '':
            draw.text((lowerThird.namePositionX, lowerThird.namePositonY), text, font=nameFontSize, fill=(1, 1, 1))
        else:
            draw.text((lowerThird.titlePositionX, lowerThird.titlePositonY), text, font=nameFontSize, fill=(1, 1, 1))

        draw.text((470, 955), speaker.title, font=titleFontSize, fill=(1, 1, 1))
        image.save('Output/' + text + '.png')
        
        if platform.system() == 'Windows':
            os.startfile('Output')
        elif platform.system() == 'Darwin':
            subprocess.Popen(['open', 'Output'])
        else:
            subprocess.Popen(['xdg-open', 'Output'])    
        return speaker
    
    def clearOutputFolder (self):
        folder = './Output'
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                return Error().failedDelete(file_path, e)

    def getNumberOfFiles (self):
        dir_path = r'./Output'
        count = 0
        for path in os.listdir(dir_path):
            if os.path.isfile(os.path.join(dir_path, path)):
                count += 1
        return count
    
    # def __getJsonData (self):
    #     with open('config.json') as config_file:
    #         data = json.load(config_file)
    #         return LowerThird(data['lowerThirdConfig']['nameFontSize'], data['lowerThirdConfig']['titleFontSize'], data['lowerThirdConfig']['namePositionX'], data['lowerThirdConfig']['namePositonY'], data['lowerThirdConfig']['titlePositionX'], data['lowerThirdConfig']['titlePositonY'])
