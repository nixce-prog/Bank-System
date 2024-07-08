from tkinter import Tk


class Window():

    def __new__(self,title,geometry) -> Tk:
        menu = Tk()
        menu.title(title)
        menu.geometry(geometry)
        menu.resizable(False, False)
        return menu