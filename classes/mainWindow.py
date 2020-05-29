from tkinter import *
import random
from classes import moduleWindow
from PIL import ImageTk

class MainWindow:
    def __init__(self, app, bot):
        self.app = app
        self.initUI(bot)

    def initUI(self, bot):
        self.font = None
        self.BG_LIGHT = 'white'
        self.logoImage = ImageTk.PhotoImage(file="bot.png")
        self.top_frame = Frame(self.app, width = 1100, height = 50, bg='#4a4a4a')
        self.NAME = Label(self.top_frame, text='', font=('Arial', 18, 'bold'), fg='white', bg='#4a4a4a')
        self.NAME.pack(pady=10, padx = 10, side=LEFT)
        self.BALANCE = Label(self.top_frame, text='', font=('Arial', 15), fg='white', bg='#4a4a4a')
        self.BALANCE.pack(pady=12, padx = 10, side=LEFT)
        self.left_part = Frame(self.app, width = 550, height = 600, bg = '#e3e3e3')
        self.right_part = Frame(self.app, width = 550, height = 600, bg = self.BG_LIGHT)
        self.frame_bot = Frame(self.left_part, width = 550, bg = '#e3e3e3', height = 700)
        self.frame_user = Frame(self.left_part, height = 300, width = 550, bg = '#e3e3e3')
        self.LOGO = Label(self.frame_bot, padx=20, height = 70, pady = 248, image = self.logoImage, bg = '#e3e3e3', justify=LEFT, anchor = W)
        self.LABEL = Label(self.frame_bot, width = 35, height = 23, text = random.choice(bot.cong),
        fg = '#486994', font = (self.font, 16, 'bold'), bg='#d1d1d1', justify = LEFT)
        self.BUTTON = Button(
            self.frame_user, cursor='hand2', padx=3, pady=7, text = 'Сказать',
            highlightbackground='#3b6ecc', highlightthickness=16, fg='white', font=('Arial', 14),
            bg = '#3b6ecc')
        self.INPUT = Entry(self.frame_user, width = 40, font=(self.font, 16), bg='#bfbfbf', fg='#292929')
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
        self.INPUT_FRAME = Entry(self.right_part, width = 20, font=(self.font, 16, 'bold'))
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
