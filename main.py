from tkinter import *
from UI.ui import *
from Controller.ControllerSpeaker import ControllerSpeaker
from Repository.RepositorySpeaker import RepositorySpeaker

def main():
    repoSpeaker = RepositorySpeaker()
    controlSpeaker = ControllerSpeaker(repoSpeaker)

    # App
    root = Tk()
    app = UI(root, controlSpeaker)
    app.draw_window()
    root.iconbitmap("Assets/img/icon.ico")
    root.mainloop()

main()
