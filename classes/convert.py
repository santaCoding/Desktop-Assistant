import pandas as pd
import PIL as pl
from tkinter import *
from tkinter import messagebox, filedialog
from functools import partial
from docx2pdf import convert

class ConvertManager:
    def __init__(self, mainWindow):
        self.title = 'Менеджер Конвертирования'
        self.mainWindow = mainWindow
        self.files_paths = None

    def convert(self, access):
        if access['mc'] == True:
            self.font = 'Arial'
            self.mainWindow.RIGHT_LABEL['text'] = 'Конвертирование'
            self.mainWindow.RIGHT_LABEL['pady'] = 25
            self.mainWindow.RIGHT_LABEL['font'] = (self.font, 25, 'bold')

            self.LABEL_CHOICE = Label(self.mainWindow.right_part, text = 'Выберите тип конвертирования:', font = (self.font, 15, 'bold'), bg='white', fg='#0e131a', pady=20)
            self.LABEL_CHOICE.pack()
            self.BUTTON_TO_PNG = Button(self.mainWindow.right_part, cursor='hand2', text = 'JPG в PNG', width = 20, height = 2, highlightbackground='#0077ff', fg='#0c3b70', font=(self.font, 14))
            self.BUTTON_TO_JPG = Button(self.mainWindow.right_part, cursor='hand2', text = 'PNG в JPG', width = 20, height = 2, highlightbackground='#0077ff', fg='#0c3b70', font=(self.font, 14))
            self.BUTTON_DOCX_TO_PDF = Button(self.mainWindow.right_part,  cursor='hand2',text = 'DOCX в PDF', width = 20, height = 2, highlightbackground='#0077ff', fg='#0c3b70', font=(self.font, 14))
            self.BUTTON_TXT_TO_CSV = Button(self.mainWindow.right_part, cursor='hand2', text = 'TXT в CSV', width = 20, height = 2, highlightbackground='#0077ff', fg='#0c3b70', font=(self.font, 14))
            self.BUTTON_TO_BMP = Button(self.mainWindow.right_part, cursor='hand2', text = 'JPG в BMP', width = 20, height = 2, highlightbackground='#0077ff', fg='#0c3b70', font=(self.font, 14))
            self.BUTTON_EXIT = Button(self.mainWindow.right_part, cursor='hand2', text='Выход', font=('Trebuchet MS', 14, 'bold'), highlightbackground='#3b6ecc', highlightthickness=30, fg='white')
            self.LABEL_NOTE = Label(self.mainWindow.right_part, text = '', font = (self.font, 14), bg='white', fg='#8ea2d4', pady=20)
            self.BUTTON_TO_PNG.pack()
            self.BUTTON_TO_JPG.pack()
            self.BUTTON_TO_BMP.pack()
            self.BUTTON_DOCX_TO_PDF.pack()
            self.BUTTON_TXT_TO_CSV.pack()
            self.BUTTON_EXIT.place(x= 230, y=500, width = 90, height = 40)

            self.BUTTON_TO_PNG.bind('<Button-1>', partial(self.JPGandPNG, extension='.png', title='JPG в PNG', text = 'Для конвертирования в PNG,\nВы можете выбрать форматы JPEG\JPG\BMP.\nРасположение так же выборочно. Допустим множественныц выбор.'))
            self.BUTTON_TO_JPG.bind('<Button-1>', partial(self.JPGandPNG, extension='.jpeg', title='PNG в JPG', text = 'Для конвертирования в JPG,\nВы можете выбрать форматы PNG\BMP\JPEG.\nРасположение так же выборочно. Допустим множественныц выбор.'))
            self.BUTTON_TO_BMP.bind('<Button-1>', partial(self.JPGandPNG, extension='.bmp', title='JPG/PNG в BMP', text='Для конвертирования в BMP,\nВы можете выбрать форматы PNG\JPG\JPEG.\nРасположение так же выборочно. Допустим множественныц выбор.'))
            self.BUTTON_DOCX_TO_PDF.bind('<Button-1>', self.DOCXtoPDF)
            self.BUTTON_TXT_TO_CSV.bind('<Button-1>', self.TXTtoCSV)
            self.BUTTON_EXIT.bind('<Button-1>', self.exit)

            return 'Конвертирование...'
        else:
            return 'К сожалению, администратор запретил\nдоступ к этому Менеджеру.\nЧтобы получить доступ\nтребуется купить эту функцию.'

    def exit(self, event):
        self.BUTTON_DOCX_TO_PDF.destroy()
        self.BUTTON_TO_PNG.destroy()
        self.BUTTON_TO_JPG.destroy()
        self.BUTTON_TXT_TO_CSV.destroy()
        self.BUTTON_TO_BMP.destroy()
        self.LABEL_NOTE.destroy()
        self.LABEL_CHOICE.destroy()
        self.mainWindow.RIGHT_LABEL['text'] = 'Скажите Боту что-то сделать'
        self.mainWindow.RIGHT_LABEL['pady'] = 260
        self.mainWindow.RIGHT_LABEL['font'] = (self.font, 16, 'bold')
        self.BUTTON_EXIT.destroy()
        self.mainWindow.LABEL['text'] = 'Да да?'

    def JPGandPNG(self, event, extension, title, text):
        def getImages(event):
            self.files_paths = filedialog.askopenfilenames()

        def convertToExtension(event):
            if self.files_paths:
                for path in self.files_paths:
                    try:
                        img = pl.Image.open(path)
                        export_files = filedialog.asksaveasfilename(defaultextension=extension)
                        if export_files:
                            img.save(export_files)
                            self.LABEL_NOTE['text'] = 'Готово!'
                        else:
                            messagebox.showerror('Ошибка', 'Введите имя файла')
                    except:
                        messagebox.showerror('Ошибка', 'Неверный формат файла!')
            else:
                messagebox.showerror('Ошибка', 'Не выбрано ни одного файла!')
            self.files_paths = None

        self.LABEL_NOTE['text'] = text
        self.LABEL_NOTE.pack()
        self.LABEL_CHOICE['text'] = title
        self.LABEL_CHOICE['pady'] = 30
        self.BUTTON_DOCX_TO_PDF.destroy()
        self.BUTTON_TXT_TO_CSV.destroy()
        self.BUTTON_TO_BMP.destroy()
        self.BUTTON_TO_PNG['text'] = 'Выберите файлы'
        self.BUTTON_TO_JPG['text'] = 'Конвертировать'

        self.BUTTON_TO_PNG.bind('<Button-1>', getImages)
        self.BUTTON_TO_JPG.bind('<Button-1>', convertToExtension)

    def DOCXtoPDF(self, event):
        def getFiles(event):
            self.files_paths = filedialog.askopenfilenames()

        def convertToExtension(event):
            if self.files_paths:
                for path in self.files_paths:
                    try:
                        export_file = filedialog.asksaveasfilename(defaultextension='.pdf')
                        if export_file:
                            convert(path, export_file)
                            self.LABEL_NOTE['text'] = 'Готово!'
                        else:
                            messagebox.showerror('Ошибка', 'Введите имя файла')
                    except:
                        messagebox.showerror('Ошибка', 'Неверный формат файла!')
            else:
                messagebox.showerror('Ошибка', 'Не выбрано ни одного файла!')
            self.files_paths = None

        self.LABEL_NOTE['text'] = 'Для конвертирования в PDF,\nВы можете использовать формат DOCX.'
        self.LABEL_NOTE.pack()
        self.LABEL_CHOICE['text'] = 'DOCX в PDF'
        self.LABEL_CHOICE['pady'] = 30
        self.BUTTON_DOCX_TO_PDF.destroy()
        self.BUTTON_TXT_TO_CSV.destroy()
        self.BUTTON_TO_BMP.destroy()
        self.BUTTON_TO_PNG['text'] = 'Выберите файлы'
        self.BUTTON_TO_JPG['text'] = 'Конвертировать'

        self.BUTTON_TO_PNG.bind('<Button-1>', getFiles)
        self.BUTTON_TO_JPG.bind('<Button-1>', convertToExtension)

    def TXTtoCSV(self, event):
        def getTXT(event):
            self.files_paths = filedialog.askopenfilenames()

        def convertToCSV(event):
            if self.files_paths:
                for path in self.files_paths:
                        read_file = pd.read_csv(path)
                        export_file = filedialog.asksaveasfilename(defaultextension='.csv')
                        if export_file:
                            read_file.to_csv(export_file, index = None, header = True, encoding='utf8')
                            self.LABEL_NOTE['text'] = 'Готово!'
                        else:
                            messagebox.showerror('Ошибка', 'Введите имя файла')
                    
            else:
                messagebox.showerror('Ошибка', 'Не выбрано ни одного файла!')
            self.files_paths = None


        self.LABEL_NOTE['text'] = 'Для конвертирования в CSV,\nВы можете использовать TXT\\RTF форматы.'
        self.LABEL_NOTE.pack()
        self.LABEL_CHOICE['text'] = 'TXT в CSV'
        self.LABEL_CHOICE['pady'] = 30
        self.BUTTON_DOCX_TO_PDF.destroy()
        self.BUTTON_TXT_TO_CSV.destroy()
        self.BUTTON_TO_BMP.destroy()
        self.BUTTON_TO_PNG['text'] = 'Выберите файлы'
        self.BUTTON_TO_JPG['text'] = 'Конвертировать'

        self.BUTTON_TO_PNG.bind('<Button-1>', getTXT)
        self.BUTTON_TO_JPG.bind('<Button-1>', convertToCSV)
