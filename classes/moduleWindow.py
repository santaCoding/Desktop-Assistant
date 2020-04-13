from tkinter import *

class ModuleWindow:
    def __init__(self, app, adminStatus, content):
        self.moduleWindowTk = Toplevel(app)
        self.moduleWindowTk.title('Права администратора')
        self.initUI(app, adminStatus, content)

    def initUI(self, app, adminStatus, content):
        self.moduleWindowTk.configure(background = '#5164b1')
        self.center()
        self.contentModuleWindow(adminStatus, content) #функция контента модульного окна
        self.MODULE_LABEL.pack()
        self.MODULE_INPUT.pack()
        self.MODULE_INPUT.focus_set()
        self.MODULE_BUTTON.pack()
        self.moduleWindowTk.transient(app)
        self.moduleWindowTk.grab_set()
        self.moduleWindowTk.focus_set()
        self.moduleWindowTk.wait_window()
    
    def center(self):
        width = self.moduleWindowTk.winfo_screenwidth()
        height = self.moduleWindowTk.winfo_screenheight()
        self.moduleWindowTk.geometry('400x100')
        self.moduleWindowTk.wm_geometry(f'+{width//2-200}+{height//2-70}')

    def contentModuleWindow(self, adminStatus, content):
        self.flag = False
        def check_password(event):
                password = self.MODULE_INPUT.get()
                if password == 'Qwerty':
                    self.flag = True
                    self.moduleWindowTk.destroy()
                else:
                    self.MODULE_LABEL['text'] = 'Неверный пароль!'
                    self.flag = False

        self.MODULE_BUTTON = Button(self.moduleWindowTk, width = 15, text = content['textButton'], bg='#0077ff', highlightbackground='#0077ff', fg='#0c3b70', font=('Gilroy', 14, 'bold'), pady = 7, padx = 10)
        self.MODULE_INPUT = Entry(self.moduleWindowTk, width = 50, font=('Gilroy', 16), bg='white')
        if content['show']:
            self.MODULE_INPUT['show'] = '*'
        self.MODULE_INPUT.bind('<Return>', eval(content['func']))
        self.MODULE_BUTTON.bind('<Button-1>', eval(content['func']))
        self.MODULE_LABEL = Label(self.moduleWindowTk, width = 40, text = content['textLabel'], bg = '#5164b1', fg = 'white', font = ('Gilroy', 15))
        

    def getValue(self):
        return self.flag