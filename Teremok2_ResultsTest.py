# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Teremok2_ResultsTest.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(900, 570)
        self.printResults_button = QPushButton(Form)
        self.printResults_button.setObjectName(u"printResults_button")
        self.printResults_button.setGeometry(QRect(320, 520, 291, 41))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(14)
        self.printResults_button.setFont(font)
        self.printResults_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.printResults_button.setMouseTracking(True)
        self.printResults_button.setTabletTracking(False)
        self.printResults_button.setStyleSheet(u"QPushButton{\n"
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
        self.printResults_button.setCheckable(False)
        self.printResults_button.setAutoDefault(False)
        self.warning = QLabel(Form)
        self.warning.setObjectName(u"warning")
        self.warning.setGeometry(QRect(90, 340, 731, 91))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.warning.setFont(font1)
        self.warning.setAlignment(Qt.AlignCenter)
        self.warning.setWordWrap(True)
        self.OK_button = QPushButton(Form)
        self.OK_button.setObjectName(u"OK_button")
        self.OK_button.setGeometry(QRect(420, 470, 91, 41))
        self.OK_button.setFont(font)
        self.OK_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.OK_button.setMouseTracking(True)
        self.OK_button.setTabletTracking(False)
        self.OK_button.setStyleSheet(u"QPushButton{\n"
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
        self.OK_button.setCheckable(False)
        self.OK_button.setAutoDefault(False)
        self.rateDescription = QLabel(Form)
        self.rateDescription.setObjectName(u"rateDescription")
        self.rateDescription.setGeometry(QRect(60, 140, 731, 171))
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(False)
        self.rateDescription.setFont(font2)
        self.rateDescription.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.rateDescription.setWordWrap(True)
        self.windowTitle = QLabel(Form)
        self.windowTitle.setObjectName(u"windowTitle")
        self.windowTitle.setGeometry(QRect(380, 10, 155, 26))
        self.windowTitle.setFont(font1)
        self.windowTitle.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.windowTitle.setWordWrap(False)
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(60, 80, 591, 32))
        self.resultsString = QHBoxLayout(self.layoutWidget)
        self.resultsString.setObjectName(u"resultsString")
        self.resultsString.setContentsMargins(0, 0, 0, 0)
        self.lab_1 = QLabel(self.layoutWidget)
        self.lab_1.setObjectName(u"lab_1")
        self.lab_1.setFont(font2)
        self.lab_1.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lab_1.setWordWrap(False)

        self.resultsString.addWidget(self.lab_1)

        self.results_QLE = QLineEdit(self.layoutWidget)
        self.results_QLE.setObjectName(u"results_QLE")
        font3 = QFont()
        font3.setPointSize(14)
        self.results_QLE.setFont(font3)
        self.results_QLE.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid rgb(33, 33, 34);\n"
"}")
        self.results_QLE.setAlignment(Qt.AlignCenter)
        self.results_QLE.setReadOnly(True)

        self.resultsString.addWidget(self.results_QLE)

        self.lab_2 = QLabel(self.layoutWidget)
        self.lab_2.setObjectName(u"lab_2")
        self.lab_2.setFont(font2)
        self.lab_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lab_2.setWordWrap(False)

        self.resultsString.addWidget(self.lab_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.printResults_button.setText(QCoreApplication.translate("Form", u"\u0420\u0430\u0441\u043f\u0435\u0447\u0430\u0442\u0430\u0442\u044c \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u044b", None))
        self.warning.setText(QCoreApplication.translate("Form", u"* \u0422\u0435\u0441\u0442 \u0410\u0422\u0415\u041a \u043d\u0435 \u044f\u0432\u043b\u044f\u0435\u0442\u0441\u044f \u0434\u0438\u0430\u0433\u043d\u043e\u0441\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u043c \u0442\u0435\u0441\u0442\u043e\u043c, \u0430 \u0441\u043b\u0443\u0436\u0438\u0442 \u0434\u043b\u044f \u043e\u0446\u0435\u043d\u043a\u0438 \u0434\u0438\u043d\u0430\u043c\u0438\u043a\u0438. \u0422\u0435\u0441\u0442 \u043d\u0435 \u043f\u0440\u0435\u0434\u043d\u0430\u0437\u043d\u0430\u0447\u0435\u043d \u0434\u043b\u044f \u043f\u043e\u0434\u0442\u0432\u0435\u0440\u0436\u0434\u0435\u043d\u0438\u044f \u043d\u0430\u043b\u0438\u0447\u0438\u044f \u0430\u0443\u0442\u0438\u0437\u043c\u0430, \u0434\u043b\u044f \u0442\u043e\u0447\u043d\u043e\u0439 \u043f\u043e\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0438 \u0434\u0438\u0430\u0433\u043d\u043e\u0437\u0430 \u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u043e \u043e\u0431\u0440\u0430\u0442\u0438\u0442\u044c\u0441\u044f \u043a \u0441\u043f\u0435\u0446\u0438\u0430\u043b"
                        "\u0438\u0441\u0442\u0430\u043c.", None))
        self.OK_button.setText(QCoreApplication.translate("Form", u"\u041e\u041a", None))
        self.rateDescription.setText(QCoreApplication.translate("Form", u"\u0428\u043a\u0430\u043b\u0430 \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u043e\u0432:\n"
"10-15 \u043d\u0435 \u0430\u0443\u0442\u0438\u0447\u043d\u044b\u0439 \u0440\u0435\u0431\u0435\u043d\u043e\u043a, \u043f\u043e\u043b\u043d\u043e\u0441\u0442\u044c\u044e \u043d\u043e\u0440\u043c\u0430\u043b\u044c\u043d\u044b\u0439, \u0445\u043e\u0440\u043e\u0448\u043e \u0440\u0430\u0437\u0432\u0438\u0442\u044b\u0439 \u0440\u0435\u0431\u0435\u043d\u043e\u043a\n"
"16\u201330 \u043d\u0435 \u0430\u0443\u0442\u0438\u0447\u043d\u044b\u0439 \u0440\u0435\u0431\u0435\u043d\u043e\u043a, \u043d\u0435\u0431\u043e\u043b\u044c\u0448\u0438\u0435 \u043e\u0442\u043a\u043b\u043e\u043d\u0435\u043d\u0438\u044f \u0432 \u0441\u0442\u043e\u0440\u043e\u043d\u0443 \u0437\u0430\u0434\u0435\u0440\u0436\u043a\u0438 \u0440\u0430\u0437\u0432\u0438\u0442\u0438\u044f\n"
"31-40 \u043c\u044f\u0433\u043a\u0430\u044f \u0438\u043b\u0438 \u0443\u043c\u0435\u0440\u0435\u043d\u043d\u0430\u044f \u0441\u0442\u0435\u043f\u0435\u043d\u044c \u0430\u0443\u0442"
                        "\u0438\u0437\u043c\u0430\n"
"41-60 \u0441\u0440\u0435\u0434\u043d\u044f\u044f \u0441\u0442\u0435\u043f\u0435\u043d\u044c \u0430\u0443\u0442\u0438\u0437\u043c\u0430\n"
"61 \u0438 \u0432\u044b\u0448\u0435 \u0442\u044f\u0436\u0435\u043b\u044b\u0439 \u0430\u0443\u0442\u0438\u0437\u043c", None))
        self.windowTitle.setText(QCoreApplication.translate("Form", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u044b \u0442\u0435\u0441\u0442\u0430", None))
        self.lab_1.setText(QCoreApplication.translate("Form", u"\u0412\u0430\u0448 \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442 \u043f\u043e \u043e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u044e \u0442\u0435\u0441\u0442\u0430 \u0410\u0422\u0415\u041a:", None))
        self.results_QLE.setPlaceholderText(QCoreApplication.translate("Form", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442", None))
        self.lab_2.setText(QCoreApplication.translate("Form", u"\u0431\u0430\u043b\u043b\u043e\u0432.", None))
    # retranslateUi

