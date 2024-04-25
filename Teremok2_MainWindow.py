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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QComboBox,
    QDateEdit, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QListView,
    QMainWindow, QPlainTextEdit, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QTabWidget, QTimeEdit,
    QVBoxLayout, QWidget)

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
        self.child_GB.setGeometry(QRect(50, 280, 1121, 321))
        self.layoutWidget = QWidget(self.child_GB)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(24, 29, 901, 66))
        self.gridLayout_6 = QGridLayout(self.layoutWidget)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.childFIO_label = QLabel(self.layoutWidget)
        self.childFIO_label.setObjectName(u"childFIO_label")
        self.childFIO_label.setFont(font)
        self.childFIO_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.childFIO_label, 0, 0, 1, 1)

        self.birthdayChild_label = QLabel(self.layoutWidget)
        self.birthdayChild_label.setObjectName(u"birthdayChild_label")
        self.birthdayChild_label.setFont(font)
        self.birthdayChild_label.setLayoutDirection(Qt.LeftToRight)
        self.birthdayChild_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.birthdayChild_label, 0, 1, 1, 1)

        self.diagnos_label = QLabel(self.layoutWidget)
        self.diagnos_label.setObjectName(u"diagnos_label")
        self.diagnos_label.setFont(font)
        self.diagnos_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.diagnos_label, 0, 2, 1, 1)

        self.childFIO_input = QLineEdit(self.layoutWidget)
        self.childFIO_input.setObjectName(u"childFIO_input")
        self.childFIO_input.setFont(font)
        self.childFIO_input.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid rgb(33, 33, 34);\n"
"}")
        self.childFIO_input.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.childFIO_input, 1, 0, 1, 1)

        self.birthdayChild_input = QDateEdit(self.layoutWidget)
        self.birthdayChild_input.setObjectName(u"birthdayChild_input")
        self.birthdayChild_input.setFont(font)
        self.birthdayChild_input.setStyleSheet(u"QDateEdit{\n"
"border: 1px solid rgb(33, 33, 34);\n"
"padding: 1px;\n"
"}")
        self.birthdayChild_input.setAlignment(Qt.AlignCenter)
        self.birthdayChild_input.setButtonSymbols(QAbstractSpinBox.UpDownArrows)

        self.gridLayout_6.addWidget(self.birthdayChild_input, 1, 1, 1, 1)

        self.diagnos_input = QLineEdit(self.layoutWidget)
        self.diagnos_input.setObjectName(u"diagnos_input")
        self.diagnos_input.setFont(font)
        self.diagnos_input.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid rgb(33, 33, 34);\n"
"}")
        self.diagnos_input.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.diagnos_input, 1, 2, 1, 1)

        self.layoutWidget1 = QWidget(self.child_GB)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(20, 110, 1091, 105))
        self.verticalLayout = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.aboutChild_label = QLabel(self.layoutWidget1)
        self.aboutChild_label.setObjectName(u"aboutChild_label")
        self.aboutChild_label.setFont(font)
        self.aboutChild_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.aboutChild_label)

        self.aboutChild_input = QPlainTextEdit(self.layoutWidget1)
        self.aboutChild_input.setObjectName(u"aboutChild_input")

        self.verticalLayout.addWidget(self.aboutChild_input)

        self.layoutWidget2 = QWidget(self.child_GB)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(20, 230, 371, 61))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.selectParent_label = QLabel(self.layoutWidget2)
        self.selectParent_label.setObjectName(u"selectParent_label")
        self.selectParent_label.setFont(font)
        self.selectParent_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.selectParent_label)

        self.selectParent_comboBox = QComboBox(self.layoutWidget2)
        self.selectParent_comboBox.setObjectName(u"selectParent_comboBox")

        self.verticalLayout_2.addWidget(self.selectParent_comboBox)

        self.layoutWidget3 = QWidget(self.child_GB)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(480, 230, 471, 66))
        self.gridLayout_7 = QGridLayout(self.layoutWidget3)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.dateFirstConsultation_label = QLabel(self.layoutWidget3)
        self.dateFirstConsultation_label.setObjectName(u"dateFirstConsultation_label")
        self.dateFirstConsultation_label.setFont(font)
        self.dateFirstConsultation_label.setLayoutDirection(Qt.LeftToRight)
        self.dateFirstConsultation_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.dateFirstConsultation_label, 0, 0, 1, 1)

        self.timeFirstConsultation_label = QLabel(self.layoutWidget3)
        self.timeFirstConsultation_label.setObjectName(u"timeFirstConsultation_label")
        self.timeFirstConsultation_label.setFont(font)
        self.timeFirstConsultation_label.setLayoutDirection(Qt.LeftToRight)
        self.timeFirstConsultation_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.timeFirstConsultation_label, 0, 1, 1, 1)

        self.dateFirstConsultation_input = QDateEdit(self.layoutWidget3)
        self.dateFirstConsultation_input.setObjectName(u"dateFirstConsultation_input")
        self.dateFirstConsultation_input.setFont(font)
        self.dateFirstConsultation_input.setStyleSheet(u"QDateEdit{\n"
"border: 1px solid rgb(33, 33, 34);\n"
"padding: 1px;\n"
"}")
        self.dateFirstConsultation_input.setAlignment(Qt.AlignCenter)
        self.dateFirstConsultation_input.setButtonSymbols(QAbstractSpinBox.UpDownArrows)

        self.gridLayout_7.addWidget(self.dateFirstConsultation_input, 1, 0, 1, 1)

        self.timeFirstConsultation_input = QTimeEdit(self.layoutWidget3)
        self.timeFirstConsultation_input.setObjectName(u"timeFirstConsultation_input")

        self.gridLayout_7.addWidget(self.timeFirstConsultation_input, 1, 1, 1, 1)

        self.parent_GB = QGroupBox(self.tab1_firstConsultation)
        self.parent_GB.setObjectName(u"parent_GB")
        self.parent_GB.setGeometry(QRect(50, 20, 1121, 251))
        self.saveParentData_button = QPushButton(self.parent_GB)
        self.saveParentData_button.setObjectName(u"saveParentData_button")
        self.saveParentData_button.setGeometry(QRect(820, 190, 291, 45))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(14)
        self.saveParentData_button.setFont(font1)
        self.saveParentData_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.saveParentData_button.setMouseTracking(True)
        self.saveParentData_button.setTabletTracking(False)
        self.saveParentData_button.setStyleSheet(u"QPushButton{\n"
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
        self.saveParentData_button.setCheckable(False)
        self.saveParentData_button.setAutoDefault(False)
        self.childFIO_label_2 = QLabel(self.parent_GB)
        self.childFIO_label_2.setObjectName(u"childFIO_label_2")
        self.childFIO_label_2.setGeometry(QRect(10, 200, 341, 20))
        self.childFIO_label_2.setFont(font)
        self.childFIO_label_2.setAlignment(Qt.AlignCenter)
        self.layoutWidget4 = QWidget(self.parent_GB)
        self.layoutWidget4.setObjectName(u"layoutWidget4")
        self.layoutWidget4.setGeometry(QRect(9, 40, 1101, 136))
        self.gridLayout_5 = QGridLayout(self.layoutWidget4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.parentTelephoneNumber_label = QLabel(self.layoutWidget4)
        self.parentTelephoneNumber_label.setObjectName(u"parentTelephoneNumber_label")
        self.parentTelephoneNumber_label.setFont(font)
        self.parentTelephoneNumber_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.parentTelephoneNumber_label, 0, 2, 1, 1)

        self.birthdayParent_input = QDateEdit(self.layoutWidget4)
        self.birthdayParent_input.setObjectName(u"birthdayParent_input")
        self.birthdayParent_input.setFont(font)
        self.birthdayParent_input.setStyleSheet(u"QDateEdit{\n"
"border: 1px solid rgb(33, 33, 34);\n"
"padding: 1px;\n"
"}")
        self.birthdayParent_input.setAlignment(Qt.AlignCenter)
        self.birthdayParent_input.setButtonSymbols(QAbstractSpinBox.UpDownArrows)

        self.gridLayout_5.addWidget(self.birthdayParent_input, 3, 2, 1, 1)

        self.parentTelephoneNumber_input = QLineEdit(self.layoutWidget4)
        self.parentTelephoneNumber_input.setObjectName(u"parentTelephoneNumber_input")
        self.parentTelephoneNumber_input.setFont(font)
        self.parentTelephoneNumber_input.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid rgb(33, 33, 34);\n"
"}")
        self.parentTelephoneNumber_input.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.parentTelephoneNumber_input, 1, 2, 1, 1)

        self.passNumber_label = QLabel(self.layoutWidget4)
        self.passNumber_label.setObjectName(u"passNumber_label")
        self.passNumber_label.setFont(font)
        self.passNumber_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.passNumber_label, 0, 3, 1, 1)

        self.parentFIO_label = QLabel(self.layoutWidget4)
        self.parentFIO_label.setObjectName(u"parentFIO_label")
        self.parentFIO_label.setFont(font)
        self.parentFIO_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.parentFIO_label, 0, 0, 1, 2)

        self.whoGavePass_input = QLineEdit(self.layoutWidget4)
        self.whoGavePass_input.setObjectName(u"whoGavePass_input")
        self.whoGavePass_input.setFont(font)
        self.whoGavePass_input.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid rgb(33, 33, 34);\n"
"}")
        self.whoGavePass_input.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.whoGavePass_input, 3, 4, 1, 1)

        self.passportDate_input = QDateEdit(self.layoutWidget4)
        self.passportDate_input.setObjectName(u"passportDate_input")
        self.passportDate_input.setFont(font)
        self.passportDate_input.setStyleSheet(u"QDateEdit{\n"
"border: 1px solid rgb(33, 33, 34);\n"
"padding: 1px;\n"
"}")
        self.passportDate_input.setAlignment(Qt.AlignCenter)
        self.passportDate_input.setButtonSymbols(QAbstractSpinBox.UpDownArrows)

        self.gridLayout_5.addWidget(self.passportDate_input, 1, 4, 1, 1)

        self.parentAdres_label = QLabel(self.layoutWidget4)
        self.parentAdres_label.setObjectName(u"parentAdres_label")
        self.parentAdres_label.setFont(font)
        self.parentAdres_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.parentAdres_label, 2, 0, 1, 2)

        self.birthdayParent_label = QLabel(self.layoutWidget4)
        self.birthdayParent_label.setObjectName(u"birthdayParent_label")
        self.birthdayParent_label.setFont(font)
        self.birthdayParent_label.setLayoutDirection(Qt.LeftToRight)
        self.birthdayParent_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.birthdayParent_label, 2, 2, 1, 1)

        self.passSeria_input = QLineEdit(self.layoutWidget4)
        self.passSeria_input.setObjectName(u"passSeria_input")
        self.passSeria_input.setFont(font)
        self.passSeria_input.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid rgb(33, 33, 34);\n"
"}")
        self.passSeria_input.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.passSeria_input, 3, 3, 1, 1)

        self.parentFIO_input = QLineEdit(self.layoutWidget4)
        self.parentFIO_input.setObjectName(u"parentFIO_input")
        self.parentFIO_input.setFont(font)
        self.parentFIO_input.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid rgb(33, 33, 34);\n"
"}")
        self.parentFIO_input.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.parentFIO_input, 1, 0, 1, 2)

        self.passSeria_label = QLabel(self.layoutWidget4)
        self.passSeria_label.setObjectName(u"passSeria_label")
        self.passSeria_label.setFont(font)
        self.passSeria_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.passSeria_label, 2, 3, 1, 1)

        self.parentAdres_input = QLineEdit(self.layoutWidget4)
        self.parentAdres_input.setObjectName(u"parentAdres_input")
        self.parentAdres_input.setFont(font)
        self.parentAdres_input.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid rgb(33, 33, 34);\n"
"}")
        self.parentAdres_input.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.parentAdres_input, 3, 0, 1, 2)

        self.whoGavePass_label = QLabel(self.layoutWidget4)
        self.whoGavePass_label.setObjectName(u"whoGavePass_label")
        self.whoGavePass_label.setFont(font)
        self.whoGavePass_label.setLayoutDirection(Qt.LeftToRight)
        self.whoGavePass_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.whoGavePass_label, 2, 4, 1, 1)

        self.passportDate_label = QLabel(self.layoutWidget4)
        self.passportDate_label.setObjectName(u"passportDate_label")
        self.passportDate_label.setFont(font)
        self.passportDate_label.setLayoutDirection(Qt.LeftToRight)
        self.passportDate_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.passportDate_label, 0, 4, 1, 1)

        self.passNumber_input = QLineEdit(self.layoutWidget4)
        self.passNumber_input.setObjectName(u"passNumber_input")
        self.passNumber_input.setFont(font)
        self.passNumber_input.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid rgb(33, 33, 34);\n"
"}")
        self.passNumber_input.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.passNumber_input, 1, 3, 1, 1)

        self.gridLayout_5.setColumnStretch(0, 1)
        self.gridLayout_5.setColumnStretch(4, 1)
        self.clearAll_button = QPushButton(self.tab1_firstConsultation)
        self.clearAll_button.setObjectName(u"clearAll_button")
        self.clearAll_button.setEnabled(False)
        self.clearAll_button.setGeometry(QRect(660, 610, 211, 45))
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
        self.saveChildData_button = QPushButton(self.tab1_firstConsultation)
        self.saveChildData_button.setObjectName(u"saveChildData_button")
        self.saveChildData_button.setGeometry(QRect(880, 610, 291, 45))
        self.saveChildData_button.setFont(font1)
        self.saveChildData_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.saveChildData_button.setMouseTracking(True)
        self.saveChildData_button.setTabletTracking(False)
        self.saveChildData_button.setStyleSheet(u"QPushButton{\n"
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
        self.saveChildData_button.setCheckable(False)
        self.saveChildData_button.setAutoDefault(False)
        self.tabWidget.addTab(self.tab1_firstConsultation, "")
        self.tab3_testAtek = QWidget()
        self.tab3_testAtek.setObjectName(u"tab3_testAtek")
        self.groupBox_4 = QGroupBox(self.tab3_testAtek)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(60, 20, 1121, 621))
        self.warning_3 = QLabel(self.groupBox_4)
        self.warning_3.setObjectName(u"warning_3")
        self.warning_3.setGeometry(QRect(160, 30, 851, 31))
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        self.warning_3.setFont(font2)
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
        self.layoutWidget5 = QWidget(self.groupBox_4)
        self.layoutWidget5.setObjectName(u"layoutWidget5")
        self.layoutWidget5.setGeometry(QRect(50, 80, 1011, 81))
        self.horizontalLayout_7 = QHBoxLayout(self.layoutWidget5)
        self.horizontalLayout_7.setSpacing(25)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.testChildFIO_label = QLabel(self.layoutWidget5)
        self.testChildFIO_label.setObjectName(u"testChildFIO_label")
        self.testChildFIO_label.setFont(font)
        self.testChildFIO_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.testChildFIO_label)

        self.testChildFIO_input = QLineEdit(self.layoutWidget5)
        self.testChildFIO_input.setObjectName(u"testChildFIO_input")
        self.testChildFIO_input.setFont(font)
        self.testChildFIO_input.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid rgb(33, 33, 34);\n"
"}")
        self.testChildFIO_input.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.testChildFIO_input)


        self.horizontalLayout_7.addLayout(self.verticalLayout_19)

        self.layoutWidget_2 = QWidget(self.groupBox_4)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(30, 310, 1061, 241))
        self.verticalLayout_25 = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.resultsFindingData_label_2 = QLabel(self.layoutWidget_2)
        self.resultsFindingData_label_2.setObjectName(u"resultsFindingData_label_2")
        font3 = QFont()
        font3.setPointSize(14)
        font3.setBold(False)
        self.resultsFindingData_label_2.setFont(font3)
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
        self.tab2_documents = QWidget()
        self.tab2_documents.setObjectName(u"tab2_documents")
        self.tab2_documents.setStyleSheet(u"QScrollArea{\n"
"border: none;\n"
"}\n"
"")
        self.scrollArea = QScrollArea(self.tab2_documents)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(-20, 0, 1271, 651))
        self.scrollArea.setStyleSheet(u"")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1254, 1843))
        self.scrollAreaWidgetContents.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setVerticalSpacing(20)
        self.gridLayout.setContentsMargins(20, 20, 20, 20)
        self.findDocument_GB = QGroupBox(self.scrollAreaWidgetContents)
        self.findDocument_GB.setObjectName(u"findDocument_GB")
        font4 = QFont()
        font4.setPointSize(14)
        font4.setBold(False)
        font4.setItalic(False)
        self.findDocument_GB.setFont(font4)
        self.findDocument_GB.setStyleSheet(u"")
        self.gridLayout_2 = QGridLayout(self.findDocument_GB)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.findParentPassport_label = QLabel(self.findDocument_GB)
        self.findParentPassport_label.setObjectName(u"findParentPassport_label")
        self.findParentPassport_label.setFont(font)
        self.findParentPassport_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.findParentPassport_label)

        self.findParentPassportNumber_input = QLineEdit(self.findDocument_GB)
        self.findParentPassportNumber_input.setObjectName(u"findParentPassportNumber_input")
        self.findParentPassportNumber_input.setFont(font)
        self.findParentPassportNumber_input.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid rgb(33, 33, 34);\n"
"}")
        self.findParentPassportNumber_input.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.findParentPassportNumber_input)

        self.findParentPassportSeria_input = QLineEdit(self.findDocument_GB)
        self.findParentPassportSeria_input.setObjectName(u"findParentPassportSeria_input")
        self.findParentPassportSeria_input.setFont(font)
        self.findParentPassportSeria_input.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid rgb(33, 33, 34);\n"
"}")
        self.findParentPassportSeria_input.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.findParentPassportSeria_input)


        self.gridLayout_2.addLayout(self.verticalLayout_4, 1, 0, 1, 1)

        self.findParentFioData_button = QPushButton(self.findDocument_GB)
        self.findParentFioData_button.setObjectName(u"findParentFioData_button")
        self.findParentFioData_button.setFont(font1)
        self.findParentFioData_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.findParentFioData_button.setMouseTracking(True)
        self.findParentFioData_button.setTabletTracking(False)
        self.findParentFioData_button.setStyleSheet(u"QPushButton{\n"
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
        self.findParentFioData_button.setCheckable(False)
        self.findParentFioData_button.setAutoDefault(False)

        self.gridLayout_2.addWidget(self.findParentFioData_button, 0, 2, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.findParentFIO_label = QLabel(self.findDocument_GB)
        self.findParentFIO_label.setObjectName(u"findParentFIO_label")
        self.findParentFIO_label.setFont(font)
        self.findParentFIO_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.findParentFIO_label)

        self.findParentFIO_input = QLineEdit(self.findDocument_GB)
        self.findParentFIO_input.setObjectName(u"findParentFIO_input")
        self.findParentFIO_input.setFont(font)
        self.findParentFIO_input.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid rgb(33, 33, 34);\n"
"}")
        self.findParentFIO_input.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.findParentFIO_input)


        self.gridLayout_2.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        self.findParentPassData_button = QPushButton(self.findDocument_GB)
        self.findParentPassData_button.setObjectName(u"findParentPassData_button")
        self.findParentPassData_button.setFont(font1)
        self.findParentPassData_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.findParentPassData_button.setMouseTracking(True)
        self.findParentPassData_button.setTabletTracking(False)
        self.findParentPassData_button.setStyleSheet(u"QPushButton{\n"
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
        self.findParentPassData_button.setCheckable(False)
        self.findParentPassData_button.setAutoDefault(False)

        self.gridLayout_2.addWidget(self.findParentPassData_button, 1, 2, 1, 1)

        self.findChildFioData_button = QPushButton(self.findDocument_GB)
        self.findChildFioData_button.setObjectName(u"findChildFioData_button")
        self.findChildFioData_button.setFont(font1)
        self.findChildFioData_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.findChildFioData_button.setMouseTracking(True)
        self.findChildFioData_button.setTabletTracking(False)
        self.findChildFioData_button.setStyleSheet(u"QPushButton{\n"
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
        self.findChildFioData_button.setCheckable(False)
        self.findChildFioData_button.setAutoDefault(False)

        self.gridLayout_2.addWidget(self.findChildFioData_button, 2, 2, 1, 1)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.findChildFIO_label = QLabel(self.findDocument_GB)
        self.findChildFIO_label.setObjectName(u"findChildFIO_label")
        self.findChildFIO_label.setFont(font)
        self.findChildFIO_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.findChildFIO_label)

        self.findChildFIO_input = QLineEdit(self.findDocument_GB)
        self.findChildFIO_input.setObjectName(u"findChildFIO_input")
        self.findChildFIO_input.setFont(font)
        self.findChildFIO_input.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid rgb(33, 33, 34);\n"
"}")
        self.findChildFIO_input.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.findChildFIO_input)


        self.gridLayout_2.addLayout(self.verticalLayout_5, 2, 0, 1, 1)

        self.documentFindRes_listview = QListView(self.findDocument_GB)
        self.documentFindRes_listview.setObjectName(u"documentFindRes_listview")
        self.documentFindRes_listview.setEnabled(True)
        self.documentFindRes_listview.setMinimumSize(QSize(0, 200))

        self.gridLayout_2.addWidget(self.documentFindRes_listview, 5, 0, 3, 3)


        self.gridLayout.addWidget(self.findDocument_GB, 3, 0, 1, 1)

        self.createDocument_GB = QGroupBox(self.scrollAreaWidgetContents)
        self.createDocument_GB.setObjectName(u"createDocument_GB")
        self.createDocument_GB.setFont(font4)
        self.createDocument_GB.setFlat(False)
        self.createDocument_GB.setCheckable(False)
        self.gridLayout_4 = QGridLayout(self.createDocument_GB)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(10)
        self.gridLayout_4.setVerticalSpacing(25)
        self.gridLayout_4.setContentsMargins(-1, 25, -1, -1)
        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setSpacing(10)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.warning = QLabel(self.createDocument_GB)
        self.warning.setObjectName(u"warning")
        self.warning.setFont(font2)
        self.warning.setLayoutDirection(Qt.LeftToRight)
        self.warning.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.warning)

        self.Permission_checkbox = QCheckBox(self.createDocument_GB)
        self.Permission_checkbox.setObjectName(u"Permission_checkbox")
        self.Permission_checkbox.setFont(font)

        self.verticalLayout_15.addWidget(self.Permission_checkbox)


        self.verticalLayout_18.addLayout(self.verticalLayout_15)


        self.gridLayout_4.addLayout(self.verticalLayout_18, 2, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.documentPeriodDate_label = QLabel(self.createDocument_GB)
        self.documentPeriodDate_label.setObjectName(u"documentPeriodDate_label")
        self.documentPeriodDate_label.setFont(font)
        self.documentPeriodDate_label.setLayoutDirection(Qt.LeftToRight)
        self.documentPeriodDate_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.documentPeriodDate_label)

        self.documentPeriodDate_input = QDateEdit(self.createDocument_GB)
        self.documentPeriodDate_input.setObjectName(u"documentPeriodDate_input")
        self.documentPeriodDate_input.setFont(font)
        self.documentPeriodDate_input.setStyleSheet(u"QDateEdit{\n"
"border: 1px solid rgb(33, 33, 34);\n"
"padding: 1px;\n"
"}")
        self.documentPeriodDate_input.setAlignment(Qt.AlignCenter)
        self.documentPeriodDate_input.setButtonSymbols(QAbstractSpinBox.UpDownArrows)

        self.horizontalLayout.addWidget(self.documentPeriodDate_input)


        self.gridLayout_4.addLayout(self.horizontalLayout, 4, 0, 1, 1)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.price_label = QLabel(self.createDocument_GB)
        self.price_label.setObjectName(u"price_label")
        self.price_label.setFont(font)
        self.price_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.price_label)

        self.price_input = QLineEdit(self.createDocument_GB)
        self.price_input.setObjectName(u"price_input")
        self.price_input.setFont(font)
        self.price_input.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid rgb(33, 33, 34);\n"
"}")
        self.price_input.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.price_input)


        self.gridLayout_4.addLayout(self.horizontalLayout_12, 7, 0, 1, 1)

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


        self.gridLayout_4.addLayout(self.horizontalLayout_6, 3, 0, 1, 1)

        self.warning_2 = QLabel(self.createDocument_GB)
        self.warning_2.setObjectName(u"warning_2")
        self.warning_2.setFont(font2)
        self.warning_2.setLayoutDirection(Qt.LeftToRight)
        self.warning_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.warning_2, 9, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_3, 11, 0, 1, 1)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setSpacing(20)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
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

        self.findChildrenFioData_button = QPushButton(self.createDocument_GB)
        self.findChildrenFioData_button.setObjectName(u"findChildrenFioData_button")
        self.findChildrenFioData_button.setFont(font1)
        self.findChildrenFioData_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.findChildrenFioData_button.setMouseTracking(True)
        self.findChildrenFioData_button.setTabletTracking(False)
        self.findChildrenFioData_button.setStyleSheet(u"QPushButton{\n"
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
        self.findChildrenFioData_button.setCheckable(False)
        self.findChildrenFioData_button.setAutoDefault(False)

        self.verticalLayout_16.addWidget(self.findChildrenFioData_button)


        self.verticalLayout_13.addLayout(self.verticalLayout_16)

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


        self.verticalLayout_13.addLayout(self.verticalLayout_17)

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

        self.birthdayParent_label_2 = QLabel(self.createDocument_GB)
        self.birthdayParent_label_2.setObjectName(u"birthdayParent_label_2")
        self.birthdayParent_label_2.setFont(font)
        self.birthdayParent_label_2.setLayoutDirection(Qt.LeftToRight)
        self.birthdayParent_label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.birthdayParent_label_2)

        self.documentBirthdayParent_input = QDateEdit(self.createDocument_GB)
        self.documentBirthdayParent_input.setObjectName(u"documentBirthdayParent_input")
        self.documentBirthdayParent_input.setFont(font)
        self.documentBirthdayParent_input.setStyleSheet(u"QDateEdit{\n"
"border: 1px solid rgb(33, 33, 34);\n"
"padding: 1px;\n"
"}")
        self.documentBirthdayParent_input.setAlignment(Qt.AlignCenter)
        self.documentBirthdayParent_input.setButtonSymbols(QAbstractSpinBox.UpDownArrows)

        self.verticalLayout_13.addWidget(self.documentBirthdayParent_input)


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

        self.documentParentAdres_label = QLabel(self.createDocument_GB)
        self.documentParentAdres_label.setObjectName(u"documentParentAdres_label")
        self.documentParentAdres_label.setFont(font)
        self.documentParentAdres_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.documentParentAdres_label)

        self.documentParentAdres_input = QLineEdit(self.createDocument_GB)
        self.documentParentAdres_input.setObjectName(u"documentParentAdres_input")
        self.documentParentAdres_input.setFont(font)
        self.documentParentAdres_input.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid rgb(33, 33, 34);\n"
"}")
        self.documentParentAdres_input.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.documentParentAdres_input)


        self.verticalLayout_12.addLayout(self.verticalLayout_14)

        self.documentParentTelephoneNumber_label = QLabel(self.createDocument_GB)
        self.documentParentTelephoneNumber_label.setObjectName(u"documentParentTelephoneNumber_label")
        self.documentParentTelephoneNumber_label.setFont(font)
        self.documentParentTelephoneNumber_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.documentParentTelephoneNumber_label)

        self.documentParentTelephoneNumber_input = QLineEdit(self.createDocument_GB)
        self.documentParentTelephoneNumber_input.setObjectName(u"documentParentTelephoneNumber_input")
        self.documentParentTelephoneNumber_input.setFont(font)
        self.documentParentTelephoneNumber_input.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid rgb(33, 33, 34);\n"
"}")
        self.documentParentTelephoneNumber_input.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.documentParentTelephoneNumber_input)


        self.gridLayout_4.addLayout(self.verticalLayout_12, 1, 0, 1, 1)

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

        self.gridLayout_4.addWidget(self.createDocumentPDF_button, 10, 0, 1, 1)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.familyStepen_label = QLabel(self.createDocument_GB)
        self.familyStepen_label.setObjectName(u"familyStepen_label")
        self.familyStepen_label.setFont(font)
        self.familyStepen_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.familyStepen_label)

        self.familyStepen_input = QLineEdit(self.createDocument_GB)
        self.familyStepen_input.setObjectName(u"familyStepen_input")
        self.familyStepen_input.setFont(font)
        self.familyStepen_input.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid rgb(33, 33, 34);\n"
"}")
        self.familyStepen_input.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.familyStepen_input)


        self.gridLayout_4.addLayout(self.horizontalLayout_13, 8, 0, 1, 1)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.countOfLessons_label = QLabel(self.createDocument_GB)
        self.countOfLessons_label.setObjectName(u"countOfLessons_label")
        self.countOfLessons_label.setFont(font)
        self.countOfLessons_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.countOfLessons_label)

        self.countOfLessons_input = QLineEdit(self.createDocument_GB)
        self.countOfLessons_input.setObjectName(u"countOfLessons_input")
        self.countOfLessons_input.setFont(font)
        self.countOfLessons_input.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid rgb(33, 33, 34);\n"
"}")
        self.countOfLessons_input.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.countOfLessons_input)


        self.gridLayout_4.addLayout(self.horizontalLayout_11, 6, 0, 1, 1)


        self.gridLayout.addWidget(self.createDocument_GB, 4, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 2, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.tabWidget.addTab(self.tab2_documents, "")
        self.tab4_clientsData = QWidget()
        self.tab4_clientsData.setObjectName(u"tab4_clientsData")
        self.groupBox_6 = QGroupBox(self.tab4_clientsData)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setGeometry(QRect(50, 10, 1121, 641))
        self.findDataChildFIO_button = QPushButton(self.groupBox_6)
        self.findDataChildFIO_button.setObjectName(u"findDataChildFIO_button")
        self.findDataChildFIO_button.setGeometry(QRect(130, 180, 331, 45))
        self.findDataChildFIO_button.setFont(font1)
        self.findDataChildFIO_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.findDataChildFIO_button.setMouseTracking(True)
        self.findDataChildFIO_button.setTabletTracking(False)
        self.findDataChildFIO_button.setStyleSheet(u"QPushButton{\n"
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
        self.findDataChildFIO_button.setCheckable(False)
        self.findDataChildFIO_button.setAutoDefault(False)
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
        self.layoutWidget6 = QWidget(self.groupBox_6)
        self.layoutWidget6.setObjectName(u"layoutWidget6")
        self.layoutWidget6.setGeometry(QRect(30, 300, 1061, 241))
        self.verticalLayout_23 = QVBoxLayout(self.layoutWidget6)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.resultsFindingData_label = QLabel(self.layoutWidget6)
        self.resultsFindingData_label.setObjectName(u"resultsFindingData_label")
        self.resultsFindingData_label.setFont(font3)
        self.resultsFindingData_label.setLayoutDirection(Qt.LeftToRight)
        self.resultsFindingData_label.setAlignment(Qt.AlignCenter)
        self.resultsFindingData_label.setWordWrap(False)

        self.verticalLayout_23.addWidget(self.resultsFindingData_label)

        self.resultsFindingData_listview = QListView(self.layoutWidget6)
        self.resultsFindingData_listview.setObjectName(u"resultsFindingData_listview")
        self.resultsFindingData_listview.setEnabled(True)
        self.resultsFindingData_listview.setMinimumSize(QSize(0, 200))

        self.verticalLayout_23.addWidget(self.resultsFindingData_listview)

        self.findDataParentFIO_button = QPushButton(self.groupBox_6)
        self.findDataParentFIO_button.setObjectName(u"findDataParentFIO_button")
        self.findDataParentFIO_button.setGeometry(QRect(640, 180, 331, 45))
        self.findDataParentFIO_button.setFont(font1)
        self.findDataParentFIO_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.findDataParentFIO_button.setMouseTracking(True)
        self.findDataParentFIO_button.setTabletTracking(False)
        self.findDataParentFIO_button.setStyleSheet(u"QPushButton{\n"
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
        self.findDataParentFIO_button.setCheckable(False)
        self.findDataParentFIO_button.setAutoDefault(False)
        self.tabWidget.addTab(self.tab4_clientsData, "")
        self.tab5_statistic = QWidget()
        self.tab5_statistic.setObjectName(u"tab5_statistic")
        self.layoutWidget7 = QWidget(self.tab5_statistic)
        self.layoutWidget7.setObjectName(u"layoutWidget7")
        self.layoutWidget7.setGeometry(QRect(30, 80, 931, 72))
        self.verticalLayout_24 = QVBoxLayout(self.layoutWidget7)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(10)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.parentsRowCount_label = QLabel(self.layoutWidget7)
        self.parentsRowCount_label.setObjectName(u"parentsRowCount_label")
        self.parentsRowCount_label.setFont(font)
        self.parentsRowCount_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.parentsRowCount_label)

        self.parentsRowCount_input = QLineEdit(self.layoutWidget7)
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
        self.childRowCount_label = QLabel(self.layoutWidget7)
        self.childRowCount_label.setObjectName(u"childRowCount_label")
        self.childRowCount_label.setFont(font)
        self.childRowCount_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.childRowCount_label)

        self.childRowCount_input = QLineEdit(self.layoutWidget7)
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

        self.gridLayout_3.addWidget(self.tabWidget, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Teremok", None))
        self.child_GB.setTitle(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0431\u0451\u043d\u043e\u043a", None))
        self.childFIO_label.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0418\u041e*:", None))
        self.birthdayChild_label.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f*:", None))
        self.diagnos_label.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0438\u0430\u0433\u043d\u043e\u0437 (\u043f\u0440\u0438 \u043d\u0430\u043b\u0438\u0447\u0438\u0438):", None))
        self.childFIO_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0424\u0418\u041e \u0440\u0435\u0431\u0451\u043d\u043a\u0430", None))
        self.diagnos_input.setText("")
        self.diagnos_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0414\u0438\u0430\u0433\u043d\u043e\u0437 \u0440\u0435\u0431\u0451\u043d\u043a\u0430 (\u043f\u0440\u0438 \u043d\u0430\u043b\u0438\u0447\u0438\u0438):", None))
        self.aboutChild_label.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0449\u0438\u0435 \u0441\u0432\u0435\u0434\u0435\u043d\u0438\u044f \u043e \u0440\u0435\u0431\u0451\u043d\u043a\u0435 (\u043f\u043e\u0432\u0435\u0434\u0435\u043d\u0438\u0435, \u043f\u0440\u0438\u0432\u044b\u0447\u043a\u0438 \u0438 \u0442.\u0434.):", None))
        self.aboutChild_input.setPlainText("")
        self.aboutChild_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u0435 \u0434\u043b\u044f \u043e\u0431\u0449\u0438\u0445 \u0441\u0432\u0435\u0434\u0435\u043d\u0438\u0439", None))
        self.selectParent_label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u0440\u043e\u0434\u0438\u0442\u0435\u043b\u044f \u0440\u0435\u0431\u0451\u043d\u043a\u0430*:", None))
        self.dateFirstConsultation_label.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u043f\u0440\u043e\u0432\u0435\u0434\u0435\u043d\u0438\u044f \u041f\u041a*:", None))
        self.timeFirstConsultation_label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0440\u0435\u043c\u044f \u043f\u0440\u043e\u0432\u0435\u0434\u0435\u043d\u0438\u044f \u041f\u041a:", None))
        self.parent_GB.setTitle(QCoreApplication.translate("MainWindow", u"\u0420\u043e\u0434\u0438\u0442\u0435\u043b\u044c", None))
        self.saveParentData_button.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435 \u0440\u043e\u0434\u0438\u0442\u0435\u043b\u044f", None))
        self.childFIO_label_2.setText(QCoreApplication.translate("MainWindow", u"* - \u043f\u043e\u043b\u044f, \u043e\u0431\u044f\u0437\u0430\u0442\u0435\u043b\u044c\u043d\u044b\u0435 \u043a \u0437\u0430\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044e", None))
        self.parentTelephoneNumber_label.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u043c\u0435\u0440 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430 *:", None))
        self.parentTelephoneNumber_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u043c\u0435\u0440 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430", None))
        self.passNumber_label.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u043c\u0435\u0440 \u043f\u0430\u0441\u043f\u043e\u0440\u0442\u0430:", None))
        self.parentFIO_label.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0418\u041e*:", None))
        self.whoGavePass_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041a\u0435\u043c \u0432\u044b\u0434\u0430\u043d", None))
        self.parentAdres_label.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0434\u0440\u0435\u0441:", None))
        self.birthdayParent_label.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f:", None))
        self.passSeria_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0421\u0435\u0440\u0438\u044f \u043f\u0430\u0441\u043f\u043e\u0440\u0442\u0430", None))
        self.parentFIO_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0424\u0418\u041e \u0440\u043e\u0434\u0438\u0442\u0435\u043b\u044f", None))
        self.passSeria_label.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0435\u0440\u0438\u044f \u043f\u0430\u0441\u043f\u043e\u0440\u0442\u0430:", None))
        self.parentAdres_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0410\u0434\u0440\u0435\u0441", None))
        self.whoGavePass_label.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0435\u043c \u0432\u044b\u0434\u0430\u043d:", None))
        self.passportDate_label.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u0432\u044b\u0434\u0430\u0447\u0438:", None))
        self.passNumber_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u043c\u0435\u0440 \u043f\u0430\u0441\u043f\u043e\u0440\u0442\u0430", None))
        self.clearAll_button.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0439\u0442\u0438 \u0431\u0435\u0437 \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f", None))
        self.saveChildData_button.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435 \u041f\u041a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1_firstConsultation), QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0432\u0438\u0447\u043d\u0430\u044f \u043a\u043e\u043d\u0441\u0443\u043b\u044c\u0442\u0430\u0446\u0438\u044f", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a \u0441\u0443\u0449\u0435\u0441\u0442\u0432\u0443\u044e\u0449\u0438\u0445 \u0437\u0430\u043f\u0438\u0441\u0435\u0439", None))
        self.warning_3.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0434\u0430\u043d\u043d\u044b\u0435 \u0434\u043b\u044f \u043d\u0430\u0447\u0430\u043b\u0430 \u0442\u0435\u0441\u0442\u0430 \u0438\u043b\u0438 \u043f\u043e\u0438\u0441\u043a\u0430 \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u043e\u0432 \u0442\u0435\u0441\u0442\u0430:", None))
        self.findDataTest_button.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u043e\u0432 \u0442\u0435\u0441\u0442\u0430", None))
        self.startTest_button.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447\u0430\u0442\u044c \u0442\u0435\u0441\u0442", None))
        self.testChildFIO_label.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0418\u041e \u0440\u0435\u0431\u0451\u043d\u043a\u0430:", None))
        self.testChildFIO_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0424\u0418\u041e \u0440\u0435\u0431\u0451\u043d\u043a\u0430", None))
        self.resultsFindingData_label_2.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u044b \u043f\u043e\u0438\u0441\u043a\u0430:", None))
        self.deleteCurrentData_button_3.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u044b\u0435 \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab3_testAtek), QCoreApplication.translate("MainWindow", u"\u0422\u0435\u0441\u0442 \u0410\u0422\u0415\u041a", None))
        self.findDocument_GB.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a \u0434\u043e\u0433\u043e\u0432\u043e\u0440\u043e\u0432", None))
        self.findParentPassport_label.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a \u043f\u043e \u043f\u0430\u0441\u043f\u043e\u0440\u0442\u043d\u044b\u043c \u0434\u0430\u043d\u043d\u044b\u043c \u043e\u0434\u043d\u043e\u0433\u043e \u0438\u0437 \u0440\u043e\u0434\u0438\u0442\u0435\u043b\u0435\u0439:", None))
        self.findParentPassportNumber_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u043c\u0435\u0440 \u043f\u0430\u0441\u043f\u043e\u0440\u0442\u0430", None))
        self.findParentPassportSeria_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0421\u0435\u0440\u0438\u044f \u043f\u0430\u0441\u043f\u043e\u0440\u0442\u0430", None))
        self.findParentFioData_button.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a \u043f\u043e \u0424\u0418\u041e \u0440\u043e\u0434\u0438\u0442\u0435\u043b\u044f", None))
        self.findParentFIO_label.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a \u043f\u043e \u0424\u0418\u041e \u0440\u043e\u0434\u0438\u0442\u0435\u043b\u044f:", None))
        self.findParentFIO_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0424\u0418\u041e \u0440\u043e\u0434\u0438\u0442\u0435\u043b\u044f", None))
        self.findParentPassData_button.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a \u043f\u043e \u043f\u0430\u0441\u043f\u043e\u0440\u0442\u0443 \u0440\u043e\u0434\u0438\u0442\u0435\u043b\u044f", None))
        self.findChildFioData_button.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a \u043f\u043e \u0424\u0418\u041e \u0440\u0435\u0431\u0451\u043d\u043a\u0430", None))
        self.findChildFIO_label.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a \u043f\u043e \u0424\u0418\u041e \u0440\u0435\u0431\u0451\u043d\u043a\u0430:", None))
        self.findChildFIO_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0424\u0418\u041e \u0440\u0435\u0431\u0451\u043d\u043a\u0430", None))
        self.createDocument_GB.setTitle(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u043d\u0438\u0435 \u043d\u043e\u0432\u043e\u0433\u043e \u0434\u043e\u0433\u043e\u0432\u043e\u0440\u0430", None))
        self.warning.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043c\u0435\u0447\u0430\u044f \u201c\u0420\u0430\u0437\u0440\u0435\u0448\u0430\u044e\u201d, \u044f \u0434\u0430\u044e \u0441\u0432\u043e\u0451 \u0441\u043e\u0433\u043b\u0430\u0441\u0438\u0435 \u043d\u0430 \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u043d\u0438\u0435 \u0444\u043e\u0442\u043e \u0438 \u0432\u0438\u0434\u0435\u043e\u043c\u0430\u0442\u0435\u0440\u0438\u0430\u043b\u043e\u0432 \u0432 \u043a\u043e\u043c\u043c\u0435\u0440\u0447\u0435\u0441\u043a\u0438\u0445 \u0446\u0435\u043b\u044f\u0445", None))
        self.Permission_checkbox.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u0440\u0435\u0448\u0435\u043d\u0438\u0435 \u043d\u0430 \u0444\u043e\u0442\u043e\u0441\u044a\u0451\u043c\u043a\u0443 \u0438 \u0432\u0438\u0434\u0435\u043e\u0441\u044a\u0451\u043c\u043a\u0443, \u0430 \u0442\u0430\u043a\u0436\u0435 \u0438\u0445 \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u043d\u0438\u0435 \u0432 \u043a\u043e\u043c\u043c\u0435\u0440\u0447\u0435\u0441\u043a\u0438\u0445 \u0446\u0435\u043b\u044f\u0445", None))
        self.documentPeriodDate_label.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0440\u043e\u043a \u0441\u043e\u0441\u0442\u0430\u0432\u043b\u0435\u043d\u0438\u044f \u0434\u043e\u0433\u043e\u0432\u043e\u0440\u0430*:", None))
        self.price_label.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c \u0443\u0441\u043b\u0443\u0433*:", None))
        self.price_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c \u0443\u0441\u043b\u0443\u0433", None))
        self.createData_label.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f \u0438 \u043f\u043e\u0434\u043f\u0438\u0441\u0438 \u0434\u043e\u0433\u043e\u0432\u043e\u0440\u0430*:", None))
        self.warning_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>*\u0417\u0430\u043f\u043e\u043b\u043d\u0438\u0442\u0435 \u043e\u0441\u0442\u0430\u043b\u044c\u043d\u044b\u0435 \u043f\u043e\u043b\u044f \u0434\u043b\u044f \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f \u0434\u043e\u0433\u043e\u0432\u043e\u0440\u0430.<br/>\u0415\u0441\u043b\u0438 \u043d\u0430\u0439\u0434\u0435\u043d\u043d\u044b\u0435 \u0432\u044b\u0448\u0435 \u0434\u0430\u043d\u043d\u044b\u0435 \u043d\u0435\u043a\u043e\u0440\u0440\u0435\u043a\u0442\u043d\u044b \u043f\u0435\u0440\u0435\u0439\u0434\u0438\u0442\u0435 \u0432 \u043e\u043a\u043d\u043e &quot;\u0414\u0430\u043d\u043d\u044b\u0435 \u043e \u043a\u043b\u0438\u0435\u043d\u0442\u0430\u0445&quot; \u0438 \u0432\u043d\u0435\u0441\u0438\u0442\u0435 \u043d\u0443\u0436\u043d\u044b\u0435 \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f.</p><p><br/></p><p>\u041f\u043e\u0441\u043b\u0435 \u0437\u0430\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f \u0432\u0441\u0435\u0445 \u043f\u043e\u043b\u0435\u0439 \u043d\u0435\u043e\u0431\u0445\u043e"
                        "\u0434\u0438\u043c\u043e \u0441\u0444\u043e\u0440\u043c\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0434\u043e\u0433\u043e\u0432\u043e\u0440 \u0432 PDF \u0444\u0430\u0439\u043b, \u0440\u0430\u0441\u043f\u0435\u0447\u0430\u0442\u0430\u0442\u044c \u0438 \u043f\u043e\u0434\u043f\u0438\u0441\u0430\u0442\u044c \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442</p></body></html>", None))
        self.createChildFIO_label.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0418\u041e \u0440\u0435\u0431\u0451\u043d\u043a\u0430:", None))
        self.createChildFIO_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0424\u0418\u041e \u0440\u0435\u0431\u0451\u043d\u043a\u0430", None))
        self.findChildrenFioData_button.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0439\u0442\u0438 \u0434\u0430\u043d\u043d\u044b\u0435 \u043f\u043e \u0424\u0418\u041e \u0440\u0435\u0431\u0451\u043d\u043a\u0430", None))
        self.createChildBirthday_label.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f \u0440\u0435\u0431\u0451\u043d\u043a\u0430:", None))
        self.createParentFIO_label.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0418\u041e \u0440\u043e\u0434\u0438\u0442\u0435\u043b\u044f:", None))
        self.createParentFIO_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0424\u0418\u041e \u0440\u043e\u0434\u0438\u0442\u0435\u043b\u044f", None))
        self.birthdayParent_label_2.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f \u0440\u043e\u0434\u0438\u0442\u0435\u043b\u044f:", None))
        self.createParentPassport_label.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0441\u043f\u043e\u0440\u0442\u043d\u044b\u0435 \u0434\u0430\u043d\u043d\u044b\u0435 \u043e\u0434\u043d\u043e\u0433\u043e \u0438\u0437 \u0440\u043e\u0434\u0438\u0442\u0435\u043b\u0435\u0439:", None))
        self.createParentPassportSeria_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0421\u0435\u0440\u0438\u044f \u043f\u0430\u0441\u043f\u043e\u0440\u0442\u0430", None))
        self.createParentPassportNumber_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u043c\u0435\u0440 \u043f\u0430\u0441\u043f\u043e\u0440\u0442\u0430", None))
        self.documentParentAdres_label.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0434\u0440\u0435\u0441:", None))
        self.documentParentAdres_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0410\u0434\u0440\u0435\u0441", None))
        self.documentParentTelephoneNumber_label.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u043c\u0435\u0440 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430 *:", None))
        self.documentParentTelephoneNumber_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u043c\u0435\u0440 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430", None))
        self.createDocumentPDF_button.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0444\u043e\u0440\u043c\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0434\u043e\u0433\u043e\u0432\u043e\u0440 \u0432 PDF", None))
        self.familyStepen_label.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0435\u043f\u0435\u043d\u044c \u0440\u043e\u0434\u0441\u0442\u0432\u0430*:", None))
        self.familyStepen_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0435\u043f\u0435\u043d\u044c \u0440\u043e\u0434\u0441\u0442\u0432\u0430", None))
        self.countOfLessons_label.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0437\u0430\u043d\u044f\u0442\u0438\u0439*:", None))
        self.countOfLessons_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0437\u0430\u043d\u044f\u0442\u0438\u0439", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2_documents), QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0433\u043e\u0432\u043e\u0440\u044b", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a \u0441\u0443\u0449\u0435\u0441\u0442\u0432\u0443\u044e\u0449\u0438\u0445 \u0434\u0430\u043d\u043d\u044b\u0445", None))
        self.findDataChildFIO_button.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0439\u0442\u0438 \u0434\u0430\u043d\u043d\u044b\u0435 \u0440\u0435\u0431\u0451\u043d\u043a\u0430 \u043f\u043e \u0424\u0418\u041e", None))
        self.statusFindingData_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0439\u0434\u0435\u043d\u044b / \u043d\u0435 \u043d\u0430\u0439\u0434\u0435\u043d\u044b", None))
        self.findDataChildFIO_label.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0418\u041e \u0440\u0435\u0431\u0451\u043d\u043a\u0430:", None))
        self.findDataChildFIO_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0424\u0418\u041e \u0440\u0435\u0431\u0451\u043d\u043a\u0430", None))
        self.findDataParentFIO_label.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0418\u041e \u0440\u043e\u0434\u0438\u0442\u0435\u043b\u044f:", None))
        self.findDataParentFIO_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0424\u0418\u041e \u0440\u043e\u0434\u0438\u0442\u0435\u043b\u044f", None))
        self.deleteCurrentData_button.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.changeCurrentData_button.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0441\u043c\u043e\u0442\u0440\u0435\u0442\u044c/\u0438\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.resultsFindingData_label.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u044b \u043f\u043e\u0438\u0441\u043a\u0430:", None))
        self.findDataParentFIO_button.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0439\u0442\u0438 \u0434\u0430\u043d\u043d\u044b\u0435 \u0440\u043e\u0434\u0438\u0442\u0435\u043b\u044f \u043f\u043e \u0424\u0418\u041e", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab4_clientsData), QCoreApplication.translate("MainWindow", u"\u0414\u0430\u043d\u043d\u044b\u0435 \u043e \u043a\u043b\u0438\u0435\u043d\u0442\u0430\u0445", None))
        self.parentsRowCount_label.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0440\u043e\u0434\u0438\u0442\u0435\u043b\u0435\u0439, \u0437\u0430\u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0445 \u0432 \u0431\u0430\u0437\u0435 \u0432 \u043d\u0430\u0441\u0442\u043e\u044f\u0449\u0438\u0439 \u043c\u043e\u043c\u0435\u043d\u0442:", None))
        self.parentsRowCount_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0440\u043e\u0434\u0438\u0442\u0435\u043b\u0435\u0439", None))
        self.childRowCount_label.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0434\u0435\u0442\u0435\u0439, \u0437\u0430\u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0445 \u0432 \u0431\u0430\u0437\u0435 \u0432 \u043d\u0430\u0441\u0442\u043e\u044f\u0449\u0438\u0439 \u043c\u043e\u043c\u0435\u043d\u0442:", None))
        self.childRowCount_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0434\u0435\u0442\u0435\u0439", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab5_statistic), QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430", None))
    # retranslateUi

