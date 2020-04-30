from tkinter import *
from time import sleep
from functools import partial

class AuthorizationManager:
    def __init__(self, user, app):
        self.title = 'Менеджер Авторизаций'
        self.owner = user
        self.items = [] #список ссылок на экземпляры пунктов

    def showContent(self, right_frame, mainWindow):
        if self.items:
            for item in self.items:
                ITEM_FRAME = Frame(right_frame, width = 550, bg='#5164b1', padx = 150)
                ITEM_FRAME.pack()
                LABEL_SITE = Label(ITEM_FRAME, text = f'Сайт: {item.site}')
                LABEL_SITE.pack()
        else:
            mainWindow.RIGHT_LABEL['text'] = 'Менеджер авторизаций пуст!'
            return 'Упс!'

    def exit(self, mainWindow, event):
        self.INPUT_LOGIN.destroy()
        self.INPUT_PASSWORD.destroy()
        self.INPUT_SITE.destroy()
        self.LABEL_LOGIN.destroy()
        self.LABEL_PASSWORD.destroy()
        self.LABEL_SITE.destroy()
        self.WARNING.destroy()
        self.ITEM_FRAME.destroy()
        self.EXIT.destroy()
        mainWindow.RIGHT_LABEL['text'] = 'Скажите Боту что-то сделать'
        mainWindow.RIGHT_LABEL['pady'] = 260
        mainWindow.RIGHT_LABEL['font'] = ('Trebuchet MS', 16, 'bold')
        mainWindow.LABEL['text'] = 'Да да?'
        

    def addItem(self, right_frame, mainWindow) -> str:
        mainWindow.RIGHT_LABEL['text'] = self.title
        mainWindow.RIGHT_LABEL['pady'] = 50
        mainWindow.RIGHT_LABEL['font'] = ('Trebuchet MS', 20, 'bold')
        self.site = None
        self.login = None
        self.password = None

        # проверка 
        def check() -> bool:
            if (self.site != '' and self.site is not None) and (self.login != '' and self.login is not None) and (self.password != '' and self.password is not None):
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
            if self.site != '':
                self.INPUT_SITE.destroy()
                self.INPUT_SITE = None
                self.LABEL_SITE['text'] = f'Сайт: {self.site}'
                if not check():
                    if self.INPUT_LOGIN is not None:
                        self.INPUT_LOGIN.focus_set()
                    else:
                        self.INPUT_PASSWORD.focus_set()
            else:
                self.WARNING['text'] = 'Вы не ввели сайт!'
                self.WARNING['bg'] = '#b54141'
                

        def addLogin(event):
            self.login = self.INPUT_LOGIN.get()
            if self.login != '':
                self.INPUT_LOGIN.destroy()
                self.INPUT_LOGIN = None
                self.LABEL_LOGIN['text'] = f'Логин: {self.login}'
                if not check():
                    if self.INPUT_SITE is not None:
                        self.INPUT_SITE.focus_set()
                    else:
                        self.INPUT_PASSWORD.focus_set()
            else:
                self.WARNING['text'] = 'Вы не ввели логин!'
                self.WARNING['bg'] = '#b54141'
                

        def addPassword(event):
            self.password = self.INPUT_PASSWORD.get()
            if self.password != '':
                self.INPUT_PASSWORD.destroy()
                self.INPUT_PASSWORD = None
                self.LABEL_PASSWORD['text'] = f'Пароль: {self.password}'
                if not check():
                    if self.INPUT_SITE is not None:
                        self.INPUT_SITE.focus_set()
                    else:
                        self.INPUT_LOGIN.focus_set()
            else:
                self.WARNING['text'] = 'Вы не ввели пароль!'
                self.WARNING['bg'] = '#b54141'

        def delWarning(event):
            self.WARNING['text'] = ''
            self.WARNING['bg'] = 'white'

        self.ITEM_FRAME = Frame(right_frame, width = 550, bg='white', padx = 150)
        self.ITEM_FRAME.pack()
        self.INPUT_SITE = Entry(self.ITEM_FRAME, bg = 'white', fg = 'black', width = 30, font = ('Trebuchet MS', 16))
        self.INPUT_LOGIN = Entry(self.ITEM_FRAME, bg = 'white', fg = 'black', width = 30, font = ('Trebuchet MS', 16))
        self.INPUT_PASSWORD = Entry(self.ITEM_FRAME, bg = 'white', fg = 'black', width = 30, font = ('Trebuchet MS', 16))
        self.LABEL_SITE = Label(self.ITEM_FRAME, text = 'Введите сайт:', fg = '#333b4f', bg = 'white', font = ('Trebuchet MS', 14))
        self.LABEL_LOGIN = Label(self.ITEM_FRAME, text = 'Введите логин:', fg = '#333b4f', bg = 'white', font = ('Trebuchet MS', 14))
        self.LABEL_PASSWORD = Label(self.ITEM_FRAME, text = 'Введите пароль:', fg = '#333b4f', bg = 'white', font = ('Trebuchet MS', 14))
        self.WARNING = Label(right_frame, text='', width=30, height = 2, font=('Trebuchet MS', 14), bg='white', fg='white')
        self.EXIT =Button(right_frame, text='Выход', width=20, height = 2, font=('Trebuchet MS', 14), highlightbackground='#0077ff', fg='white')
        self.WARNING.place(x=300, y=550)
        self.EXIT.place(x= 200, y=500)
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
        self.WARNING.bind('<Button-1>', delWarning)
        self.EXIT.bind('<Button-1>', partial(self.exit, mainWindow))

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
    