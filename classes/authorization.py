from tkinter import *
from time import sleep

class Singleton:
    def __init__(self, decorated, user, app, right_frame, mainWindow):
        self._decorated = decorated

    def instance(self, user, app, right_frame, mainWindow):
        try:
            return self._instance
        except AttributeError:
            self._instance = self._decorated()
            return self._instance

    def __call__(self):
        raise TypeError('Singleton должен быть вызван через \'.instance()\'')

    def __instancecheck__(self, inst):
        return isinstance(inst, self._decorated)


class AuthorizationManager:
    def __init__(self, user, app):
        self.title = 'Менеджер Авторизаций'
        self.owner = user
        self.items = [] #список ссылок на экземпляры пунктов

    def showContent(self, right_frame):
        if self.items:
            for item in self.items:
                ITEM_FRAME = Frame(right_frame, width = 550, bg='#5164b1', padx = 150)
                ITEM_FRAME.pack()
                LABEL_SITE = Label(ITEM_FRAME, text = f'Сайт: {item.site}')
                LABEL_SITE.pack()
        else:
            return 'Менеджер Авторизаций пуст!'

    #def clearFrame(self, right_frame, mainWindow):
        


    def addItem(self, right_frame, mainWindow) -> str:
        #self.clearFrame(right_frame, mainWindow)
        mainWindow.RIGHT_LABEL['text'] = self.title
        mainWindow.RIGHT_LABEL['pady'] = 50
        mainWindow.RIGHT_LABEL['font'] = ('Gilroy', 23, 'bold')
        self.site = None
        self.login = None
        self.password = None
        def check() -> bool:
            if self.site is not None and self.login is not None and self.password is not None:
                self.LABEL_LOGIN.destroy()
                self.LABEL_SITE.destroy()
                self.LABEL_PASSWORD.destroy()
                self.ITEM_FRAME.destroy()
                mainWindow.RIGHT_LABEL['text'] = 'Готово'
                mainWindow.RIGHT_LABEL['pady'] = 260
                item = AuthorizationItem(self.site, self.login, self.password)
                self.items.append(item)
                mainWindow.LABEL['text'] = f'Пункт авторизации\nдля сайта {self.site} сохранен!'
                mainWindow.INPUT.focus_set()

                return True
            else:
                return False

        def addSite(event):
            self.site = self.INPUT_SITE.get()
            self.INPUT_SITE.destroy()
            self.INPUT_SITE = None
            self.LABEL_SITE['text'] = f'Сайт: {self.site}'
            if not check():
                if self.INPUT_LOGIN is not None:
                    self.INPUT_LOGIN.focus_set()
                else:
                    self.INPUT_PASSWORD.focus_set()

        def addLogin(event):
            self.login = self.INPUT_LOGIN.get()
            self.INPUT_LOGIN.destroy()
            self.INPUT_LOGIN = None
            self.LABEL_LOGIN['text'] = f'Логин: {self.login}'
            if not check():
                if self.INPUT_SITE is not None:
                    self.INPUT_SITE.focus_set()
                else:
                    self.INPUT_PASSWORD.focus_set()

        def addPassword(event):
            self.password = self.INPUT_PASSWORD.get()
            self.INPUT_PASSWORD.destroy()
            self.INPUT_PASSWORD = None
            self.LABEL_PASSWORD['text'] = f'Пароль: {self.password}'
            if not check():
                if self.INPUT_SITE is not None:
                    self.INPUT_SITE.focus_set()
                else:
                    self.INPUT_LOGIN.focus_set()

        self.ITEM_FRAME = Frame(right_frame, width = 550, bg='#5164b1', padx = 150)
        self.ITEM_FRAME.pack()
        self.INPUT_SITE = Entry(self.ITEM_FRAME, bg = 'white', fg = 'black', width = 20, font = ('Gilroy', 16))
        self.INPUT_LOGIN = Entry(self.ITEM_FRAME, bg = 'white', fg = 'black', width = 20, font = ('Gilroy', 16))
        self.INPUT_PASSWORD = Entry(self.ITEM_FRAME, bg = 'white', fg = 'black', width = 20, font = ('Gilroy', 16))
        self.LABEL_SITE = Label(self.ITEM_FRAME, text = 'Введите сайт:', fg = 'white', bg = '#5164b1', font = ('Gilroy', 16, 'bold'))
        self.LABEL_LOGIN = Label(self.ITEM_FRAME, text = 'Введите логин:', fg = 'white', bg = '#5164b1', font = ('Gilroy', 16, 'bold'))
        self.LABEL_PASSWORD = Label(self.ITEM_FRAME, text = 'Введите пароль:', fg = 'white', bg = '#5164b1', font = ('Gilroy', 16, 'bold'))
        self.LABEL_SITE.pack()
        self.INPUT_SITE.pack()
        self.INPUT_SITE.focus_set()
        self.LABEL_LOGIN.pack()
        self.INPUT_LOGIN.pack()
        self.LABEL_PASSWORD.pack()
        self.INPUT_PASSWORD.pack()

        self.INPUT_SITE.bind('<Return>', addSite)
        self.INPUT_LOGIN.bind('<Return>', addLogin)
        self.INPUT_PASSWORD.bind('<Return>', addPassword)

        return 'Записываю новый пункт...'





        
        


#-------------------------------------------------------------------------------------#



class AuthorizationItem:
    def __init__(self, site, login, password):
        self._site = site
        self._login = login
        self._password = password
    
    @property
    def site(self):
        return self._site

    @property
    def login(self):
        return self._login

    @property
    def password(self):
        return self._password
    