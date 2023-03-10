import sys, csv, time, webbrowser, traceback, os, datetime, json, shutil, logging
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6 import *
from res.ui_mainui import Ui_MainWindow
from res.ui_splashui import Ui_SplashScreen
from res.utils import *
import data
from styles import ButtonStyles, TextStyles
from qt_material import apply_stylesheet

base_dir = os.path.dirname(__file__)
APPCONFIG = data.config_app()
appversiontext = f"Version {APPCONFIG['version']} | Copyright 2023 by S3R43o3"

book = {
    "isbn": None,
    "title": None,
    "author": None,
    "genre": None,
    "out-date": None,
    "available": None,
    "lend-knd":""
}

def setup_logger():
    d = datetime.datetime.today().strftime("%d.%m.%Y")
    logging.basicConfig(filename=os.path.join(base_dir+"\\logs","log-"+d+".log"), encoding='utf-8', level= logging.INFO,  format='%(asctime)s %(message)s', datefmt='%d/%m/%Y %I:%M:%S %p')
    
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
        self.showing = False 
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
        self.splash.versionLabel.setText(f"Version {APPCONFIG['version']}")
        self.timer = QTimer()
        self.progressBar = self.splash.loadProgress
        self.cancelBTN = self.splash.cancelBtn
        self.shadowanim = QPropertyAnimation(self.shadow1, b'color')
        self.animationTimer = QTimer()
        self.animationTimer.setSingleShot(True)
        self.animationTimer.timeout.connect(self.change_animation)
        logging.info("[Splash]: Start Splash-Animation!")
        #self.splash.cancelBtn.clicked.connect(lambda: self.close())
    
    def change_animation(self):
        if self.showing == False:
            self.start_animate_shadow()
            self.showing = True
        else:
            self.stop_animate_shadow()
            self.showing = False

    def exit_animate_shadow(self):
        if self.shadowanim:
            self.shadowanim = None
        else:
            return

    def start_animate_shadow(self):
        self.shadowanim.setDuration(300)
        self.shadowanim.setStartValue(QColor(255, 0, 0, 0))
        self.shadowanim.setEndValue(QColor(255, 0, 0, 90))
        self.shadowanim.setEasingCurve(QEasingCurve.InOutQuad)
        self.shadowanim.start()
        self.animationTimer.setSingleShot(True)
        self.animationTimer.start(450)

    def stop_animate_shadow(self):
        self.shadowanim.setDuration(300)
        self.shadowanim.setStartValue(QColor(255, 0, 0, 90))
        self.shadowanim.setEndValue(QColor(255, 0, 0, 0))
        self.shadowanim.setEasingCurve(QEasingCurve.InOutQuad)
        self.shadowanim.start()        
        self.animationTimer.setSingleShot(True)
        self.animationTimer.start(450)

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
        self.setWindowTitle(f'Bookworm {APPCONFIG["version"]}')
        self.setWindowIcon(QIcon(os.path.join(base_dir, 'appicon.ico')))
        self.userdb = data.UserData()
        self.splash = Splash()
        self.threadpool = QThreadPool()
        logging.info("[Main]: Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())
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
        self.load_user_list()
        self.load_book_list()
        self.load_available_list()
        self.apply_styles()
        self.setup_buttons()
        self.update_backup_display()
        self.ui.version_label.setText(appversiontext)
        self.ui.stackedWidget.setCurrentWidget(self.ui.homeView)
        self.ui.stackedWidgetHelp.setCurrentWidget(self.ui.helpHomeView)

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
        # self.splash.exit_animate_shadow
        self.splash.close()
        self.show()
        self.menuAnim()
        self.activeworkder = None
        print("Thread finished")

    def start_splash(self):
        worker = Worker(self.run_splashscreen)
        worker.signals.result.connect(self.output_worker)
        worker.signals.finished.connect(self.thread_complete)
        worker.signals.progress.connect(self.progress_fn)
        self.activeworkder = worker
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
        
        self.ui.useEditBtnFrame.setStyleSheet(ButtonStyles.NormalButton)
        self.ui.userEditInfoLabel.setStyleSheet(TextStyles.InformationText)
        self.ui.version_label.setStyleSheet(TextStyles.VersionText)
        self.ui.helpCommonHeader.setStyleSheet(TextStyles.SubHeaderHelp)
        self.ui.helpCommonLabel.setStyleSheet(TextStyles.InformationText)
        self.ui.helpImportHeader.setStyleSheet(TextStyles.SubHeaderHelp)
        self.ui.helpImportLabel.setStyleSheet(TextStyles.InformationText)
        self.ui.helpHomeLabel.setStyleSheet(TextStyles.SubHeaderHelp)
        self.ui.helpIndexHeader.setStyleSheet(TextStyles.SubHeaderHelp)
        self.ui.helpIndexLabel.setStyleSheet(TextStyles.InformationText)
        self.ui.helpUserHeader.setStyleSheet(TextStyles.SubHeaderHelp)
        self.ui.helpUserLabel.setStyleSheet(TextStyles.InformationText)

        self.ui.backupAvailbleLabel.setStyleSheet(TextStyles.InformationText)
        self.ui.backupDateLabel.setStyleSheet(TextStyles.InformationText)

        self.ui.helpIssueBtn.setStyleSheet(ButtonStyles.NormalButton)

    def close_splash(self):
        self.splash.timer.stop()
        self.splash.close()

    def setup_buttons(self):
        self.ui.lendDayBox.currentTextChanged.connect(lambda: self.set_lenddate_label())
        self.ui.userTable.itemSelectionChanged.connect(lambda: self.show_user_information())
        self.ui.indexSearchInput.textChanged.connect(self.search_book)
        self.ui.userSearchInput.textChanged.connect(self.search_user)

        self.splash.splash.cancelBtn.clicked.connect(lambda: self.close_splash())
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
        self.ui.menu_btn_help.clicked.connect(lambda: self.ui.stackedWidgetHelp.setCurrentWidget(self.ui.helpHomeView))
        #self.ui.menu_btn_help.setEnabled(False)

        self.ui.userBookBackBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.userlistView))
        self.ui.newUserBtn.clicked.connect(lambda: self.show_newuser_view())
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
        self.ui.loadBackupBtn.clicked.connect(lambda: self.get_backup_data())
        #self.ui.loadBackupBtn.setEnabled(False)

        # Useredit view
        self.ui.userEditBtn.clicked.connect(lambda: self.go_edit_view())
        self.ui.userEditBackBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.userlistView))
        self.ui.userEditChangeBtn.clicked.connect(lambda: self.update_user())

        # Help view
        self.ui.comHelpBtn.clicked.connect(lambda: self.ui.stackedWidgetHelp.setCurrentWidget(self.ui.helpCommonView))
        self.ui.importHelpBtn.clicked.connect(lambda: self.ui.stackedWidgetHelp.setCurrentWidget(self.ui.helpImportView))
        self.ui.indexHelpBtn.clicked.connect(lambda: self.ui.stackedWidgetHelp.setCurrentWidget(self.ui.helpIndexView))
        self.ui.userHelpBtn.clicked.connect(lambda: self.ui.stackedWidgetHelp.setCurrentWidget(self.ui.helpUserView))
        self.ui.helpBackBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.homeView))
        self.ui.helpIssueBtn.clicked.connect(lambda: webbrowser.open("https://github.com/sera619/Bookworm-Bookmanagementsystem/issues"))
        self.ui.delBackupBtn.clicked.connect(lambda: self.remove_backup_data())
        # social 
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

    def go_edit_view(self):
        self.ui.userEditInfoLabel.setText("??ndere die Daten und klicke den '??ndern'-Button.")
        if not self.ui.userTable.selectedIndexes():
            return

        row = self.ui.userTable.selectedIndexes()
        if row:
            rows = set(i.row() for i in row)
        else:
            rows = [self.ui.userTable.rowCount() - 1]
        
        for r in rows:
            name = self.ui.userTable.item(r, 1).text()
        
        userdata = self.userdb.get_userinfo(name)

        self.ui.userEditNameInput.setText(userdata['name'])
        self.ui.userEditCityInput.setText(userdata['city'])
        self.ui.userEditBirthdayInput.setText(userdata['birthday'])
        self.ui.userEditAddressInput.setText(userdata['address'])
        self.ui.userEditPhoneInput.setText(userdata['phone'])
        self.ui.userEditMailInput.setText(userdata['mail'])
        self.userdb.userid_to_change = userdata['kndNum']
        self.ui.stackedWidget.setCurrentWidget(self.ui.userEditView)
    
    def update_user(self):
        newname = self.ui.userEditNameInput.text()
        newcity = self.ui.userEditCityInput.text()
        newbirthday = self.ui.userEditBirthdayInput.text()
        newaddress =  self.ui.userEditAddressInput.text()
        newphone = self.ui.userEditPhoneInput.text()
        newmail =  self.ui.userEditMailInput.text()
        currentusername = self.userdb.get_user_name(self.userdb.userid_to_change)
        changedinfos = ['Email', 'Addresse', 'Telefon', 'Stadt', 'Geburtstag', 'Name']
        if not self.userdb.edit_usermail(currentusername, newmail) or not is_mail_valid(newmail):
            changedinfos.remove('Email')
        if not self.userdb.edit_useraddress(currentusername, newaddress):
            changedinfos.remove('Addresse')
        if not self.userdb.edit_userphone(currentusername, newphone):
            changedinfos.remove('Telefon')
        if not self.userdb.edit_usercity(currentusername, newcity):
            changedinfos.remove('Stadt')
        if not self.userdb.edit_userbirthday(currentusername, newbirthday) or not is_birthday_valid(newbirthday):
            changedinfos.remove('Geburtstag')
        
        if not self.userdb.edit_username(currentusername, newname):
            changedinfos.remove('Name')

        changed =""         
        for x in changedinfos:
            changed += "- "+ x + "\n"
        
        if changed == "":
            changed = "None"

        button = QMessageBox.information(
            self,
            'Kundenupdate',
            f'Die folgende Kundeninformation von\n{newname}\nwurden erfolgreich ge??ndert:\n{changed}',
            QMessageBox.StandardButton.Ok 
        )
        if button == QMessageBox.StandardButton.Ok:
            self.userdb.userid_to_change = None
            self.clear_userinformation()
            self.reset_edituser_view()
            self.load_user_list()
            self.ui.stackedWidget.setCurrentWidget(self.ui.userlistView)

    def reset_edituser_view(self):
        self.ui.userEditInfoLabel.setText("??ndere die Daten und klicke den '??ndern'-Button.")
        self.ui.userEditNameInput.clear()
        self.ui.userEditCityInput.clear()
        self.ui.userEditBirthdayInput.clear()
        self.ui.userEditAddressInput.clear()
        self.ui.userEditPhoneInput.clear()
        self.ui.userEditMailInput.clear()

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
        self.ui.newuserLastNameInput.clear()

    def show_newuser_view(self):
        self.ui.newuserKndNumInput.setText(f"  ( {str(self.userdb.lastKdnNum + 1)} )" + self.ui.newuserKndNumInput.text()  )
        self.ui.stackedWidget.setCurrentWidget(self.ui.newUserView)

    def new_user(self):
        new_adress = self.ui.newuserAdressInput.text()
        new_birthday = self.ui.newuserBirthdayInput.text()
        new_city =self.ui.newuserCityInput.text()
        new_mail = self.ui.newuserMailInput.text()
        new_name = self.ui.newuserNameInput.text()
        new_lastname = self.ui.newuserLastNameInput.text()
        new_phone = self.ui.newuserPhoneInput.text()
        
        if new_mail == "" or new_adress == "" or new_birthday == "" or new_city == ""  or new_name =="" or new_phone == "" or new_lastname == "":
            button = QMessageBox.warning(
                self,
                'Information fehlt',
                f'Bitte f??lle alle vorhandenen Felder aus!\n',
                QMessageBox.StandardButton.Ok
            )
            if button == QMessageBox.StandardButton.Ok:
                return

        if not is_mail_valid(new_mail):
            button = QMessageBox.warning(
                self,
                'E-Mail nicht gefunden',
                f'Bitte gebe eine korrekte E-Mail Addresse ein!\n\nBsp.: beispielmail@beispiel.com',
                QMessageBox.StandardButton.Ok
            )
            if button == QMessageBox.StandardButton.Ok:
                self.ui.newuserMailInput.setText("")
                return
        
        if not is_birthday_valid(new_birthday):
            button = QMessageBox.warning(
                self,
                'Geburtsdatum nicht korrekt',
                f'Das Geburtsdatum ist nicht korrekt!\n\nBitte verwende gebe das Geburtsdatum ein!\n\nBsp.: 22.05.2002',
                QMessageBox.StandardButton.Ok
            )
            if button == QMessageBox.StandardButton.Ok:
                self.ui.newuserBirthdayInput.setText("")
                return

        new_fullname = f"{new_name.capitalize()} {new_lastname.capitalize()}"
        button = QMessageBox.information(
            self,
            'Neuer Nutzer',
            f'Neuer Nutzer\n"{new_fullname}"\nwurde erstellt!',
            QMessageBox.StandardButton.Ok
        )
        if button == QMessageBox.StandardButton.Ok:
            new_kndnum = str(self.userdb.generate_kdnNum())
            self.userdb.add_user(new_kndnum, new_fullname, new_mail, new_phone, new_city, new_adress, new_birthday, [])
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
        
        full_name = name
        button = QMessageBox.question(
            self,
            'Nutzer l??schen?',
            f'M??chstest du den Benutzer\n"{full_name}"\nwirklich l??schen?',
            QMessageBox.StandardButton.Yes |
            QMessageBox.StandardButton.No
        )
        if button == QMessageBox.StandardButton.Yes:
            self.userdb.remove_user(full_name)
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
        load_booklist()
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
            'Best??tigen',
            'Bist du sicher das du dieses Buch l??schen m??chtest?',
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
                        f'Buch\n\"{bookname}\"\nvon\n\"{self.userdb.get_user_name(lender)}\"\nzur??ck bekommen!',
                        QMessageBox.StandardButton.Ok
                    )
                    if button == QMessageBox.StandardButton.Ok:
                        self.ui.stackedWidget.setCurrentWidget(self.ui.avaibleView)

    def search_book(self, s):
        self.ui.indexTable.setCurrentItem(None)
        if not s:
            return
        matching_items = self.ui.indexTable.findItems(s, Qt.MatchContains)
        if matching_items:
            item = matching_items[0]
            self.ui.indexTable.setCurrentItem(item)
    
    def search_user(self, s):
        self.ui.userTable.setCurrentItem(None)
        if not s:
            return
        match_items = self.ui.userTable.findItems(s, Qt.MatchContains)
        if match_items:
            item = match_items[0]
            self.ui.userTable.setCurrentItem(item)
        

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
        #print("Buch hinzugef??gt: " + title)
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
    
    # Import/Export
    def import_data_file(self):
        path = self.ui.importFileInput.text()
        if path == "" or path == None:
            return

        button = QMessageBox.warning(
            self,
            'Warung',
            'Bist du sicher das du eine neue B??cherliste importieren m??chtest?\n\nBeachte bitte:\nEin Backup der aktuellen Liste wurde im Verzeichnis \"Backup\" erstellt!\nDie aktuelle B??cherliste wird mit der neuen ersetzt!\n\nFortfahren?',
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
            'Backup\n\nVon dem B??cherindex und deiner Kundendaten wird ein Backup erstellt.\nDiese werden im Installations-Ordner unter \"backup\" gespeichert.\nBitte beachte regelm????ige Backups deiner Daten anzulegen oder zu aktualisieren!',
            QMessageBox.StandardButton.Ok |
            QMessageBox.StandardButton.Cancel
        )
        if button == QMessageBox.StandardButton.Ok:
            save_booklist(True)
            data.backup_data()
            date = datetime.datetime.today().strftime("%d.%m.%Y")
            time = datetime.datetime.now().strftime("%H:%M:%S")
            backup = date + " " + time
            APPCONFIG['lastBackup'] = backup
            data.save_config(APPCONFIG)
            self.ui.stackedWidget.setCurrentWidget(self.ui.homeView)
            self.update_backup_display()
        elif button == QMessageBox.StandardButton.Cancel:
            return

    def get_backup_data(self):
        if not data.backupdata_exists():
            return
        button = QMessageBox.warning(
            self,
            'Warnung',
            'Daten Widerherstellen\nDas Backup deiner Daten wird wieder hergestellt.\n\nBeachte bitte:\nDeine aktuellen Daten gehen dadurch verloren es wird KEIN Backup erstellt!\n\nFortfahren?',
            QMessageBox.StandardButton.Yes |
            QMessageBox.StandardButton.No
        )
        if button == QMessageBox.StandardButton.Yes:
            os.remove(data.BOOKLIST_F)
            shutil.copy2(data.BOOKLIST_F_B, data.BOOKLIST_F)
            load_booklist()
            self.userdb = None
            data.get_backup_data()
            self.userdb = data.UserData()
            self.load_user_list()
            self.load_available_list()
            self.load_book_list()
            button2 = QMessageBox.information(
                self,
                'Information',
                'Daten wurden wieder hergestellt.\nBitte starte die Software neu, um alle ??nderungen zu aktualisieren!',
                QMessageBox.StandardButton.Ok
            )
            if button2 == QMessageBox.StandardButton.Ok:
                self.ui.stackedWidget.setCurrentWidget(self.ui.homeView)
        elif button == QMessageBox.StandardButton.No:
            return

    def remove_backup_data(self):
        if not data.backupdata_exists():
            return
        button = QMessageBox.warning(
            self,
            'Achtung!',
            'Backup l??schen.\n\nDas vorhandene Backup wird unwiderruflich gel??scht!\n\nFortfahren?',
            QMessageBox.StandardButton.Yes |
            QMessageBox.StandardButton.No
        )
        if button == QMessageBox.StandardButton.Yes:
            data.remove_backup_data()
            APPCONFIG['lastBackup'] = None
            data.save_config(APPCONFIG)
            self.update_backup_display()
            os.remove('./backup/Backup-booklist.csv')
        elif button == QMessageBox.StandardButton.No:
            return

    def update_backup_display(self):
        self.ui.backupAvailbleLabel.setText("")
        if data.backupdata_exists():
            self.ui.backupDateLabel.setStyleSheet(TextStyles.InformationTextOkay)
            self.ui.backupAvailbleLabel.setStyleSheet(TextStyles.InformationTextOkay)
            self.ui.backupDateLabel.setText("Letztes Backup: " + APPCONFIG['lastBackup'])
            self.ui.backupAvailbleLabel.setText("Backup verf??gbar!")
        else:
            self.ui.backupDateLabel.setText("")
            self.ui.backupAvailbleLabel.setStyleSheet(TextStyles.InformationText)
            self.ui.backupAvailbleLabel.setText("Kein Backup verf??gbar!")



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
        path = data.BOOKLIST_F_B
    else:
        path = data.BOOKLIST_F
    with open(path, 'w', newline='') as f:
            write = csv.writer(f)
            #write.writerow(fields)
            for row in rows:
                write.writerow(row)

# load booklist as csv file
def load_booklist() -> list:
    new_list = []
    with open(data.BOOKLIST_F, 'r') as f:
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

def main(app: QApplication, window: MainWindow):
    
    #window.splash.show() 
    #window.start_splash()
    #window.splash.change_animation()

    window.show()
    sys.exit(app.exec())

global booklist

if __name__ == '__main__':
    setup_logger()
    logging.info("-----------------------------------------------")
    logging.info("[Main]: Software started")
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(os.path.join(base_dir, 'appicon.ico')))
    booklist = load_booklist()
    window = MainWindow()
    try:
        main(app, window)
    except KeyboardInterrupt:
        print("Key exit")
    except Exception as e:
        print("Anderer fehler:\n", e)
        logging.error("[Main]: Error: ", e)
    finally:
        logging.info("[Main]: Software closed.")
        app.quit()
        sys.exit()

