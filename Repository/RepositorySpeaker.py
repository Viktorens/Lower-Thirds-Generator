from UI.uiErrors import *
from Repository.testingStrings import speakerName
from PIL import Image, ImageDraw, ImageFont
import os, shutil
from datetime import datetime


class RepositorySpeaker:
    def addSpeaker(self, speaker):
        try:
            name = speaker.name
            assert speakerName(name) is True
        except AssertionError:
            return invalidSpeakerName(name)

        try:
            familyName = speaker.familyName
            assert speakerName(familyName) is True
        except AssertionError:
            return invalidSpeakerFamilyName(familyName)
        
        else:
            text = name + ' ' + familyName
            image = Image.open('Assets/default.png')
            draw = ImageDraw.Draw(image)
            fontName = ImageFont.truetype('fonts/arial.ttf', 70)
            fontTitle = ImageFont.truetype('fonts/arial.ttf', 40)
            if speaker.title == '':
                draw.text((500, 908), text, font=fontName, fill=(0, 0, 0))
            else:
                draw.text((500, 885), text, font=fontName, fill=(0, 0, 0))
            draw.text((500, 965), speaker.title, font=fontTitle, fill=(0, 0, 0))
            image.save('Output/' + datetime.now().strftime("%Y%m%d_%H%M%S") + text + '.png')
        
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
                return failedDelete(file_path, e)
