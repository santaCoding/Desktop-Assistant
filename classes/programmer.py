from tkinter import *
from functools import partial
from PIL import ImageTk
from tkinter import messagebox
import webbrowser

class ProgrammingManager:
    def __init__(self, mainWindow):
        self.title = 'Менеджер Программирования'
        self.recourses = ProgrammingRecourses(self, mainWindow)
        self.logos = {'Python' : ImageTk.PhotoImage(file='img/Python.png'),
        'PHP' : ImageTk.PhotoImage(file='img/PHP.png'),
        'Cpp' : ImageTk.PhotoImage(file='img/Cpp.png'),
        'Java' : ImageTk.PhotoImage(file='img/Java.png'),
        'JavaScript' : ImageTk.PhotoImage(file='img/JavaScript.png'),
        'Csh' : ImageTk.PhotoImage(file='img/Csh.png')
        }

    # добавление в список
    def add(self, mainWindow, name_lang, user, db, event):
        user.languages.append(name_lang)
        db.setValue(user.nickname, user.languages, 'languages')
        self.ADD_LANG1.destroy()
        self.ADD_LANG2.destroy()
        messagebox.showinfo('Добавление языка', f'Язык программирования {name_lang} добавлен в Ваш набор!')
        self.checkExistence(mainWindow, name_lang, user, db)

    # удаление из списка
    def delete(self, mainWindow, name_lang, user, db, event):
        index = user.languages.index(name_lang)
        user.languages.pop(index)
        db.setValue(user.nickname, user.languages, 'languages')
        self.DELETE_LANG.destroy()
        messagebox.showinfo('Удаление языка', f'Язык программирования {name_lang} удален из Вашего набора!')
        self.checkExistence(mainWindow, name_lang, user, db)

    # проверка на существование в списке
    def checkExistence(self, mainWindow, name_lang, user, db):
        if name_lang not in user.languages:
            self.ADD_LANG1 = Label(mainWindow.right_part, bg='#177a63', cursor='hand2')
            self.ADD_LANG2 = Label(mainWindow.right_part, bg='#177a63', cursor='hand2')
            self.ADD_LANG1.bind('<Button-1>', partial(self.add, mainWindow, name_lang, user, db))
            self.ADD_LANG2.bind('<Button-1>', partial(self.add, mainWindow, name_lang, user, db))
            self.ADD_LANG1.place(x=343, y=51, width=5, height=15)
            self.ADD_LANG2.place(x=338, y=56, width=15, height=5)
        else:
            self.DELETE_LANG = Label(mainWindow.right_part, bg='#822f2f', cursor='hand2')
            self.DELETE_LANG.bind('<Button-1>', partial(self.delete, mainWindow, name_lang, user, db))
            self.DELETE_LANG.place(x=338, y=56, width=15, height=5)

    # общая для всех функция (рутина)
    def routine(self, mainWindow, name_lang, user, db):
        self.PROMPT['text'] = 'Выберите категорию применения языка'
        self.PROMPT.pack()
        mainWindow.RIGHT_LABEL['font'] = ('Arial', 25, 'bold')
        mainWindow.RIGHT_LABEL['fg'] = '#3573a6'
        try:
            self.FRAME.destroy()
        except:
            pass
        try:
            self.FRAME_USER_LANG.destroy()
            self.TITLE.destroy()
        except:
            pass
        self.FRAME = Frame(mainWindow.right_part)
        self.FRAME.pack()
        self.checkExistence(mainWindow, name_lang, user, db)

    def Python(self, mainWindow, name_lang, user, db, event):
        self.routine(mainWindow, name_lang, user, db)
        mainWindow.RIGHT_LABEL['text'] = 'Python'
        WEB_LBL = Label(self.FRAME, text = 'WEB-разработка', font=('Arial', 17), fg='#3573a6', cursor='hand2', bg='#cfd3ff')
        ML_LBL = Label(self.FRAME, text = 'Machine Learning', font=('Arial', 17), fg='#3573a6', cursor='hand2', bg='#cfd3ff')
        AP_LBL = Label(self.FRAME, text = 'Автоматизация процессов', font=('Arial', 17), fg='#3573a6', cursor='hand2', bg='#cfd3ff')
        WEB_LBL.bind('<Button-1>', partial(self.recourses.WEBPython, mainWindow))
        ML_LBL.bind('<Button-1>', partial(self.recourses.MLPython, mainWindow))
        AP_LBL.bind('<Button-1>', partial(self.recourses.APPython, mainWindow))
        WEB_LBL.pack(pady=10)
        ML_LBL.pack(pady=10)
        AP_LBL.pack(pady=10)

    def PHP(self, mainWindow, name_lang, user, db, event):
        mainWindow.RIGHT_LABEL['text'] = 'PHP'
        self.routine(mainWindow, name_lang, user, db)
        BACKEND = Label(self.FRAME, text = 'BackEnd разработка', font=('Arial', 17), fg='#3573a6', cursor='hand2', bg='#cfd3ff')
        BACKEND.bind('<Button-1>', partial(self.recourses.PHP, mainWindow))
        BACKEND.pack(pady=40)
        
    def Csh(self, mainWindow, name_lang, user, db, event):
        mainWindow.RIGHT_LABEL['text'] = 'C#'
        self.routine(mainWindow, name_lang, user, db)
        DOT_NET = Label(self.FRAME, text='.NET', font=('Arial', 17), fg='#3573a6', cursor='hand2', bg='#cfd3ff')
        DOT_NET.bind('<Button-1>', partial(self.recourses.Csh, mainWindow))
        DOT_NET.pack(pady=40)

    def Java(self, mainWindow, name_lang, user, db, event):
        mainWindow.RIGHT_LABEL['text'] = 'Java'
        self.routine(mainWindow, name_lang, user, db)
        ANDROID = Label(self.FRAME, text='Android', font=('Arial', 17), fg='#3573a6', cursor='hand2', bg='#cfd3ff')
        BACKEND = Label(self.FRAME, text='BackEnd-разработка', font=('Arial', 17), fg='#3573a6', cursor='hand2', bg='#cfd3ff')
        ANDROID.bind('<Button-1>', partial(self.recourses.JavaAndroid, mainWindow))
        BACKEND.bind('<Button-1>', partial(self.recourses.JavaBack, mainWindow))
        ANDROID.pack(pady=10)
        BACKEND.pack(pady=10)

    def JavaScript(self, mainWindow, name_lang, user, db, event):
        mainWindow.RIGHT_LABEL['text'] = 'JavaScript'
        self.routine(mainWindow, name_lang, user, db)
        FRONT = Label(self.FRAME, text='FrontEnd-разработка', font=('Arial', 17), fg='#3573a6', cursor='hand2', bg='#cfd3ff')
        DESKTOP = Label(self.FRAME, text='Desktop', font=('Arial', 17), fg='#3573a6', cursor='hand2', bg='#cfd3ff')
        FRONT.bind('<Button-1>', partial(self.recourses.JSFront, mainWindow))
        DESKTOP.bind('<Button-1>', partial(self.recourses.JSDesktop, mainWindow))
        FRONT.pack(pady=10)
        DESKTOP.pack(pady=10)

    def Cpp(self, mainWindow, name_lang, user, db, event):
        mainWindow.RIGHT_LABEL['text'] = 'C++'
        self.routine(mainWindow, name_lang, user, db)
        GAME = Label(self.FRAME, text='GameDev', font=('Arial', 17), fg='#3573a6', cursor='hand2', bg='#cfd3ff')
        GAME.bind('<Button-1>', partial(self.recourses.CppGame, mainWindow))
        GAME.pack(pady=10)

    def exit(self, mainWindow, event):
        self.FRAME.destroy()
        self.BUTTON_EXIT.destroy()
        self.PROMPT.destroy()
        mainWindow.RIGHT_LABEL['text'] = 'Скажите Боту что-то сделать'
        mainWindow.RIGHT_LABEL['pady'] = 260
        mainWindow.RIGHT_LABEL['font'] = ('Arial', 16, 'bold')
        mainWindow.RIGHT_LABEL['fg'] = '#7e92ab'
        try:
            self.FRAME_USER_LANG.destroy()
            self.TITLE.destroy()
        except:
            pass
        try:
            self.ADD_LANG1.destroy()
            self.ADD_LANG2.destroy()
        except:
            pass
        try:
            self.DELETE_LANG.destroy()
        except:
            pass

        try:
            self.recourses.FRAME1.destroy()
            self.recourses.FRAME2.destroy()
        except:
            pass
        try:
            self.recourses.TEXT.destroy()
        except:
            pass
        try:
            self.recourses.PROMPT_BOOKS.destroy()
            self.recourses.booksLbl.destroy()
            self.recourses.LINKS.destroy()
            self.recourses.PROMPT_LINKS.destroy()
        except:
            pass
    
    # основная функция
    def showContent(self, access:dict, mainWindow, user, db):
        def selectLangs(event):
            try:
                self.TITLE.destroy()
                self.FRAME_USER_LANG.destroy()
            except:
                pass
            self.PROMPT.pack(pady=7)
            self.FRAME = Frame(mainWindow.right_part)
            self.FRAME.pack(pady=40)
            iteration = 0
            for lang in list(self.logos.keys()):
                if iteration % 2 == 0:
                    self.labels_frame = Frame(self.FRAME)
                    self.labels_frame.pack(pady=10)
                lang_label = Label(self.labels_frame, image=self.logos[lang], cursor='hand2')
                lang_label.bind('<Button-1>', partial(eval(f'self.{lang}'), mainWindow, lang, user, db))
                lang_label.pack(side=LEFT, padx=60)
                iteration += 1 

        if access['mp'] == True:
            mainWindow.RIGHT_LABEL['text'] = self.title
            mainWindow.RIGHT_LABEL['pady'] = 30
            self.BUTTON_EXIT = Button(mainWindow.right_part, cursor='hand2', text='Выход', font=('Trebuchet MS', 14, 'bold'), highlightbackground='#3b6ecc', highlightthickness=30, fg='white')
            self.BUTTON_EXIT.bind('<Button-1>', partial(self.exit, mainWindow))
            self.BUTTON_EXIT.place(x= 230, y=500, width = 90, height = 40)
            self.PROMPT = Label(mainWindow.right_part, text='Выберите язык программирования', font=('Arial', 14), fg='grey')
            if not user.languages:
                selectLangs(None)
                return self.title
            else:
                self.TITLE = Label(mainWindow.right_part, text='Выбранные языки программирования:', font=('Arial', 15, 'bold'), fg='#223e63')
                self.TITLE.pack()
                self.FRAME_USER_LANG = Frame(mainWindow.right_part)
                self.FRAME_USER_LANG.pack()
                for lang in user.languages:
                    langLbl = Label(self.FRAME_USER_LANG, text=lang, bg='#2d5487', fg='white', font=('Arial', 14, 'bold'), cursor='hand2')
                    langLbl.bind('<Button-1>', partial(eval(f'self.{lang}'), mainWindow, lang, user, db))
                    langLbl.pack(pady=10)
                
                self.EXTRA = Label(self.FRAME_USER_LANG, text='Просмотреть каталог языков программирования', font=('Arial', 13), fg='#034ba8', cursor='hand2')
                self.EXTRA.bind('<Button-1>', selectLangs)
                self.EXTRA.pack(pady=10)
                return self.title
        else:
            return 'К сожалению, администратор запретил\nдоступ к этому Менеджеру.\nЧтобы получить доступ\nтребуется купить эту функцию.'


class ProgrammingRecourses:
    def __init__(self, manager, mainWindow):
        self.manager = manager
        self.books = {
            'WEBPython' : ['Django: практика создания Web-сайтов на Python (2018)', 'Владимир Дронов: Django. Практика создания веб-сайтов на Python', 'Разработка веб-приложений с использованием Flask на языке Python'],
            'MLPython' : ['Python и машинное обучение', 'Гудфеллоу Я., Бенджио И., Курвилль А. − Глубокое обучение, 2017 г.', 'Орельен Жерон − Прикладное машинное обучение, 2018 г.', 'Адриан Роузброк − Deep Learning for Computer Vision with Python, 2017 г.'],
            'APPython' : ['Автоматизация рутинных задач с помощью Python - Эл Свейгарт'],
            'PHP' : ['Изучаем PHP и MySQL (Линн Бейли)', 'PHP. Объекты, шаблоны и методики программирования (Мэт Зандстра)', 'Самоучитель PHP 7 – Игорь Симдянов', 'Изучаем PHP 7 – Дэвид Скляр'],
            'Csh' : ['C# для профессионалов - Джон Скит', 'Изучаем C#', 'C# 7.0. Карманный справочник', 'Microsoft Visual C#. Подробное руководство'],
            'JavaAndroid' : ['«Философия Java», Брюс Эккель', '«Java 8. Руководство для начинающих», Герберт Шилдт', 'Hello, Android', 'Android. Сборник рецептов'],
            'JavaBack' : ['Изучаем Java EE 7', 'EJB 3 в действии'],
            'JSFront' : ['Илья Кантор «Современный учебник JavaScript»', 'Флэнаган Дэвид «JavaScript. Подробное руководство»', 'Кайл Симпсон «Вы не знаете JS»', 'Нік Морган «JavaScript для дітей. Веселий вступ до програмування»'],
            'JSDesktop' : ['Фримен, Робсон – Изучаем программирование на JavaScript', 'Минник, Холланд – JavaScript для чайников', 'Д. Крокфорд – Как устроен JavaScript'],
            'CppGame' : ['Язык программирования С++. Лекции и упражнения', '3D-ландшафты в реальном времени на С++ и DirectX 9', 'C/C++ в задачах и примерах']
        }
        self.links = {
            'WEBPython' : ['https://habr.com/ru/post/346306/', 'https://python-scripts.com/flask-or-django', 'https://developer.mozilla.org/ru/docs/Learn/Server-side/Django'],
            'MLPython' : ['https://habr.com/ru/post/319288/', 'https://tproger.ru/experts/how-to-learn-machine-learning/', 'https://netology.ru/blog/2019-01-machine-learning-python'],
            'APPython' : ['https://habr.com/ru/company/huawei/blog/314008/', 'https://python-scripts.com/web-automation-with-python-and-selenium'],
            'PHP' : ['https://www.php.net/manual/ru/intro-whatis.php', 'https://web-creator.ru/articles/php', 'https://skillbox.ru/media/code/5_zabluzhdeniy_o_razrabotke_na_php/'],
            'Csh' : ['https://levelup.ua/gde-v-sovremennom-mire-primenyaetsya-c', 'https://metanit.com/sharp/tutorial/1.1.php', 'https://professorweb.ru/my/csharp/charp_theory/level1/infonet.php'],
            'JavaAndroid' : ['https://javarush.ru/groups/posts/1079-gde-ispoljhzuetsja-java', 'https://habr.com/ru/post/335332/', 'https://apptractor.ru/learn/plan-izucheniya-android-razrabotki-dlya-nachinayushhih.html'],
            'JavaBack' : ['https://tproger.ru/translations/building-a-web-app-with-java-servlets/', 'https://webformyself.com/primenenie-java-dlya-veb-razrabotki/', 'https://javarush.ru/groups/posts/2125-veb-prilozhenie-na-java'],
            'JSFront' : ['https://tproger.ru/curriculum/intro-to-frontend-development/', 'https://itvdn.com/ru/specialities/frontend-developer', 'https://klondike-studio.ru/wiki/front-end/'],
            'JSDesktop' : ['https://habr.com/ru/post/272389/', 'https://medium.com/web-standards/desktop-app-5b9f008966cd', 'https://tproger.ru/translations/desktop-js-app-with-electron/'],
            'CppGame' : ['https://dou.ua/lenta/articles/gamedev-for-beginners/', 'https://proglib.io/p/gamedev-beginning/', 'https://proglib.io/p/gamedev-learning/']
        }
    def callLink(self, link, event):
        webbrowser.open_new_tab(link)

    def routine(self, mainWindow):
        try:
            self.manager.ADD_LANG1.destroy()
            self.manager.ADD_LANG2.destroy()
        except:
            pass
        try:
            self.manager.DELETE_LANG.destroy()
        except:
            pass
        self.manager.FRAME.destroy()
        self.manager.PROMPT.destroy()
        self.FRAME1 = Frame(mainWindow.right_part)
        self.FRAME1.pack()
        self.FRAME2 = Frame(mainWindow.right_part)
        self.FRAME2.pack()
        self.PROMPT_BOOKS = Label(mainWindow.right_part, text='Полезные книги:', font=('Arial', 16, 'bold'), fg='#1c3a61')
        self.PROMPT_LINKS = Label(mainWindow.right_part, text='Полезные ссылки:', font=('Arial', 16, 'bold'), fg='#1c3a61')
        self.LINKS = Frame(mainWindow.right_part)
        self.TEXT = Label(self.FRAME2, text='', font=('Arial', 16), fg='#33465e', justify=LEFT, anchor=W)
        self.manager.BUTTON_EXIT.place(x=30, y=30, width = 90, height = 40)

    def showContent(self, category, mainWindow):
        self.PROMPT_BOOKS.pack(pady=5)
        books = ''
        item=1
        for book in self.books[category]:
            books += str(item) + '. ' + book
            if self.books[category].index(book) != len(self.books[category]) - 1:
                books += '\n\n'
            item+=1
        self.booksLbl = Label(mainWindow.right_part, text=books, fg='#262626', font=('Arial', 13), justify=LEFT, anchor=W)
        self.booksLbl.pack()
        item=1
        links = ''
        self.PROMPT_LINKS.pack(pady=5)
        self.LINKS.pack()
        for link in self.links[category]:
            linksLbl = Label(self.LINKS, text=str(item) + '. ' + link, fg='#266cc7', font=('Arial', 13), justify=LEFT, anchor=W, cursor='hand2')
            linksLbl.bind('<Button-1>', partial(self.callLink, link))
            linksLbl.pack()
            item += 1

    def CppGame(self, mainWindow, event):
        self.routine(mainWindow)
        mainWindow.RIGHT_LABEL['text'] = 'Разработка игр'
        self.game = ImageTk.PhotoImage(file='img/Game.jpg')
        gameImg = Label(self.FRAME2, image=self.game)
        gameImg.pack()
        self.TEXT['text'] = 'Язык C++ предоставляет практически неограниченные\nвозможности для создания различных проектов:\nначиная от консольных программ и заканчивая полноценными\n3D играми с графикой, анимацией и динамикой.'
        self.TEXT.pack()
        self.showContent('CppGame', mainWindow)

    def JSDesktop(self, mainWindow, event):
        self.routine(mainWindow)
        mainWindow.RIGHT_LABEL['text'] = 'Desktop-разработка'
        self.TEXT['text'] = 'Ни для кого не секрет, что в наше время\nJavaScript стал одним из самых популярных\nязыков программирования. В далекие 90е годы,\nв момент зарождения языка, когда он был создан с\nединственной целью добавить интерактивность веб страницам\nи улучшить процесс взаимодействия с пользователем, кто\nбы мог подумать, что он достигнет столь небывалых высот.\nВедь сейчас на нем можно делать практически все что угодно.\nХотите написать сайт: и бэкэнд и фронтэнд на JavaScript?\nпожалуйста! Хотите написать мобильное приложение\nна JavaScript? нет проблем. Программируете микроконтроллер –\nи тут вам на помощь придет JavaScript.'
        self.TEXT.pack()
        self.showContent('JSDesktop', mainWindow)

    def JSFront(self, mainWindow, event):
        self.routine(mainWindow)
        mainWindow.RIGHT_LABEL['text'] = 'FrontEnd-разработка'
        self.react = ImageTk.PhotoImage(file='img/React.jpg')
        self.node = ImageTk.PhotoImage(file='img/Node.jpg')
        self.angular = ImageTk.PhotoImage(file='img/Angular.jpg')
        self.jquery = ImageTk.PhotoImage(file='img/jQuery.jpg')
        reactImg = Label(self.FRAME1, image=self.react)
        nodeImg = Label(self.FRAME1, image=self.node)
        angularImg = Label(self.FRAME1, image=self.angular)
        jqueryImg = Label(self.FRAME1, image=self.jquery)
        reactImg.pack(side=LEFT, padx=5)
        nodeImg.pack(side=LEFT, padx=5)
        angularImg.pack(side=LEFT, padx=5)
        jqueryImg.pack(side=LEFT, padx=5)
        self.TEXT['text'] = 'Изменения во фронтенде и веб-разработке\nпроисходят невероятно быстро. Сегодня, если вы\nне мастер Webpack, React Hooks, Jest, Vue и NG, вы,\nвероятно, чувствуете разделяющую вас от топовых\nпрофессионалов пропасть, которая продолжает расширяться.\nНо всё меняется.'
        self.TEXT.pack()
        self.showContent('JSFront', mainWindow)

    def JavaBack(self, mainWindow, event):
        self.routine(mainWindow)
        mainWindow.RIGHT_LABEL['text'] = 'BackEnd-разработка'
        self.TEXT['text'] = 'Одной из самых приятных особенностей Java\nявляется её многогранная природа. Конечно, создание\nтрадиционных десктопных и даже мобильных приложений — это здорово.\nНо что, если вы хотите уйти с проторенных дорожек\nи зайти на территорию разработки web приложений на Java?\nДля вас есть хорошая новость: в комплекте с языком идёт\nполноценный Servlet API, который позволяет вам\nсоздавать надёжные веб-приложения без особых хлопот.'
        self.TEXT.pack()
        self.showContent('JavaBack', mainWindow)
    
    def JavaAndroid(self, mainWindow, event):
        self.routine(mainWindow)
        mainWindow.RIGHT_LABEL['text'] = 'Android-разработка'
        self.andr = ImageTk.PhotoImage(file='img/Android.jpg')
        andrImg = Label(self.FRAME1, image=self.andr)
        andrImg.pack()
        self.TEXT['text'] = 'Среди программистов на Java то и дело слышны разговоры\nо разработке под Android. Именно Android держит\nJava на первом плане в последние несколько лет. Насколько\nже важно понимать или знать Android для разработчиков на\nJava? Ну, зависит от того, нравится ли вам разработка\nприложений и хотите ли вы, чтобы вашими приложениями\nпользовалось множество\nлюдей. Если да, то Android даст вам эту возможность.'
        self.TEXT.pack()
        self.showContent('JavaAndroid', mainWindow)

    def Csh(self, mainWindow, event):
        self.routine(mainWindow)
        mainWindow.RIGHT_LABEL['text'] = '.NET'
        self.dotNet = ImageTk.PhotoImage(file='img/dotNet.jpg')
        dotNetImg = Label(self.FRAME1, image=self.dotNet)
        dotNetImg.pack()
        self.TEXT['text'] = 'Среда .NET Framework и язык C# базируются на принципах\nобъектно-ориентированного программирования.\nКомпоненты ADO.NET предоставляют доступ к реляционным\nбазам данных и другим источникам данных, файловой\nсистеме и каталогам. Повышенная безопасность и высокая\nстепень контроля за использованием сборок\nнравится разработчикам.'
        self.TEXT.pack()
        self.showContent('Csh', mainWindow)

    def PHP(self, mainWindow, event):
        self.routine(mainWindow)
        mainWindow.RIGHT_LABEL['text'] = 'BackEnd - разработка'
        self.TEXT['text'] = 'Статические сайты, как правило, используются на сайтах\nвизитках либо для документации. Для чего-то более серьезного\nуже нужен динамический сайт. Что его характеризует?\nДанные отделены от логики работы сайта и\nнаходятся в хранилище. Например, если на сайте есть\nраздел со статьями, то для вывода статьи существует\nровно один обработчик (код, который отвечает за этот вывод),\nа данные при этом зависят от ссылки,\nпо которой открыта статья. То есть в динамических сайтах однотипные\nстраницы генерируются из одного места с подстановкой\nразных данных. В случае статического сайта, каждая ссылка была\nбы представлена физическим файлом с вбитым в него контентом.'
        self.TEXT.pack()
        self.showContent('PHP', mainWindow)

    def APPython(self, mainWindow, event):
        self.routine(mainWindow)
        mainWindow.RIGHT_LABEL['text'] = 'Автоматизация процессов'
        self.TEXT['text'] = 'Автоматизация процессов стала полноценным «трендом»\nнашего времени и продолжает расширять свое влияние\nпрактически во всех сферах деятельности:\nначиная с сельского хозяйства и заканчивая «умными домами»\nили искусственным интеллектом.'
        self.TEXT.pack()
        self.showContent('APPython', mainWindow)

    def MLPython(self, mainWindow, event):
        self.routine(mainWindow)
        mainWindow.RIGHT_LABEL['text'] = 'Машинное обучение'
        self.TEXT['text'] = 'По сути, машинное обучение — это технология,\nкоторая помогает приложениям на основе искусственного интеллекта\nобучаться и выдавать результаты автоматически,\nбез человеческого вмешательства.\nPython лучше всего подходит для выполнения таких задач,\nпотому что он довольно понятный по сравнению с другими языками.'
        self.TEXT.pack()
        self.ml = ImageTk.PhotoImage(file='img/ML.jpg')
        mlLogo = Label(self.FRAME1, image=self.ml)
        mlLogo.pack()
        self.showContent('MLPython', mainWindow)

    def WEBPython(self, mainWindow, event):
        self.routine(mainWindow)
        self.TEXT['text'] = 'Согласно данным опроса разработчиков Python в 2019,\nDjango и Flask являются самыми популярными веб фреймворками\nсреди разработчиков.\nВы вряд ли ошибетесь, выбрав один из этих фреймворков\nдля работы с вашим новым веб приложением.\nХотя выбор того, какой из них будет лучше работать для вас\nи ваших целей, есть ряд явных отличий, которые нужно иметь в виду,\nперед тем как сделать выбор.'
        self.TEXT.pack()
        self.django = ImageTk.PhotoImage(file='img/Django.png')
        self.flask = ImageTk.PhotoImage(file='img/Flask.jpg')
        mainWindow.RIGHT_LABEL['text'] = 'WEB-Python'
        djangoLogo = Label(self.FRAME1, image=self.django)
        flaskLogo = Label(self.FRAME1, image=self.flask)
        djangoLogo.pack(side=LEFT, padx=10)
        flaskLogo.pack(side=LEFT, padx=10)
        self.showContent('WEBPython', mainWindow)