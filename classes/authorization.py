from tkinter import *
from functools import partial
from tkinter import messagebox, filedialog

class AuthorizationManager:
    def __init__(self, user):
        self.title = 'Менеджер Авторизаций'
        self.owner = user
        self.items = [] #список ссылок на экземпляры пунктов

    def showContent(self, right_frame, mainWindow):
        mainWindow.RIGHT_LABEL['text'] = self.title
        mainWindow.RIGHT_LABEL['pady'] = 40
        if self.items:
            self.ITEMS_FRAME=Frame(right_frame,width=200,bd=1)
            def data():
                self.HEADER = Label(right_frame, bg='white', width=72, text = '%-10s%-30s%-35s%s' % ('#', 'Сайт', 'Логин', 'Пароль'), fg='black', justify=LEFT, anchor=W)
                self.HEADER.place(x=10, y=90)
                for item in range(len(self.items)):
                    self.LABEL_SITE = Label(self.MAIN_FRAME, bg='#ababab', cursor='X_cursor',width=60, text = '%-8d%-15s%-25s%s' % (item+1, self.items[item].site, self.items[item].login, self.items[item].password), fg='white', anchor=W)
                    self.LABEL_SITE.bind('<Button-1>', partial(self.delItem, right_frame, mainWindow, self.items[item], self.ITEMS_FRAME))
                    self.LABEL_SITE.pack(pady=5)

            def myfunction(event):
                self.CANVAS.configure(scrollregion=self.CANVAS.bbox("all"),width=510, height=400)

            self.ITEMS_FRAME.pack()
            self.CANVAS=Canvas(self.ITEMS_FRAME)
            self.MAIN_FRAME=Frame(self.CANVAS)
            self.SCROLLBAR=Scrollbar(self.ITEMS_FRAME,orient="vertical",command=self.CANVAS.yview)
            self.CANVAS.configure(yscrollcommand=self.SCROLLBAR.set)

            self.SCROLLBAR.pack(side="right",fill="y")
            self.CANVAS.pack(side="left")
            self.CANVAS.create_window((0,0),window=self.MAIN_FRAME,anchor='nw')
            self.MAIN_FRAME.bind("<Configure>",myfunction)
            data()
            self.LABEL_PROMPT = Label(right_frame, bg='white', text=f'Чтобы удалить вход, нажмите на него', fg='#8ea2d4', font = ('Arial', 14, 'bold'))
            self.LABEL_PROMPT.place(x=50, y=555)
            self.EXIT = Button(right_frame, cursor='hand2', text='Выход', font=('Arial', 14), highlightbackground='#3b6ecc', highlightthickness=30, fg='white')
            self.EXIT.bind('<Button-1>', partial(self.exit, mainWindow))
            self.EXIT.place(x= 400, y=545, width = 90, height = 40)
            return 'М.А.'
        else:
            mainWindow.RIGHT_LABEL['pady'] = 260
            mainWindow.RIGHT_LABEL['text'] = 'Менеджер авторизаций пуст!'
            try:
                self.LABEL_PROMPT.destroy()
            except AttributeError:
                pass
            try:
                self.ITEMS_FRAME.destroy()
            except:
                pass
            try:
                self.EXIT.destroy()
            except:
                pass
            try:
                self.HEADER.destroy()
            except:
                pass
            return 'Упс!'

    def exit(self, mainWindow, event):
        try:
            self.WARNING.destroy()
        except:
            pass
        try:
            self.ITEMS_FRAME.destroy()
        except:
            pass
        try:
            self.LABEL_PROMPT.destroy()
        except:
            pass
        try:
            self.HEADER.destroy()
        except:
            pass
        self.ITEM_FRAME.destroy()
        self.EXIT.destroy()
        mainWindow.RIGHT_LABEL['text'] = 'Скажите Боту что-то сделать'
        mainWindow.RIGHT_LABEL['pady'] = 260
        mainWindow.RIGHT_LABEL['font'] = ('Arial', 16, 'bold')
        mainWindow.LABEL['text'] = 'Да да?'
        

    def addItem(self, right_frame, mainWindow) -> str:
        mainWindow.RIGHT_LABEL['text'] = self.title
        mainWindow.RIGHT_LABEL['pady'] = 50
        mainWindow.RIGHT_LABEL['font'] = ('Arial', 20, 'bold')
        self.site = None
        self.login = None
        self.password = None

        # проверка 
        def check() -> bool:
            if (self.site != '' and self.site is not None) and (self.login != '' and self.login is not None) and (self.password != '' and self.password is not None):
                self.LABEL_LOGIN.destroy()
                self.LABEL_SITE.destroy()
                self.LABEL_PASSWORD.destroy()
                mainWindow.RIGHT_LABEL['text'] = 'Готово'
                mainWindow.RIGHT_LABEL['pady'] = 260
                item = AuthorizationItem(self.site, self.login, self.password)
                self.items.append(item)
                mainWindow.LABEL['text'] = f'Пункт авторизации\nдля сайта {self.site} сохранен!'
                self.EXIT.destroy()
                self.WARNING.destroy()
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
        self.INPUT_SITE = Entry(self.ITEM_FRAME, bg = 'white', fg = 'black', width = 30, font = ('Arial', 16))
        self.INPUT_LOGIN = Entry(self.ITEM_FRAME, bg = 'white', fg = 'black', width = 30, font = ('Arial', 16))
        self.INPUT_PASSWORD = Entry(self.ITEM_FRAME, bg = 'white', fg = 'black', width = 30, font = ('Arial', 16))
        self.LABEL_SITE = Label(self.ITEM_FRAME, text = 'Введите сайт:', fg = '#333b4f', bg = 'white', font = ('Arial', 14))
        self.LABEL_LOGIN = Label(self.ITEM_FRAME, text = 'Введите логин:', fg = '#333b4f', bg = 'white', font = ('Arial', 14))
        self.LABEL_PASSWORD = Label(self.ITEM_FRAME, text = 'Введите пароль:', fg = '#333b4f', bg = 'white', font = ('Arial', 14))
        self.WARNING = Label(right_frame, text='', cursor='X_cursor', width=30, height = 2, font=('Arial', 14), bg='white', fg='white')
        self.EXIT = Button(right_frame, cursor='hand2', text='Выход', font=('Arial', 14), highlightbackground='#3b6ecc', highlightthickness=30, fg='white')
        self.WARNING.place(x=285, y=550)
        self.EXIT.place(x= 230, y=500, width = 90, height = 40)
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

    def delItem(self, right_frame, mainWindow, item_adress, ITEMS_FRAME, event):
        answer = messagebox.askyesno('Удаление', f'Удалить вход для {item_adress.site}?')
        if answer == True:
            for item in range(len(self.items)):
                if self.items[item] == item_adress:
                    del self.items[item]
                    index = item
                    break
            messagebox.showinfo('Удаление', f'Вход для {item_adress.site} удален!')
            ITEMS_FRAME.destroy()
            self.showContent(right_frame, mainWindow)

    #def getItem(self)
        

#-------------------------------------------------------------------------------------#

class ItemDescriptor:
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name
        
#-------------------------------------------------------------------------------------#

class AuthorizationItem:
    site, login, password = ItemDescriptor(), ItemDescriptor(), ItemDescriptor()
    
    def __init__(self, site, login, password):
        self.site = site
        self.login = login
        self.password = password