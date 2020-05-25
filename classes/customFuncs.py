from platform import *
from tkinter import *
from functools import partial

def system_info():
    '''Возвращает все основные параметры системы'''
    return f'Платформа : {platform()}\nСистема : {system()},\nИздано : {release()},\nМашина : {machine()},\nПроцессор: : {processor()},\nАрхитектура : {architecture()[0]}'

def addPaidOption(main_window, admin_access:bool, funcs:dict) -> str:
    '''
    Принимает на вход ссылку на главное окно, статус админа и словарь функций
    Возвращает строку с результатом
    '''
    def show_data():
        LEFT_FRAME_FUNCS = Frame(main_window.right_part)
        RIGHT_FRAME_FUNCS = Frame(main_window.right_part)
        LEFT_FRAME_FUNCS.place(x = 15, y = 100)
        RIGHT_FRAME_FUNCS.place(x = 290, y = 100)
        LEFT_LABEL = Label(LEFT_FRAME_FUNCS)
        RIGHT_LABEL = Label(RIGHT_FRAME_FUNCS)
        LEFT_LABEL.pack()
        RIGHT_LABEL.pack()
        item = 0
        falses = 0
        trues = 0
        for function in funcs:
            if list(funcs.values())[item] == False:
                falses += 1
                func = Label(LEFT_FRAME_FUNCS, width = 25, text = function, bg='#485259', cursor='hand2', fg='white', pady=10, padx=10)
                func.bind('<Button-1>', partial(functionOn, function, LEFT_FRAME_FUNCS, RIGHT_FRAME_FUNCS))
                func.pack(pady = 5)
            else:
                trues += 1
                func = Label(RIGHT_FRAME_FUNCS, width = 25, text = function, bg='#485259', cursor='hand2', fg='white', pady=10, padx=10)
                func.bind('<Button-1>', partial(functionOff, function, LEFT_FRAME_FUNCS, RIGHT_FRAME_FUNCS))
                func.pack(pady = 5)
            item += 1
        LEFT_LABEL['text'] = f'Список недоступных функций: [{falses}]'
        RIGHT_LABEL['text'] = f'Список включенных функций: [{trues}]'

    def functionOn(name_function, LEFT_FRAME_FUNCS, RIGHT_FRAME_FUNCS, event):
        funcs[name_function] = True
        LEFT_FRAME_FUNCS.destroy()
        RIGHT_FRAME_FUNCS.destroy()
        show_data()

    def functionOff(name_function, LEFT_FRAME_FUNCS, RIGHT_FRAME_FUNCS, event):
        funcs[name_function] = False
        LEFT_FRAME_FUNCS.destroy()
        RIGHT_FRAME_FUNCS.destroy()
        show_data()

    if admin_access:
        main_window.RIGHT_LABEL['text'] = 'Открыть платную функцию'
        main_window.RIGHT_LABEL['pady'] = 40
        DONE_BUTTON = Button(main_window.right_frame, cursor='hand2', text='Выход', highlightbackground='#3b6ecc', highlightthickness=30, fg='white')
        DONE_BUTTON.bind('<Button-1>', partial(done))
        show_data()
        return 'Добавление функции (~ админ)'
    else:
        return 'У Вас нет доступа к функциям такого типа!\nВойдите под администратором'


def showAdminComands(admin_access:bool) -> str:
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