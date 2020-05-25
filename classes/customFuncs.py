from platform import *
from tkinter import *
from functools import partial

class CustomFunctions:
    def __init__(self, access):
        self.funcs = access

    def getAccess(self):
        return self.funcs

    def system_info(self):
        '''Возвращает все основные параметры системы'''
        return f'Платформа : {platform()}\nСистема : {system()},\nИздано : {release()},\nМашина : {machine()},\nПроцессор: : {processor()},\nАрхитектура : {architecture()[0]}'

    def addPaidOption(self, main_window, admin_access:bool) -> str:
        '''
        Принимает на вход ссылку на главное окно, статус админа и словарь функций
        Возвращает строку с результатом
        '''
        self.LEFT_FRAME_FUNCS = Frame(main_window.right_part)
        self.RIGHT_FRAME_FUNCS = Frame(main_window.right_part)

        def exit():
            self.LEFT_FRAME_FUNCS.destroy()
            self.RIGHT_FRAME_FUNCS.destroy()
            main_window.RIGHT_LABEL['text'] = 'Скажите Боту что-то сделать'
            main_window.RIGHT_LABEL['pady'] = 260
            main_window.LABEL['text'] = 'Да да?'

        def save(event):
            self.SAVE_BUTTON['text'] = 'Сохранено'
            self.SAVE_BUTTON['highlightbackground'] = '#76a897'
            if self.funcs == self.updated_funcs:
                main_window.LABEL['text'] = 'Функции остались прежними!'
            else:
                main_window.LABEL['text'] = 'Функции обновлены!'

        def show_data():
            self.LEFT_FRAME_FUNCS.place(x = 15, y = 100)
            self.RIGHT_FRAME_FUNCS.place(x = 290, y = 100)
            self.LEFT_LABEL = Label(self.LEFT_FRAME_FUNCS)
            self.RIGHT_LABEL = Label(self.RIGHT_FRAME_FUNCS)
            self.EXIT_BUTTON = Button(main_window.right_part, cursor='hand2', text='Выход', highlightbackground='#3b6ecc', highlightthickness=30, fg='white')
            self.EXIT_BUTTON.bind('<Button-1>', partial(exit))
            self.SAVE_BUTTON = Button(main_window.right_part, cursor='hand2', text='Сохранить', highlightbackground='#a8a8a8', highlightthickness=30, fg='black')
            self.SAVE_BUTTON.bind('<Button-1>', partial(save))
            self.SAVE_BUTTON.place(x = 200, y = 545, width = 80, height = 30)
            self.EXIT_BUTTON.place(x = 400, y = 545, width = 90, height = 40)
            self.LEFT_LABEL.pack()
            self.RIGHT_LABEL.pack()
            item = 0
            falses = 0
            trues = 0
            self.updated_funcs = self.funcs[:]
            for function in self.updated_funcs:
                if list(self.updated_funcs.values())[item] == False:
                    falses += 1
                    func = Label(self.LEFT_FRAME_FUNCS, width = 25, text = function, bg='#485259', cursor='hand2', fg='white', pady=10, padx=10)
                    func.bind('<Button-1>', partial(functionOn, function))
                    func.pack(pady = 5)
                else:
                    trues += 1
                    func = Label(self.RIGHT_FRAME_FUNCS, width = 25, text = function, bg='#485259', cursor='hand2', fg='white', pady=10, padx=10)
                    func.bind('<Button-1>', partial(functionOff, function))
                    func.pack(pady = 5)
                item += 1
            self.LEFT_LABEL['text'] = f'Список недоступных функций: [{falses}]'
            self.RIGHT_LABEL['text'] = f'Список включенных функций: [{trues}]'

        def functionOn(name_function, event):
            self.updated_funcs[name_function] = True
            self.LEFT_FRAME_FUNCS.destroy()
            self.RIGHT_FRAME_FUNCS.destroy()
            show_data()

        def functionOff(name_function, event):
            self.updated_funcs[name_function] = False
            self.LEFT_FRAME_FUNCS.destroy()
            self.RIGHT_FRAME_FUNCS.destroy()
            show_data()

        if admin_access:
            main_window.RIGHT_LABEL['text'] = 'Открыть платную функцию'
            main_window.RIGHT_LABEL['pady'] = 40
            show_data()
            return 'Добавление функции (~ админ)'
        else:
            return 'У Вас нет доступа к функциям такого типа!\nВойдите под администратором'


    def showAdminComands(self, admin_access:bool) -> str:
        '''
        Принимает статус админа
        Возвращает строку cо списком команд админа
        '''
        if admin_access:
            return '\\admin - права админа\n\\nf - новая функция (админ)\n\\new - новый вход\n\sys - системная информация\
                \n\ma - менеджер авторизаций\n\mc - менеджер конвертирования\n\me - менеджер извлечения\n\whoami - что знает бот\
                \n\whoay - информация о боте\n\cany - что может бот \n\exit - выход из админа'
        else:
            return 'У Вас нет доступа к функциям такого типа!\nВойдите под администратором'