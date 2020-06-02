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

    def showContent(self, access, mainWindow):
        def selectLangs(event):
            self.FRAME = Frame(mainWindow.right_part)
            self.FRAME.pack()
            for lang in self.builtin:
                lang_label = Label(self.FRAME, text = lang, image=self.logos[lang], font=('Arial', 13), fg='grey')
                if lang == 'Cpp':
                    lang_label['text'] = 'C++'
                elif lang == 'Csh':
                    lang_label['text'] = 'C#'
                lang_label.bind('<Button-1>', partial(eval(f'self.{lang}'), mainWindow))
                lang_label.pack(pady = 5)

        if access['Менеджер Программирования'] == True:
            if not self.user_languages:
                mainWindow.RIGHT_LABEL['text'] = self.title
                mainWindow.RIGHT_LABEL['pady'] = 40
                selectLangs(None)
            else:
                pass