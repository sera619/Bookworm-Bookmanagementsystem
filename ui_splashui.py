# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'splashui.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QProgressBar,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
import ressource_rc

class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        if not SplashScreen.objectName():
            SplashScreen.setObjectName(u"SplashScreen")
        SplashScreen.resize(450, 450)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SplashScreen.sizePolicy().hasHeightForWidth())
        SplashScreen.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u":/icons/fonts/favicon.ico", QSize(), QIcon.Normal, QIcon.Off)
        SplashScreen.setWindowIcon(icon)
        SplashScreen.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(SplashScreen)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(SplashScreen)
        self.frame.setObjectName(u"frame")
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet(u"QFrame{\n"
"	border: 1px solid rgba(200,0,0,120);\n"
"	border-radius: 225px;\n"
"	background-color: qlineargradient(spread:pad, x1:0.5175, y1:0.517, x2:0.983, y2:0.965909, stop:0.0738636 rgba(0, 0, 0, 226), stop:0.664773 rgba(33, 33, 33, 222), stop:1 rgba(57, 57, 57, 222));\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Plain)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(9, 16, 9, 16)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QFrame{\n"
"	border: None;\n"
"	background-color: None;\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(9)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, 0, -1, 0)
        self.iconLabel = QLabel(self.frame_4)
        self.iconLabel.setObjectName(u"iconLabel")
        self.iconLabel.setPixmap(QPixmap(u":/icons/fonts/appicon128x128.png"))
        self.iconLabel.setScaledContents(False)
        self.iconLabel.setMargin(37)

        self.verticalLayout_5.addWidget(self.iconLabel, 0, Qt.AlignHCenter)

        self.headerLabel = QLabel(self.frame_4)
        self.headerLabel.setObjectName(u"headerLabel")
        self.headerLabel.setStyleSheet(u"QLabel{	\n"
"	color: rgb(170, 0, 0);\n"
"	font: 24pt \"Ethnocentric\";\n"
"}\n"
"")
        self.headerLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.headerLabel)

        self.versionLabel = QLabel(self.frame_4)
        self.versionLabel.setObjectName(u"versionLabel")
        self.versionLabel.setStyleSheet(u"QLabel{	\n"
"	\n"
"	color: rgba(170, 0, 0, 180);\n"
"	font: 9pt \"Ethnocentric\";\n"
"}\n"
"")
        self.versionLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.versionLabel)


        self.verticalLayout_3.addWidget(self.frame_4)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setSpacing(12)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(9, 0, 9, 0)
        self.loadProgress = QProgressBar(self.frame_3)
        self.loadProgress.setObjectName(u"loadProgress")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.loadProgress.sizePolicy().hasHeightForWidth())
        self.loadProgress.setSizePolicy(sizePolicy1)
        self.loadProgress.setMinimumSize(QSize(350, 0))
        self.loadProgress.setStyleSheet(u"QProgressBar{\n"
"	border: solid 'darkred';\n"
"	border-radius: 10px;\n"
"	background-color: rgb(18, 18, 18);\n"
"	color: none;\n"
"	font-weight: 800;\n"
"}\n"
"\n"
"QProgressBar::Chunk{\n"
"	border-radius: 10px;\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 0, 0, 255), stop:1 rgba(65, 0, 0, 255));\n"
"\n"
"}")
        self.loadProgress.setValue(24)
        self.loadProgress.setAlignment(Qt.AlignCenter)
        self.loadProgress.setTextDirection(QProgressBar.TopToBottom)

        self.verticalLayout_4.addWidget(self.loadProgress, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"QLabel{	\n"
"	color: rgb(170, 0, 0);\n"
"	font: 12pt  \"Ethnocentric\";\n"
"}\n"
"")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_2, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_3.addWidget(self.frame_3, 0, Qt.AlignTop)

        self.cancelBtn = QPushButton(self.frame_2)
        self.cancelBtn.setObjectName(u"cancelBtn")
        self.cancelBtn.setStyleSheet(u"QPushButton{\n"
"	border: 1px solid rgba(170, 0, 0,165);\n"
"	padding: 2px 20px;\n"
"	border-radius: 2%;\n"
"	color: rgb(255, 0, 0);\n"
"background-color: rgba(0,0,0,0);\n"
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

        self.verticalLayout_3.addWidget(self.cancelBtn, 0, Qt.AlignHCenter)


        self.verticalLayout_2.addWidget(self.frame_2, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(SplashScreen)

        QMetaObject.connectSlotsByName(SplashScreen)
    # setupUi

    def retranslateUi(self, SplashScreen):
        SplashScreen.setWindowTitle(QCoreApplication.translate("SplashScreen", u"Form", None))
        self.iconLabel.setText("")
        self.headerLabel.setText(QCoreApplication.translate("SplashScreen", u"Bookworm", None))
        self.versionLabel.setText(QCoreApplication.translate("SplashScreen", u"TextLabel", None))
        self.label_2.setText(QCoreApplication.translate("SplashScreen", u"loading...", None))
        self.cancelBtn.setText(QCoreApplication.translate("SplashScreen", u"Cancel", None))
    # retranslateUi

