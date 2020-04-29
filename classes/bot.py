import random
from classes import user, mainWindow, authorization, convert, extract
from tkinter import *
from PIL import ImageTk

class Assistant:
    def __init__(self, app):
        self.app = app
        self.cong = ['Здравствуй!', 'Здарова', 'Привет!', 'Здрасте здрасте)']
        self.mainWindow = mainWindow.MainWindow(self.app, self)
        self.user = user.User() # экземпляр пользователя
        self.autho = authorization.AuthorizationManager(self.user, self.app)
        self.convert = convert.ConvertManager(self.mainWindow)
        self.extract = extract.Extraction(self.mainWindow)
        self.name = 'Бот Alex'
        self.info = {}
        self.deal = ['Неплохо, а Ваши как?', 'Все супер!', 'Очень даже хорошо)', 'Отлично!']
        self.good = ['Ну слава БОТу!', 'Ну вот и супер)', 'Отлично)']
        self.bad = ['Очень жаль(', 'Грустно это слышать!', 'Не унывайте, все будет хорошо!']
        self.dontget = ['Повторите пожалуйста', 'Я Вас не совсем понял', 'Что-то я Вас не понимаю...', 'А можно попроще, я не совсем понимаю...']
        self.bye = ['Пока-пока!', 'Надеюсь, Вы скоро вернетесь!', 'Очень жду дальнейшей встречи!']
        self.thanks = ['Вы тоже!', 'Спасибо большое!', 'Это взаимно', 'Ага да']
        self.facts = ['Идея для создания Бота Alexa\nоснована на книге Эла Свейгарта\n"Автоматизация рутины"!',
        'Изначально Бота Alexa планировали\nделать два человека.',
        'Я имею много менеджеров,\nнапример Менеджер Авторизации,\nМенеджер Конвертирования,\nМенеджер Извлечения.',
        'Во мне есть некоторые платные\nдля обычного пользователя функции.']
        self.answers = {
            'привет здравствуй здарова здравствуйте здрасте добрый_день добрый_вечер доброе_утро' : self.cong,
            'как_дела как_поживаешь как_твои_дела ты_как' : self.deal,
            'хорошо отлично супер неплохо замечательно блеск' : self.good,
            'не_нравишься ты_плохой ты_ужасный ты_тупой' : self.thanks,
            'плохо так_себе не_очень ужасно чудовищно' : self.bad,
            'пока до_свидания чао до_встречи закончить завершить выход' : self.bye,
            'факт' : self.facts
        }
        self.extraAnswers = {
            'что_ты_умеешь что_ты_можешь' : 'Я могу:\n1. Запомнить Ваши имя, возраст\n2. Показывать Вам проблемы и информацию\nпо Вашей ОС\n3. Создавать напоминания и напоминать\n4. Сохранять логины и пароли для сайтов, \nчтобы Вы их не забыли\n5. Конвертировать файлы\n6. Извлекать данные из файлов',
            'как_ты_устроен как_ты_работаешь' : 'Я принимаю написанное Вами,\nобрабатываю Ваш запрос,\nищу подходящий ответ или запускаю функцию,\nесли Вы меня просите что-то сделать,\nделаю это и в любом случае отвечаю Вам\nуспехом или неуспехом',
            'кто_такой_бот' : 'БОТ - это всемогущий повелитель,\nсоздавший всех ботов\nпо образу и подобию своему.',
            'как_он_выглядит как_выглядит_бот как_бот_выглядит' : 'БОТ представляется каждому в разных обличиях:\n - кому-то в виде Siri,\n - кому-то в виде Google Assistant,\n - а кому-то в виде Cortana.\nКаждому - свое!',
            'ты_бот' : 'Возможно)\nА может я что-то больше, чем просто машина?',
            'расскажи_о_себе ты_кто кто_ты кто_тебя_создал откуда_ты кто_тебя_написал' : 'Меня написал студент 2-го курса ИКСа\nАлександр Федоренко на ЯП "Python".',
            'кто_админ кто_такой_админ' : 'Администратор - человек, который имеет доступ\nк внутренним функциям моей системы\nи может регулировать платные функции.\nДля доступа администратора нужен подходящий пароль.'
        }
        self.data = {
            'твое_имя тебя_зовут' : 'f\'Меня зовут {self.getName()}\'',
            'как_меня_зовут как_мое_имя' : 'self.user.getName()',
            'меня_зовут запиши_мое_имя запомни_мое_имя' : 'self.user.setName(self.mainWindow)',
            'забудь_мое_имя удали_мое_имя забудь_меня забудь_как_меня_зовут' : 'self.user.delData(self.mainWindow, \'name\', \'Мне забыть что Вас зовут \')',
            'запомни_мой_возраст запиши_мой_возраст запомни_сколько_мне_лет запиши_сколько_мне_лет' : 'self.user.setAge(self.mainWindow)',
            'забудь_мой_возраст удали_мой_возраст' : 'self.user.delData(self.mainWindow, \'age\', \'Мне забыть что Вам \')',
            'сколько_мне_лет мой_возраст' : 'self.user.getAge()',
            'что_ты_знаешь что_ты_помнишь' : 'self.getInfo()',
            'забудь' : 'self.forgetData()'
        }
        self.customFuncs = {
            'я_админ зайти_в_админку доступ_админ админ_доступ' : 'self.user.getAdminStatus(self.mainWindow)',
            'выйти_из_админа выйти_из_администратора я_не_админ выйти_из_режима_администратора выйти_из_под_админа' : 'self.user.exitAdmin(self.mainWindow)',
            'новая_авторизация авторизация занести_авторизацию занести_логин_и_пароль запомнить_авторизацию новый_вход новая_авторизация' : 'self.autho.addItem(self.mainWindow.right_part, self.mainWindow)',
            'менеджер_авторизаций покажи_авторизации покажи_логины покажи_пароли логины пароли' : 'self.autho.showContent(self.mainWindow.right_part)',
            'какой_логин какой_пароль какая_авторизация какой_пункт' : 'self.autho.getItem()',
            'удали_авторизацию удали_вход удалить_авторизацию удали_пункт' : 'self.autho.delItem()',
            'очистить_менеджер удалить_пункты удалить_все_пункты очистить_пункты' : 'self.autho.clearManager()',
            'конверт' : 'self.convert.convert()',
            'извлечь извлечение' : 'self.extract.extract()'
        }
            
    def getName(self):
        return self.name

    def getInfo(self):
        response = ''
        if self.user.name is not None:
            self.info['Имя'] = self.user.getName()
        if self.user.age is not None:
            self.info['Возраст'] = self.user.getAge()
        for label in self.info:
            response += (f'\n{label} : {self.info[label]}')

        return f'Я знаю Ваши: {response}' if response else 'Я о Вас ничего не знаю('
    
    def forgetData(self):
        if self.info:
            answer = str(input('Бот: Что я должен забыть?'))
            if 'имя' in answer.lower():
                self.response = self.user.delName()
                return self.response
            elif 'возраст' in answer.lower():
                self.response = self.user.delAge()
                return self.response
        else:
            return 'Мне нечего забывать, я и так о Вас ничего не знаю...'

    def getResponse(self, event):
        phrase = self.mainWindow.INPUT.get()
        tupleSetResponse = ('self.answers', 'self.extraAnswers', 'self.data', 'self.customFuncs')
        for exactLists in range(len(tupleSetResponse)):
            response = self.setResponse(phrase, eval(tupleSetResponse[exactLists]), tupleSetResponse[exactLists])
            if response is not None:
                self.mainWindow.LABEL['text'] = response
                self.mainWindow.INPUT.bind('<Return>', self.getResponse)
                self.mainWindow.BUTTON.bind('<Button-1>', self.getResponse)
                break
        else:
            self.mainWindow.LABEL['text'] = random.choice(self.dontget)
        self.mainWindow.INPUT.delete(0, END)

    def setResponse(self, phrase, varDict, dictTitle):
        for key in varDict.keys():
            for parsedPhrase in key.split():
                parsedPhrase = parsedPhrase.replace('_', ' ')
                if parsedPhrase in phrase.lower():
                    if dictTitle == 'self.answers':
                        response = random.choice(varDict[key])
                    elif dictTitle == 'self.extraAnswers':
                        response = varDict[key]
                    elif dictTitle == 'self.data' or dictTitle == 'self.customFuncs':
                        response = eval(varDict[key])
                    return response
                    break
        else:
            response = None
            return response