from tkinter import *
from functools import partial
from PIL import ImageTk
from tkinter import messagebox

class ProgrammingManager:
    def __init__(self):
        self.title = 'Менеджер Программирования'
        self.user_languages = []
        self.recourses = ProgrammingRecourses(self)
        self.logos = {'Python' : ImageTk.PhotoImage(file='img/Python.png'),
        'PHP' : ImageTk.PhotoImage(file='img/PHP.png'),
        'Cpp' : ImageTk.PhotoImage(file='img/Cpp.png'),
        'Java' : ImageTk.PhotoImage(file='img/Java.png'),
        'JavaScript' : ImageTk.PhotoImage(file='img/JavaScript.png'),
        'Csh' : ImageTk.PhotoImage(file='img/Csh.png'),
        'Perl' : ImageTk.PhotoImage(file='img/Perl.png'),
        'Swift' : ImageTk.PhotoImage(file='img/Swift.png'),
        'Kotlin' : ImageTk.PhotoImage(file='img/Kotlin.png'),
        'Go' : ImageTk.PhotoImage(file='img/Go.png')}

    def add(self, mainWindow, name_lang, event):
        self.user_languages.append(name_lang)
        self.ADD_LANG1.destroy()
        self.ADD_LANG2.destroy()
        messagebox.showinfo('Добавление языка', f'Язык программирования {name_lang} добавлен в Ваш набор!')
        self.checkExistence(mainWindow, name_lang)

    def delete(self, mainWindow, name_lang, event):
        index = self.user_languages.index(name_lang)
        self.user_languages.pop(index)
        self.DELETE_LANG.destroy()
        messagebox.showinfo('Удаление языка', f'Язык программирования {name_lang} удален из Вашего набора!')
        self.checkExistence(mainWindow, name_lang)

    def checkExistence(self, mainWindow, name_lang):
        if name_lang not in self.user_languages:
            self.ADD_LANG1 = Label(mainWindow.right_part, bg='#177a63', cursor='hand2')
            self.ADD_LANG2 = Label(mainWindow.right_part, bg='#177a63', cursor='hand2')
            self.ADD_LANG1.bind('<Button-1>', partial(self.add, mainWindow, name_lang))
            self.ADD_LANG2.bind('<Button-1>', partial(self.add, mainWindow, name_lang))
            self.ADD_LANG1.place(x=343, y=51, width=5, height=15)
            self.ADD_LANG2.place(x=338, y=56, width=15, height=5)
        else:
            self.DELETE_LANG = Label(mainWindow.right_part, bg='#822f2f', cursor='hand2')
            self.DELETE_LANG.bind('<Button-1>', partial(self.delete, mainWindow, name_lang))
            self.DELETE_LANG.place(x=338, y=56, width=15, height=5)

    def Python(self, mainWindow, name_lang, event):
        mainWindow.RIGHT_LABEL['text'] = 'Python'
        mainWindow.RIGHT_LABEL['font'] = ('Arial', 25, 'bold')
        mainWindow.RIGHT_LABEL['fg'] = '#3573a6'
        self.FRAME.destroy()
        self.FRAME = Frame(mainWindow.right_part)
        self.FRAME.pack()
        self.PROMPT['text'] = 'Выберите категорию применения языка'
        self.checkExistence(mainWindow, name_lang)
        WEB_LBL = Label(self.FRAME, text = 'WEB-разработка', font=('Arial', 17), fg='#3573a6', cursor='hand2', bg='#cfd3ff')
        ML_LBL = Label(self.FRAME, text = 'Machine Learning', font=('Arial', 17), fg='#3573a6', cursor='hand2', bg='#cfd3ff')
        AP_LBL = Label(self.FRAME, text = 'Автоматизация процессов', font=('Arial', 17), fg='#3573a6', cursor='hand2', bg='#cfd3ff')
        WEB_LBL.bind('<Button-1>', partial(self.recourses.WEBPython, mainWindow))
        WEB_LBL.pack(pady=10)
        ML_LBL.pack(pady=10)
        AP_LBL.pack(pady=10)

    def PHP(self, mainWindow, name_lang, event):
        mainWindow.RIGHT_LABEL['text'] = 'PHP'
        mainWindow.RIGHT_LABEL['font'] = ('Arial', 25, 'bold')
        mainWindow.RIGHT_LABEL['fg'] = '#3573a6'
        self.FRAME.destroy()
        self.FRAME = Frame(mainWindow.right_part)
        self.FRAME.pack()
        self.PROMPT['text'] = 'Выберите категорию применения языка'
        self.checkExistence(mainWindow, name_lang)
        

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
            for lang in list(self.logos.keys()):
                if iteration % 2 == 0:
                    self.labels_frame = Frame(self.FRAME)
                    self.labels_frame.pack(pady=10)
                lang_label = Label(self.labels_frame, image=self.logos[lang], cursor='hand2')
                lang_label.bind('<Button-1>', partial(eval(f'self.{lang}'), mainWindow, lang))
                lang_label.pack(side=LEFT, padx=60)
                iteration += 1 

        if access['Менеджер Программирования'] == True:
            if not self.user_languages:
                mainWindow.RIGHT_LABEL['text'] = self.title
                mainWindow.RIGHT_LABEL['pady'] = 30
                self.PROMPT = Label(mainWindow.right_part, text='Выберите язык программирования', font=('Arial', 14), fg='grey')
                self.PROMPT.pack(pady=7)
                selectLangs(None)
                return 'Менеджер Программирования'
            else:
                pass
        else:
            return 'К сожалению, администратор запретил\nдоступ к этому Менеджеру.\nЧтобы получить доступ\nтребуется купить эту функцию.'


class ProgrammingRecourses:
    def __init__(self, manager):
        self.manager = manager
        self.books = {
            'Python' : ['Django: практика создания Web-сайтов на Python (2018)', ]
        }

    def WEBPython(self, mainWindow, event):
        try:
            self.manager.ADD_LANG1.destroy()
            self.manager.ADD_LANG2.destroy()
        except:
            self.manager.DELETE_LANG.destroy()
        self.manager.FRAME.destroy()
        self.manager.PROMPT.destroy()
        self.FRAME1 = Frame(mainWindow.right_part)
        self.FRAME1.pack()
        self.FRAME2 = Frame(mainWindow.right_part)
        self.FRAME2.pack()
        self.TEXT = Label(self.FRAME2, text='Согласно данным опроса разработчиков Python в 2019,\nDjango и Flask являются самыми популярными веб фреймворками\nсреди разработчиков.\nВы вряд ли ошибетесь, выбрав один из этих фреймворков\nдля работы с вашим новым веб приложением.\nХотя выбор того, какой из них будет лучше работать для вас\nи ваших целей, есть ряд явных отличий, которые нужно иметь в виду,\nперед тем как сделать выбор.', font=('Arial', 16), fg='#33465e', justify=LEFT, anchor=W)
        self.TEXT.pack(pady=10)
        self.django = ImageTk.PhotoImage(file='img/Django.png')
        self.flask = ImageTk.PhotoImage(file='img/Flask.jpg')
        mainWindow.RIGHT_LABEL['text'] = 'WEB-Python'
        djangoLogo = Label(self.FRAME1, image=self.django)
        flaskLogo = Label(self.FRAME1, image=self.flask)
        djangoLogo.pack(side=LEFT, padx=10)
        flaskLogo.pack(side=LEFT, padx=10)
        PROMPT = Label(mainWindow.right_part, text='Полезные книги:\t\tПолезные ссылки:', font=('Arial', 16, 'bold'), fg='#33465e')
        PROMPT.pack(pady=5)

        