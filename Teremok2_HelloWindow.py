# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Teremok2_HelloWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_TeremokFirstWindow(object):
    def setupUi(self, TeremokFirstWindow):
        if not TeremokFirstWindow.objectName():
            TeremokFirstWindow.setObjectName(u"TeremokFirstWindow")
        TeremokFirstWindow.resize(720, 720)
        font = QFont()
        font.setFamilies([u"Rage Italic"])
        TeremokFirstWindow.setFont(font)
        TeremokFirstWindow.setStyleSheet(u"background-color: #FFFFFF;")
        self.centralwidget = QWidget(TeremokFirstWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.close_button = QPushButton(self.centralwidget)
        self.close_button.setObjectName(u"close_button")
        self.close_button.setGeometry(QRect(440, 20, 260, 50))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(20)
        self.close_button.setFont(font1)
        self.close_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.close_button.setMouseTracking(True)
        self.close_button.setTabletTracking(False)
        self.close_button.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(221, 255, 255, 1);\n"
"border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(221, 255, 255, 0.7);\n"
"border: 1px solid rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgba(221, 255, 255, 0.5);\n"
"border: 2px solid rgb(0, 0, 0);\n"
"}")
        self.close_button.setCheckable(False)
        self.close_button.setAutoDefault(False)
        self.openSys_button = QPushButton(self.centralwidget)
        self.openSys_button.setObjectName(u"openSys_button")
        self.openSys_button.setGeometry(QRect(210, 490, 300, 50))
        self.openSys_button.setFont(font1)
        self.openSys_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.openSys_button.setMouseTracking(True)
        self.openSys_button.setTabletTracking(False)
        self.openSys_button.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(221, 255, 255, 1);\n"
"border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(221, 255, 255, 0.7);\n"
"border: 1px solid rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgba(221, 255, 255, 0.5);\n"
"border: 2px solid rgb(0, 0, 0);\n"
"}")
        self.openSys_button.setCheckable(False)
        self.openSys_button.setAutoDefault(False)
        self.title = QFrame(self.centralwidget)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(40, 230, 650, 241))
        self.verticalLayout = QVBoxLayout(self.title)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.titleName = QLabel(self.title)
        self.titleName.setObjectName(u"titleName")
        font2 = QFont()
        font2.setFamilies([u"Comic Sans MS"])
        font2.setPointSize(64)
        font2.setWeight(QFont.Medium)
        font2.setItalic(False)
        self.titleName.setFont(font2)
        self.titleName.setStyleSheet(u"color: rgb(23, 109, 248);")
        self.titleName.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.titleName)

        self.titleDescription = QLabel(self.title)
        self.titleDescription.setObjectName(u"titleDescription")
        font3 = QFont()
        font3.setPointSize(24)
        self.titleDescription.setFont(font3)
        self.titleDescription.setAlignment(Qt.AlignCenter)
        self.titleDescription.setWordWrap(True)
        self.titleDescription.setMargin(15)

        self.verticalLayout.addWidget(self.titleDescription)

        TeremokFirstWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(TeremokFirstWindow)

        QMetaObject.connectSlotsByName(TeremokFirstWindow)
    # setupUi

    def retranslateUi(self, TeremokFirstWindow):
        TeremokFirstWindow.setWindowTitle(QCoreApplication.translate("TeremokFirstWindow", u"\u0422\u0435\u0440\u0435\u043c\u043e\u043a - \u041f\u0440\u0438\u0432\u0435\u0442\u0441\u0442\u0432\u0435\u043d\u043d\u043e\u0435 \u043e\u043a\u043d\u043e", None))
        self.close_button.setText(QCoreApplication.translate("TeremokFirstWindow", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c", None))
        self.openSys_button.setText(QCoreApplication.translate("TeremokFirstWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0441\u0438\u0441\u0442\u0435\u043c\u0443", None))
        self.titleName.setText(QCoreApplication.translate("TeremokFirstWindow", u"\u0422\u0415\u0420\u0415\u041c\u041e\u041a", None))
        self.titleDescription.setText(QCoreApplication.translate("TeremokFirstWindow", u"\u0421\u0438\u0441\u0442\u0435\u043c\u0430 \u0443\u0447\u0435\u0442\u0430 \u0434\u043b\u044f \u0446\u0435\u043d\u0442\u0440\u0430 \u043f\u043e\u043c\u043e\u0449\u0438 \u0434\u0435\u0442\u044f\u043c \u0441 \u041e\u0412\u0417", None))
    # retranslateUi

