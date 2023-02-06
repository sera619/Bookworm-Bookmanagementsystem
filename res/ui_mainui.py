# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainui.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QComboBox,
    QFormLayout, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QStackedWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
import ressource_rc
import ressource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1046, 608)
        icon = QIcon()
        icon.addFile(u":/icons/fonts/favicon.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QMainWindow{\n"
"	border: solid 1px rgba(255, 255, 255, 0);\n"
"	border-radius: 25px;\n"
"}\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.topFrame = QFrame(self.centralwidget)
        self.topFrame.setObjectName(u"topFrame")
        self.topFrame.setStyleSheet(u"QFrame{\n"
"	border: rgba(255, 0, 0, 0);\n"
"	border-radius: 25px;\n"
" }")
        self.topFrame.setFrameShape(QFrame.StyledPanel)
        self.topFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.topFrame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.topFrame)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setStyleSheet(u"QFrame{\n"
"		border-radius: 25px;\n"
" }")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_5)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(45, -1, 45, -1)
        self.menu_btn = QPushButton(self.frame_5)
        self.menu_btn.setObjectName(u"menu_btn")
        self.menu_btn.setStyleSheet(u"QPushButton{\n"
"	border: 1px solid rgba(170, 0, 0,165);\n"
"	padding: 2px 20px;\n"
"	border-radius: 2%;\n"
"	color: rgb(255, 0, 0)\n"
"}\n"
"\n"
"QPushButton::Hover{\n"
"	border: 1.4px solid rgb(255, 0, 0);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 0, 0, 70), stop:1 rgba(65, 0, 0, 70));\n"
"	\n"
"}\n"
"\n"
"QPushButton::Pressed{\n"
"	border: 1.4px solid;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0  rgba(65, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));\n"
"	border-color: rgb(255, 0, 0);\n"
"	color: #FFF;\n"
"}")

        self.verticalLayout_17.addWidget(self.menu_btn)


        self.horizontalLayout.addWidget(self.frame_5, 0, Qt.AlignHCenter)

        self.headerFrame = QFrame(self.topFrame)
        self.headerFrame.setObjectName(u"headerFrame")
        sizePolicy.setHeightForWidth(self.headerFrame.sizePolicy().hasHeightForWidth())
        self.headerFrame.setSizePolicy(sizePolicy)
        self.headerFrame.setFrameShape(QFrame.StyledPanel)
        self.headerFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.headerFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.headerLabel = QLabel(self.headerFrame)
        self.headerLabel.setObjectName(u"headerLabel")
        font = QFont()
        font.setFamilies([u"Ethnocentric"])
        font.setPointSize(32)
        font.setBold(False)
        font.setItalic(False)
        self.headerLabel.setFont(font)
        self.headerLabel.setStyleSheet(u"QLabel{	\n"
"	color: rgb(170, 0, 0);\n"
"	font: 32pt \"Ethnocentric\";\n"
"}\n"
"")

        self.verticalLayout_2.addWidget(self.headerLabel, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout.addWidget(self.headerFrame)

        self.topmenuFrame = QFrame(self.topFrame)
        self.topmenuFrame.setObjectName(u"topmenuFrame")
        self.topmenuFrame.setStyleSheet(u"QPushButton{\n"
"	border: 1px solid rgba(170, 0, 0,165);\n"
"	padding: 2px 20px;\n"
"	border-radius: 2%;\n"
"	color: rgb(255, 0, 0)\n"
"}\n"
"\n"
"QPushButton::Hover{\n"
"	border: 1.4px solid rgb(255, 0, 0);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 0, 0, 70), stop:1 rgba(65, 0, 0, 70));\n"
"	\n"
"}\n"
"\n"
"QPushButton::Pressed{\n"
"	border: 1.4px solid;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0  rgba(65, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));\n"
"	border-color: rgb(255, 0, 0);\n"
"	color: #FFF;\n"
"}")
        self.topmenuFrame.setFrameShape(QFrame.StyledPanel)
        self.topmenuFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.topmenuFrame)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(45, 10, 10, 0)
        self.min_window_btn = QPushButton(self.topmenuFrame)
        self.min_window_btn.setObjectName(u"min_window_btn")
        self.min_window_btn.setMaximumSize(QSize(25, 25))
        self.min_window_btn.setSizeIncrement(QSize(20, 20))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/minus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.min_window_btn.setIcon(icon1)
        self.min_window_btn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.min_window_btn)

        self.max_window_btn = QPushButton(self.topmenuFrame)
        self.max_window_btn.setObjectName(u"max_window_btn")
        self.max_window_btn.setMaximumSize(QSize(25, 25))
        self.max_window_btn.setSizeIncrement(QSize(20, 20))
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/square.png", QSize(), QIcon.Normal, QIcon.Off)
        self.max_window_btn.setIcon(icon2)
        self.max_window_btn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.max_window_btn)

        self.x_button = QPushButton(self.topmenuFrame)
        self.x_button.setObjectName(u"x_button")
        self.x_button.setMaximumSize(QSize(25, 25))
        self.x_button.setSizeIncrement(QSize(20, 20))
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.x_button.setIcon(icon3)
        self.x_button.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.x_button)


        self.horizontalLayout.addWidget(self.topmenuFrame, 0, Qt.AlignLeft|Qt.AlignTop)


        self.verticalLayout.addWidget(self.topFrame, 0, Qt.AlignTop)

        self.centerFrame = QFrame(self.centralwidget)
        self.centerFrame.setObjectName(u"centerFrame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centerFrame.sizePolicy().hasHeightForWidth())
        self.centerFrame.setSizePolicy(sizePolicy1)
        self.centerFrame.setStyleSheet(u"QFrame{\n"
"	border: rgba(255, 0, 0, 0);\n"
"	border-radius: 25px;\n"
" }")
        self.centerFrame.setFrameShape(QFrame.StyledPanel)
        self.centerFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.centerFrame)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(9, 9, 0, 0)
        self.menuFrame = QFrame(self.centerFrame)
        self.menuFrame.setObjectName(u"menuFrame")
        self.menuFrame.setMinimumSize(QSize(150, 0))
        self.menuFrame.setMaximumSize(QSize(0, 16777215))
        self.menuFrame.setStyleSheet(u"QPushButton{\n"
"	border: 1px solid rgba(170, 0, 0,165);\n"
"	padding: 2px 20px;\n"
"	border-radius: 2%;\n"
"	color: rgb(255, 0, 0)\n"
"}\n"
"\n"
"QPushButton::Hover{\n"
"	border: 1.2px solid rgb(255, 0, 0);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 0, 0, 70), stop:1 rgba(65, 0, 0, 70));\n"
"	\n"
"}\n"
"\n"
"QPushButton::Pressed{\n"
"	border: 1.4px solid;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0  rgba(65, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));\n"
"	border-color: rgb(255, 0, 0);\n"
"	color: #FFF;\n"
"}\n"
"\n"
"QPushButton::Focus{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0  rgba(65, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));\n"
"	border: 1.4px solid rgb(255, 0, 0);\n"
"	color: #FFF;\n"
"}")
        self.menuFrame.setFrameShape(QFrame.StyledPanel)
        self.menuFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.menuFrame)
        self.verticalLayout_3.setSpacing(25)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 9, -1, 9)
        self.menu_btn_home = QPushButton(self.menuFrame)
        self.menu_btn_home.setObjectName(u"menu_btn_home")
        self.menu_btn_home.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.menu_btn_home)

        self.menu_btn_index = QPushButton(self.menuFrame)
        self.menu_btn_index.setObjectName(u"menu_btn_index")

        self.verticalLayout_3.addWidget(self.menu_btn_index)

        self.menu_btn_awaylist = QPushButton(self.menuFrame)
        self.menu_btn_awaylist.setObjectName(u"menu_btn_awaylist")

        self.verticalLayout_3.addWidget(self.menu_btn_awaylist)

        self.menu_btn_userindex = QPushButton(self.menuFrame)
        self.menu_btn_userindex.setObjectName(u"menu_btn_userindex")

        self.verticalLayout_3.addWidget(self.menu_btn_userindex)

        self.menu_btn_import = QPushButton(self.menuFrame)
        self.menu_btn_import.setObjectName(u"menu_btn_import")

        self.verticalLayout_3.addWidget(self.menu_btn_import)

        self.menu_btn_backup = QPushButton(self.menuFrame)
        self.menu_btn_backup.setObjectName(u"menu_btn_backup")

        self.verticalLayout_3.addWidget(self.menu_btn_backup)

        self.menu_btn_help = QPushButton(self.menuFrame)
        self.menu_btn_help.setObjectName(u"menu_btn_help")

        self.verticalLayout_3.addWidget(self.menu_btn_help)


        self.horizontalLayout_7.addWidget(self.menuFrame, 0, Qt.AlignLeft|Qt.AlignTop)

        self.mainFrame = QFrame(self.centerFrame)
        self.mainFrame.setObjectName(u"mainFrame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.mainFrame.sizePolicy().hasHeightForWidth())
        self.mainFrame.setSizePolicy(sizePolicy2)
        self.mainFrame.setFrameShape(QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.mainFrame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.mainFrame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy2.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy2)
        self.homeView = QWidget()
        self.homeView.setObjectName(u"homeView")
        sizePolicy2.setHeightForWidth(self.homeView.sizePolicy().hasHeightForWidth())
        self.homeView.setSizePolicy(sizePolicy2)
        self.homeView.setStyleSheet(u"")
        self.verticalLayout_5 = QVBoxLayout(self.homeView)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 9, 9, 9)
        self.frame = QFrame(self.homeView)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 16777215))
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.appLogoLabel = QLabel(self.frame)
        self.appLogoLabel.setObjectName(u"appLogoLabel")
        sizePolicy1.setHeightForWidth(self.appLogoLabel.sizePolicy().hasHeightForWidth())
        self.appLogoLabel.setSizePolicy(sizePolicy1)
        self.appLogoLabel.setStyleSheet(u"padding: 40px;")
        self.appLogoLabel.setPixmap(QPixmap(u":/icons/fonts/appicon128x128.png"))
        self.appLogoLabel.setScaledContents(False)
        self.appLogoLabel.setAlignment(Qt.AlignCenter)
        self.appLogoLabel.setWordWrap(False)
        self.appLogoLabel.setMargin(0)

        self.verticalLayout_6.addWidget(self.appLogoLabel, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.homeHeaderLabel = QLabel(self.frame)
        self.homeHeaderLabel.setObjectName(u"homeHeaderLabel")
        font1 = QFont()
        font1.setFamilies([u"Ethnocentric"])
        font1.setPointSize(26)
        font1.setBold(False)
        font1.setItalic(False)
        self.homeHeaderLabel.setFont(font1)
        self.homeHeaderLabel.setStyleSheet(u"QLabel{\n"
"	\n"
"	font: 26pt \"Ethnocentric\";\n"
"}")
        self.homeHeaderLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.homeHeaderLabel, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.homeInfoLabel = QLabel(self.frame)
        self.homeInfoLabel.setObjectName(u"homeInfoLabel")
        sizePolicy2.setHeightForWidth(self.homeInfoLabel.sizePolicy().hasHeightForWidth())
        self.homeInfoLabel.setSizePolicy(sizePolicy2)
        self.homeInfoLabel.setStyleSheet(u"QLabel{\n"
"font: 12pt \"Ethnocentric\";\n"
"	color: rgb(170, 0, 0);\n"
"}\n"
"")
        self.homeInfoLabel.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_6.addWidget(self.homeInfoLabel)

        self.frame_17 = QFrame(self.frame)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.socialGitBtn = QPushButton(self.frame_17)
        self.socialGitBtn.setObjectName(u"socialGitBtn")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setKerning(True)
        self.socialGitBtn.setFont(font2)
        self.socialGitBtn.setStyleSheet(u"QPushButton{\n"
"	border: 1px solid rgba(170, 0, 0,165);\n"
"	padding: 2px 20px;\n"
"	border-radius: 2%;\n"
"	color: rgb(255, 0, 0)\n"
"}\n"
"\n"
"QPushButton::Hover{\n"
"	border: 1.4px solid rgb(255, 0, 0);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 0, 0, 70), stop:1 rgba(65, 0, 0, 70));\n"
"	\n"
"}\n"
"\n"
"QPushButton::Pressed{\n"
"	border: 1.4px solid;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0  rgba(65, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));\n"
"	border-color: rgb(255, 0, 0);\n"
"	color: #FFF;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/github.png", QSize(), QIcon.Normal, QIcon.Off)
        self.socialGitBtn.setIcon(icon4)
        self.socialGitBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_15.addWidget(self.socialGitBtn, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_6.addWidget(self.frame_17, 0, Qt.AlignVCenter)


        self.verticalLayout_5.addWidget(self.frame)

        self.stackedWidget.addWidget(self.homeView)
        self.lendView = QWidget()
        self.lendView.setObjectName(u"lendView")
        self.verticalLayout_18 = QVBoxLayout(self.lendView)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, -1, 0, -1)
        self.frame_19 = QFrame(self.lendView)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_19)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(-1, 0, -1, 0)
        self.frame_20 = QFrame(self.frame_19)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_20)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.lendHeaderLabel = QLabel(self.frame_20)
        self.lendHeaderLabel.setObjectName(u"lendHeaderLabel")
        self.lendHeaderLabel.setStyleSheet(u"QLabel{\n"
"	font: 26pt \"Ethnocentric\";\n"
"}")
        self.lendHeaderLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_21.addWidget(self.lendHeaderLabel)


        self.verticalLayout_19.addWidget(self.frame_20, 0, Qt.AlignTop)

        self.line_5 = QFrame(self.frame_19)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_19.addWidget(self.line_5)

        self.frame_18 = QFrame(self.frame_19)
        self.frame_18.setObjectName(u"frame_18")
        sizePolicy1.setHeightForWidth(self.frame_18.sizePolicy().hasHeightForWidth())
        self.frame_18.setSizePolicy(sizePolicy1)
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_18)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.lendBookFrame = QFrame(self.frame_18)
        self.lendBookFrame.setObjectName(u"lendBookFrame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.lendBookFrame.sizePolicy().hasHeightForWidth())
        self.lendBookFrame.setSizePolicy(sizePolicy3)
        self.lendBookFrame.setFrameShape(QFrame.StyledPanel)
        self.lendBookFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.lendBookFrame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(10)
        self.gridLayout_3.setVerticalSpacing(15)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.lendKdnInput = QLineEdit(self.lendBookFrame)
        self.lendKdnInput.setObjectName(u"lendKdnInput")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.lendKdnInput.sizePolicy().hasHeightForWidth())
        self.lendKdnInput.setSizePolicy(sizePolicy4)
        self.lendKdnInput.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.lendKdnInput, 3, 1, 1, 1)

        self.label_30 = QLabel(self.lendBookFrame)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setStyleSheet(u"QLabel{\n"
"	font: 12px \"Ethnocentric\";\n"
"	color: rgb(170, 0, 0);\n"
"}")
        self.label_30.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_30, 3, 0, 1, 1)

        self.label_25 = QLabel(self.lendBookFrame)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setStyleSheet(u"QLabel{\n"
"	font: 12px \"Ethnocentric\";\n"
"	color: rgb(170, 0, 0);\n"
"}")
        self.label_25.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_25, 0, 0, 1, 1)

        self.label_26 = QLabel(self.lendBookFrame)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setStyleSheet(u"QLabel{\n"
"	font: 12px \"Ethnocentric\";\n"
"	color: rgb(170, 0, 0);\n"
"}")
        self.label_26.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_26, 1, 0, 1, 1)

        self.lemdIsbnInput = QLineEdit(self.lendBookFrame)
        self.lemdIsbnInput.setObjectName(u"lemdIsbnInput")
        sizePolicy4.setHeightForWidth(self.lemdIsbnInput.sizePolicy().hasHeightForWidth())
        self.lemdIsbnInput.setSizePolicy(sizePolicy4)
        self.lemdIsbnInput.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.lemdIsbnInput, 0, 1, 1, 1)

        self.lendTitleInput = QLineEdit(self.lendBookFrame)
        self.lendTitleInput.setObjectName(u"lendTitleInput")
        sizePolicy4.setHeightForWidth(self.lendTitleInput.sizePolicy().hasHeightForWidth())
        self.lendTitleInput.setSizePolicy(sizePolicy4)
        self.lendTitleInput.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.lendTitleInput, 1, 1, 1, 1)

        self.lendDayBox = QComboBox(self.lendBookFrame)
        self.lendDayBox.addItem("")
        self.lendDayBox.addItem("")
        self.lendDayBox.addItem("")
        self.lendDayBox.setObjectName(u"lendDayBox")
        self.lendDayBox.setLayoutDirection(Qt.LeftToRight)
        self.lendDayBox.setMaxVisibleItems(4)

        self.gridLayout_3.addWidget(self.lendDayBox, 4, 1, 1, 1, Qt.AlignHCenter)

        self.label_27 = QLabel(self.lendBookFrame)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setStyleSheet(u"QLabel{\n"
"	font: 12px \"Ethnocentric\";\n"
"	color: rgb(170, 0, 0);\n"
"}")
        self.label_27.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_27, 4, 0, 1, 1)

        self.label_29 = QLabel(self.lendBookFrame)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setStyleSheet(u"QLabel{\n"
"	font: 12px \"Ethnocentric\";\n"
"	color: rgb(170, 0, 0);\n"
"}")
        self.label_29.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_29, 5, 0, 1, 1)

        self.lendDateLabel = QLabel(self.lendBookFrame)
        self.lendDateLabel.setObjectName(u"lendDateLabel")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.lendDateLabel.sizePolicy().hasHeightForWidth())
        self.lendDateLabel.setSizePolicy(sizePolicy5)
        self.lendDateLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.lendDateLabel, 5, 1, 1, 1)


        self.verticalLayout_20.addWidget(self.lendBookFrame, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_19.addWidget(self.frame_18)

        self.frame_21 = QFrame(self.frame_19)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setStyleSheet(u"QPushButton{\n"
"	border: 1px solid rgba(170, 0, 0,165);\n"
"	padding: 2px 20px;\n"
"	border-radius: 2%;\n"
"	color: rgb(255, 0, 0)\n"
"}\n"
"\n"
"QPushButton::Hover{\n"
"	border: 1.4px solid rgb(255, 0, 0);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 0, 0, 70), stop:1 rgba(65, 0, 0, 70));\n"
"	\n"
"}\n"
"\n"
"QPushButton::Pressed{\n"
"	border: 1.4px solid;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0  rgba(65, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));\n"
"	border-color: rgb(255, 0, 0);\n"
"	color: #FFF;\n"
"}")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lendBtn = QPushButton(self.frame_21)
        self.lendBtn.setObjectName(u"lendBtn")
        self.lendBtn.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.lendBtn, 0, Qt.AlignHCenter)


        self.verticalLayout_19.addWidget(self.frame_21, 0, Qt.AlignBottom)


        self.verticalLayout_18.addWidget(self.frame_19)

        self.stackedWidget.addWidget(self.lendView)
        self.helpView = QWidget()
        self.helpView.setObjectName(u"helpView")
        self.verticalLayout_25 = QVBoxLayout(self.helpView)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.frame_27 = QFrame(self.helpView)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_27)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(9, 9, 9, 0)
        self.frame_28 = QFrame(self.frame_27)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setMinimumSize(QSize(0, 10))
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_28)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.label_34 = QLabel(self.frame_28)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setStyleSheet(u"QLabel{\n"
"	\n"
"	font: 26pt \"Ethnocentric\";\n"
"}")
        self.label_34.setAlignment(Qt.AlignCenter)

        self.verticalLayout_28.addWidget(self.label_34)


        self.verticalLayout_27.addWidget(self.frame_28, 0, Qt.AlignTop)

        self.line_6 = QFrame(self.frame_27)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_27.addWidget(self.line_6)

        self.frame_29 = QFrame(self.frame_27)
        self.frame_29.setObjectName(u"frame_29")
        sizePolicy3.setHeightForWidth(self.frame_29.sizePolicy().hasHeightForWidth())
        self.frame_29.setSizePolicy(sizePolicy3)
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_19.setSpacing(10)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.frame_31 = QFrame(self.frame_29)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setStyleSheet(u"QPushButton{\n"
"	border: 1px solid;\n"
"	padding: 2px 20px;\n"
"	border-radius: 2%;\n"
"	color: rgb(255, 0, 0)\n"
"}\n"
"\n"
"QPushButton::Hover{\n"
"	border: 1.4px solid rgba(255, 47, 47, 25);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 0, 0, 45), stop:1 rgba(65, 0, 0, 45));\n"
"	color: #FFF;\n"
"}\n"
"\n"
"QPushButton::Pressed{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0  rgba(65, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));\n"
"	border-color: rgb(255, 0, 0);\n"
"	color: rgb(238, 238, 238);\n"
"}\n"
"\n"
"\n"
"QPushButton::Focus{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0  rgba(65, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));\n"
"	border-color: rgb(255, 0, 0);\n"
"	color: rgb(238, 238, 238);\n"
"}")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_31)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.frame_33 = QFrame(self.frame_31)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setStyleSheet(u"QPushButton{\n"
"	border: 1px solid rgba(170, 0, 0,165);\n"
"	padding: 2px 20px;\n"
"	border-radius: 2%;\n"
"	color: rgb(255, 0, 0)\n"
"}\n"
"\n"
"QPushButton::Hover{\n"
"	border: 1.2px solid rgb(255, 0, 0);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 0, 0, 70), stop:1 rgba(65, 0, 0, 70));\n"
"	\n"
"}\n"
"\n"
"QPushButton::Pressed{\n"
"	border: 1.4px solid;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0  rgba(65, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));\n"
"	border-color: rgb(255, 0, 0);\n"
"	color: #FFF;\n"
"}\n"
"\n"
"QPushButton::Focus{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0  rgba(65, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));\n"
"	border: 1.4px solid rgb(255, 0, 0);\n"
"	color: #FFF;\n"
"}")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_33)
        self.verticalLayout_31.setSpacing(20)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 25, 0, 10)
        self.comHelpBtn = QPushButton(self.frame_33)
        self.comHelpBtn.setObjectName(u"comHelpBtn")

        self.verticalLayout_31.addWidget(self.comHelpBtn)

        self.indexHelpBtn = QPushButton(self.frame_33)
        self.indexHelpBtn.setObjectName(u"indexHelpBtn")

        self.verticalLayout_31.addWidget(self.indexHelpBtn)

        self.userHelpBtn = QPushButton(self.frame_33)
        self.userHelpBtn.setObjectName(u"userHelpBtn")

        self.verticalLayout_31.addWidget(self.userHelpBtn)

        self.importHelpBtn = QPushButton(self.frame_33)
        self.importHelpBtn.setObjectName(u"importHelpBtn")

        self.verticalLayout_31.addWidget(self.importHelpBtn)


        self.verticalLayout_29.addWidget(self.frame_33, 0, Qt.AlignTop)


        self.horizontalLayout_19.addWidget(self.frame_31, 0, Qt.AlignLeft)

        self.frame_32 = QFrame(self.frame_29)
        self.frame_32.setObjectName(u"frame_32")
        sizePolicy.setHeightForWidth(self.frame_32.sizePolicy().hasHeightForWidth())
        self.frame_32.setSizePolicy(sizePolicy)
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_32)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.helpTextHeadLabel = QLabel(self.frame_32)
        self.helpTextHeadLabel.setObjectName(u"helpTextHeadLabel")
        self.helpTextHeadLabel.setStyleSheet(u"QLabel{\n"
"	\n"
"	font: 14pt \"Ethnocentric\";\n"
"}")
        self.helpTextHeadLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_30.addWidget(self.helpTextHeadLabel, 0, Qt.AlignTop)

        self.helpTextLabel = QLabel(self.frame_32)
        self.helpTextLabel.setObjectName(u"helpTextLabel")
        sizePolicy3.setHeightForWidth(self.helpTextLabel.sizePolicy().hasHeightForWidth())
        self.helpTextLabel.setSizePolicy(sizePolicy3)
        self.helpTextLabel.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_30.addWidget(self.helpTextLabel)

        self.loadBackupBtn = QPushButton(self.frame_32)
        self.loadBackupBtn.setObjectName(u"loadBackupBtn")
        self.loadBackupBtn.setStyleSheet(u"QPushButton{\n"
"	border: 1px solid rgba(170, 0, 0,165);\n"
"	padding: 2px 20px;\n"
"	border-radius: 2%;\n"
"	color: rgb(255, 0, 0)\n"
"}\n"
"\n"
"QPushButton::Hover{\n"
"	border: 1.4px solid rgb(255, 0, 0);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 0, 0, 70), stop:1 rgba(65, 0, 0, 70));\n"
"	\n"
"}\n"
"\n"
"QPushButton::Pressed{\n"
"	border: 1.4px solid;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0  rgba(65, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));\n"
"	border-color: rgb(255, 0, 0);\n"
"	color: #FFF;\n"
"}")

        self.verticalLayout_30.addWidget(self.loadBackupBtn, 0, Qt.AlignHCenter)


        self.horizontalLayout_19.addWidget(self.frame_32)


        self.verticalLayout_27.addWidget(self.frame_29)

        self.frame_30 = QFrame(self.frame_27)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setStyleSheet(u"QPushButton{\n"
"	border: 1px solid rgba(170, 0, 0,165);\n"
"	padding: 2px 20px;\n"
"	border-radius: 2%;\n"
"	color: rgb(255, 0, 0)\n"
"}\n"
"\n"
"QPushButton::Hover{\n"
"	border: 1.4px solid rgb(255, 0, 0);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 0, 0, 70), stop:1 rgba(65, 0, 0, 70));\n"
"	\n"
"}\n"
"\n"
"QPushButton::Pressed{\n"
"	border: 1.4px solid;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0  rgba(65, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));\n"
"	border-color: rgb(255, 0, 0);\n"
"	color: #FFF;\n"
"}")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 9, 0, 9)
        self.helpBackBtn = QPushButton(self.frame_30)
        self.helpBackBtn.setObjectName(u"helpBackBtn")

        self.horizontalLayout_18.addWidget(self.helpBackBtn, 0, Qt.AlignHCenter)


        self.verticalLayout_27.addWidget(self.frame_30, 0, Qt.AlignBottom)


        self.verticalLayout_25.addWidget(self.frame_27)

        self.stackedWidget.addWidget(self.helpView)
        self.indexView = QWidget()
        self.indexView.setObjectName(u"indexView")
        self.verticalLayout_8 = QVBoxLayout(self.indexView)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.indexView)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_2)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.indexHeaderLabel = QLabel(self.frame_2)
        self.indexHeaderLabel.setObjectName(u"indexHeaderLabel")
        self.indexHeaderLabel.setFont(font1)
        self.indexHeaderLabel.setStyleSheet(u"QLabel{\n"
"	\n"
"	font: 26pt \"Ethnocentric\";\n"
"}")
        self.indexHeaderLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.indexHeaderLabel, 0, Qt.AlignTop)

        self.line_7 = QFrame(self.frame_2)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_7.addWidget(self.line_7)

        self.frame_36 = QFrame(self.frame_2)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.frame_36)
        self.verticalLayout_34.setSpacing(0)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 9, 0, 9)
        self.indexTable = QTableWidget(self.frame_36)
        if (self.indexTable.columnCount() < 6):
            self.indexTable.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.indexTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.indexTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.indexTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.indexTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.indexTable.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        brush = QBrush(QColor(255, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setForeground(brush);
        self.indexTable.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.indexTable.setObjectName(u"indexTable")
        self.indexTable.setInputMethodHints(Qt.ImhNoEditMenu)
        self.indexTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.indexTable.setDragDropOverwriteMode(False)
        self.indexTable.setAlternatingRowColors(True)
        self.indexTable.setSelectionMode(QAbstractItemView.SingleSelection)
        self.indexTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.indexTable.setSortingEnabled(True)

        self.verticalLayout_34.addWidget(self.indexTable)


        self.verticalLayout_7.addWidget(self.frame_36)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"QPushButton{\n"
"	border: 1px solid rgba(170, 0, 0,165);\n"
"	padding: 2px 20px;\n"
"	border-radius: 2%;\n"
"	color: rgb(255, 0, 0)\n"
"}\n"
"\n"
"QPushButton::Hover{\n"
"	border: 1.4px solid rgb(255, 0, 0);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 0, 0, 70), stop:1 rgba(65, 0, 0, 70));\n"
"	\n"
"}\n"
"\n"
"QPushButton::Pressed{\n"
"	border: 1.4px solid;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0  rgba(65, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));\n"
"	border-color: rgb(255, 0, 0);\n"
"	color: #FFF;\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_8.setSpacing(10)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.avaibleBtn = QPushButton(self.frame_3)
        self.avaibleBtn.setObjectName(u"avaibleBtn")

        self.horizontalLayout_8.addWidget(self.avaibleBtn)

        self.index_btn_delete = QPushButton(self.frame_3)
        self.index_btn_delete.setObjectName(u"index_btn_delete")

        self.horizontalLayout_8.addWidget(self.index_btn_delete)

        self.index_btn_add = QPushButton(self.frame_3)
        self.index_btn_add.setObjectName(u"index_btn_add")

        self.horizontalLayout_8.addWidget(self.index_btn_add)


        self.verticalLayout_7.addWidget(self.frame_3, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_8.addWidget(self.frame_2)

        self.stackedWidget.addWidget(self.indexView)
        self.addBookView = QWidget()
        self.addBookView.setObjectName(u"addBookView")
        self.verticalLayout_10 = QVBoxLayout(self.addBookView)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.addBookView)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_4)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(9, 9, 9, 9)
        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"QLabel{\n"
"	\n"
"	font: 26pt \"Ethnocentric\";\n"
"}")

        self.verticalLayout_11.addWidget(self.label_2, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.line_8 = QFrame(self.frame_4)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.line_8.setFrameShape(QFrame.HLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_11.addWidget(self.line_8)

        self.frame_37 = QFrame(self.frame_4)
        self.frame_37.setObjectName(u"frame_37")
        sizePolicy3.setHeightForWidth(self.frame_37.sizePolicy().hasHeightForWidth())
        self.frame_37.setSizePolicy(sizePolicy3)
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.frame_37)
        self.verticalLayout_35.setSpacing(0)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.addBookFrame = QFrame(self.frame_37)
        self.addBookFrame.setObjectName(u"addBookFrame")
        self.addBookFrame.setFrameShape(QFrame.StyledPanel)
        self.addBookFrame.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.addBookFrame)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignCenter)
        self.formLayout.setHorizontalSpacing(30)
        self.formLayout.setVerticalSpacing(15)
        self.formLayout.setContentsMargins(0, -1, 0, 2)
        self.label_3 = QLabel(self.addBookFrame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"QLabel{\n"
"	font: 12px \"Ethnocentric\";\n"
"	color: rgb(170, 0, 0);\n"
"}")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_3)

        self.addisbnInput = QLineEdit(self.addBookFrame)
        self.addisbnInput.setObjectName(u"addisbnInput")
        self.addisbnInput.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.addisbnInput)

        self.label_4 = QLabel(self.addBookFrame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"QLabel{\n"
"	font: 12px \"Ethnocentric\";\n"
"	color: rgb(170, 0, 0);\n"
"}")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_4)

        self.addTitleInput = QLineEdit(self.addBookFrame)
        self.addTitleInput.setObjectName(u"addTitleInput")
        self.addTitleInput.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.addTitleInput)

        self.label_5 = QLabel(self.addBookFrame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"QLabel{\n"
"	font: 12px \"Ethnocentric\";\n"
"	color: rgb(170, 0, 0);\n"
"}")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_5)

        self.addAuthorInput = QLineEdit(self.addBookFrame)
        self.addAuthorInput.setObjectName(u"addAuthorInput")
        self.addAuthorInput.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.addAuthorInput)

        self.label_6 = QLabel(self.addBookFrame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"QLabel{\n"
"	font: 12px \"Ethnocentric\";\n"
"	color: rgb(170, 0, 0);\n"
"}")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_6)

        self.addGenreInput = QLineEdit(self.addBookFrame)
        self.addGenreInput.setObjectName(u"addGenreInput")
        self.addGenreInput.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.addGenreInput)

        self.label_7 = QLabel(self.addBookFrame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"QLabel{\n"
"	font: 12px \"Ethnocentric\";\n"
"	color: rgb(170, 0, 0);\n"
"}")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_7)

        self.addOutdateInput = QLineEdit(self.addBookFrame)
        self.addOutdateInput.setObjectName(u"addOutdateInput")
        self.addOutdateInput.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.addOutdateInput)


        self.verticalLayout_35.addWidget(self.addBookFrame, 0, Qt.AlignVCenter)


        self.verticalLayout_11.addWidget(self.frame_37, 0, Qt.AlignHCenter)

        self.frame_7 = QFrame(self.frame_4)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"QPushButton{\n"
"	border: 1px solid rgba(170, 0, 0,165);\n"
"	padding: 2px 20px;\n"
"	border-radius: 2%;\n"
"	color: rgb(255, 0, 0)\n"
"}\n"
"\n"
"QPushButton::Hover{\n"
"	border: 1.4px solid rgb(255, 0, 0);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 0, 0, 70), stop:1 rgba(65, 0, 0, 70));\n"
"	\n"
"}\n"
"\n"
"QPushButton::Pressed{\n"
"	border: 1.4px solid;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0  rgba(65, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));\n"
"	border-color: rgb(255, 0, 0);\n"
"	color: #FFF;\n"
"}")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_9.setSpacing(10)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.addBookBtn = QPushButton(self.frame_7)
        self.addBookBtn.setObjectName(u"addBookBtn")

        self.horizontalLayout_9.addWidget(self.addBookBtn)

        self.clearAddInputBtn = QPushButton(self.frame_7)
        self.clearAddInputBtn.setObjectName(u"clearAddInputBtn")

        self.horizontalLayout_9.addWidget(self.clearAddInputBtn)


        self.verticalLayout_11.addWidget(self.frame_7, 0, Qt.AlignHCenter)


        self.verticalLayout_10.addWidget(self.frame_4)

        self.stackedWidget.addWidget(self.addBookView)
        self.userlistView = QWidget()
        self.userlistView.setObjectName(u"userlistView")
        self.verticalLayout_13 = QVBoxLayout(self.userlistView)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.frame_38 = QFrame(self.userlistView)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.frame_38)
        self.verticalLayout_36.setSpacing(0)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.frame_39 = QFrame(self.frame_38)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.frame_39)
        self.verticalLayout_37.setSpacing(0)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.frame_39)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"QLabel{\n"
"	\n"
"	font: 26pt \"Ethnocentric\";\n"
"}")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_37.addWidget(self.label_8)

        self.line = QFrame(self.frame_39)
        self.line.setObjectName(u"line")
        self.line.setMinimumSize(QSize(1, 0))
        self.line.setStyleSheet(u"gridline-color: rgb(255, 0, 0);\n"
"background-color: rgb(255, 0, 0);")
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setMidLineWidth(0)
        self.line.setFrameShape(QFrame.HLine)

        self.verticalLayout_37.addWidget(self.line)

        self.frame_8 = QFrame(self.frame_39)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 9, 0, 0)
        self.userTable = QTableWidget(self.frame_8)
        if (self.userTable.columnCount() < 2):
            self.userTable.setColumnCount(2)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.userTable.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.userTable.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        self.userTable.setObjectName(u"userTable")
        self.userTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.userTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.userTable.setTextElideMode(Qt.ElideMiddle)
        self.userTable.setSortingEnabled(True)

        self.horizontalLayout_11.addWidget(self.userTable)

        self.frame_9 = QFrame(self.frame_8)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy)
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_9)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.frame_9)
        self.frame_11.setObjectName(u"frame_11")
        sizePolicy3.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy3)
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_11)
        self.verticalLayout_14.setSpacing(15)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.frame_11)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"QLabel{\n"
"	\n"
"	font: 16pt \"Ethnocentric\";\n"
"}")

        self.verticalLayout_14.addWidget(self.label_9, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.frame_12 = QFrame(self.frame_11)
        self.frame_12.setObjectName(u"frame_12")
        sizePolicy3.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy3)
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_12)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(12, 12, 12, 12)
        self.usermailLabel = QLabel(self.frame_12)
        self.usermailLabel.setObjectName(u"usermailLabel")

        self.gridLayout.addWidget(self.usermailLabel, 2, 1, 1, 1)

        self.kndNumLabel = QLabel(self.frame_12)
        self.kndNumLabel.setObjectName(u"kndNumLabel")

        self.gridLayout.addWidget(self.kndNumLabel, 0, 1, 1, 1)

        self.usernameLabel = QLabel(self.frame_12)
        self.usernameLabel.setObjectName(u"usernameLabel")

        self.gridLayout.addWidget(self.usernameLabel, 1, 1, 1, 1)

        self.label_10 = QLabel(self.frame_12)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"QLabel{\n"
"	font: 12px \"Ethnocentric\";\n"
"}")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_10, 1, 0, 1, 1)

        self.label_20 = QLabel(self.frame_12)
        self.label_20.setObjectName(u"label_20")
        sizePolicy2.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy2)
        self.label_20.setStyleSheet(u"QLabel{\n"
"	\n"
"	font: 12px \"Ethnocentric\";\n"
"}")
        self.label_20.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_20, 3, 0, 1, 1)

        self.usercityLabel = QLabel(self.frame_12)
        self.usercityLabel.setObjectName(u"usercityLabel")

        self.gridLayout.addWidget(self.usercityLabel, 5, 1, 1, 1)

        self.label_12 = QLabel(self.frame_12)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"QLabel{\n"
"	\n"
"	font: 12px \"Ethnocentric\";\n"
"}")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_12, 2, 0, 1, 1)

        self.label_14 = QLabel(self.frame_12)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"QLabel{\n"
"	font: 12px \"Ethnocentric\";\n"
"}")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_14, 0, 0, 1, 1)

        self.label_18 = QLabel(self.frame_12)
        self.label_18.setObjectName(u"label_18")
        sizePolicy2.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy2)
        self.label_18.setStyleSheet(u"QLabel{\n"
"	\n"
"	font: 12px \"Ethnocentric\";\n"
"}")
        self.label_18.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_18, 5, 0, 1, 1)

        self.useradressLabel = QLabel(self.frame_12)
        self.useradressLabel.setObjectName(u"useradressLabel")

        self.gridLayout.addWidget(self.useradressLabel, 6, 1, 1, 1)

        self.userphoneLabel = QLabel(self.frame_12)
        self.userphoneLabel.setObjectName(u"userphoneLabel")

        self.gridLayout.addWidget(self.userphoneLabel, 3, 1, 1, 1)

        self.label_16 = QLabel(self.frame_12)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setStyleSheet(u"QLabel{\n"
"	\n"
"	font: 12px \"Ethnocentric\";\n"
"}")
        self.label_16.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_16, 6, 0, 1, 1)

        self.label_11 = QLabel(self.frame_12)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"QLabel{\n"
"	font: 12px \"Ethnocentric\";\n"
"}")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_11, 7, 0, 1, 1)

        self.usergbLabel = QLabel(self.frame_12)
        self.usergbLabel.setObjectName(u"usergbLabel")

        self.gridLayout.addWidget(self.usergbLabel, 7, 1, 1, 1)


        self.verticalLayout_14.addWidget(self.frame_12)


        self.verticalLayout_12.addWidget(self.frame_11)

        self.frame_10 = QFrame(self.frame_9)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"QPushButton{\n"
"	border: 1px solid rgba(170, 0, 0,165);\n"
"	padding: 2px 20px;\n"
"	border-radius: 2%;\n"
"	color: rgb(255, 0, 0)\n"
"}\n"
"\n"
"QPushButton::Hover{\n"
"	border: 1.4px solid rgb(255, 0, 0);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 0, 0, 70), stop:1 rgba(65, 0, 0, 70));\n"
"	\n"
"}\n"
"\n"
"QPushButton::Pressed{\n"
"	border: 1.4px solid;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0  rgba(65, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));\n"
"	border-color: rgb(255, 0, 0);\n"
"	color: #FFF;\n"
"}")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.showUserBookBtn = QPushButton(self.frame_10)
        self.showUserBookBtn.setObjectName(u"showUserBookBtn")

        self.horizontalLayout_12.addWidget(self.showUserBookBtn)

        self.newUserBtn = QPushButton(self.frame_10)
        self.newUserBtn.setObjectName(u"newUserBtn")

        self.horizontalLayout_12.addWidget(self.newUserBtn)

        self.deleteUserBtn = QPushButton(self.frame_10)
        self.deleteUserBtn.setObjectName(u"deleteUserBtn")

        self.horizontalLayout_12.addWidget(self.deleteUserBtn)


        self.verticalLayout_12.addWidget(self.frame_10, 0, Qt.AlignHCenter)


        self.horizontalLayout_11.addWidget(self.frame_9)


        self.verticalLayout_37.addWidget(self.frame_8)


        self.verticalLayout_36.addWidget(self.frame_39)


        self.verticalLayout_13.addWidget(self.frame_38)

        self.stackedWidget.addWidget(self.userlistView)
        self.userBookView = QWidget()
        self.userBookView.setObjectName(u"userBookView")
        self.verticalLayout_22 = QVBoxLayout(self.userBookView)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.frame_22 = QFrame(self.userBookView)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_22)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(9, 9, 9, 0)
        self.frame_25 = QFrame(self.frame_22)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_25)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.userBookHeadLabel = QLabel(self.frame_25)
        self.userBookHeadLabel.setObjectName(u"userBookHeadLabel")
        self.userBookHeadLabel.setStyleSheet(u"QLabel{\n"
"	font: 26pt \"Ethnocentric\";\n"
"}")
        self.userBookHeadLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_24.addWidget(self.userBookHeadLabel, 0, Qt.AlignTop)

        self.line_2 = QFrame(self.frame_25)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_24.addWidget(self.line_2)


        self.verticalLayout_23.addWidget(self.frame_25, 0, Qt.AlignTop)

        self.frame_23 = QFrame(self.frame_22)
        self.frame_23.setObjectName(u"frame_23")
        sizePolicy3.setHeightForWidth(self.frame_23.sizePolicy().hasHeightForWidth())
        self.frame_23.setSizePolicy(sizePolicy3)
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_23)
        self.verticalLayout_26.setSpacing(9)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 9)
        self.frame_26 = QFrame(self.frame_23)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_17.setSpacing(6)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(20, 0, 20, 0)
        self.label_28 = QLabel(self.frame_26)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setStyleSheet(u"QLabel{\n"
"	\n"
"	color: rgb(206, 0, 0);\n"
"	\n"
"	font: 9pt \"Ethnocentric\";\n"
"}")

        self.horizontalLayout_17.addWidget(self.label_28, 0, Qt.AlignRight|Qt.AlignBottom)

        self.userBookKndLabel = QLabel(self.frame_26)
        self.userBookKndLabel.setObjectName(u"userBookKndLabel")
        self.userBookKndLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_17.addWidget(self.userBookKndLabel, 0, Qt.AlignLeft)

        self.label_31 = QLabel(self.frame_26)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setStyleSheet(u"QLabel{\n"
"	\n"
"	color: rgb(206, 0, 0);\n"
"	\n"
"	font: 9pt \"Ethnocentric\";\n"
"}")

        self.horizontalLayout_17.addWidget(self.label_31, 0, Qt.AlignRight|Qt.AlignBottom)

        self.userBooknameLabel = QLabel(self.frame_26)
        self.userBooknameLabel.setObjectName(u"userBooknameLabel")

        self.horizontalLayout_17.addWidget(self.userBooknameLabel, 0, Qt.AlignLeft)

        self.label_32 = QLabel(self.frame_26)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setStyleSheet(u"QLabel{\n"
"	\n"
"	color: rgb(206, 0, 0);\n"
"	\n"
"	font: 9pt \"Ethnocentric\";\n"
"}")

        self.horizontalLayout_17.addWidget(self.label_32, 0, Qt.AlignRight|Qt.AlignBottom)

        self.userBookMailLabel = QLabel(self.frame_26)
        self.userBookMailLabel.setObjectName(u"userBookMailLabel")

        self.horizontalLayout_17.addWidget(self.userBookMailLabel)

        self.label_33 = QLabel(self.frame_26)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setStyleSheet(u"QLabel{\n"
"	\n"
"	color: rgb(206, 0, 0);\n"
"	\n"
"	font: 9pt \"Ethnocentric\";\n"
"}")

        self.horizontalLayout_17.addWidget(self.label_33, 0, Qt.AlignRight|Qt.AlignBottom)

        self.userBookPhoneLabel = QLabel(self.frame_26)
        self.userBookPhoneLabel.setObjectName(u"userBookPhoneLabel")

        self.horizontalLayout_17.addWidget(self.userBookPhoneLabel)


        self.verticalLayout_26.addWidget(self.frame_26, 0, Qt.AlignVCenter)

        self.userBookTable = QTableWidget(self.frame_23)
        if (self.userBookTable.columnCount() < 5):
            self.userBookTable.setColumnCount(5)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.userBookTable.setHorizontalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.userBookTable.setHorizontalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.userBookTable.setHorizontalHeaderItem(2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.userBookTable.setHorizontalHeaderItem(3, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.userBookTable.setHorizontalHeaderItem(4, __qtablewidgetitem12)
        self.userBookTable.setObjectName(u"userBookTable")
        sizePolicy3.setHeightForWidth(self.userBookTable.sizePolicy().hasHeightForWidth())
        self.userBookTable.setSizePolicy(sizePolicy3)
        self.userBookTable.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.userBookTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.userBookTable.setAlternatingRowColors(True)
        self.userBookTable.setSelectionMode(QAbstractItemView.SingleSelection)
        self.userBookTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.userBookTable.setIconSize(QSize(16, 16))
        self.userBookTable.setSortingEnabled(True)

        self.verticalLayout_26.addWidget(self.userBookTable)


        self.verticalLayout_23.addWidget(self.frame_23)

        self.frame_24 = QFrame(self.frame_22)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.userBookBackBtn = QPushButton(self.frame_24)
        self.userBookBackBtn.setObjectName(u"userBookBackBtn")
        self.userBookBackBtn.setStyleSheet(u"QPushButton{\n"
"	border: 1px solid rgba(170, 0, 0,165);\n"
"	padding: 2px 20px;\n"
"	border-radius: 2%;\n"
"	color: rgb(255, 0, 0)\n"
"}\n"
"\n"
"QPushButton::Hover{\n"
"	border: 1.4px solid rgb(255, 0, 0);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 0, 0, 70), stop:1 rgba(65, 0, 0, 70));\n"
"	\n"
"}\n"
"\n"
"QPushButton::Pressed{\n"
"	border: 1.4px solid;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0  rgba(65, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));\n"
"	border-color: rgb(255, 0, 0);\n"
"	color: #FFF;\n"
"}")

        self.horizontalLayout_16.addWidget(self.userBookBackBtn, 0, Qt.AlignHCenter)


        self.verticalLayout_23.addWidget(self.frame_24)


        self.verticalLayout_22.addWidget(self.frame_22)

        self.stackedWidget.addWidget(self.userBookView)
        self.newUserView = QWidget()
        self.newUserView.setObjectName(u"newUserView")
        self.verticalLayout_15 = QVBoxLayout(self.newUserView)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(9, 9, 9, 0)
        self.label_13 = QLabel(self.newUserView)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"QLabel{\n"
"	font: 26pt \"Ethnocentric\";\n"
"}")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_13, 0, Qt.AlignTop)

        self.line_3 = QFrame(self.newUserView)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_15.addWidget(self.line_3)

        self.frame_35 = QFrame(self.newUserView)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_35)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.frame_13 = QFrame(self.frame_35)
        self.frame_13.setObjectName(u"frame_13")
        sizePolicy1.setHeightForWidth(self.frame_13.sizePolicy().hasHeightForWidth())
        self.frame_13.setSizePolicy(sizePolicy1)
        self.frame_13.setMinimumSize(QSize(400, 300))
        self.frame_13.setMaximumSize(QSize(400, 300))
        self.frame_13.setStyleSheet(u"QLabel{\n"
"	font: 12px \"Ethnocentric\";\n"
"	color: rgb(170, 0, 0);\n"
"}")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_13)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(20)
        self.newuserAdressInput = QLineEdit(self.frame_13)
        self.newuserAdressInput.setObjectName(u"newuserAdressInput")
        sizePolicy4.setHeightForWidth(self.newuserAdressInput.sizePolicy().hasHeightForWidth())
        self.newuserAdressInput.setSizePolicy(sizePolicy4)
        self.newuserAdressInput.setFocusPolicy(Qt.ClickFocus)
        self.newuserAdressInput.setMaxLength(50)
        self.newuserAdressInput.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.newuserAdressInput, 6, 1, 1, 1)

        self.label_24 = QLabel(self.frame_13)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout_2.addWidget(self.label_24, 7, 0, 1, 1, Qt.AlignHCenter)

        self.label_17 = QLabel(self.frame_13)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_17, 0, 0, 1, 1)

        self.label_23 = QLabel(self.frame_13)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_23, 6, 0, 1, 1)

        self.label_21 = QLabel(self.frame_13)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_21, 4, 0, 1, 1)

        self.newuserLastNameInput = QLineEdit(self.frame_13)
        self.newuserLastNameInput.setObjectName(u"newuserLastNameInput")
        sizePolicy4.setHeightForWidth(self.newuserLastNameInput.sizePolicy().hasHeightForWidth())
        self.newuserLastNameInput.setSizePolicy(sizePolicy4)
        self.newuserLastNameInput.setFocusPolicy(Qt.ClickFocus)
        self.newuserLastNameInput.setMaxLength(20)
        self.newuserLastNameInput.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.newuserLastNameInput, 1, 1, 1, 1)

        self.newuserPhoneInput = QLineEdit(self.frame_13)
        self.newuserPhoneInput.setObjectName(u"newuserPhoneInput")
        sizePolicy4.setHeightForWidth(self.newuserPhoneInput.sizePolicy().hasHeightForWidth())
        self.newuserPhoneInput.setSizePolicy(sizePolicy4)
        self.newuserPhoneInput.setFocusPolicy(Qt.ClickFocus)
        self.newuserPhoneInput.setInputMethodHints(Qt.ImhDigitsOnly)
        self.newuserPhoneInput.setMaxLength(15)
        self.newuserPhoneInput.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.newuserPhoneInput, 4, 1, 1, 1)

        self.newuserKndNumInput = QLineEdit(self.frame_13)
        self.newuserKndNumInput.setObjectName(u"newuserKndNumInput")
        sizePolicy4.setHeightForWidth(self.newuserKndNumInput.sizePolicy().hasHeightForWidth())
        self.newuserKndNumInput.setSizePolicy(sizePolicy4)
        self.newuserKndNumInput.setFocusPolicy(Qt.ClickFocus)
        self.newuserKndNumInput.setAlignment(Qt.AlignCenter)
        self.newuserKndNumInput.setReadOnly(True)

        self.gridLayout_2.addWidget(self.newuserKndNumInput, 0, 1, 1, 1)

        self.newuserNameInput = QLineEdit(self.frame_13)
        self.newuserNameInput.setObjectName(u"newuserNameInput")
        self.newuserNameInput.setFocusPolicy(Qt.ClickFocus)
        self.newuserNameInput.setMaxLength(20)
        self.newuserNameInput.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.newuserNameInput, 2, 1, 1, 1)

        self.newuserBirthdayInput = QLineEdit(self.frame_13)
        self.newuserBirthdayInput.setObjectName(u"newuserBirthdayInput")
        self.newuserBirthdayInput.setFocusPolicy(Qt.ClickFocus)
        self.newuserBirthdayInput.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.newuserBirthdayInput, 7, 1, 1, 1)

        self.label_22 = QLabel(self.frame_13)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_22, 5, 0, 1, 1)

        self.label_19 = QLabel(self.frame_13)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_19, 3, 0, 1, 1)

        self.label_15 = QLabel(self.frame_13)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_15, 1, 0, 1, 1)

        self.newuserCityInput = QLineEdit(self.frame_13)
        self.newuserCityInput.setObjectName(u"newuserCityInput")
        sizePolicy4.setHeightForWidth(self.newuserCityInput.sizePolicy().hasHeightForWidth())
        self.newuserCityInput.setSizePolicy(sizePolicy4)
        self.newuserCityInput.setFocusPolicy(Qt.ClickFocus)
        self.newuserCityInput.setMaxLength(30)
        self.newuserCityInput.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.newuserCityInput, 5, 1, 1, 1)

        self.newuserMailInput = QLineEdit(self.frame_13)
        self.newuserMailInput.setObjectName(u"newuserMailInput")
        sizePolicy4.setHeightForWidth(self.newuserMailInput.sizePolicy().hasHeightForWidth())
        self.newuserMailInput.setSizePolicy(sizePolicy4)
        self.newuserMailInput.setFocusPolicy(Qt.ClickFocus)
        self.newuserMailInput.setMaxLength(35)
        self.newuserMailInput.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.newuserMailInput, 3, 1, 1, 1)

        self.label_40 = QLabel(self.frame_13)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_40, 2, 0, 1, 1)


        self.verticalLayout_32.addWidget(self.frame_13, 0, Qt.AlignHCenter)


        self.verticalLayout_15.addWidget(self.frame_35)

        self.frame_16 = QFrame(self.newUserView)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.frame_14 = QFrame(self.frame_16)
        self.frame_14.setObjectName(u"frame_14")
        sizePolicy6 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.frame_14.sizePolicy().hasHeightForWidth())
        self.frame_14.setSizePolicy(sizePolicy6)
        self.frame_14.setStyleSheet(u"QPushButton{\n"
"	border: 1px solid rgba(170, 0, 0,165);\n"
"	padding: 2px 20px;\n"
"	border-radius: 2%;\n"
"	color: rgb(255, 0, 0)\n"
"}\n"
"\n"
"QPushButton::Hover{\n"
"	border: 1.4px solid rgb(255, 0, 0);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 0, 0, 70), stop:1 rgba(65, 0, 0, 70));\n"
"	\n"
"}\n"
"\n"
"QPushButton::Pressed{\n"
"	border: 1.4px solid;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0  rgba(65, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));\n"
"	border-color: rgb(255, 0, 0);\n"
"	color: #FFF;\n"
"}")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_13.setSpacing(10)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.newuserCreateBtn = QPushButton(self.frame_14)
        self.newuserCreateBtn.setObjectName(u"newuserCreateBtn")

        self.horizontalLayout_13.addWidget(self.newuserCreateBtn, 0, Qt.AlignHCenter)

        self.newuserClearBtn = QPushButton(self.frame_14)
        self.newuserClearBtn.setObjectName(u"newuserClearBtn")

        self.horizontalLayout_13.addWidget(self.newuserClearBtn, 0, Qt.AlignHCenter)


        self.horizontalLayout_14.addWidget(self.frame_14, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_15.addWidget(self.frame_16)

        self.stackedWidget.addWidget(self.newUserView)
        self.exportView = QWidget()
        self.exportView.setObjectName(u"exportView")
        self.verticalLayout_38 = QVBoxLayout(self.exportView)
        self.verticalLayout_38.setSpacing(6)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.frame_40 = QFrame(self.exportView)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.verticalLayout_39 = QVBoxLayout(self.frame_40)
        self.verticalLayout_39.setSpacing(0)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.frame_41 = QFrame(self.frame_40)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.frame_41)
        self.verticalLayout_40.setSpacing(0)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.label_35 = QLabel(self.frame_41)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setStyleSheet(u"QLabel{\n"
"	\n"
"	font: 26pt \"Ethnocentric\";\n"
"}")
        self.label_35.setAlignment(Qt.AlignCenter)

        self.verticalLayout_40.addWidget(self.label_35)


        self.verticalLayout_39.addWidget(self.frame_41, 0, Qt.AlignTop)

        self.line_9 = QFrame(self.frame_40)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.line_9.setFrameShape(QFrame.HLine)
        self.line_9.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_39.addWidget(self.line_9)

        self.frame_42 = QFrame(self.frame_40)
        self.frame_42.setObjectName(u"frame_42")
        sizePolicy3.setHeightForWidth(self.frame_42.sizePolicy().hasHeightForWidth())
        self.frame_42.setSizePolicy(sizePolicy3)
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_42)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.frame_44 = QFrame(self.frame_42)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.verticalLayout_41 = QVBoxLayout(self.frame_44)
        self.verticalLayout_41.setSpacing(6)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.frame_49 = QFrame(self.frame_44)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setFrameShape(QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QFrame.Raised)
        self.verticalLayout_44 = QVBoxLayout(self.frame_49)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.label_36 = QLabel(self.frame_49)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setStyleSheet(u"QLabel{\n"
"	\n"
"	font: 16pt \"Ethnocentric\";\n"
"}")
        self.label_36.setAlignment(Qt.AlignCenter)

        self.verticalLayout_44.addWidget(self.label_36, 0, Qt.AlignTop)


        self.verticalLayout_41.addWidget(self.frame_49, 0, Qt.AlignVCenter)

        self.frame_50 = QFrame(self.frame_44)
        self.frame_50.setObjectName(u"frame_50")
        sizePolicy2.setHeightForWidth(self.frame_50.sizePolicy().hasHeightForWidth())
        self.frame_50.setSizePolicy(sizePolicy2)
        self.frame_50.setFrameShape(QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QFrame.Raised)
        self.verticalLayout_45 = QVBoxLayout(self.frame_50)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.label_37 = QLabel(self.frame_50)
        self.label_37.setObjectName(u"label_37")
        sizePolicy2.setHeightForWidth(self.label_37.sizePolicy().hasHeightForWidth())
        self.label_37.setSizePolicy(sizePolicy2)
        self.label_37.setAlignment(Qt.AlignCenter)

        self.verticalLayout_45.addWidget(self.label_37)


        self.verticalLayout_41.addWidget(self.frame_50, 0, Qt.AlignVCenter)

        self.frame_47 = QFrame(self.frame_44)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setFrameShape(QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.verticalLayout_42 = QVBoxLayout(self.frame_47)
        self.verticalLayout_42.setSpacing(0)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.frame_46 = QFrame(self.frame_47)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_46)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.importFileInput = QLineEdit(self.frame_46)
        self.importFileInput.setObjectName(u"importFileInput")
        sizePolicy4.setHeightForWidth(self.importFileInput.sizePolicy().hasHeightForWidth())
        self.importFileInput.setSizePolicy(sizePolicy4)
        self.importFileInput.setMinimumSize(QSize(250, 0))
        self.importFileInput.setMaximumSize(QSize(350, 16777215))
        self.importFileInput.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_22.addWidget(self.importFileInput)

        self.importSearchFileBtn = QPushButton(self.frame_46)
        self.importSearchFileBtn.setObjectName(u"importSearchFileBtn")
        self.importSearchFileBtn.setStyleSheet(u"QPushButton{\n"
"	border: 1px solid rgba(170, 0, 0,165);\n"
"	padding: 2px 20px;\n"
"	border-radius: 2%;\n"
"	color: rgb(255, 0, 0)\n"
"}\n"
"\n"
"QPushButton::Hover{\n"
"	border: 1.4px solid rgb(255, 0, 0);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 0, 0, 70), stop:1 rgba(65, 0, 0, 70));\n"
"	\n"
"}\n"
"\n"
"QPushButton::Pressed{\n"
"	border: 1.4px solid;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0  rgba(65, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));\n"
"	border-color: rgb(255, 0, 0);\n"
"	color: #FFF;\n"
"}")

        self.horizontalLayout_22.addWidget(self.importSearchFileBtn)


        self.verticalLayout_42.addWidget(self.frame_46)


        self.verticalLayout_41.addWidget(self.frame_47)

        self.importDataBtn = QPushButton(self.frame_44)
        self.importDataBtn.setObjectName(u"importDataBtn")
        self.importDataBtn.setStyleSheet(u"QPushButton{\n"
"	border: 1px solid rgba(170, 0, 0,165);\n"
"	padding: 2px 20px;\n"
"	border-radius: 2%;\n"
"	color: rgb(255, 0, 0)\n"
"}\n"
"\n"
"QPushButton::Hover{\n"
"	border: 1.4px solid rgb(255, 0, 0);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 0, 0, 70), stop:1 rgba(65, 0, 0, 70));\n"
"	\n"
"}\n"
"\n"
"QPushButton::Pressed{\n"
"	border: 1.4px solid;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0  rgba(65, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));\n"
"	border-color: rgb(255, 0, 0);\n"
"	color: #FFF;\n"
"}")

        self.verticalLayout_41.addWidget(self.importDataBtn, 0, Qt.AlignHCenter)


        self.horizontalLayout_21.addWidget(self.frame_44, 0, Qt.AlignHCenter)

        self.frame_45 = QFrame(self.frame_42)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.verticalLayout_43 = QVBoxLayout(self.frame_45)
        self.verticalLayout_43.setSpacing(0)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.frame_51 = QFrame(self.frame_45)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setFrameShape(QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QFrame.Raised)
        self.verticalLayout_46 = QVBoxLayout(self.frame_51)
        self.verticalLayout_46.setSpacing(0)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.verticalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.label_38 = QLabel(self.frame_51)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setStyleSheet(u"QLabel{\n"
"	\n"
"	font: 16pt \"Ethnocentric\";\n"
"}")
        self.label_38.setAlignment(Qt.AlignCenter)

        self.verticalLayout_46.addWidget(self.label_38)


        self.verticalLayout_43.addWidget(self.frame_51, 0, Qt.AlignVCenter)

        self.frame_52 = QFrame(self.frame_45)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setFrameShape(QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QFrame.Raised)
        self.verticalLayout_47 = QVBoxLayout(self.frame_52)
        self.verticalLayout_47.setSpacing(9)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.verticalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.label_39 = QLabel(self.frame_52)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setAlignment(Qt.AlignCenter)
        self.label_39.setWordWrap(True)

        self.verticalLayout_47.addWidget(self.label_39, 0, Qt.AlignVCenter)

        self.exportFileInputbox = QComboBox(self.frame_52)
        self.exportFileInputbox.addItem("")
        self.exportFileInputbox.addItem("")
        self.exportFileInputbox.setObjectName(u"exportFileInputbox")
        self.exportFileInputbox.setMinimumSize(QSize(150, 0))
        self.exportFileInputbox.setMaximumSize(QSize(150, 16777215))
        self.exportFileInputbox.setInsertPolicy(QComboBox.InsertAtBottom)

        self.verticalLayout_47.addWidget(self.exportFileInputbox, 0, Qt.AlignHCenter)

        self.exportFileTypeBox = QComboBox(self.frame_52)
        self.exportFileTypeBox.addItem("")
        self.exportFileTypeBox.addItem("")
        self.exportFileTypeBox.addItem("")
        self.exportFileTypeBox.setObjectName(u"exportFileTypeBox")
        self.exportFileTypeBox.setMinimumSize(QSize(150, 0))
        self.exportFileTypeBox.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_47.addWidget(self.exportFileTypeBox, 0, Qt.AlignHCenter)


        self.verticalLayout_43.addWidget(self.frame_52)

        self.frame_48 = QFrame(self.frame_45)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setFrameShape(QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_48)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(9, 9, 9, 0)
        self.exportDataBtn = QPushButton(self.frame_48)
        self.exportDataBtn.setObjectName(u"exportDataBtn")
        self.exportDataBtn.setStyleSheet(u"QPushButton{\n"
"	border: 1px solid rgba(170, 0, 0,165);\n"
"	padding: 2px 20px;\n"
"	border-radius: 2%;\n"
"	color: rgb(255, 0, 0)\n"
"}\n"
"\n"
"QPushButton::Hover{\n"
"	border: 1.4px solid rgb(255, 0, 0);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 0, 0, 70), stop:1 rgba(65, 0, 0, 70));\n"
"	\n"
"}\n"
"\n"
"QPushButton::Pressed{\n"
"	border: 1.4px solid;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0  rgba(65, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));\n"
"	border-color: rgb(255, 0, 0);\n"
"	color: #FFF;\n"
"}")

        self.horizontalLayout_23.addWidget(self.exportDataBtn, 0, Qt.AlignHCenter)


        self.verticalLayout_43.addWidget(self.frame_48, 0, Qt.AlignBottom)


        self.horizontalLayout_21.addWidget(self.frame_45)


        self.verticalLayout_39.addWidget(self.frame_42)

        self.frame_43 = QFrame(self.frame_40)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_43)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.exportBackBtn = QPushButton(self.frame_43)
        self.exportBackBtn.setObjectName(u"exportBackBtn")
        self.exportBackBtn.setStyleSheet(u"QPushButton{\n"
"	border: 1px solid rgba(170, 0, 0,165);\n"
"	padding: 2px 20px;\n"
"	border-radius: 2%;\n"
"	color: rgb(255, 0, 0)\n"
"}\n"
"\n"
"QPushButton::Hover{\n"
"	border: 1.4px solid rgb(255, 0, 0);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 0, 0, 70), stop:1 rgba(65, 0, 0, 70));\n"
"	\n"
"}\n"
"\n"
"QPushButton::Pressed{\n"
"	border: 1.4px solid;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0  rgba(65, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));\n"
"	border-color: rgb(255, 0, 0);\n"
"	color: #FFF;\n"
"}")

        self.horizontalLayout_20.addWidget(self.exportBackBtn)


        self.verticalLayout_39.addWidget(self.frame_43, 0, Qt.AlignHCenter|Qt.AlignBottom)


        self.verticalLayout_38.addWidget(self.frame_40)

        self.stackedWidget.addWidget(self.exportView)
        self.avaibleView = QWidget()
        self.avaibleView.setObjectName(u"avaibleView")
        self.verticalLayout_9 = QVBoxLayout(self.avaibleView)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.availbleHeadFrame = QWidget(self.avaibleView)
        self.availbleHeadFrame.setObjectName(u"availbleHeadFrame")
        self.verticalLayout_16 = QVBoxLayout(self.availbleHeadFrame)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.availbleHeadFrame)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"QLabel{\n"
"	\n"
"	font: 26pt \"Ethnocentric\";\n"
"}")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.label)


        self.verticalLayout_9.addWidget(self.availbleHeadFrame, 0, Qt.AlignTop)

        self.line_4 = QFrame(self.avaibleView)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_9.addWidget(self.line_4)

        self.frame_15 = QFrame(self.avaibleView)
        self.frame_15.setObjectName(u"frame_15")
        sizePolicy3.setHeightForWidth(self.frame_15.sizePolicy().hasHeightForWidth())
        self.frame_15.setSizePolicy(sizePolicy3)
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.frame_15)
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 9, 0, 0)
        self.tableAvaible = QTableWidget(self.frame_15)
        if (self.tableAvaible.columnCount() < 6):
            self.tableAvaible.setColumnCount(6)
        brush1 = QBrush(QColor(255, 0, 0, 255))
        brush1.setStyle(Qt.NoBrush)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setForeground(brush1);
        self.tableAvaible.setHorizontalHeaderItem(0, __qtablewidgetitem13)
        brush2 = QBrush(QColor(255, 0, 0, 255))
        brush2.setStyle(Qt.NoBrush)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setForeground(brush2);
        self.tableAvaible.setHorizontalHeaderItem(1, __qtablewidgetitem14)
        brush3 = QBrush(QColor(255, 0, 0, 255))
        brush3.setStyle(Qt.NoBrush)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setForeground(brush3);
        self.tableAvaible.setHorizontalHeaderItem(2, __qtablewidgetitem15)
        brush4 = QBrush(QColor(255, 0, 0, 255))
        brush4.setStyle(Qt.NoBrush)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setForeground(brush4);
        self.tableAvaible.setHorizontalHeaderItem(3, __qtablewidgetitem16)
        brush5 = QBrush(QColor(255, 0, 0, 255))
        brush5.setStyle(Qt.NoBrush)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setForeground(brush5);
        self.tableAvaible.setHorizontalHeaderItem(4, __qtablewidgetitem17)
        brush6 = QBrush(QColor(255, 0, 0, 255))
        brush6.setStyle(Qt.NoBrush)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setForeground(brush6);
        self.tableAvaible.setHorizontalHeaderItem(5, __qtablewidgetitem18)
        self.tableAvaible.setObjectName(u"tableAvaible")
        self.tableAvaible.setInputMethodHints(Qt.ImhNoEditMenu)
        self.tableAvaible.setEditTriggers(QAbstractItemView.AnyKeyPressed|QAbstractItemView.EditKeyPressed)
        self.tableAvaible.setDragDropOverwriteMode(False)
        self.tableAvaible.setAlternatingRowColors(True)
        self.tableAvaible.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableAvaible.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableAvaible.setTextElideMode(Qt.ElideLeft)
        self.tableAvaible.setSortingEnabled(True)
        self.tableAvaible.setColumnCount(6)

        self.verticalLayout_33.addWidget(self.tableAvaible)


        self.verticalLayout_9.addWidget(self.frame_15)

        self.frame_6 = QFrame(self.avaibleView)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"QPushButton{\n"
"	border: 1px solid rgba(170, 0, 0,165);\n"
"	padding: 2px 20px;\n"
"	border-radius: 2%;\n"
"	color: rgb(255, 0, 0)\n"
"}\n"
"\n"
"QPushButton::Hover{\n"
"	border: 1.4px solid rgb(255, 0, 0);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 0, 0, 70), stop:1 rgba(65, 0, 0, 70));\n"
"	\n"
"}\n"
"\n"
"QPushButton::Pressed{\n"
"	border: 1.4px solid;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0  rgba(65, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));\n"
"	border-color: rgb(255, 0, 0);\n"
"	color: #FFF;\n"
"}")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 9, 0, 3)
        self.resumeBookBtn = QPushButton(self.frame_6)
        self.resumeBookBtn.setObjectName(u"resumeBookBtn")

        self.horizontalLayout_10.addWidget(self.resumeBookBtn)


        self.verticalLayout_9.addWidget(self.frame_6, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.stackedWidget.addWidget(self.avaibleView)

        self.verticalLayout_4.addWidget(self.stackedWidget)


        self.horizontalLayout_7.addWidget(self.mainFrame)


        self.verticalLayout.addWidget(self.centerFrame)

        self.bottomFrame = QFrame(self.centralwidget)
        self.bottomFrame.setObjectName(u"bottomFrame")
        self.bottomFrame.setStyleSheet(u"QFrame{\n"
"	border: rgba(255, 0, 0, 0);\n"
"	border-radius: 25px;\n"
" }")
        self.bottomFrame.setFrameShape(QFrame.StyledPanel)
        self.bottomFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.bottomFrame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.leftFram = QFrame(self.bottomFrame)
        self.leftFram.setObjectName(u"leftFram")
        self.leftFram.setStyleSheet(u"border-radius: 25px;")
        self.leftFram.setFrameShape(QFrame.StyledPanel)
        self.leftFram.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.leftFram)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.version_label = QLabel(self.leftFram)
        self.version_label.setObjectName(u"version_label")
        self.version_label.setStyleSheet(u"QLabel{\n"
"	color:rgba(153, 153, 153, 130)\n"
"\n"
"}")

        self.horizontalLayout_6.addWidget(self.version_label, 0, Qt.AlignTop)


        self.horizontalLayout_4.addWidget(self.leftFram, 0, Qt.AlignLeft|Qt.AlignTop)

        self.rightFrame = QFrame(self.bottomFrame)
        self.rightFrame.setObjectName(u"rightFrame")
        self.rightFrame.setStyleSheet(u"border-radius: 25px;")
        self.rightFrame.setFrameShape(QFrame.StyledPanel)
        self.rightFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.rightFrame)
        self.horizontalLayout_5.setSpacing(20)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_34 = QFrame(self.rightFrame)
        self.frame_34.setObjectName(u"frame_34")
        sizePolicy3.setHeightForWidth(self.frame_34.sizePolicy().hasHeightForWidth())
        self.frame_34.setSizePolicy(sizePolicy3)
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_34)

        self.currentDateLabel = QLabel(self.rightFrame)
        self.currentDateLabel.setObjectName(u"currentDateLabel")
        self.currentDateLabel.setStyleSheet(u"QLabel{\n"
"	font: 16pt \"Digital-7\";\n"
"	color: rgb(199, 0, 0);\n"
"}\n"
"")
        self.currentDateLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.currentDateLabel, 0, Qt.AlignRight)

        self.currentTimeLabel = QLabel(self.rightFrame)
        self.currentTimeLabel.setObjectName(u"currentTimeLabel")
        font3 = QFont()
        font3.setFamilies([u"Digital-7"])
        font3.setPointSize(16)
        font3.setBold(False)
        font3.setItalic(False)
        self.currentTimeLabel.setFont(font3)
        self.currentTimeLabel.setStyleSheet(u"QLabel{\n"
"	font: 16pt \"Digital-7\";\n"
"	color: rgb(199, 0, 0);\n"
"}\n"
"")
        self.currentTimeLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.currentTimeLabel, 0, Qt.AlignLeft)


        self.horizontalLayout_4.addWidget(self.rightFrame)


        self.verticalLayout.addWidget(self.bottomFrame, 0, Qt.AlignBottom)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(7)
        self.lendDayBox.setCurrentIndex(0)
        self.exportFileInputbox.setCurrentIndex(-1)
        self.exportFileTypeBox.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Bibiolothekar", None))
        self.menu_btn.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.headerLabel.setText(QCoreApplication.translate("MainWindow", u"Bookworm", None))
        self.min_window_btn.setText("")
        self.max_window_btn.setText("")
        self.x_button.setText("")
        self.menu_btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.menu_btn_index.setText(QCoreApplication.translate("MainWindow", u"Index", None))
        self.menu_btn_awaylist.setText(QCoreApplication.translate("MainWindow", u"Ausgeliehen", None))
        self.menu_btn_userindex.setText(QCoreApplication.translate("MainWindow", u"Kundenindex", None))
        self.menu_btn_import.setText(QCoreApplication.translate("MainWindow", u"Importieren", None))
        self.menu_btn_backup.setText(QCoreApplication.translate("MainWindow", u"Backup", None))
        self.menu_btn_help.setText(QCoreApplication.translate("MainWindow", u"Hilfe", None))
        self.appLogoLabel.setText("")
        self.homeHeaderLabel.setText(QCoreApplication.translate("MainWindow", u"Willkommen", None))
        self.homeInfoLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Diese Software<br/>wurde f\u00fcr Karolin geschrieben.</p><p>Software <br/>Development &amp; Design <br/>by S3R43o3 2023</p></body></html>", None))
        self.socialGitBtn.setText(QCoreApplication.translate("MainWindow", u"  GitHub", None))
        self.lendHeaderLabel.setText(QCoreApplication.translate("MainWindow", u"Entleihen", None))
        self.lendKdnInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Bsp: 458971", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Kunden Nummer", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"ISBN", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Titel", None))
        self.lemdIsbnInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Bsp: 0123456", None))
        self.lendTitleInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"bsp: Der Klient", None))
        self.lendDayBox.setItemText(0, QCoreApplication.translate("MainWindow", u"14", None))
        self.lendDayBox.setItemText(1, QCoreApplication.translate("MainWindow", u"28", None))
        self.lendDayBox.setItemText(2, QCoreApplication.translate("MainWindow", u"60", None))

        self.lendDayBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"W\u00e4hle...", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Ausleihzeit (Tage)", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"R\u00fcckgabedatum", None))
        self.lendDateLabel.setText("")
        self.lendBtn.setText(QCoreApplication.translate("MainWindow", u"Entleihen", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Hilfe", None))
        self.comHelpBtn.setText(QCoreApplication.translate("MainWindow", u"Allgemein", None))
        self.indexHelpBtn.setText(QCoreApplication.translate("MainWindow", u"Index Hilfe", None))
        self.userHelpBtn.setText(QCoreApplication.translate("MainWindow", u"Kunden Hilfe", None))
        self.importHelpBtn.setText(QCoreApplication.translate("MainWindow", u"Datenimport", None))
        self.helpTextHeadLabel.setText(QCoreApplication.translate("MainWindow", u"Allgemein", None))
        self.helpTextLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.loadBackupBtn.setText(QCoreApplication.translate("MainWindow", u"Daten Wiederherstellen", None))
        self.helpBackBtn.setText(QCoreApplication.translate("MainWindow", u"Zur\u00fcck", None))
        self.indexHeaderLabel.setText(QCoreApplication.translate("MainWindow", u"B\u00fccherIndex", None))
        ___qtablewidgetitem = self.indexTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ISBN", None));
        ___qtablewidgetitem1 = self.indexTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Titel", None));
        ___qtablewidgetitem2 = self.indexTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Author", None));
        ___qtablewidgetitem3 = self.indexTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Genre", None));
        ___qtablewidgetitem4 = self.indexTable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"R\u00fcckgabe", None));
        ___qtablewidgetitem5 = self.indexTable.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Verf\u00fcgbar", None));
        self.avaibleBtn.setText(QCoreApplication.translate("MainWindow", u"Entleihen", None))
        self.index_btn_delete.setText(QCoreApplication.translate("MainWindow", u"L\u00f6schen", None))
        self.index_btn_add.setText(QCoreApplication.translate("MainWindow", u"Neu", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Neuer Buch Eintrag", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"ISBN", None))
        self.addisbnInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Bsp: 0123456", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Titel", None))
        self.addTitleInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"bsp: Der Klient", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Author", None))
        self.addAuthorInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"John Grisham", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Genre", None))
        self.addGenreInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Thriller", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Ausgabe", None))
        self.addOutdateInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"12.02.2023", None))
        self.addBookBtn.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.clearAddInputBtn.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Kundenindex", None))
        ___qtablewidgetitem6 = self.userTable.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Knd-Nummer", None));
        ___qtablewidgetitem7 = self.userTable.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Information", None))
        self.usermailLabel.setText("")
        self.kndNumLabel.setText("")
        self.usernameLabel.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Telefon", None))
        self.usercityLabel.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"E-Mail", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Knd. Nummer", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Wohnort", None))
        self.useradressLabel.setText("")
        self.userphoneLabel.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Adresse", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Geburtstag", None))
        self.usergbLabel.setText("")
        self.showUserBookBtn.setText(QCoreApplication.translate("MainWindow", u"B\u00fccher", None))
        self.newUserBtn.setText(QCoreApplication.translate("MainWindow", u"Neu", None))
        self.deleteUserBtn.setText(QCoreApplication.translate("MainWindow", u"L\u00f6schen", None))
        self.userBookHeadLabel.setText(QCoreApplication.translate("MainWindow", u"Nutzer Buchliste", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Kundennummer:", None))
        self.userBookKndLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.userBooknameLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"E-Mail:", None))
        self.userBookMailLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Telefon:", None))
        self.userBookPhoneLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        ___qtablewidgetitem8 = self.userBookTable.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"ISBN", None));
        ___qtablewidgetitem9 = self.userBookTable.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Titel", None));
        ___qtablewidgetitem10 = self.userBookTable.horizontalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Ausgabe Datum", None));
        ___qtablewidgetitem11 = self.userBookTable.horizontalHeaderItem(3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"R\u00fcckgabe Datum", None));
        ___qtablewidgetitem12 = self.userBookTable.horizontalHeaderItem(4)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Verzug", None));
        self.userBookBackBtn.setText(QCoreApplication.translate("MainWindow", u"Zur\u00fcck", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Neuer Nutzer", None))
        self.newuserAdressInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Hauptstra\u00dfe 1", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Geburtstag", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Knd-Nummer", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Adresse", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Telefon", None))
        self.newuserLastNameInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Max", None))
        self.newuserPhoneInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"015187654321", None))
        self.newuserKndNumInput.setText(QCoreApplication.translate("MainWindow", u" > Wird automatisch generiert.", None))
        self.newuserNameInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Mustermann", None))
        self.newuserBirthdayInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"12.02.1990", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Wohnort", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Mail", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.newuserCityInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Berlin", None))
        self.newuserMailInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"example@examplemail.com", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Vorname", None))
        self.newuserCreateBtn.setText(QCoreApplication.translate("MainWindow", u"Erstellen", None))
        self.newuserClearBtn.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Importieren / Exportieren", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Import", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Gebe einen Pfad zur Datei die Importiert werden soll.<br/>Beachte bitte das nur CSV-Datein<br/>f\u00fcr den B\u00fccherindex eingelesen werden k\u00f6nnen.</p></body></html>", None))
        self.importFileInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Hier Dateipfad eingeben...", None))
        self.importSearchFileBtn.setText(QCoreApplication.translate("MainWindow", u"Suchen", None))
        self.importDataBtn.setText(QCoreApplication.translate("MainWindow", u"Importieren", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>W\u00e4hle aus welche Daten und in welches Datei-Format exportiert werden soll.<br/><br/><br/>Die Daten werden in dein Download-Verzeichnis gespeichert.</p></body></html>", None))
        self.exportFileInputbox.setItemText(0, QCoreApplication.translate("MainWindow", u"Buchindex", None))
        self.exportFileInputbox.setItemText(1, QCoreApplication.translate("MainWindow", u"Kundenindex", None))

        self.exportFileInputbox.setCurrentText("")
        self.exportFileInputbox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"W\u00e4hle Daten...", None))
        self.exportFileTypeBox.setItemText(0, QCoreApplication.translate("MainWindow", u"CSV", None))
        self.exportFileTypeBox.setItemText(1, QCoreApplication.translate("MainWindow", u"JSON", None))
        self.exportFileTypeBox.setItemText(2, QCoreApplication.translate("MainWindow", u"TXT", None))

        self.exportFileTypeBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"W\u00e4hle Dateiformat...", None))
        self.exportDataBtn.setText(QCoreApplication.translate("MainWindow", u"Exportieren", None))
        self.exportBackBtn.setText(QCoreApplication.translate("MainWindow", u"Abbrechen", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Ausgeliehen", None))
        ___qtablewidgetitem13 = self.tableAvaible.horizontalHeaderItem(0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"ISBN", None));
        ___qtablewidgetitem14 = self.tableAvaible.horizontalHeaderItem(1)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Titel", None));
        ___qtablewidgetitem15 = self.tableAvaible.horizontalHeaderItem(2)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Author", None));
        ___qtablewidgetitem16 = self.tableAvaible.horizontalHeaderItem(3)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Genre", None));
        ___qtablewidgetitem17 = self.tableAvaible.horizontalHeaderItem(4)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"R\u00fcckgabe", None));
        ___qtablewidgetitem18 = self.tableAvaible.horizontalHeaderItem(5)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Verf\u00fcgbar", None));
        self.resumeBookBtn.setText(QCoreApplication.translate("MainWindow", u"Verf\u00fcgbar", None))
        self.version_label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.currentDateLabel.setText(QCoreApplication.translate("MainWindow", u"12.02.1990", None))
        self.currentTimeLabel.setText(QCoreApplication.translate("MainWindow", u"19:00", None))
    # retranslateUi

