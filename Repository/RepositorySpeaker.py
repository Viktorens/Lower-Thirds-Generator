from UI.Error import *
from PIL import Image, ImageDraw, ImageFont
import os, shutil
from datetime import datetime


class RepositorySpeaker:
    def addSpeaker(self, speaker):
        text = speaker.name + ' ' + speaker.familyName
        image = Image.open('Assets/img/default.png')
        draw = ImageDraw.Draw(image)
        fontName = ImageFont.truetype('Assets/fonts/Montserrat-Bold.ttf', 70)
        fontTitle = ImageFont.truetype('Assets/fonts/Montserrat-Thin.ttf', 40)
        if speaker.title == '':
            draw.text((470, 905), text, font=fontName, fill=(0, 0, 0))
        else:
            draw.text((470, 885), text, font=fontName, fill=(0, 0, 0))

        draw.text((470, 955), speaker.title, font=fontTitle, fill=(0, 0, 0))
        image.save('Output/' + datetime.now().strftime("%Y%m%d_%H%M%S") + text + '.png')
        os.startfile('Output')
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
