import tkinter

class UserDescriptor:
    def __get__(self, instance, owner):
        if instance.__dict__[self.name] is None:
            return None
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name

class User:
    name, age, balance, admin = UserDescriptor(), UserDescriptor(), UserDescriptor(), UserDescriptor()

    def __init__(self, name, age, balance=100, admin = False):
        self.admin = admin
        self.name = name
        self.age = age
        self.balance = balance

    def setName(self, mainWindow):
        def set(event):
            self.name = INPUT.get()
            INPUT.delete(0, tkinter.END)
            mainWindow.INPUT.focus_set()
            if self.name is False or self.name is None or len(self.name) == 0:
                self.name = None
                mainWindow.LABEL['text'] = 'Вы ничего не ввели'
            else:
                mainWindow.LABEL['text'] = f'Я запомнил, что Вас зовут {self.name}!'
                mainWindow.NAME['text'] = 'Здравствуйте, ' + self.name
            mainWindow.RIGHT_LABEL['text'] = 'Скажите Боту что-то сделать'
            INPUT.destroy()

        mainWindow.RIGHT_LABEL['text'] = 'Введите имя: '
        INPUT = mainWindow.setFrameInput()
        INPUT.place(x=160, y=300)
        INPUT.bind('<Return>', set)
        return 'Жду ввода имени...'
    
    def delData(self, mainWindow, dataToDel:str, questionPhrase:str) -> str:
        if self.__dict__[dataToDel] is not None:
            def userAnswer(event):
                answer = INPUT.get()
                INPUT.delete(0, tkinter.END)
                mainWindow.INPUT.focus_set()
                if answer.lower() == 'да':
                    self.__dict__[dataToDel] = None
                    mainWindow.LABEL['text'] = 'Я забыл эту информацию!'
                elif answer.lower() == 'нет':
                    mainWindow.LABEL['text'] = 'Окей, я все еще помню эту информацию!'
                else:
                    mainWindow.LABEL['text'] = 'Я Вас не понял('
                INPUT.destroy()
                mainWindow.RIGHT_LABEL['text'] = 'Скажите Боту что-то сделать'

            mainWindow.RIGHT_LABEL['text'] = f'{questionPhrase}{self.__dict__[dataToDel]}?'
            INPUT = mainWindow.setFrameInput()
            INPUT.bind('<Return>', userAnswer)
            return 'Жду ответа...'
        else:
            return 'Я и так не знаю этой информации!'

    def setAge(self, mainWindow):
        def set(event):
            self.age = INPUT.get()
            mainWindow.INPUT.focus_set()
            if self.age is False or self.age is None or len(str(self.age)) == 0:
                self.age = None
                mainWindow.LABEL['text'] = 'Вы ничего не ввели'
            else:
                mainWindow.LABEL['text'] = f'Я запомнил, что Вам {self.age}!'
            mainWindow.RIGHT_LABEL['text'] = 'Скажите Боту что-то сделать'
            INPUT.destroy()

        mainWindow.RIGHT_LABEL['text'] = 'Введите возраст: '
        INPUT = mainWindow.setFrameInput()
        INPUT.bind('<Return>', set)
        return 'Жду ввода возраста...'

    def getAdminStatus(self, mainWindow, app):
        if self.admin is False:
            self.admin = mainWindow.setModuleWindow(self.admin, content = {'textButton' : 'Подтвердить', 'textLabel' : 'Введите пароль:', 'show' : True, 'func' : 'check_password'})
            app.focus_set()
            mainWindow.INPUT.focus_set()
            if self.admin:
                mainWindow.app.title('Бот Alex ~ admin')
                return 'Добро пожаловать, администратор!'
            else:
                return 'Вы пока не вошли под администратором'
        else:
            return 'Вы уже являетесь администратором!'

    def exitAdmin(self, mainWindow):
        if self.admin:
            self.admin = False
            mainWindow.app.title('Бот Alex')
            return 'Вы вышли из режима администратора!'
        else:
            return 'Сперва войдите в режим администратора!'

    def setAdminStatus(self, value):
        self.admin = value