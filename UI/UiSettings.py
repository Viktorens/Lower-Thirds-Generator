from tkinter import *
from Controller.Controller import Controller
from Assets.strings.strings import *
import pyglet


class UiSettings:
    def __init__(self, gui_master):
        self.__window = gui_master

        self.__window.resizable(0, 0)
        self.__nameFontSizeText = Entry(self.__window, width=7, bg="#fff", foreground='black')
        self.__namePositionXText = Entry(self.__window, width=7, bg="#fff", foreground='black')
        self.__namePositionYText = Entry(self.__window, width=7, bg="#fff", foreground='black')

        self.__titleFontSizeText = Entry(self.__window, width=7, bg="#fff", foreground='black')
        self.__titlePositionXText = Entry(self.__window, width=7, bg="#fff", foreground='black')
        self.__titlePositionYText = Entry(self.__window, width=7, bg="#fff", foreground='black')


    def draw_window(self):
        '''
        Initializing the window
        '''
        # initializing fonts
        pyglet.font.add_file('Assets/fonts/Montserrat-Black.ttf')
        pyglet.font.add_file('Assets/fonts/Montserrat-Bold.ttf')
        pyglet.font.add_file('Assets/fonts/Montserrat-Medium.ttf')

        w = 300  # width for the window
        h = 300  # height for the window

        # get screen width and height
        ws = self.__window.winfo_screenwidth()  # width of the screen
        hs = self.__window.winfo_screenheight()  # height of the screen

        # calculate x and y coordinates for the Tk root window
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        self.__window.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.__window.title(settingsTitleText)
        self.__window.config(bg="#fff")

        '''
        Creating the elements
        '''
        lowerThird = Controller.getJsonData()

        # Title
        title = Label(self.__window, text=settingsTitleText, font=('Montserrat-Black', 20), bg="#fff", foreground="#000")
        title.place(relx=0.5, rely=0.1, anchor=CENTER)
        
        # Labels
        nameFontSizeLabel = Label(self.__window, text=nameFontSizeText, font=('Montserrat-Medium', 9), bg="#fff", foreground="#000")
        nameFontSizeLabel.place(relx=0.125, rely=0.24, anchor=W)
        namePositionXLabel = Label(self.__window, text=namePositionXText, font=('Montserrat-Medium', 9), bg="#fff", foreground="#000")
        namePositionXLabel.place(relx=0.125, rely=0.32, anchor=W)
        namePositionYLabel = Label(self.__window, text=namePositionYText, font=('Montserrat-Medium', 9), bg="#fff", foreground="#000")
        namePositionYLabel.place(relx=0.125, rely=0.4, anchor=W)

        titleFontSizeLabel = Label(self.__window, text=titleFontSizeText, font=('Montserrat-Medium', 9), bg="#fff", foreground="#000")
        titleFontSizeLabel.place(relx=0.125, rely=0.48, anchor=W)
        titlePositionXLabel = Label(self.__window, text=titlePositionXText, font=('Montserrat-Medium', 9), bg="#fff", foreground="#000")
        titlePositionXLabel.place(relx=0.125, rely=0.56, anchor=W)
        titlePositionYLabel = Label(self.__window, text=titlePositionYText, font=('Montserrat-Medium', 9), bg="#fff", foreground="#000")
        titlePositionYLabel.place(relx=0.125, rely=0.64, anchor=W)

        # Entries
        self.__nameFontSizeText.place(relx=0.85, rely=0.24, anchor=E)
        self.__nameFontSizeText.insert(0, lowerThird.nameFontSize)
        self.__namePositionXText.place(relx=0.85, rely=0.32, anchor=E)
        self.__namePositionXText.insert(0, lowerThird.namePositionX)
        self.__namePositionYText.place(relx=0.85, rely=0.4, anchor=E)
        self.__namePositionYText.insert(0, lowerThird.namePositonY)

        self.__titleFontSizeText.place(relx=0.85, rely=0.48, anchor=E)
        self.__titleFontSizeText.insert(0, lowerThird.titleFontSize)
        self.__titlePositionXText.place(relx=0.85, rely=0.56, anchor=E)
        self.__titlePositionXText.insert(0, lowerThird.titlePositionX)
        self.__titlePositionYText.place(relx=0.85, rely=0.64, anchor=E)
        self.__titlePositionYText.insert(0, lowerThird.titlePositonY)

        #Buttons
        defaultButton = Button(self.__window, text=defaultButtonText, font=('Montserrat-Bold', 10), width=7, relief=RIDGE, bg='whitesmoke', activebackground='white')
        defaultButton.place(relx=0.33, rely=0.85, anchor=CENTER)

        saveButton = Button(self.__window, text=saveButtonText, font=('Montserrat-Bold', 10), width=7, relief=RIDGE, bg='whitesmoke', activebackground='white')
        saveButton.place(relx=0.66, rely=0.85, anchor=CENTER)
