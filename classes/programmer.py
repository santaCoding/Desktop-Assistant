from tkinter import *
from functools import partial
from PIL import ImageTk

class ProgrammingManager:
    def __init__(self):
        self.title = 'Менеджер Программирования'
        self.user_languages = []
        self.builtin = ['Python', 'PHP', 'Cpp', 'Java', 'JavaScript', 'Csh', 'Perl', 'Swift', 'Kotlin', 'Go']
        self.logos = {'Python' : ImageTk.PhotoImage(file='Python.png'),
        'PHP' : ImageTk.PhotoImage(file='PHP.png'),
        'Cpp' : ImageTk.PhotoImage(file='Cpp.png'),
        'Java' : ImageTk.PhotoImage(file='Java.png'),
        'JavaScript' : ImageTk.PhotoImage(file='JavaScript.png'),
        'Csh' : ImageTk.PhotoImage(file='Csh.png'),
        'Perl' : ImageTk.PhotoImage(file='Perl.png'),
        'Swift' : ImageTk.PhotoImage(file='Swift.png'),
        'Kotlin' : ImageTk.PhotoImage(file='Kotlin.png'),
        'Go' : ImageTk.PhotoImage(file='Go.png')}
    
    def Python(self, mainWindow, event):
        pass

    def PHP(self, mainWindow, event):
        pass

    def Cpp(self, mainWindow, event):
        pass

    def Java(self, mainWindow, event):
        pass

    def JavaScript(self, mainWindow, event):
        pass

    def Csh(self, mainWindow, event):
        pass

    def Perl(self, mainWindow, event):
        pass

    def Swift(self, mainWindow, event):
        pass

    def Kotlin(self, mainWindow, event):
        pass

    def Go(self, mainWindow, event):
        pass

    def showContent(self, access:dict, mainWindow):
        def selectLangs(event):
            self.FRAME = Frame(mainWindow.right_part)
            self.FRAME.pack()
            iteration = 0
            for lang in self.builtin:
                if iteration % 2 == 0:
                    self.labels_frame = Frame(self.FRAME)
                    self.labels_frame.pack(pady=10)
                lang_label = Label(self.labels_frame, image=self.logos[lang], cursor='hand2')
                lang_label.bind('<Button-1>', partial(eval(f'self.{lang}'), mainWindow))
                lang_label.pack(side=LEFT, padx=60)
                iteration += 1 

        if access['Менеджер Программирования'] == True:
            if not self.user_languages:
                mainWindow.RIGHT_LABEL['text'] = self.title
                mainWindow.RIGHT_LABEL['pady'] = 30
                self.PROMPT = Label(mainWindow.right_part, text='Выберите язык программирования', font=('Arial', 14), fg='grey')
                self.PROMPT.pack(pady=10)
                selectLangs(None)
            else:
                pass