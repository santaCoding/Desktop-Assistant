import classes.bot
import random
from tkinter import *

class MetaSystem:
    def __init__(self):
        self.app = Tk()
        self.app.title('Бот Alex')
        self.app.configure(background = 'white')
        self.bot = classes.bot.Assistant(self.app)
        self.center(self.app)
        self.runApp()

    def center(self, app):
        width = app.winfo_screenwidth()
        height = app.winfo_screenheight()
        app.geometry('1100x650')
        app.wm_geometry(f'+{width//2-550}+{height//2-370}')
        app.resizable(width=False, height=False)

    def runApp(self):
        self.app.mainloop()

if __name__ == '__main__':
    application = MetaSystem()
