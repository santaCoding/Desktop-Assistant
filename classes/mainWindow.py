from tkinter import *
import random
from classes import moduleWindow
from PIL import ImageTk

class MainWindow:
    def __init__(self, app, bot):
        self.app = app
        self.initUI(bot)

    def initUI(self, bot):
        self.font = 'Trebuchet MS'
        self.BG_LIGHT = 'white'
        self.logoImage = ImageTk.PhotoImage(file="bot.png")
        self.top_frame = Frame(self.app, width = 1100, height = 50, bg='#373737')
        self.left_part = Frame(self.app, width = 550, height = 600, bg = '#e3e3e3')
        self.right_part = Frame(self.app, width = 550, height = 600, bg = self.BG_LIGHT)
        self.frame_bot = Frame(self.left_part, width = 550, bg = '#e3e3e3', height = 700)
        self.frame_user = Frame(self.left_part, height = 300, width = 550, bg = '#e3e3e3')
        self.LOGO = Label(self.frame_bot, width = 70, height = 70, pady = 248, image = self.logoImage, bg = '#e3e3e3')
        self.LABEL = Label(self.frame_bot, width = 40, height = 23, text = random.choice(bot.cong),
        fg = '#486994', font = (self.font, 16, 'bold'), bg='#e3e3e3', justify = LEFT)
        self.BUTTON = Button(
            self.frame_user, padx=10, pady=7, text = 'Сказать',
            highlightbackground='#0077ff', fg='#0c3b70', font=('Arial', 14, 'bold'),
            bg = '#0077ff')
        self.INPUT = Entry(self.frame_user, width = 50, font=(self.font, 16), bg='#bfbfbf', fg='#292929')
        self.INPUT.bind('<Return>', bot.getResponse)
        self.BUTTON.bind('<Button-1>', bot.getResponse)
        self.RIGHT_LABEL = Label(self.right_part, width = 65, height = 2, bg = self.BG_LIGHT, text = 'Скажите Боту что-то сделать', fg='#7e92ab', font = (self.font, 16, 'bold'), pady=260)
        self.INPUT.focus_set()
        self.top_frame.pack(side=TOP, fill=BOTH)
        self.left_part.pack(side=LEFT, fill=BOTH)
        self.right_part.pack(side=LEFT, fill=BOTH)
        self.frame_bot.pack()
        self.frame_user.pack()
        self.LOGO.pack(side=LEFT)
        self.LABEL.pack(side=RIGHT)
        self.INPUT.pack(side=LEFT)
        self.BUTTON.pack(side=LEFT)
        self.RIGHT_LABEL.pack(side=TOP)

    def setFrameInput(self):
        self.INPUT_FRAME = Entry(self.right_part, width = 30, font=(self.font, 16, 'bold'))
        self.INPUT_FRAME.pack()
        self.INPUT_FRAME.focus_set()
        return self.INPUT_FRAME

    def setTopFrameLabel(self):
        self.LABEL_TOP_FRAME = Label(self.top_frame, font = (self.font, 16), fg = 'white')
        self.LABEL_TOP_FRAME.pack(side = LEFT)
        return self.LABEL_TOP_FRAME

    def setModuleWindow(self, adminStatus, content):
        self.moduleWindow = moduleWindow.ModuleWindow(self.app, adminStatus, content)
        adminStatus = self.moduleWindow.getValue()
        return adminStatus
