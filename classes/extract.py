import io
from tkinter import *
from tkinter import filedialog, messagebox
import fitz
from docx import *
from moviepy.editor import *

class Extraction:
    def __init__(self, mainWindow):
        self.title = 'Менеджер Извлечения'
        self.mainWindow = mainWindow

    def exit(self):
        self.TXT_FROM_PDF.destroy()
        self.MP3_FROM_MP4.destroy()
        self.LABEL_CHOICE.destroy()
        self.BUTTON_EXIT.destroy()
        self.LABEL_NOTE.destroy()
        self.mainWindow.RIGHT_LABEL['text'] = 'Скажите Боту что-то сделать'
        self.mainWindow.RIGHT_LABEL['pady'] = 260
        self.mainWindow.RIGHT_LABEL['font'] = (self.font, 16, 'bold')
        self.mainWindow.LABEL['text'] = 'Да да?'

    def extract(self, access):
        if access['Менеджер Извлечения'] == True:
            self.font = 'Arial'
            self.mainWindow.RIGHT_LABEL['text'] = self.title
            self.mainWindow.RIGHT_LABEL['pady'] = 20
            self.mainWindow.RIGHT_LABEL['font'] = (self.font, 20, 'bold')

            self.LABEL_CHOICE = Label(self.mainWindow.right_part, text = 'Что вы хотите извлечь?', font = (self.font, 15, 'bold'), bg='white', fg='#0e131a', pady=20)
            self.TXT_FROM_PDF = Button(self.mainWindow.right_part,  cursor='hand2',text = 'Текст из PDF', width = 20, height = 2, highlightbackground='#0077ff', fg='#0c3b70', font=(self.font, 14))
            self.MP3_FROM_MP4 = Button(self.mainWindow.right_part, cursor='hand2', text = 'Звук из видео', width = 20, height = 2, highlightbackground='#0077ff', fg='#0c3b70', font=(self.font, 14))
            self.BUTTON_EXIT = Button(self.mainWindow.right_part, cursor='hand2', text='Выход', font=('Trebuchet MS', 14), highlightbackground='#3b6ecc', highlightthickness=30, fg='white')
            self.LABEL_NOTE = Label(self.mainWindow.right_part, text = '', font = (self.font, 14), bg='white', fg='#8ea2d4', pady=20)
            self.LABEL_CHOICE.pack()
            self.TXT_FROM_PDF.pack()
            self.MP3_FROM_MP4.pack()
            self.BUTTON_EXIT.place(x= 230, y=500, width = 90, height = 40)

            self.TXT_FROM_PDF['command'] = self.TXTfromPDF
            self.MP3_FROM_MP4['command'] = self.MP3fromMP4
            self.BUTTON_EXIT['command'] = self.exit

            return 'Извлечение...'
        else:
            return 'К сожалению, администратор запретил\nдоступ к этому Менеджеру.\nЧтобы получить доступ\nтребуется купить эту функцию.'

    def TXTfromPDF(self):
        def getPDF():
            self.files_paths = filedialog.askopenfilenames()

        def extractTXT():
            if self.files_paths:
                for path in self.files_paths:
                    try:
                        docPDF = fitz.open(path)
                        docDOCX = Document()
                        export_path = filedialog.asksaveasfilename(defaultextension='.docx')
                        if export_path:
                            for page in range(docPDF.pageCount):
                                tempPage = docPDF.loadPage(page)
                                pageText = tempPage.getText('text')
                                docDOCX.add_paragraph(pageText)
                            docDOCX.save(export_path)
                            self.LABEL_NOTE['text'] = 'Готово!'
                        else:
                            messagebox.showerror('Ошибка', 'Введите имя файла')
                    except:
                        messagebox.showerror('Ошибка', 'Неверный формат файла!')
            else:
                messagebox.showerror('Ошибка', 'Не выбрано ни одного файла!')
            self.files_paths = None


        self.LABEL_NOTE['text'] = 'Извлеченный текст из PDF-файла будет помещен в файл DOCX.\nТекст может быть немного видоизменен,\nэто зависит от качества PDF-файла\nи дополнительных настроек Microsoft Word.'
        self.LABEL_NOTE.pack()
        self.LABEL_CHOICE['text'] = 'Текст из PDF'
        self.TXT_FROM_PDF['text'] = 'Выбрать PDF'
        self.MP3_FROM_MP4['text'] = 'Извлечь текст'
        self.TXT_FROM_PDF['command'] = getPDF
        self.MP3_FROM_MP4['command'] = extractTXT

    def MP3fromMP4(self):
        def getVideo():
            self.files_paths = filedialog.askopenfilenames()

        def convertToMP3():
            if self.files_paths:
                for path in self.files_paths:
                    try:
                        video = VideoFileClip(path)
                        export_file = filedialog.asksaveasfilename(defaultextension='.mp3')
                        if export_file:
                            video.audio.write_audiofile(export_file)
                            self.LABEL_NOTE['text'] = 'Готово!'
                        else:
                            messagebox.showerror('Ошибка', 'Введите имя файла')
                    except:
                        messagebox.showerror('Ошибка', 'Неверный формат файла!')
            else:
                messagebox.showerror('Ошибка', 'Не выбрано ни одного файла!')
            self.files_paths = None


        self.LABEL_NOTE['text'] = 'Для извлечения звука из видео,\nВы можете выбрать всевозможные видео-форматы.\nЧем больше весит\длится видео - тем дольше будет извлечение.'
        self.LABEL_NOTE.pack()
        self.LABEL_CHOICE['text'] = 'Звук из видео'
        self.TXT_FROM_PDF['text'] = 'Выбрать видео'
        self.MP3_FROM_MP4['text'] = 'Извлечь MP3'

        self.TXT_FROM_PDF['command'] = getVideo
        self.MP3_FROM_MP4['command'] = convertToMP3
