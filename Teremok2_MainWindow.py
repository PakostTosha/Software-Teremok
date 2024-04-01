# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Teremok2_MainWindow.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QDateEdit,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QListView, QMainWindow, QPlainTextEdit,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QTabWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setLayoutDirection(Qt.LeftToRight)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet(u"background-color: rgb(255,255,255);")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        font = QFont()
        font.setPointSize(14)
        self.tabWidget.setFont(font)
        self.tabWidget.setCursor(QCursor(Qt.ArrowCursor))
        self.tabWidget.setMouseTracking(False)
        self.tabWidget.setTabletTracking(False)
        self.tabWidget.setFocusPolicy(Qt.TabFocus)
        self.tabWidget.setStyleSheet(u"QTabBar::tab::!selected{\n"
"background-color: rgb(221, 255, 255);\n"
"}\n"
"QTabBar::tab::selected{\n"
"background-color: rgb(255, 255, 255);\n"
"border: none;\n"
"}\n"
"QWidget{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QTabBar::tab{\n"
"border: 1px solid rgb(0, 0, 0);\n"
"border-collapse: collapse;\n"
"padding: 5px 10px;\n"
"}")
        self.tab1_firstConsultation = QWidget()
        self.tab1_firstConsultation.setObjectName(u"tab1_firstConsultation")
        self.tab1_firstConsultation.setFocusPolicy(Qt.TabFocus)
        self.child_GB = QGroupBox(self.tab1_firstConsultation)
        self.child_GB.setObjectName(u"child_GB")
        self.child_GB.setGeometry(QRect(90, 10, 1121, 381))
        self.layoutWidget = QWidget(self.child_GB)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 30, 1081, 321))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.childFIO_label = QLabel(self.layoutWidget)
        self.childFIO_label.setObjectName(u"childFIO_label")
        self.childFIO_label.setFont(font)
        self.childFIO_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.childFIO_label)

        self.childFIO_input = QLineEdit(self.layoutWidget)
        self.childFIO_input.setObjectName(u"childFIO_input")
        self.childFIO_input.setFont(font)
        self.childFIO_input.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid rgb(33, 33, 34);\n"
"}")
        self.childFIO_input.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.childFIO_input)


        self.verticalLayout_8.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.birthday_label = QLabel(self.layoutWidget)
        self.birthday_label.setObjectName(u"birthday_label")
        self.birthday_label.setFont(font)
        self.birthday_label.setLayoutDirection(Qt.LeftToRight)
        self.birthday_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.birthday_label)

        self.birthday_input = QDateEdit(self.layoutWidget)
        self.birthday_input.setObjectName(u"birthday_input")
        self.birthday_input.setFont(font)
        self.birthday_input.setStyleSheet(u"QDateEdit{\n"
"border: 1px solid rgb(33, 33, 34);\n"
"padding: 1px;\n"
"}")
        self.birthday_input.setAlignment(Qt.AlignCenter)
        self.birthday_input.setButtonSymbols(QAbstractSpinBox.UpDownArrows)

        self.verticalLayout_2.addWidget(self.birthday_input)


        self.verticalLayout_8.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.diagnos_label = QLabel(self.layoutWidget)
        self.diagnos_label.setObjectName(u"diagnos_label")
        self.diagnos_label.setFont(font)
        self.diagnos_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.diagnos_label)

        self.diagnos_input = QLineEdit(self.layoutWidget)
        self.diagnos_input.setObjectName(u"diagnos_input")
        self.diagnos_input.setFont(font)
        self.diagnos_input.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid rgb(33, 33, 34);\n"
"}")
        self.diagnos_input.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.diagnos_input)


        self.verticalLayout_8.addLayout(self.verticalLayout_3)


        self.horizontalLayout.addLayout(self.verticalLayout_8)

        self.horizontalSpacer = QSpacerItem(30, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.aboutChild_label = QLabel(self.layoutWidget)
        self.aboutChild_label.setObjectName(u"aboutChild_label")
        self.aboutChild_label.setFont(font)
        self.aboutChild_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.aboutChild_label)

        self.aboutChild_input = QPlainTextEdit(self.layoutWidget)
        self.aboutChild_input.setObjectName(u"aboutChild_input")

        self.verticalLayout_4.addWidget(self.aboutChild_input)


        self.horizontalLayout.addLayout(self.verticalLayout_4)

        self.parent_GB = QGroupBox(self.tab1_firstConsultation)
        self.parent_GB.setObjectName(u"parent_GB")
        self.parent_GB.setGeometry(QRect(90, 420, 1121, 128))
        self.layoutWidget1 = QWidget(self.parent_GB)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(20, 30, 1081, 68))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.parentFIO_label = QLabel(self.layoutWidget1)
        self.parentFIO_label.setObjectName(u"parentFIO_label")
        self.parentFIO_label.setFont(font)
        self.parentFIO_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.parentFIO_label)

        self.parentFIO_input = QLineEdit(self.layoutWidget1)
        self.parentFIO_input.setObjectName(u"parentFIO_input")
        self.parentFIO_input.setFont(font)
        self.parentFIO_input.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid rgb(33, 33, 34);\n"
"}")
        self.parentFIO_input.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.parentFIO_input)


        self.horizontalLayout_3.addLayout(self.verticalLayout_9)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.passport_label = QLabel(self.layoutWidget1)
        self.passport_label.setObjectName(u"passport_label")
        self.passport_label.setFont(font)
        self.passport_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.passport_label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.passSeria_input = QLineEdit(self.layoutWidget1)
        self.passSeria_input.setObjectName(u"passSeria_input")
        self.passSeria_input.setFont(font)
        self.passSeria_input.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid rgb(33, 33, 34);\n"
"}")
        self.passSeria_input.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.passSeria_input)

        self.passNumber_input = QLineEdit(self.layoutWidget1)
        self.passNumber_input.setObjectName(u"passNumber_input")
        self.passNumber_input.setFont(font)
        self.passNumber_input.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid rgb(33, 33, 34);\n"
"}")
        self.passNumber_input.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.passNumber_input)


        self.verticalLayout_10.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_3.addLayout(self.verticalLayout_10)

        self.saveData_button = QPushButton(self.tab1_firstConsultation)
        self.saveData_button.setObjectName(u"saveData_button")
        self.saveData_button.setGeometry(QRect(969, 600, 251, 45))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(14)
        self.saveData_button.setFont(font1)
        self.saveData_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.saveData_button.setMouseTracking(True)
        self.saveData_button.setTabletTracking(False)
        self.saveData_button.setStyleSheet(u"QPushButton{\n"
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
        self.saveData_button.setCheckable(False)
        self.saveData_button.setAutoDefault(False)
        self.clearAll_button = QPushButton(self.tab1_firstConsultation)
        self.clearAll_button.setObjectName(u"clearAll_button")
        self.clearAll_button.setEnabled(False)
        self.clearAll_button.setGeometry(QRect(740, 600, 211, 45))
        self.clearAll_button.setFont(font1)
        self.clearAll_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.clearAll_button.setMouseTracking(True)
        self.clearAll_button.setTabletTracking(False)
        self.clearAll_button.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(0, 0, 0, 0.8);\n"
"color: rgba(221, 255, 255, 1);\n"
"border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(0, 0, 0, 0.6);\n"
"border: 1px solid rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgba(0, 0, 0, 0.4);\n"
"border: 2px solid rgb(0, 0, 0);\n"
"}")
        self.clearAll_button.setCheckable(False)
        self.clearAll_button.setAutoDefault(False)
        self.childFIO_label_2 = QLabel(self.tab1_firstConsultation)
        self.childFIO_label_2.setObjectName(u"childFIO_label_2")
        self.childFIO_label_2.setGeometry(QRect(90, 560, 341, 20))
        self.childFIO_label_2.setFont(font)
        self.childFIO_label_2.setAlignment(Qt.AlignCenter)
        self.tabWidget.addTab(self.tab1_firstConsultation, "")
        self.tab2_documents = QWidget()
        self.tab2_documents.setObjectName(u"tab2_documents")
        self.tab2_documents.setStyleSheet(u"QScrollArea{\n"
"border: none;\n"
"}\n"
"")
        self.scrollArea = QScrollArea(self.tab2_documents)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(-20, 0, 1271, 681))
        self.scrollArea.setStyleSheet(u"")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1254, 1526))
        self.scrollAreaWidgetContents.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setVerticalSpacing(77)
        self.gridLayout.setContentsMargins(20, 20, 20, 20)
        self.createDocument_GB = QGroupBox(self.scrollAreaWidgetContents)
        self.createDocument_GB.setObjectName(u"createDocument_GB")
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(False)
        font2.setItalic(False)
        self.createDocument_GB.setFont(font2)
        self.createDocument_GB.setFlat(False)
        self.createDocument_GB.setCheckable(False)
        self.gridLayout_4 = QGridLayout(self.createDocument_GB)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(10)
        self.gridLayout_4.setVerticalSpacing(25)
        self.gridLayout_4.setContentsMargins(-1, 25, -1, -1)
        self.createDocumentPDF_button = QPushButton(self.createDocument_GB)
        self.createDocumentPDF_button.setObjectName(u"createDocumentPDF_button")
        self.createDocumentPDF_button.setFont(font1)
        self.createDocumentPDF_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.createDocumentPDF_button.setMouseTracking(True)
        self.createDocumentPDF_button.setTabletTracking(False)
        self.createDocumentPDF_button.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(221, 255, 255, 1);\n"
"padding: 5px;\n"
"border-radius: 20px;\n"
"}\n"
"\n"
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
        self.createDocumentPDF_button.setCheckable(False)
        self.createDocumentPDF_button.setAutoDefault(False)

        self.gridLayout_4.addWidget(self.createDocumentPDF_button, 4, 0, 1, 1)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setSpacing(20)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.createParentFIO_label = QLabel(self.createDocument_GB)
        self.createParentFIO_label.setObjectName(u"createParentFIO_label")
        self.createParentFIO_label.setFont(font)
        self.createParentFIO_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.createParentFIO_label)

        self.createParentFIO_input = QLineEdit(self.createDocument_GB)
        self.createParentFIO_input.setObjectName(u"createParentFIO_input")
        self.createParentFIO_input.setFont(font)
        self.createParentFIO_input.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid rgb(33, 33, 34);\n"
"}")
        self.createParentFIO_input.setAlignment(Qt.AlignCenter)
        self.createParentFIO_input.setReadOnly(True)

        self.verticalLayout_13.addWidget(self.createParentFIO_input)


        self.verticalLayout_12.addLayout(self.verticalLayout_13)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.createParentPassport_label = QLabel(self.createDocument_GB)
        self.createParentPassport_label.setObjectName(u"createParentPassport_label")
        self.createParentPassport_label.setFont(font)
        self.createParentPassport_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.createParentPassport_label)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.createParentPassportSeria_input = QLineEdit(self.createDocument_GB)
        self.createParentPassportSeria_input.setObjectName(u"createParentPassportSeria_input")
        self.createParentPassportSeria_input.setFont(font)
        self.createParentPassportSeria_input.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid rgb(33, 33, 34);\n"
"}")
        self.createParentPassportSeria_input.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.createParentPassportSeria_input)

        self.createParentPassportNumber_input = QLineEdit(self.createDocument_GB)
        self.createParentPassportNumber_input.setObjectName(u"createParentPassportNumber_input")
        self.createParentPassportNumber_input.setFont(font)
        self.createParentPassportNumber_input.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid rgb(33, 33, 34);\n"
"}")
        self.createParentPassportNumber_input.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.createParentPassportNumber_input)


        self.verticalLayout_14.addLayout(self.horizontalLayout_5)


        self.verticalLayout_12.addLayout(self.verticalLayout_14)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.createChildFIO_label = QLabel(self.createDocument_GB)
        self.createChildFIO_label.setObjectName(u"createChildFIO_label")
        self.createChildFIO_label.setFont(font)
        self.createChildFIO_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.createChildFIO_label)

        self.createChildFIO_input = QLineEdit(self.createDocument_GB)
        self.createChildFIO_input.setObjectName(u"createChildFIO_input")
        self.createChildFIO_input.setFont(font)
        self.createChildFIO_input.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid rgb(33, 33, 34);\n"
"}")
        self.createChildFIO_input.setAlignment(Qt.AlignCenter)
        self.createChildFIO_input.setReadOnly(True)

        self.verticalLayout_16.addWidget(self.createChildFIO_input)


        self.verticalLayout_12.addLayout(self.verticalLayout_16)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.createChildBirthday_label = QLabel(self.createDocument_GB)
        self.createChildBirthday_label.setObjectName(u"createChildBirthday_label")
        self.createChildBirthday_label.setFont(font)
        self.createChildBirthday_label.setLayoutDirection(Qt.LeftToRight)
        self.createChildBirthday_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.createChildBirthday_label)

        self.createChildBirthday_input = QDateEdit(self.createDocument_GB)
        self.createChildBirthday_input.setObjectName(u"createChildBirthday_input")
        self.createChildBirthday_input.setFont(font)
        self.createChildBirthday_input.setStyleSheet(u"QDateEdit{\n"
"border: 1px solid rgb(33, 33, 34);\n"
"padding: 1px;\n"
"}")
        self.createChildBirthday_input.setAlignment(Qt.AlignCenter)
        self.createChildBirthday_input.setButtonSymbols(QAbstractSpinBox.UpDownArrows)

        self.verticalLayout_17.addWidget(self.createChildBirthday_input)


        self.verticalLayout_12.addLayout(self.verticalLayout_17)


        self.gridLayout_4.addLayout(self.verticalLayout_12, 0, 0, 1, 1)

        self.warning_2 = QLabel(self.createDocument_GB)
        self.warning_2.setObjectName(u"warning_2")
        font3 = QFont()
        font3.setPointSize(14)
        font3.setBold(True)
        self.warning_2.setFont(font3)
        self.warning_2.setLayoutDirection(Qt.LeftToRight)
        self.warning_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.warning_2, 3, 0, 1, 1)

        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setSpacing(10)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.warning = QLabel(self.createDocument_GB)
        self.warning.setObjectName(u"warning")
        self.warning.setFont(font3)
        self.warning.setLayoutDirection(Qt.LeftToRight)
        self.warning.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.warning)

        self.Permission_checkbox = QCheckBox(self.createDocument_GB)
        self.Permission_checkbox.setObjectName(u"Permission_checkbox")
        self.Permission_checkbox.setFont(font)

        self.verticalLayout_15.addWidget(self.Permission_checkbox)


        self.verticalLayout_18.addLayout(self.verticalLayout_15)


        self.gridLayout_4.addLayout(self.verticalLayout_18, 1, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.createData_label = QLabel(self.createDocument_GB)
        self.createData_label.setObjectName(u"createData_label")
        self.createData_label.setFont(font)
        self.createData_label.setLayoutDirection(Qt.LeftToRight)
        self.createData_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.createData_label)

        self.createData_input = QDateEdit(self.createDocument_GB)
        self.createData_input.setObjectName(u"createData_input")
        self.createData_input.setFont(font)
        self.createData_input.setStyleSheet(u"QDateEdit{\n"
"border: 1px solid rgb(33, 33, 34);\n"
"padding: 1px;\n"
"}")
        self.createData_input.setAlignment(Qt.AlignCenter)
        self.createData_input.setButtonSymbols(QAbstractSpinBox.UpDownArrows)

        self.horizontalLayout_6.addWidget(self.createData_input)


        self.gridLayout_4.addLayout(self.horizontalLayout_6, 2, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_3, 5, 0, 1, 1)


        self.gridLayout.addWidget(self.createDocument_GB, 2, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 1, 0, 1, 1)

        self.findDocument_GB = QGroupBox(self.scrollAreaWidgetContents)
        self.findDocument_GB.setObjectName(u"findDocument_GB")
        self.findDocument_GB.setFont(font2)
        self.findDocument_GB.setStyleSheet(u"")
        self.gridLayout_2 = QGridLayout(self.findDocument_GB)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(10)
        self.gridLayout_2.setVerticalSpacing(25)
        self.gridLayout_2.setContentsMargins(-1, 25, -1, -1)
        self.documentFindRes_listview = QListView(self.findDocument_GB)
        self.documentFindRes_listview.setObjectName(u"documentFindRes_listview")
        self.documentFindRes_listview.setEnabled(True)
        self.documentFindRes_listview.setMinimumSize(QSize(0, 200))

        self.gridLayout_2.addWidget(self.documentFindRes_listview, 2, 0, 1, 1)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(20)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.findParentFIO_label = QLabel(self.findDocument_GB)
        self.findParentFIO_label.setObjectName(u"findParentFIO_label")
        self.findParentFIO_label.setFont(font)
        self.findParentFIO_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.findParentFIO_label)

        self.findParentFIO_input = QLineEdit(self.findDocument_GB)
        self.findParentFIO_input.setObjectName(u"findParentFIO_input")
        self.findParentFIO_input.setFont(font)
        self.findParentFIO_input.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid rgb(33, 33, 34);\n"
"}")
        self.findParentFIO_input.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.findParentFIO_input)


        self.verticalLayout_7.addLayout(self.verticalLayout_5)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.findParentPassport_label = QLabel(self.findDocument_GB)
        self.findParentPassport_label.setObjectName(u"findParentPassport_label")
        self.findParentPassport_label.setFont(font)
        self.findParentPassport_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.findParentPassport_label)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.findParentPassportSeria_input = QLineEdit(self.findDocument_GB)
        self.findParentPassportSeria_input.setObjectName(u"findParentPassportSeria_input")
        self.findParentPassportSeria_input.setFont(font)
        self.findParentPassportSeria_input.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid rgb(33, 33, 34);\n"
"}")
        self.findParentPassportSeria_input.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.findParentPassportSeria_input)

        self.findParentPassportNumber_input = QLineEdit(self.findDocument_GB)
        self.findParentPassportNumber_input.setObjectName(u"findParentPassportNumber_input")
        self.findParentPassportNumber_input.setFont(font)
        self.findParentPassportNumber_input.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid rgb(33, 33, 34);\n"
"}")
        self.findParentPassportNumber_input.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.findParentPassportNumber_input)


        self.verticalLayout_11.addLayout(self.horizontalLayout_4)


        self.verticalLayout_7.addLayout(self.verticalLayout_11)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.findChildFIO_label = QLabel(self.findDocument_GB)
        self.findChildFIO_label.setObjectName(u"findChildFIO_label")
        self.findChildFIO_label.setFont(font)
        self.findChildFIO_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.findChildFIO_label)

        self.findChildFIO_input = QLineEdit(self.findDocument_GB)
        self.findChildFIO_input.setObjectName(u"findChildFIO_input")
        self.findChildFIO_input.setFont(font)
        self.findChildFIO_input.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid rgb(33, 33, 34);\n"
"}")
        self.findChildFIO_input.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.findChildFIO_input)


        self.verticalLayout_7.addLayout(self.verticalLayout_6)


        self.gridLayout_2.addLayout(self.verticalLayout_7, 0, 0, 1, 1)

        self.findDocuments_button = QPushButton(self.findDocument_GB)
        self.findDocuments_button.setObjectName(u"findDocuments_button")
        self.findDocuments_button.setFont(font1)
        self.findDocuments_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.findDocuments_button.setMouseTracking(True)
        self.findDocuments_button.setTabletTracking(False)
        self.findDocuments_button.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(221, 255, 255, 1);\n"
"padding: 5px;\n"
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
        self.findDocuments_button.setCheckable(False)
        self.findDocuments_button.setAutoDefault(False)

        self.gridLayout_2.addWidget(self.findDocuments_button, 3, 0, 1, 1)


        self.gridLayout.addWidget(self.findDocument_GB, 0, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 3, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.tabWidget.addTab(self.tab2_documents, "")
        self.tab3_testAtek = QWidget()
        self.tab3_testAtek.setObjectName(u"tab3_testAtek")
        self.groupBox_4 = QGroupBox(self.tab3_testAtek)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(60, 20, 1121, 621))
        self.warning_3 = QLabel(self.groupBox_4)
        self.warning_3.setObjectName(u"warning_3")
        self.warning_3.setGeometry(QRect(160, 30, 851, 31))
        self.warning_3.setFont(font3)
        self.warning_3.setLayoutDirection(Qt.LeftToRight)
        self.warning_3.setAlignment(Qt.AlignCenter)
        self.warning_3.setWordWrap(True)
        self.findDataTest_button = QPushButton(self.groupBox_4)
        self.findDataTest_button.setObjectName(u"findDataTest_button")
        self.findDataTest_button.setGeometry(QRect(400, 250, 311, 45))
        self.findDataTest_button.setFont(font1)
        self.findDataTest_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.findDataTest_button.setMouseTracking(True)
        self.findDataTest_button.setTabletTracking(False)
        self.findDataTest_button.setStyleSheet(u"QPushButton{\n"
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
        self.findDataTest_button.setCheckable(False)
        self.findDataTest_button.setAutoDefault(False)
        self.startTest_button = QPushButton(self.groupBox_4)
        self.startTest_button.setObjectName(u"startTest_button")
        self.startTest_button.setEnabled(True)
        self.startTest_button.setGeometry(QRect(460, 180, 201, 45))
        self.startTest_button.setFont(font1)
        self.startTest_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.startTest_button.setMouseTracking(True)
        self.startTest_button.setTabletTracking(False)
        self.startTest_button.setStyleSheet(u"QPushButton{\n"
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
        self.startTest_button.setCheckable(False)
        self.startTest_button.setAutoDefault(False)
        self.startTest_button.setFlat(False)
        self.layoutWidget2 = QWidget(self.groupBox_4)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(50, 80, 1011, 81))
        self.horizontalLayout_7 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_7.setSpacing(25)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.testChildFIO_label = QLabel(self.layoutWidget2)
        self.testChildFIO_label.setObjectName(u"testChildFIO_label")
        self.testChildFIO_label.setFont(font)
        self.testChildFIO_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.testChildFIO_label)

        self.testChildFIO_input = QLineEdit(self.layoutWidget2)
        self.testChildFIO_input.setObjectName(u"testChildFIO_input")
        self.testChildFIO_input.setFont(font)
        self.testChildFIO_input.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid rgb(33, 33, 34);\n"
"}")
        self.testChildFIO_input.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.testChildFIO_input)


        self.horizontalLayout_7.addLayout(self.verticalLayout_19)

        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.testParentFIO_label = QLabel(self.layoutWidget2)
        self.testParentFIO_label.setObjectName(u"testParentFIO_label")
        self.testParentFIO_label.setFont(font)
        self.testParentFIO_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.testParentFIO_label)

        self.testParentFIO_input = QLineEdit(self.layoutWidget2)
        self.testParentFIO_input.setObjectName(u"testParentFIO_input")
        self.testParentFIO_input.setFont(font)
        self.testParentFIO_input.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid rgb(33, 33, 34);\n"
"}")
        self.testParentFIO_input.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.testParentFIO_input)


        self.horizontalLayout_7.addLayout(self.verticalLayout_20)

        self.layoutWidget_2 = QWidget(self.groupBox_4)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(30, 310, 1061, 241))
        self.verticalLayout_25 = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.resultsFindingData_label_2 = QLabel(self.layoutWidget_2)
        self.resultsFindingData_label_2.setObjectName(u"resultsFindingData_label_2")
        font4 = QFont()
        font4.setPointSize(14)
        font4.setBold(False)
        self.resultsFindingData_label_2.setFont(font4)
        self.resultsFindingData_label_2.setLayoutDirection(Qt.LeftToRight)
        self.resultsFindingData_label_2.setAlignment(Qt.AlignCenter)
        self.resultsFindingData_label_2.setWordWrap(False)

        self.verticalLayout_25.addWidget(self.resultsFindingData_label_2)

        self.resultsFindingDataTest_listview_2 = QListView(self.layoutWidget_2)
        self.resultsFindingDataTest_listview_2.setObjectName(u"resultsFindingDataTest_listview_2")
        self.resultsFindingDataTest_listview_2.setEnabled(True)
        self.resultsFindingDataTest_listview_2.setMinimumSize(QSize(0, 200))

        self.verticalLayout_25.addWidget(self.resultsFindingDataTest_listview_2)

        self.deleteCurrentData_button_3 = QPushButton(self.groupBox_4)
        self.deleteCurrentData_button_3.setObjectName(u"deleteCurrentData_button_3")
        self.deleteCurrentData_button_3.setGeometry(QRect(390, 560, 331, 45))
        self.deleteCurrentData_button_3.setFont(font1)
        self.deleteCurrentData_button_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.deleteCurrentData_button_3.setMouseTracking(True)
        self.deleteCurrentData_button_3.setTabletTracking(False)
        self.deleteCurrentData_button_3.setStyleSheet(u"QPushButton{\n"
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
        self.deleteCurrentData_button_3.setCheckable(False)
        self.deleteCurrentData_button_3.setAutoDefault(False)
        self.tabWidget.addTab(self.tab3_testAtek, "")
        self.tab4_clientsData = QWidget()
        self.tab4_clientsData.setObjectName(u"tab4_clientsData")
        self.groupBox_6 = QGroupBox(self.tab4_clientsData)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setGeometry(QRect(50, 10, 1121, 641))
        self.warning_4 = QLabel(self.groupBox_6)
        self.warning_4.setObjectName(u"warning_4")
        self.warning_4.setGeometry(QRect(260, 40, 581, 26))
        self.warning_4.setFont(font3)
        self.warning_4.setLayoutDirection(Qt.LeftToRight)
        self.warning_4.setAlignment(Qt.AlignCenter)
        self.warning_4.setWordWrap(False)
        self.findData_button = QPushButton(self.groupBox_6)
        self.findData_button.setObjectName(u"findData_button")
        self.findData_button.setGeometry(QRect(380, 180, 331, 45))
        self.findData_button.setFont(font1)
        self.findData_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.findData_button.setMouseTracking(True)
        self.findData_button.setTabletTracking(False)
        self.findData_button.setStyleSheet(u"QPushButton{\n"
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
        self.findData_button.setCheckable(False)
        self.findData_button.setAutoDefault(False)
        self.statusFindingData_input = QLineEdit(self.groupBox_6)
        self.statusFindingData_input.setObjectName(u"statusFindingData_input")
        self.statusFindingData_input.setGeometry(QRect(440, 230, 211, 30))
        self.statusFindingData_input.setFont(font)
        self.statusFindingData_input.setStyleSheet(u"QLineEdit{\n"
"border: none;\n"
"}")
        self.statusFindingData_input.setAlignment(Qt.AlignCenter)
        self.statusFindingData_input.setReadOnly(True)
        self.layoutWidget_5 = QWidget(self.groupBox_6)
        self.layoutWidget_5.setObjectName(u"layoutWidget_5")
        self.layoutWidget_5.setGeometry(QRect(40, 80, 1011, 81))
        self.horizontalLayout_8 = QHBoxLayout(self.layoutWidget_5)
        self.horizontalLayout_8.setSpacing(25)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.findDataChildFIO_label = QLabel(self.layoutWidget_5)
        self.findDataChildFIO_label.setObjectName(u"findDataChildFIO_label")
        self.findDataChildFIO_label.setFont(font)
        self.findDataChildFIO_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_21.addWidget(self.findDataChildFIO_label)

        self.findDataChildFIO_input = QLineEdit(self.layoutWidget_5)
        self.findDataChildFIO_input.setObjectName(u"findDataChildFIO_input")
        self.findDataChildFIO_input.setFont(font)
        self.findDataChildFIO_input.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid rgb(33, 33, 34);\n"
"}")
        self.findDataChildFIO_input.setAlignment(Qt.AlignCenter)

        self.verticalLayout_21.addWidget(self.findDataChildFIO_input)


        self.horizontalLayout_8.addLayout(self.verticalLayout_21)

        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.findDataParentFIO_label = QLabel(self.layoutWidget_5)
        self.findDataParentFIO_label.setObjectName(u"findDataParentFIO_label")
        self.findDataParentFIO_label.setFont(font)
        self.findDataParentFIO_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.findDataParentFIO_label)

        self.findDataParentFIO_input = QLineEdit(self.layoutWidget_5)
        self.findDataParentFIO_input.setObjectName(u"findDataParentFIO_input")
        self.findDataParentFIO_input.setFont(font)
        self.findDataParentFIO_input.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid rgb(33, 33, 34);\n"
"}")
        self.findDataParentFIO_input.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.findDataParentFIO_input)


        self.horizontalLayout_8.addLayout(self.verticalLayout_22)

        self.deleteCurrentData_button = QPushButton(self.groupBox_6)
        self.deleteCurrentData_button.setObjectName(u"deleteCurrentData_button")
        self.deleteCurrentData_button.setGeometry(QRect(210, 560, 331, 45))
        self.deleteCurrentData_button.setFont(font1)
        self.deleteCurrentData_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.deleteCurrentData_button.setMouseTracking(True)
        self.deleteCurrentData_button.setTabletTracking(False)
        self.deleteCurrentData_button.setStyleSheet(u"QPushButton{\n"
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
        self.deleteCurrentData_button.setCheckable(False)
        self.deleteCurrentData_button.setAutoDefault(False)
        self.changeCurrentData_button = QPushButton(self.groupBox_6)
        self.changeCurrentData_button.setObjectName(u"changeCurrentData_button")
        self.changeCurrentData_button.setGeometry(QRect(570, 560, 331, 45))
        self.changeCurrentData_button.setFont(font1)
        self.changeCurrentData_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.changeCurrentData_button.setMouseTracking(True)
        self.changeCurrentData_button.setTabletTracking(False)
        self.changeCurrentData_button.setStyleSheet(u"QPushButton{\n"
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
        self.changeCurrentData_button.setCheckable(False)
        self.changeCurrentData_button.setAutoDefault(False)
        self.layoutWidget3 = QWidget(self.groupBox_6)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(30, 300, 1061, 241))
        self.verticalLayout_23 = QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.resultsFindingData_label = QLabel(self.layoutWidget3)
        self.resultsFindingData_label.setObjectName(u"resultsFindingData_label")
        self.resultsFindingData_label.setFont(font4)
        self.resultsFindingData_label.setLayoutDirection(Qt.LeftToRight)
        self.resultsFindingData_label.setAlignment(Qt.AlignCenter)
        self.resultsFindingData_label.setWordWrap(False)

        self.verticalLayout_23.addWidget(self.resultsFindingData_label)

        self.resultsFindingData_listview = QListView(self.layoutWidget3)
        self.resultsFindingData_listview.setObjectName(u"resultsFindingData_listview")
        self.resultsFindingData_listview.setEnabled(True)
        self.resultsFindingData_listview.setMinimumSize(QSize(0, 200))

        self.verticalLayout_23.addWidget(self.resultsFindingData_listview)

        self.tabWidget.addTab(self.tab4_clientsData, "")
        self.tab5_statistic = QWidget()
        self.tab5_statistic.setObjectName(u"tab5_statistic")
        self.layoutWidget4 = QWidget(self.tab5_statistic)
        self.layoutWidget4.setObjectName(u"layoutWidget4")
        self.layoutWidget4.setGeometry(QRect(30, 80, 931, 72))
        self.verticalLayout_24 = QVBoxLayout(self.layoutWidget4)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(10)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.parentsRowCount_label = QLabel(self.layoutWidget4)
        self.parentsRowCount_label.setObjectName(u"parentsRowCount_label")
        self.parentsRowCount_label.setFont(font)
        self.parentsRowCount_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.parentsRowCount_label)

        self.parentsRowCount_input = QLineEdit(self.layoutWidget4)
        self.parentsRowCount_input.setObjectName(u"parentsRowCount_input")
        self.parentsRowCount_input.setFont(font)
        self.parentsRowCount_input.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid rgb(33, 33, 34);\n"
"}")
        self.parentsRowCount_input.setAlignment(Qt.AlignCenter)
        self.parentsRowCount_input.setReadOnly(True)

        self.horizontalLayout_9.addWidget(self.parentsRowCount_input)


        self.verticalLayout_24.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(10)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.childRowCount_label = QLabel(self.layoutWidget4)
        self.childRowCount_label.setObjectName(u"childRowCount_label")
        self.childRowCount_label.setFont(font)
        self.childRowCount_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.childRowCount_label)

        self.childRowCount_input = QLineEdit(self.layoutWidget4)
        self.childRowCount_input.setObjectName(u"childRowCount_input")
        self.childRowCount_input.setFont(font)
        self.childRowCount_input.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid rgb(33, 33, 34);\n"
"}")
        self.childRowCount_input.setAlignment(Qt.AlignCenter)
        self.childRowCount_input.setReadOnly(True)

        self.horizontalLayout_10.addWidget(self.childRowCount_input)


        self.verticalLayout_24.addLayout(self.horizontalLayout_10)

        self.tabWidget.addTab(self.tab5_statistic, "")

        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Teremok", None))
        self.child_GB.setTitle(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0431\u0451\u043d\u043e\u043a", None))
        self.childFIO_label.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f \u0418\u043c\u044f \u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e \u0440\u0435\u0431\u0451\u043d\u043a\u0430 *:", None))
        self.childFIO_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0424\u0418\u041e \u0440\u0435\u0431\u0451\u043d\u043a\u0430", None))
        self.birthday_label.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f \u0440\u0435\u0431\u0451\u043d\u043a\u0430 *:", None))
        self.diagnos_label.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0438\u0430\u0433\u043d\u043e\u0437 \u0440\u0435\u0431\u0451\u043d\u043a\u0430 (\u043f\u0440\u0438 \u043d\u0430\u043b\u0438\u0447\u0438\u0438):", None))
        self.diagnos_input.setText("")
        self.diagnos_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0414\u0438\u0430\u0433\u043d\u043e\u0437 \u0440\u0435\u0431\u0451\u043d\u043a\u0430 (\u043f\u0440\u0438 \u043d\u0430\u043b\u0438\u0447\u0438\u0438):", None))
        self.aboutChild_label.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0449\u0438\u0435 \u0441\u0432\u0435\u0434\u0435\u043d\u0438\u044f \u043e \u0440\u0435\u0431\u0451\u043d\u043a\u0435 (\u043f\u043e\u0432\u0435\u0434\u0435\u043d\u0438\u0435, \u043f\u0440\u0438\u0432\u044b\u0447\u043a\u0438 \u0438 \u0442.\u0434.):", None))
        self.aboutChild_input.setPlainText("")
        self.aboutChild_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u0435 \u0434\u043b\u044f \u043e\u0431\u0449\u0438\u0445 \u0441\u0432\u0435\u0434\u0435\u043d\u0438\u0439", None))
        self.parent_GB.setTitle(QCoreApplication.translate("MainWindow", u"\u0420\u043e\u0434\u0438\u0442\u0435\u043b\u044c", None))
        self.parentFIO_label.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f \u0418\u043c\u044f \u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e \u0440\u043e\u0434\u0438\u0442\u0435\u043b\u044f *:", None))
        self.parentFIO_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0424\u0418\u041e \u0440\u043e\u0434\u0438\u0442\u0435\u043b\u044f", None))
        self.passport_label.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0441\u043f\u043e\u0440\u0442\u043d\u044b\u0435 \u0434\u0430\u043d\u043d\u044b\u0435 \u043e\u0434\u043d\u043e\u0433\u043e \u0438\u0437 \u0440\u043e\u0434\u0438\u0442\u0435\u043b\u0435\u0439 *:", None))
        self.passSeria_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0421\u0435\u0440\u0438\u044f \u043f\u0430\u0441\u043f\u043e\u0440\u0442\u0430", None))
        self.passNumber_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u043c\u0435\u0440 \u043f\u0430\u0441\u043f\u043e\u0440\u0442\u0430", None))
        self.saveData_button.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.clearAll_button.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0439\u0442\u0438 \u0431\u0435\u0437 \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f", None))
        self.childFIO_label_2.setText(QCoreApplication.translate("MainWindow", u"* - \u043f\u043e\u043b\u044f, \u043e\u0431\u044f\u0437\u0430\u0442\u0435\u043b\u044c\u043d\u044b\u0435 \u043a \u0437\u0430\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044e", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1_firstConsultation), QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0432\u0438\u0447\u043d\u0430\u044f \u043a\u043e\u043d\u0441\u0443\u043b\u044c\u0442\u0430\u0446\u0438\u044f", None))
        self.createDocument_GB.setTitle(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u043d\u0438\u0435 \u043d\u043e\u0432\u043e\u0433\u043e \u0434\u043e\u0433\u043e\u0432\u043e\u0440\u0430", None))
        self.createDocumentPDF_button.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0444\u043e\u0440\u043c\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0434\u043e\u0433\u043e\u0432\u043e\u0440 \u0432 PDF", None))
        self.createParentFIO_label.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0418\u041e \u0440\u043e\u0434\u0438\u0442\u0435\u043b\u044f:", None))
        self.createParentFIO_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0424\u0418\u041e \u0440\u043e\u0434\u0438\u0442\u0435\u043b\u044f", None))
        self.createParentPassport_label.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0441\u043f\u043e\u0440\u0442\u043d\u044b\u0435 \u0434\u0430\u043d\u043d\u044b\u0435 \u043e\u0434\u043d\u043e\u0433\u043e \u0438\u0437 \u0440\u043e\u0434\u0438\u0442\u0435\u043b\u0435\u0439:", None))
        self.createParentPassportSeria_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0421\u0435\u0440\u0438\u044f \u043f\u0430\u0441\u043f\u043e\u0440\u0442\u0430", None))
        self.createParentPassportNumber_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u043c\u0435\u0440 \u043f\u0430\u0441\u043f\u043e\u0440\u0442\u0430", None))
        self.createChildFIO_label.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0418\u041e \u0440\u0435\u0431\u0451\u043d\u043a\u0430:", None))
        self.createChildFIO_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0424\u0418\u041e \u0440\u0435\u0431\u0451\u043d\u043a\u0430", None))
        self.createChildBirthday_label.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f \u0440\u0435\u0431\u0451\u043d\u043a\u0430:", None))
        self.warning_2.setText(QCoreApplication.translate("MainWindow", u"*\u041f\u043e\u0441\u043b\u0435 \u0437\u0430\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f \u0432\u0441\u0435\u0445 \u043f\u043e\u043b\u0435\u0439 \u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u043e \u0441\u0444\u043e\u0440\u043c\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0434\u043e\u0433\u043e\u0432\u043e\u0440 \u0432 PDF \u0444\u0430\u0439\u043b, \u0440\u0430\u0441\u043f\u0435\u0447\u0430\u0442\u0430\u0442\u044c \u0438 \u043f\u043e\u0434\u043f\u0438\u0441\u0430\u0442\u044c \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442", None))
        self.warning.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043c\u0435\u0447\u0430\u044f \u201c\u0420\u0430\u0437\u0440\u0435\u0448\u0430\u044e\u201d, \u044f \u0434\u0430\u044e \u0441\u0432\u043e\u0451 \u0441\u043e\u0433\u043b\u0430\u0441\u0438\u0435 \u043d\u0430 \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u043d\u0438\u0435 \u0444\u043e\u0442\u043e \u0438 \u0432\u0438\u0434\u0435\u043e\u043c\u0430\u0442\u0435\u0440\u0438\u0430\u043b\u043e\u0432 \u0432 \u043a\u043e\u043c\u043c\u0435\u0440\u0447\u0435\u0441\u043a\u0438\u0445 \u0446\u0435\u043b\u044f\u0445", None))
        self.Permission_checkbox.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u0440\u0435\u0448\u0435\u043d\u0438\u0435 \u043d\u0430 \u0444\u043e\u0442\u043e\u0441\u044a\u0451\u043c\u043a\u0443 \u0438 \u0432\u0438\u0434\u0435\u043e\u0441\u044a\u0451\u043c\u043a\u0443, \u0430 \u0442\u0430\u043a\u0436\u0435 \u0438\u0445 \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u043d\u0438\u0435 \u0432 \u043a\u043e\u043c\u043c\u0435\u0440\u0447\u0435\u0441\u043a\u0438\u0445 \u0446\u0435\u043b\u044f\u0445", None))
        self.createData_label.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f \u0438 \u043f\u043e\u0434\u043f\u0438\u0441\u0438 \u0434\u043e\u0433\u043e\u0432\u043e\u0440\u0430:", None))
        self.findDocument_GB.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a \u0434\u043e\u0433\u043e\u0432\u043e\u0440\u043e\u0432", None))
        self.findParentFIO_label.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a \u043f\u043e \u0424\u0418\u041e \u0440\u043e\u0434\u0438\u0442\u0435\u043b\u044f:", None))
        self.findParentFIO_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0424\u0418\u041e \u0440\u043e\u0434\u0438\u0442\u0435\u043b\u044f", None))
        self.findParentPassport_label.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a \u043f\u043e \u043f\u0430\u0441\u043f\u043e\u0440\u0442\u043d\u044b\u043c \u0434\u0430\u043d\u043d\u044b\u043c \u043e\u0434\u043d\u043e\u0433\u043e \u0438\u0437 \u0440\u043e\u0434\u0438\u0442\u0435\u043b\u0435\u0439:", None))
        self.findParentPassportSeria_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0421\u0435\u0440\u0438\u044f \u043f\u0430\u0441\u043f\u043e\u0440\u0442\u0430", None))
        self.findParentPassportNumber_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u043c\u0435\u0440 \u043f\u0430\u0441\u043f\u043e\u0440\u0442\u0430", None))
        self.findChildFIO_label.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a \u043f\u043e \u0424\u0418\u041e \u0440\u0435\u0431\u0451\u043d\u043a\u0430:", None))
        self.findChildFIO_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0424\u0418\u041e \u0440\u0435\u0431\u0451\u043d\u043a\u0430", None))
        self.findDocuments_button.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0439\u0442\u0438 \u0438 \u043f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u044b", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2_documents), QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0433\u043e\u0432\u043e\u0440\u044b", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a \u0441\u0443\u0449\u0435\u0441\u0442\u0432\u0443\u044e\u0449\u0438\u0445 \u0437\u0430\u043f\u0438\u0441\u0435\u0439", None))
        self.warning_3.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0434\u0430\u043d\u043d\u044b\u0435 \u0434\u043b\u044f \u043d\u0430\u0447\u0430\u043b\u0430 \u0442\u0435\u0441\u0442\u0430 \u0438\u043b\u0438 \u043f\u043e\u0438\u0441\u043a\u0430 \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u043e\u0432 \u0442\u0435\u0441\u0442\u0430:", None))
        self.findDataTest_button.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u043e\u0432 \u0442\u0435\u0441\u0442\u0430", None))
        self.startTest_button.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447\u0430\u0442\u044c \u0442\u0435\u0441\u0442", None))
        self.testChildFIO_label.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0418\u041e \u0440\u0435\u0431\u0451\u043d\u043a\u0430:", None))
        self.testChildFIO_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0424\u0418\u041e \u0440\u0435\u0431\u0451\u043d\u043a\u0430", None))
        self.testParentFIO_label.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0418\u041e \u0440\u043e\u0434\u0438\u0442\u0435\u043b\u044f:", None))
        self.testParentFIO_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0424\u0418\u041e \u0440\u043e\u0434\u0438\u0442\u0435\u043b\u044f", None))
        self.resultsFindingData_label_2.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u044b \u043f\u043e\u0438\u0441\u043a\u0430:", None))
        self.deleteCurrentData_button_3.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u044b\u0435 \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab3_testAtek), QCoreApplication.translate("MainWindow", u"\u0422\u0435\u0441\u0442 \u0410\u0422\u0415\u041a", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a \u0441\u0443\u0449\u0435\u0441\u0442\u0432\u0443\u044e\u0449\u0438\u0445 \u0434\u0430\u043d\u043d\u044b\u0445", None))
        self.warning_4.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u044f\u0437\u0430\u0442\u0435\u043b\u044c\u043d\u043e \u0437\u0430\u043f\u043e\u043b\u043d\u0438\u0442\u0435 \u043e\u0431\u0430 \u043f\u043e\u043b\u044f \u0434\u043b\u044f \u0442\u043e\u0447\u043d\u043e\u0439 \u0438\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u0438", None))
        self.findData_button.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0439\u0442\u0438 \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.statusFindingData_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0439\u0434\u0435\u043d\u044b / \u043d\u0435 \u043d\u0430\u0439\u0434\u0435\u043d\u044b", None))
        self.findDataChildFIO_label.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0418\u041e \u0440\u0435\u0431\u0451\u043d\u043a\u0430:", None))
        self.findDataChildFIO_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0424\u0418\u041e \u0440\u0435\u0431\u0451\u043d\u043a\u0430", None))
        self.findDataParentFIO_label.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0418\u041e \u0440\u043e\u0434\u0438\u0442\u0435\u043b\u044f:", None))
        self.findDataParentFIO_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0424\u0418\u041e \u0440\u043e\u0434\u0438\u0442\u0435\u043b\u044f", None))
        self.deleteCurrentData_button.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.changeCurrentData_button.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0441\u043c\u043e\u0442\u0440\u0435\u0442\u044c/\u0438\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.resultsFindingData_label.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u044b \u043f\u043e\u0438\u0441\u043a\u0430:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab4_clientsData), QCoreApplication.translate("MainWindow", u"\u0414\u0430\u043d\u043d\u044b\u0435 \u043e \u043a\u043b\u0438\u0435\u043d\u0442\u0430\u0445", None))
        self.parentsRowCount_label.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0440\u043e\u0434\u0438\u0442\u0435\u043b\u0435\u0439, \u0437\u0430\u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0445 \u0432 \u0431\u0430\u0437\u0435 \u0432 \u043d\u0430\u0441\u0442\u043e\u044f\u0449\u0438\u0439 \u043c\u043e\u043c\u0435\u043d\u0442:", None))
        self.parentsRowCount_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0440\u043e\u0434\u0438\u0442\u0435\u043b\u0435\u0439", None))
        self.childRowCount_label.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0434\u0435\u0442\u0435\u0439, \u0437\u0430\u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0445 \u0432 \u0431\u0430\u0437\u0435 \u0432 \u043d\u0430\u0441\u0442\u043e\u044f\u0449\u0438\u0439 \u043c\u043e\u043c\u0435\u043d\u0442:", None))
        self.childRowCount_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0434\u0435\u0442\u0435\u0439", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab5_statistic), QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430", None))
    # retranslateUi

