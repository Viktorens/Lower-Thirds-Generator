from tkinter import *
from UI.ui import *
from Controller.Controller import Controller
from Repository.Repository import Repository

def main():
    repo = Repository()
    controller = Controller(repo)

    # App
    root = Tk()
    app = UI(root, controller)
    app.draw_window()
    root.iconbitmap("Assets/img/icon.ico")
    root.mainloop()

main()

