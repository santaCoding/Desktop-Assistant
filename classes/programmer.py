from tkinter import *

class ProgrammingManager:
    def __init__(self):
        self.title = 'Менеджер Программирования'
        self.user_languages = []
        self.builtin = ['Python', 'PHP', 'C++', 'Java', 'JavaScript', 'C', 'C#', 'Swift', 'Kotlin', 'Go']

    def showContent(self, access, mainWindow):
        def selectLangs(event):
            self.FRAME = Frame(mainWindow.right_part)
            self.FRAME.pack()
            for lang in len(range(self.builtin)):
                lang_label = Label(self.FRAME, text = lang, font=('Arial', 14))
                lang_label.bind('<Button-1>', )
                lang_label.pack(pady=5)

        if access['Менеджер Программирования'] == True:
            if not self.user_languages:
                selectLangs()
            else:
                pass