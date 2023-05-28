from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from Entities.Speaker import Speaker
from Assets.strings.strings import *
import webbrowser


class UI:
    def __init__(self, gui_master, controller):
        self.__window = gui_master

        self.__window.resizable(0, 0)
        self.__window.protocol("WM_DELETE_WINDOW", exit_app)
        self.__nameTxt = Entry(self.__window, width=25, bg="#fff", foreground='black')
        self.__familyNameTxt = Entry(self.__window, width=25, bg="#fff", foreground='black')
        self.__titleTxt = Entry(self.__window, width=25, bg="#fff", foreground='black')

        self.__controller = controller

    def draw_window(self):
        w = 525  # width for the window
        h = 300  # height for the window

        # get screen width and height
        ws = self.__window.winfo_screenwidth()  # width of the screen
        hs = self.__window.winfo_screenheight()  # height of the screen

        # calculate x and y coordinates for the Tk root window
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        self.__window.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.__window.title(windowTitleText)
        self.__window.config(bg="#fff")

        # UI
        title = Label(self.__window, text=windowTitleText, font='Arial 12', bg="#fff", foreground="#000")
        title.place(relx=0.5, rely=0.1, anchor=CENTER)
        
        name = Label(self.__window, text=nameText, bg="#fff", foreground="#000")
        name.place(relx=0.25, rely=0.25, anchor=W)
        self.__nameTxt.place(relx=0.58, rely=0.22, anchor=N)

        familyName = Label(self.__window, text=familyNameText, bg="#fff", foreground="#000")
        familyName.place(relx=0.25, rely=0.35, anchor=W)
        self.__familyNameTxt.place(relx=0.58, rely=0.32, anchor=N)

        title = Label(self.__window, text=titleText, bg="#fff", foreground="#000")
        title.place(relx=0.25, rely=0.45, anchor=W)
        self.__titleTxt.place(relx=0.58, rely=0.42, anchor=N)

        generateButton = Button(self.__window, text=generateButtonText, font='Arial 10', width=21, relief=RIDGE, bg='white', activebackground='whitesmoke', command=self.__addSpeakerName)
        generateButton.place(relx=0.5, rely=0.57, anchor=N)

        clearInputButton = Button(self.__window, text=clearInputButtonText, font='Arial 10', width=21, relief=RIDGE, bg='white', activebackground='whitesmoke', command=self.__clearInput)
        clearInputButton.place(relx=0.5, rely=0.67, anchor=N)

        clearOutputFolderButton = Button(self.__window, text=clearOutputFolderButtonText, font='Arial 10', width=21, relief=RIDGE, bg='#FF4C4C', activebackground='#ff3232', command=self.__clearOutputFolder)
        clearOutputFolderButton.place(relx=0.5, rely=0.77, anchor=N)

        copyrightText = Label(self.__window, text=copyright, font='Courier 8', bg="#fff", foreground="#000")
        copyrightText.place(relx=0.0, rely=1.0, anchor=SW)

        # Menu bar
        menubar = Menu(self.__window)

        # Help
        help_btn = Menu(self.__window, tearoff=0, bg="white", activebackground='whitesmoke', activeforeground='black')
        help_btn.add_command(label=contactUsText, command=self.__openWeb)
        help_btn.add_separator()
        help_btn.add_command(label=versionNumberText)
        menubar.add_cascade(label=HelpText, menu=help_btn)
        self.__window.config(menu=menubar)

    # Commands for buttons
    def __addSpeakerName(self):
        speaker = Speaker(self.__nameTxt.get(), self.__familyNameTxt.get(), self.__titleTxt.get())
        self.__controller.add(speaker)

    def __clearInput(self):
        self.__nameTxt.delete(0, 'end')
        self.__familyNameTxt.delete(0, 'end')
        self.__titleTxt.delete(0, 'end')

    def __clearOutputFolder(self):
        self.__controller.clearOutputFolder()

    def __openWeb(self):
        webbrowser.open("https://github.com/Viktorens/Lower-Thirds-Generator")

# Exit App
def exit_app():
    quit()
