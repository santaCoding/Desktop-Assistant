from platform import *
from tkinter import *

def system_info():
    '''Возвращает все основные параметры системы'''
    return f'Платформа : {platform()}\nСистема : {system()},\nИздано : {release()},\nМашина : {machine()},\nПроцессор: : {processor()},\nАрхитектура : {architecture()[0]}'

def addPaidOption(main_window, admin_access:bool):
    '''
    Принимает на вход ссылку на главное окно и статус админа
    Возвращает строку с результатом
    '''
    if admin_access:
        main_window.right_part.LABEL['text'] = 'Открыть платную функцию'
        main_window.right_part.LABEL['pady'] = 40


def showAdminComands(admin_access:bool):
    '''
    Принимает статус админа
    Возвращает строку cо списком команд админа
    '''
    if admin_access:
        return '\\admin - права админа\n\\nf - новая функция (админ)\n\\new - новый вход\n\sys - системная информация\
            \ma - менеджер авторизаций\n\mc - менеджер конвертирования\n\me - менеджер извлечения\n\whoami - что знает бот\
            \n\whoay - информация о боте\n\cany - что может бот \n\exit - выход из админа'
    else:
        return 'У Вас нет доступа к функциям такого типа!\nВойдите под администратором'