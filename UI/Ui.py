from tkinter import *
from tkinter import messagebox
from Entities.Speaker import Speaker
from UI.UiSettings import UiSettings
from Assets.strings.strings import *
import webbrowser, pyglet


class Ui:
    def __init__(self, gui_master, controller):
        self.__window = gui_master

        self.__window.resizable(0, 0)
        self.__nameTxt = Entry(self.__window, width=25, bg="#fff", foreground='black')
        self.__familyNameTxt = Entry(self.__window, width=25, bg="#fff", foreground='black')
        self.__titleTxt = Entry(self.__window, width=25, bg="#fff", foreground='black')

        self.__controller = controller

    def draw_window(self):
        '''
        Initializing the window
        '''
        # initializing fonts
        pyglet.font.add_file('Assets/fonts/Montserrat-Black.ttf')
        pyglet.font.add_file('Assets/fonts/Montserrat-Bold.ttf')
        pyglet.font.add_file('Assets/fonts/Montserrat-Medium.ttf')

        w = 852  # width for the window
        h = 480  # height for the window

        # get screen width and height
        ws = self.__window.winfo_screenwidth()  # width of the screen
        hs = self.__window.winfo_screenheight()  # height of the screen

        # calculate x and y coordinates for the Tk root window
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        self.__window.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.__window.title(windowTitleText)
        self.__window.config(bg="#fff")

        '''
        Creating the elements
        '''
        # Title
        title = Label(self.__window, text=windowTitleText, font=('Montserrat-Black', 20), bg="#fff", foreground="#000")
        title.place(relx=0.5, rely=0.1, anchor=CENTER)
        
        # Labels
        name = Label(self.__window, text=nameText, font=('Montserrat-Medium', 9), bg="#fff", foreground="#000")
        name.place(relx=0.33, rely=0.24, anchor=W)
        familyName = Label(self.__window, text=familyNameText, font=('Montserrat-Medium', 9), bg="#fff", foreground="#000")
        familyName.place(relx=0.33, rely=0.32, anchor=W)
        title = Label(self.__window, text=titleText, font=('Montserrat-Medium', 9), bg="#fff", foreground="#000")
        title.place(relx=0.33, rely=0.4, anchor=W)

        # Entries
        self.__nameTxt.place(relx=0.57, rely=0.22, anchor=N)
        self.__familyNameTxt.place(relx=0.57, rely=0.30, anchor=N)
        self.__titleTxt.place(relx=0.57, rely=0.38, anchor=N)

        # Buttons
        generateButton = Button(self.__window, text=generateButtonText, font=('Montserrat-Bold', 10), width=21, relief=RIDGE, bg='whitesmoke', activebackground='#00A300', command=self.__addSpeakerName)
        generateButton.place(relx=0.5, rely=0.54, anchor=CENTER)

        clearInputButton = Button(self.__window, text=clearInputButtonText, font=('Montserrat-Bold', 10), width=21, relief=RIDGE, bg='whitesmoke', activebackground='white', command=self.__clearInput)
        clearInputButton.place(relx=0.5, rely=0.61, anchor=CENTER)

        clearOutputFolderButton = Button(self.__window, text=clearOutputFolderButtonText, font=('Montserrat-Bold', 10), width=21, relief=RIDGE, bg='whitesmoke', activebackground='#ff3232', command=self.__clearOutputFolder)
        clearOutputFolderButton.place(relx=0.5, rely=0.68, anchor=CENTER)
        
        # Footer
        copyrightText = Label(self.__window, text=copyrightString, font=('Montserrat-Medium', 8), bg="#fff", foreground="#000")
        copyrightText.place(relx=0.0, rely=1.0, anchor=SW)

        # Menu bar
        menubar = Menu(self.__window)

        # Help Section
        help_btn = Menu(self.__window, tearoff=0, bg="white", activebackground='whitesmoke', activeforeground='black')
        help_btn.add_command(label=settingsText, command=self.__openSettingsTab)
        help_btn.add_command(label=contactUsText, command=self.__openWeb)
        help_btn.add_separator()
        help_btn.add_command(label=versionNumberText)
        menubar.add_cascade(label=helpText, menu=help_btn)
        self.__window.config(menu=menubar)

        self.__getNumberOfFiles()

    '''
    Buttons Methods
    '''
    '''
    Sends speaker to Controller
    @param new speaker to be added
    @return The updated number of stored images
    '''
    def __addSpeakerName(self):
        speaker = Speaker(self.__nameTxt.get(), self.__familyNameTxt.get(), self.__titleTxt.get())
        if self.__controller.add(speaker):
            self.__addConfirmation(speaker)
            return self.__getNumberOfFiles()
        else:
            messagebox.showwarning('Invalid input', 'Check if name or family name is correct!')
            return self.__getNumberOfFiles()

    '''
    Clears the texts inputs
    '''
    def __clearInput(self):
        self.__nameTxt.delete(0, 'end')
        self.__familyNameTxt.delete(0, 'end')
        self.__titleTxt.delete(0, 'end')

    '''
    Clears the output folder
    @return The updated number of stored images
    '''
    def __clearOutputFolder(self):
        self.__controller.clearOutputFolder()
        return self.__getNumberOfFiles()

    '''
    Gets number of files in output folder
    '''
    def __getNumberOfFiles(self):
        countFiles = numberOfFilesText + str(self.__controller.getNumberOfFiles())
        numberOfFiles = Label(self.__window, text=countFiles, font=('Montserrat-Medium', 9), bg="#fff", foreground="#000")
        numberOfFiles.place(relx=0.5, rely=0.74, anchor=CENTER)

    '''
    Shows confimration message after generating new image
    '''
    def __addConfirmation(self, speaker):
        addConfirmation = Label(self.__window, text=confirmationText + speaker.name + ' ' + speaker.familyName, font=('Montserrat-Medium', 9), bg='#00A300', foreground='#000')
        addConfirmation.place(relx=0.5, rely=0.80, anchor=CENTER)
        addConfirmation.after(5000, addConfirmation.destroy)

    '''
    Opens Github page of the project
    '''
    def __openWeb(self):
        webbrowser.open("https://github.com/Viktorens/Lower-Thirds-Generator")

    '''
    Opens the Settings Tab
    '''
    def __openSettingsTab(self):
        self.__windowSettings = Tk()
        self.app = UiSettings(self.__windowSettings, self.__controller)
        self.app.draw_window()
        self.__window.mainloop()
