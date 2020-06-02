from platform import *
from tkinter import *
from functools import partial
from tkinter import messagebox

class CustomFunctions:
    def __init__(self):
        self.access_funcs = {'Менеджер Программиста' : True, 'Менеджер Авторизации' : True, 'Менеджер Конвертирования' : True, 'Менеджер Извлечения' : True}
        self.price = 50

    def getAccess(self) -> dict:
        return self.access_funcs

    def system_info(self):
        '''Возвращает все основные параметры системы'''
        return f'Платформа :\n{platform()}\nСистема : {system()},\nИздано : {release()},\nМашина : {machine()},\nПроцессор: : {processor()},\nАрхитектура : {architecture()[0]}'

    def showFuncsToBuy(self, main_window, user):
        '''
        Принимает ссылку на главное окно
        Показывает функции для пользовательской покупки
        Изменяет словарь функций если функция была куплена
        '''
        def showData():
            self.FRAME = Frame(main_window.right_part)
            self.FRAME.pack()
            self.LABEL = Label(self.FRAME, text='Доступны такие функции для покупки:', font=('Arial', 14), fg='#a8a8a8')
            self.LABEL.pack(pady=5)
            item=0
            empty = True
            for manager in self.access_funcs:
                if list(self.access_funcs.values())[item] == False:
                    func = Label(self.FRAME, width = 25, text = manager, bg='#485259', cursor='hand2', fg='white', pady=10, padx=10)
                    func.bind('<Button-1>', partial(buyFunc, manager, user))
                    func.pack(pady = 5)
                    empty = False
                item+=1
            if empty:
                self.LABEL['text'] = 'Все функции доступны!'

        def buyFunc(name_function, user, event):
            answer = messagebox.askyesno('Покупка функции', f'Купить функцию {name_function}?')
            if answer:
                if user.balance >= self.price:
                    user.balance -= self.price
                    print(user.balance)
                    print(self.access_funcs[name_function])
                    self.access_funcs[name_function] = True
                    print(self.access_funcs[name_function])
                    print(f'self.access_funcs: {self.access_funcs}')
                    messagebox.showinfo('Покупка', f'Вы приобрели функцию {name_function}!')
                    self.FRAME.destroy()
                    showData()
                    return f'Спасибо за покупку!'
                else:
                    messagebox.showerror('Ошибка', 'На Вашем счету недостаточно средств!')
                    return '('

        main_window.RIGHT_LABEL['text'] = 'Купить платную функцию'
        main_window.RIGHT_LABEL['pady'] = 40
        showData()
        return 'Вас счет чуть выше'


    def addPaidOption(self, main_window, admin_access:bool) -> str:
        self.copied_funcs = self.access_funcs.copy()
        '''
        Принимает на вход ссылку на главное окно, статус админа и словарь функций
        Возвращает строку с результатом
        '''
        def exit(event):
            self.LEFT_FRAME_FUNCS.destroy()
            self.EXIT_BUTTON.destroy()
            self.SAVE_BUTTON.destroy()
            self.RIGHT_FRAME_FUNCS.destroy()
            self.PROMPT.destroy()
            main_window.RIGHT_LABEL['text'] = 'Скажите Боту что-то сделать'
            main_window.RIGHT_LABEL['pady'] = 260
            main_window.LABEL['text'] = 'Да да?'

        def save(event):
            self.SAVE_BUTTON['text'] = 'Сохранено'
            self.SAVE_BUTTON['highlightbackground'] = '#76a897'
            if self.access_funcs == self.copied_funcs:
                self.access_funcs = self.copied_funcs
                main_window.LABEL['text'] = 'Функции остались прежними!'
            else:
                self.access_funcs = self.copied_funcs
                main_window.LABEL['text'] = 'Функции обновлены!'

        def show_data():
            self.LEFT_FRAME_FUNCS = Frame(main_window.right_part)
            self.RIGHT_FRAME_FUNCS = Frame(main_window.right_part)
            self.LEFT_FRAME_FUNCS.place(x = 15, y = 100)
            self.RIGHT_FRAME_FUNCS.place(x = 290, y = 100)
            self.LEFT_LABEL = Label(self.LEFT_FRAME_FUNCS)
            self.RIGHT_LABEL = Label(self.RIGHT_FRAME_FUNCS)
            self.LEFT_LABEL.pack()
            self.RIGHT_LABEL.pack()

            item = 0
            falses = 0
            trues = 0

            for function in self.copied_funcs:
                if list(self.copied_funcs.values())[item] == False:
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
            self.SAVE_BUTTON['text'] = 'Сохранить'
            self.SAVE_BUTTON['highlightbackground'] = '#a8a8a8'
            self.copied_funcs[name_function] = True
            self.LEFT_FRAME_FUNCS.destroy()
            self.RIGHT_FRAME_FUNCS.destroy()
            show_data()

        def functionOff(name_function, event):
            self.SAVE_BUTTON['text'] = 'Сохранить'
            self.SAVE_BUTTON['highlightbackground'] = '#a8a8a8'
            self.copied_funcs[name_function] = False
            self.LEFT_FRAME_FUNCS.destroy()
            self.RIGHT_FRAME_FUNCS.destroy()
            show_data()

        if admin_access:
            main_window.RIGHT_LABEL['text'] = 'Открыть платную функцию'
            main_window.RIGHT_LABEL['pady'] = 40
            self.SAVE_BUTTON = Button(main_window.right_part, cursor='hand2', text='Сохранить', highlightbackground='#a8a8a8', highlightthickness=30, fg='black')
            self.SAVE_BUTTON.bind('<Button-1>', save)
            self.EXIT_BUTTON = Button(main_window.right_part, cursor='hand2', text='Выход', highlightbackground='#3b6ecc', highlightthickness=30, fg='white')
            self.EXIT_BUTTON.bind('<Button-1>', exit)
            self.SAVE_BUTTON.place(x = 50, y = 545, width = 80, height = 30)
            self.EXIT_BUTTON.place(x = 400, y = 545, width = 90, height = 40)
            self.PROMPT = Label(main_window.right_part, text = 'По окончанию изменения доступа к функциям, нажмите кнопку "Сохранить"', fg='#a8a8a8')
            self.PROMPT.place(x = 30, y = 500)
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
                \n\ma - менеджер авторизаций\n\mc - менеджер конвертирования\n\me - менеджер извлечения\n\mr - менеджер напоминания\
                \n\whoami - что знает бот\n\whoay - информация о боте\n\cany - что может бот \n\exit - выход из админа\
                \n\buy - покупка функций'
        else:
            return 'У Вас нет доступа к функциям такого типа!\nВойдите под администратором'