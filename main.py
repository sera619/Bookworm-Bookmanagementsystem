import shutil
import sys, csv, time, webbrowser, traceback, os, datetime, json
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6 import *
from res.ui_mainui import Ui_MainWindow
from res.ui_splashui import Ui_SplashScreen
from data import UserData
from qt_material import apply_stylesheet

base_dir = os.path.dirname(__file__)
version_num = "2.8"
appversiontext = f"Version {version_num} | Copyright S3R43o3 © 2023"

book = {
    "isbn": None,
    "title": None,
    "author": None,
    "genre": None,
    "out-date": None,
    "available": None,
    "lend-knd":""
}

# threading worker class
class Worker(QRunnable):
    def __init__(self, function, *args, **kwargs):
        super(Worker, self).__init__()
        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()
        self.kwargs['progress_callback'] = self.signals.progress

    @Slot()
    def run(self):
        print("Worker thread started...")
        try:
            result = self.function(*self.args, **self.kwargs)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result)
        finally:
            self.signals.finished.emit()

# worker signals
class WorkerSignals(QObject):
    finished = Signal()
    error = Signal(tuple)
    result = Signal(object)
    progress = Signal(int)

class Splash(QWidget):
    def __init__(self):
        super(Splash, self).__init__()
        self.splash = Ui_SplashScreen()
        self.splash.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowTitle(f'Bookworm v{version_num}')
        self.shadow2 = QGraphicsDropShadowEffect()
        self.shadow2.setBlurRadius(40.0)
        self.shadow2.setColor(QColor(255, 0, 0, 90))
        self.shadow1 = QGraphicsDropShadowEffect()
        self.shadow1.setBlurRadius(110.0)
        self.shadow1.setColor(QColor(200,0,0,110))
        self.shadow1.setXOffset(0)
        self.shadow1.setYOffset(0)
        self.shadow2.setXOffset(0)
        self.shadow2.setYOffset(0)
        
        self.splash.iconLabel.setGraphicsEffect(self.shadow1)
        self.splash.headerLabel.setGraphicsEffect(self.shadow2)
        self.splash.loadProgress.setValue(0)
        self.splash.loadProgress.setRange(0, 100)
        self.splash.loadProgress.setTextVisible(False)
        self.splash.loadProgress.valueChanged.connect(lambda: self.update_bartext())
        self.splash.versionLabel.setText(f"Version {version_num}")
        self.timer = QTimer()
        self.progressBar = self.splash.loadProgress
        self.cancelBTN = self.splash.cancelBtn
        self.splash.cancelBtn.clicked.connect(lambda: app.quit())

    def update_bartext(self):
        self.splash.label_2.setText("loading... " + str(self.splash.loadProgress.value()) + "%")
        
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()

        self.ui.setupUi(self)
        apply_stylesheet(app, theme='dark_red.xml')
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowTitle(f'Bookworm {version_num}')
        self.setWindowIcon(QIcon(os.path.join(base_dir, 'appicon.ico')))

        self.userdb = UserData()
        self.splash = Splash()
        self.threadpool = QThreadPool()
        print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())

        def moveWindow(e):
            if self.isMaximized() == False: 
                if e.buttons() == Qt.LeftButton:
                    globalPos = e.globalPos() 
                    self.move(self.pos() + globalPos - self.clickPosition)
                    self.clickPosition = globalPos

        self.world_timer = QTimer()
        self.world_timer.timeout.connect(lambda: self.set_date_text())
        self.world_timer.setInterval(1000)
        self.world_timer.start()

        self.ui.topFrame.mouseMoveEvent = moveWindow
        self.load_book_list()
        self.load_available_list()
        self.load_user_list()
        self.apply_styles()
        self.setup_buttons()
        self.ui.version_label.setText(appversiontext)
        self.ui.stackedWidget.setCurrentWidget(self.ui.homeView)
        
    def set_date_text(self):
        datelabel = self.ui.currentDateLabel
        timelabel = self.ui.currentTimeLabel
        datelabel.setText(datetime.datetime.today().strftime("%d.%m.%Y"))
        timelabel.setText(datetime.datetime.now().strftime("%H:%M:%S"))
    
    # Threadding test
    def progress_fn(self, n):
        #print("%d%% done" % n)
        pass

    def run_splashscreen(self, progress_callback):
        value = 0
        while value < 100:
            value += 1
            self.splash.progressBar.setValue(value)
            progress_callback.emit(value)
            time.sleep(0.05)
        return "Done."
    
    def output_worker(self, s):
        print(s)

    def thread_complete(self):
        self.counter = 0
        self.splash.close()
        self.show()
        self.menuAnim()
        print("Thread finished")

    def start_splash(self):
        worker = Worker(self.run_splashscreen)
        worker.signals.result.connect(self.output_worker)
        worker.signals.finished.connect(self.thread_complete)
        worker.signals.progress.connect(self.progress_fn)

        self.threadpool.start(worker)

    def apply_styles(self):
        self.ui.tableAvaible.horizontalHeader().setStretchLastSection(True)
        self.ui.tableAvaible.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.indexTable.horizontalHeader().setStretchLastSection(True)
        self.ui.indexTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.userTable.horizontalHeader().setStretchLastSection(True)
        self.ui.userTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.userBookTable.horizontalHeader().setStretchLastSection(True)
        self.ui.userBookTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.shadow2 = QGraphicsDropShadowEffect()
        self.shadow2.setBlurRadius(40.0)
        self.shadow2.setColor(QColor(255, 0, 0, 100))
        self.ui.headerLabel.setGraphicsEffect(self.shadow2)
        
        self.shadow3 = QGraphicsDropShadowEffect()
        self.shadow3.setBlurRadius(40.0)
        self.shadow3.setColor(QColor(255, 255, 255, 50))
        self.ui.homeHeaderLabel.setGraphicsEffect(self.shadow3)

        self.shadowapp = QGraphicsDropShadowEffect()
        self.shadowapp.setBlurRadius(70.0)
        self.shadowapp.setXOffset(0)
        self.shadowapp.setYOffset(0)
        self.shadowapp.setColor(QColor(255, 0, 0, 120))
        self.ui.appLogoLabel.setGraphicsEffect(self.shadowapp)
        
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(50.0)
        self.shadow.setXOffset(0)
        self.shadow.setXOffset(0)
        self.shadow.setColor(QColor(255, 92, 157, 550))
        self.ui.centralwidget.setGraphicsEffect(self.shadow)

        self.ui.kndNumLabel.setStyleSheet("color: 'red'; font-weight: 300; font-size: 12pt;")
        self.ui.usernameLabel.setStyleSheet("color: 'red'; font-weight: 300; font-size: 12pt;")
        self.ui.useradressLabel.setStyleSheet("color: 'red'; font-weight: 300; font-size: 12pt;")
        self.ui.usercityLabel.setStyleSheet("color: 'red'; font-weight: 300; font-size: 12pt;")
        self.ui.usermailLabel.setStyleSheet("color: 'red'; font-weight: 300; font-size: 12pt;")
        self.ui.usergbLabel.setStyleSheet("color: 'red'; font-weight: 300; font-size: 12pt;")
        self.ui.userphoneLabel.setStyleSheet("color: 'red'; font-weight: 300; font-size: 12pt;")

    def setup_buttons(self):
        self.ui.lendDayBox.currentTextChanged.connect(lambda: self.set_lenddate_label())
        self.ui.userTable.itemSelectionChanged.connect(lambda: self.show_user_information())
        self.splash.splash.cancelBtn.clicked.connect(lambda: self.splash.splash.close())
        self.ui.x_button.clicked.connect(lambda: self.close())
        self.ui.min_window_btn.clicked.connect(lambda: self.showMinimized())
        self.ui.max_window_btn.clicked.connect(lambda: self.window_handler())

        self.splash.cancelBTN.clicked.connect(lambda: self.close())
        self.ui.menu_btn.clicked.connect(lambda: self.menuAnim())

        self.ui.menu_btn_home.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.homeView))
        self.ui.menu_btn_home.clicked.connect(lambda: self.menuAnim())
        self.ui.menu_btn_index.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.indexView))
        self.ui.menu_btn_index.clicked.connect(lambda: self.menuAnim())
        self.ui.menu_btn_awaylist.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.avaibleView))
        self.ui.menu_btn_awaylist.clicked.connect(lambda: self.menuAnim())
        self.ui.menu_btn_userindex.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.userlistView))
        self.ui.menu_btn_userindex.clicked.connect(lambda: self.menuAnim())
        self.ui.menu_btn_import.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.exportView))
        self.ui.menu_btn_import.clicked.connect(lambda: self.menuAnim())
        self.ui.menu_btn_backup.clicked.connect(lambda: self.backup_data())
        self.ui.menu_btn_backup.clicked.connect(lambda: self.menuAnim())
        self.ui.menu_btn_help.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.helpView))
        self.ui.menu_btn_help.clicked.connect(lambda: self.menuAnim())
        self.ui.menu_btn_help.setEnabled(False)

        self.ui.userBookBackBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.userlistView))
        self.ui.newUserBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.newUserView))
        self.ui.index_btn_add.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.addBookView))
        
        self.ui.clearAddInputBtn.clicked.connect(lambda: self.clear_add_book_input())
        self.ui.index_btn_delete.clicked.connect(lambda: self.delete_book())
        self.ui.addBookBtn.clicked.connect(lambda: self.add_book())
        self.ui.resumeBookBtn.clicked.connect(lambda: self.resume_book())
        self.ui.avaibleBtn.clicked.connect(lambda: self.go_lend_view())
        self.ui.lendBtn.clicked.connect(lambda: self.give_book())
        self.ui.showUserBookBtn.clicked.connect(lambda: self.show_user_books())
        self.ui.deleteUserBtn.clicked.connect(lambda: self.remove_user())
        self.ui.newuserCreateBtn.clicked.connect(lambda: self.new_user())
        self.ui.newuserClearBtn.clicked.connect(lambda: self.clear_newuser_input())

        # Export/Import view
        self.ui.exportBackBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.homeView))
        self.ui.importDataBtn.clicked.connect(lambda: self.import_data_file())
        self.ui.exportDataBtn.clicked.connect(lambda: self.export_data_file())
        self.ui.importSearchFileBtn.clicked.connect(lambda: self.get_import_data())
#        self.ui.loadBackupBtn.clicked.connect(lambda: self.get_backup_data())
        self.ui.loadBackupBtn.setEnabled(False)
        self.ui.socialGitBtn.clicked.connect(lambda: webbrowser.open("https://github.com/sera619"))

    def window_handler(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

    def set_lenddate_label(self):
        days_to_add = int(self.ui.lendDayBox.currentText())
        date = (datetime.datetime.now() + datetime.timedelta(days=days_to_add) ).strftime('%d.%m.%Y')
        self.ui.lendDateLabel.setText(str(date))

    def go_lend_view(self):
        row = self.ui.indexTable.selectedIndexes()
        if len(row) == 0:
            return
        isbn_list = []
        if row:
            rows = set(i.row() for i in row)
        else:
            rows = [self.ui.indexTable.rowCount() -1]
        
        for r in sorted(rows, reverse=True):
            isb = self.ui.indexTable.item(r, 0)
            isbn_list.append(isb.text ())
        

        for book in booklist:
            if book['isbn'] == isbn_list[0]:
                if book['available'] == "No":
                    return print("buch bereits verliehen")
                self.ui.lendTitleInput.setText(book['title'])
        self.set_lenddate_label()
        self.ui.lemdIsbnInput.setText(isbn_list[0])
        self.ui.stackedWidget.setCurrentWidget(self.ui.lendView)

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()
    
    def menuAnim(self):
        width = self.ui.menuFrame.minimumWidth()
        if width == 150:
            new_width = 0
        else:
            new_width = 150
        self.animation = QPropertyAnimation(
            self.ui.menuFrame, b'minimumWidth')
        self.animation.setDuration(250)
        self.animation.setStartValue(width)
        self.animation.setEndValue(new_width)
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()
    
    def fade(self, widget):
        self.effect = QGraphicsOpacityEffect()
        widget.setGraphicsEffect(self.effect)

        self.animation = QPropertyAnimation(self.effect, b"opacity")
        self.animation.setDuration(1000)
        self.animation.setStartValue(1)
        self.animation.setEndValue(0)
        self.animation.start()

    def unfade(self, widget):
        self.effect = QGraphicsOpacityEffect()
        widget.setGraphicsEffect(self.effect)

        self.animation = QPropertyAnimation(self.effect, b"opacity")
        self.animation.setDuration(1000)
        self.animation.setStartValue(0)
        self.animation.setEndValue(1)
        self.animation.start()        
    
    def load_user_list(self):
        self.ui.userTable.clearContents()
        userlist = self.userdb.db.all()
        self.ui.userTable.setRowCount(len(userlist))
        row = 0
        for user in userlist:
            item1 = QTableWidgetItem(user['kndNum'])
            item2 = QTableWidgetItem(user['name'])
            self.ui.userTable.setItem(row, 0, item1)
            self.ui.userTable.setItem(row, 1, item2)
            self.ui.userTable.item(row, 1).setBackground(QColor(255, 255, 255, 255))
            row += 1
    
    def clear_newuser_input(self):
        self.ui.newuserAdressInput.clear()
        self.ui.newuserBirthdayInput.clear()
        self.ui.newuserCityInput.clear()
        self.ui.newuserMailInput.clear()
        self.ui.newuserNameInput.clear()
        self.ui.newuserPhoneInput.clear()

    def new_user(self):
        new_adress = self.ui.newuserAdressInput.text()
        new_birthday = self.ui.newuserBirthdayInput.text()
        new_city =self.ui.newuserCityInput.text()
        new_kndnum = str(self.userdb.generate_kdnNum())
        new_mail = self.ui.newuserMailInput.text()
        new_name = self.ui.newuserNameInput.text()
        new_phone = self.ui.newuserPhoneInput.text()
        if new_mail == "" or new_adress == "" or new_birthday == "" or new_city == "" or new_kndnum == "" or new_name =="" or new_phone == "":
            #print("enter all required fields")
            return
        button = QMessageBox.information(
            self,
            'Neuer Nutzer',
            f'Neuer Nutzer\n"{new_name}"\nwurde erstellt!',
            QMessageBox.StandardButton.Ok
        )
        if button == QMessageBox.StandardButton.Ok:
            self.userdb.add_user(new_kndnum, new_name.capitalize(), new_mail, new_phone, new_city, new_adress, new_birthday, [])
            self.clear_newuser_input()
            self.load_user_list()
            self.ui.stackedWidget.setCurrentWidget(self.ui.userlistView)

    def remove_user(self):
        row = self.ui.userTable.selectedIndexes()

        if len(row) == 0:
            return
        if row:
            rows = set(i.row() for i in row)
        else:
            rows = [self.ui.userTable.rowCount() -1]
        
        for r in rows:
            name = self.ui.userTable.item(r, 1).text()
        
        button = QMessageBox.question(
            self,
            'Nutzer löschen?',
            f'Möchstest du den Benutzer\n"{name}"\nwirklich löschen?',
            QMessageBox.StandardButton.Yes |
            QMessageBox.StandardButton.No
        )
        if button == QMessageBox.StandardButton.Yes:
            self.userdb.remove_user(name)
            self.clear_userinformation()
            self.load_user_list()
        else:
            return
    
    def clear_userinformation(self):
        self.ui.kndNumLabel.clear()
        self.ui.usernameLabel.clear()
        self.ui.useradressLabel.clear()
        self.ui.usercityLabel.clear()
        self.ui.usermailLabel.clear()
        self.ui.usergbLabel.clear()
        self.ui.userphoneLabel.clear()

    def show_user_information(self):
        if not self.ui.userTable.selectedIndexes():
            self.clear_userinformation()
            return
        row = self.ui.userTable.selectedIndexes()
        #print(row)
        if row:

            rows = set(i.row() for i in row)
        else:
            rows = [self.ui.indexTable.rowCount() -1]

        name = ""
        for r in rows:
            name = self.ui.userTable.item(r, 1).text()
            #print(name)
        if name != "":
            userinfo = self.userdb.get_userinfo(name)
            #print(userinfo)
            self.ui.kndNumLabel.setText(userinfo['kndNum'])
            self.ui.usernameLabel.setText(userinfo['name'])
            self.ui.useradressLabel.setText(userinfo['address'])
            self.ui.usercityLabel.setText(userinfo['city'])
            self.ui.usermailLabel.setText(userinfo['mail'])
            self.ui.usergbLabel.setText(userinfo['birthday'])
            self.ui.userphoneLabel.setText(userinfo['phone'])

    def load_book_list(self):
        row = 0
        new_list = []
        self.ui.indexTable.clearContents()
        for book in booklist:
            new_list.append(book)
        self.ui.indexTable.setRowCount(len(new_list))
        for b in new_list:
            self.ui.indexTable.setItem(row, 0, QTableWidgetItem(b['isbn']))
            self.ui.indexTable.setItem(row, 1, QTableWidgetItem(b['title']))
            self.ui.indexTable.setItem(row, 2, QTableWidgetItem(b['author']))
            self.ui.indexTable.setItem(row, 3, QTableWidgetItem(b['genre']))
            self.ui.indexTable.setItem(row, 4, QTableWidgetItem(b['back_date']))
            check_icon = QIcon()
            check_icon.addFile(u":/icons/icons/tick.png", QSize(), QIcon.Normal, QIcon.Off)
            x_icon = QIcon()
            x_icon.addFile(u":/icons/icons/cross.png", QSize(), QIcon.Normal, QIcon.Off)
            item = QTableWidgetItem()
            if b['available'] == "Yes":
                item.setIcon(check_icon)
            else:
                item.setIcon(x_icon)
            self.ui.indexTable.setItem(row, 5,item)
            row += 1
    
    def load_available_list(self):
        row = 0
        new_list = []
        self.ui.tableAvaible.clearContents()
        for book in booklist:
            if book['available'] == "Yes":
                continue
            new_list.append(book)
        self.ui.tableAvaible.setRowCount(len(new_list))
        for b in new_list:
            self.ui.tableAvaible.setItem(row, 0, QTableWidgetItem(b['isbn']))
            self.ui.tableAvaible.setItem(row, 1, QTableWidgetItem(b['title']))
            self.ui.tableAvaible.setItem(row, 2, QTableWidgetItem(b['author']))
            self.ui.tableAvaible.setItem(row, 3, QTableWidgetItem(b['genre']))
            self.ui.tableAvaible.setItem(row, 4, QTableWidgetItem(b['back_date']))
            x_icon = QIcon()
            x_icon.addFile(u":/icons/icons/cross.png", QSize(), QIcon.Normal, QIcon.Off)
            item = QTableWidgetItem()
            item.setIcon(x_icon)
            self.ui.tableAvaible.setItem(row, 5,item)
            row += 1
    
    def delete_book(self):
        row = self.ui.indexTable.selectedIndexes()
        isbn_list = []
        if row:

            rows = set(i.row() for i in row)
        else:
            rows = [self.ui.indexTable.rowCount() -1]

        if row == None:
            #print("no row to delete selected")
            return
        button = QMessageBox.question(
            self,
            'Bestätigen',
            'Bist du sicher das du dieses Buch löschen möchtest?',
            QMessageBox.StandardButton.Yes |
            QMessageBox.StandardButton.No
        )
        if button == QMessageBox.StandardButton.Yes:
            for r in sorted(rows, reverse=True):
                isb = self.ui.indexTable.item(r, 0)
                isbn_list.append(isb.text())
                #print(isbn_list)
                self.ui.indexTable.removeRow(r)
                #print("delete", r)
            
            for book in booklist:
                for isbn in isbn_list:
                    if book['isbn'] == str(isbn):
                        booklist.remove(book)
                        break 
            #print(booklist)
            save_booklist()
            self.load_book_list()
            self.load_available_list()
        else:
            return

    def resume_book(self):
        row = self.ui.tableAvaible.selectedIndexes()
        isbn_list = []
        if len(row) == 0:
            return
        if row:
            rows = set(i.row() for i in row)
        else:
            rows = [self.ui.tableAvaible.rowCount() -1]
        
        for r in sorted(rows, reverse=True):
            isb = self.ui.tableAvaible.item(r,0)
            isbn_list.append(isb.text())
            self.ui.tableAvaible.removeRow(r)
        
        for book in booklist:
            for isbn in isbn_list:
                if book['isbn'] == isbn and book['available'] == "No":
                    book['available'] = 'Yes'
                    book['out-date'] = ""
                    lender = book['lend_knd']
                    book['lend_knd'] = ""
                    book['back_date'] = ""
                    self.userdb.user_remove_book(lender, isbn)
                    save_booklist()
                    bookname = book['title']
                    self.load_available_list()
                    self.load_book_list()
                    button = QMessageBox.information(
                        self,
                        'Erfolg',
                        f'Buch\n\"{bookname}\"\nvon\n\"{self.userdb.get_user_name(lender)}\"\nzurück bekommen!',
                        QMessageBox.StandardButton.Ok
                    )
                    if button == QMessageBox.StandardButton.Ok:
                        self.ui.stackedWidget.setCurrentWidget(self.ui.avaibleView)

    def give_book(self):
        row = self.ui.indexTable.selectedIndexes()
        kdn = self.ui.lendKdnInput.text()
        days = int(self.ui.lendDayBox.currentText())
        if not kdn or not days:
            return print("kdn feld leer")

        isbn_list = []
        if row:
            rows = set(i.row() for i in row)
        else:
            rows = [self.ui.indexTable.rowCount() -1]
        
        for r in sorted(rows, reverse=True):
            isb = self.ui.indexTable.item(r, 0)
            isbn_list.append(isb.text())
        
        for book in booklist:
            for isbn in isbn_list:
                if book['isbn'] == isbn and book['available'] == "Yes":
                    date = (datetime.datetime.now() + datetime.timedelta(days=days)).strftime('%d.%m.%Y')
                    book['out-date'] = datetime.date.today().strftime("%d.%m.%Y")
                    book['available'] = "No"
                    book['lend_knd'] = kdn
                    book['back_date'] =str(date)
                    self.userdb.user_add_book(kdn, isbn_list[0])
                    save_booklist()
                    self.load_available_list()
                    self.load_book_list()
                    bookname = book['title']
                    button = QMessageBox.information(
                        self,
                        'Erfolg',
                        f'Das Buch:\n\"{bookname}\"\nwurde an\n\"{self.userdb.get_user_name(kdn)}\"\nverliehen!',
                        QMessageBox.StandardButton.Ok
                    )
                    if button == QMessageBox.StandardButton.Ok:
                        self.clear_lend_input()
                        self.ui.stackedWidget.setCurrentWidget(self.ui.indexView)

    def clear_lend_input(self):
        self.ui.lendDateLabel.clear()
        self.ui.lendTitleInput.clear()
        self.ui.lemdIsbnInput.clear()
        self.ui.lendKdnInput.clear()

    def add_book(self):
        author = self.ui.addAuthorInput.text()
        genre = self.ui.addGenreInput.text()
        isbn = self.ui.addisbnInput.text()
        outdate = self.ui.addOutdateInput.text()
        title = self.ui.addTitleInput.text()
        if title == "" or author == "" or genre == "" or isbn == "":
            #print("add all required fields: author, genre, isbn, title")
            return
        new_book = {
            "isbn": isbn,
            "title": title,
            "author": author,
            "genre": genre,
            "out-date":outdate,
            "available": "Yes",
            "lend_knd":"",
            "back_date":""
        }
        #print("Buch hinzugefügt: " + title)
        booklist.append(new_book)
        self.clear_add_book_input()
        self.load_book_list()
        save_booklist()
        button = QMessageBox.information(
            self,
            'Erfolg',
            f'Neuer Eintrag: "{title}" wurde erstellt!',
            QMessageBox.StandardButton.Ok
        )
        if button == QMessageBox.StandardButton.Ok:
            self.ui.stackedWidget.setCurrentWidget(self.ui.indexView)
    
    # user booklist frame
    def show_user_books(self):
        if len(self.ui.userTable.selectedItems()) == 0:
            return
        kndNum = self.ui.kndNumLabel.text()
        username = self.ui.usernameLabel.text()
        userphone = self.ui.userphoneLabel.text()
        usermail = self.ui.usermailLabel.text()

        self.ui.userBooknameLabel.setText(username)
        self.ui.userBookMailLabel.setText(usermail)
        self.ui.userBookPhoneLabel.setText(userphone)
        self.ui.userBookKndLabel.setText(kndNum)

        userBooks = self.userdb.user_get_books(kndNum)
        
        self.ui.userBookTable.setRowCount(len(userBooks))

        listToLoad = []

        for isbn in userBooks:
            for book in booklist:
                if book['isbn'] == isbn:
                    listToLoad.append(book)
        
        row = 0
        for b in listToLoad:
            self.ui.userBookTable.setItem(row, 0, QTableWidgetItem(b['isbn']))
            self.ui.userBookTable.setItem(row, 1, QTableWidgetItem(b['title']))
            self.ui.userBookTable.setItem(row, 2, QTableWidgetItem(b['out-date']))
            self.ui.userBookTable.setItem(row, 3, QTableWidgetItem(b['back_date']))
            item = QTableWidgetItem()
            check_icon = QIcon()
            check_icon.addFile(u":/icons/icons/tick.png", QSize(), QIcon.Normal, QIcon.Off)
            x_icon = QIcon()
            x_icon.addFile(u":/icons/icons/cross.png", QSize(), QIcon.Normal, QIcon.Off)
            if self.check_date_expired(b['back_date']):
                item.setIcon(check_icon)
            else:
                item.setIcon(x_icon)
            self.ui.userBookTable.setItem(row, 4, item)
            row += 1
        
        self.ui.stackedWidget.setCurrentWidget(self.ui.userBookView)

    def check_date_expired(self, date) -> bool:
        return datetime.datetime.strptime(date,"%d.%m.%Y").date() < datetime.date.today()

    def clear_add_book_input(self):
        self.ui.addAuthorInput.clear()
        self.ui.addGenreInput.clear()
        self.ui.addisbnInput.clear()
        self.ui.addOutdateInput.clear()
        self.ui.addTitleInput.clear()
        #self.ui.stackedWidget.setCurrentWidget(self.ui.indexView)
    
    # Import/Export
    def import_data_file(self):
        path = self.ui.importFileInput.text()
        if path == "" or path == None:
            return

        button = QMessageBox.warning(
            self,
            'Warung',
            'Bist du sicher das du eine neue Bücherliste importieren möchtest?\n\nBeachte bitte:\nEin Backup der aktuellen Liste wurde im Verzeichnis \"Backup\" erstellt!\nDie aktuelle Bücherliste wird mit der neuen ersetzt!\n\nFortfahren?',
            QMessageBox.StandardButton.Yes |
            QMessageBox.StandardButton.No
        )
        if button == QMessageBox.StandardButton.Yes:
            new_list = []
            save_booklist(True)
            with open(path, 'r') as f:
                file = csv.reader(f)
                for items in file:
                    #print(items)
                    new_book = {}
                    #print("loaded items\n" ,items)
                    new_book['isbn'] = items[0]
                    new_book['title'] = items[1]
                    new_book['author'] = items[2]
                    new_book['genre'] = items[3]
                    new_book['out-date'] = ""
                    new_book['available'] = "Yes"
                    new_book['lend_knd'] = ""
                    new_book['back_date'] = ""
                    new_list.append(new_book)
            self.ui.importFileInput.clear()
            global booklist
            booklist = new_list
            save_booklist()
            self.load_book_list()
            return True
        elif button == QMessageBox.StandardButton.No:
            self.ui.importFileInput.clear()
            return False

    def get_import_data(self):
        fname = QFileDialog.getOpenFileName(self, "Open File", "", "CSV Datein (*.csv);;Alle Dateien (*)")
        path, _ = fname
        if fname :
            self.ui.importFileInput.setText(path)

    def export_data_file(self):
        download_folder = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Downloads')
        datatype = self.ui.exportFileInputbox.currentText()
        filetype = self.ui.exportFileTypeBox.currentText()
        filename = ""
        if datatype == "" or filetype == "":
            return
        if datatype == "Buchindex":
            filename = "BookDataExport"
        else:
            filename = "CustomerDataExport"

        if filetype == "CSV":
            filename += ".csv"
        elif filetype == "JSON":
            filename += ".json"
        elif filetype == "TXT":
            filename += ".txt"
        
        if datatype == "Buchindex":
            if filetype == "TXT":
                with open(download_folder+"\\"+filename, 'w') as f:
                    for book in booklist:
                        new_line = (f"{book['isbn']}\t\t{book['title']}\t\t{book['author']}\t\t{book['genre']}")
                        f.write(new_line+"\n")
                return print("Buchindex als Textdatei exportiert")
            elif filetype == "JSON":
                export_list =[]
                for book in booklist:
                    book_dict = {}
                    book_dict['isbn'] = book['isbn']
                    book_dict['title'] = book['title']
                    book_dict['author'] = book['author']
                    book_dict['genre'] = book['genre']
                    export_list.append(book_dict)
                
                with open(download_folder+"\\"+filename, "w") as f:
                    f.write(json.dumps(export_list))
                return print("Buchindex als JSON-Datei exportiert")
            elif filetype == "CSV":
                export_list =[]
                for book in booklist:
                    new_list = []
                    new_list.append(book['isbn'])
                    new_list.append(book['title'])
                    new_list.append(book['author'])
                    new_list.append(book['genre'])
                    export_list.append(new_list)
                
                with open(download_folder+"\\"+filename, 'w', newline='') as f:
                    write = csv.writer(f)
                    for row in export_list:
                        write.writerow(row)
                return print("Buchindex als CSV-Datei exportiert")
        
        if datatype == "Kundenindex":
            if filetype == "TXT":
                pass
        
        
        print("Daten exportiert")

    def backup_data(self):
        button = QMessageBox.information(
            self,
            'Information',
            'Backup\n\nVon dem Bücherindex und deiner Kundendaten wird ein Backup erstellt.\nDiese werden im Installations-Ordner unter \"backup\" gespeichert.\nBitte beachte regelmäßige Backups deiner Daten anzulegen oder zu aktualisieren!',
            QMessageBox.StandardButton.Ok
        )
        if button == QMessageBox.StandardButton.Ok:
            save_booklist(True)
            self.userdb.backup_data()
            self.ui.stackedWidget.setCurrentWidget(self.ui.homeView)

    def get_backup_data(self):
        button = QMessageBox.warning(
            self,
            'Warnung',
            'Daten Widerherstellen\nDas Backup deiner Daten wird wieder hergestellt.\n\nBeachte bitte:\nDeine aktuellen Daten gehen dadurch verloren es wird KEIN Backup erstellt!\n\nFortfahren?',
            QMessageBox.StandardButton.Yes |
            QMessageBox.StandardButton.No
        )
        if button == QMessageBox.StandardButton.Yes:
            os.remove(os.path.abspath(os.curdir)+'\\data\\booklist.csv')
            shutil.copy2(os.path.abspath(os.curdir)+'\\backup\\Bücherindex-Backup.csv', os.path.abspath(os.curdir)+'\\data\\booklist.csv')
            load_booklist()
            self.userdb.get_backup_data()
            self.load_user_list()
            self.load_available_list()
            self.load_book_list()
            button2 = QMessageBox.information(
                self,
                'Information',
                'Daten wurden wieder hergestellt.\nBitte starte die Software neu, um alle Änderungen zu aktualisieren!',
                QMessageBox.StandardButton.Ok
            )
            if button2 == QMessageBox.StandardButton.Ok:
                self.ui.stackedWidget.setCurrentWidget(self.ui.homeView)
        elif button == QMessageBox.StandardButton.No:
            return


# save booklist as csv file in ./data/booklist.csv
def save_booklist(backup=False):
    rows = []
    for book in booklist:
        new = []
        #print(book)
        if book['isbn'] == 'isbn':
            continue
        new.append(book['isbn'])
        new.append(book['title'])
        new.append(book['author'])
        new.append(book['genre'])
        new.append(book['out-date'])
        new.append(book['available'])
        new.append(book['lend_knd'])
        new.append(book['back_date'])
        rows.append(new)
    if backup:
        path = os.path.abspath(os.curdir)+'\\backup\\Bücherindex-Backup.csv'
    else:
        path = os.path.abspath(os.curdir)+'\\data\\booklist.csv'
    with open(path, 'w', newline='') as f:
            write = csv.writer(f)
            #write.writerow(fields)
            for row in rows:
                write.writerow(row)

# load booklist as csv file
def load_booklist() -> list:
    new_list = []
    with open(os.path.abspath(os.curdir) +'\\data\\booklist.csv', 'r') as f:
        file = csv.reader(f)
        for items in file:
            #print(items)
            new_book = {}
            #print("loaded items\n" ,items)
            new_book['isbn'] = items[0]
            new_book['title'] = items[1]
            new_book['author'] = items[2]
            new_book['genre'] = items[3]
            new_book['out-date'] = items[4]
            new_book['available'] = items[5]
            new_book['lend_knd'] = items[6]
            new_book['back_date'] = items[7]
            new_list.append(new_book)
    return new_list

def main(app: QApplication):
    global booklist
    booklist = load_booklist()
    window = MainWindow()
    window.splash.show() 
    window.start_splash()
    #window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(os.path.join(base_dir, 'appicon.ico')))

    try:
        main(app)
    except KeyboardInterrupt:
        print("Key exit")
    finally:
        app.quit()
        sys.exit()

