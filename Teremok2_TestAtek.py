# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Teremok2_TestAtek.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QMainWindow, QPushButton,
    QRadioButton, QScrollArea, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_TestWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(720, 720)
        MainWindow.setStyleSheet(u"QMainWindow{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.saveData_button = QPushButton(self.centralwidget)
        self.saveData_button.setObjectName(u"saveData_button")
        self.saveData_button.setGeometry(QRect(340, 670, 291, 41))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(14)
        self.saveData_button.setFont(font)
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
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(0, 0, 721, 661))
        self.scrollArea.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, -6647, 702, 7306))
        self.scrollAreaWidgetContents.setStyleSheet(u"")
        self.gridLayout_2 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setVerticalSpacing(50)
        self.gridLayout_2.setContentsMargins(15, 15, 15, 15)
        self.block2 = QGroupBox(self.scrollAreaWidgetContents)
        self.block2.setObjectName(u"block2")
        self.block2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.gridLayout_3 = QGridLayout(self.block2)
        self.gridLayout_3.setSpacing(10)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(10, 10, 10, 10)
        self.block2_item01 = QGroupBox(self.block2)
        self.block2_item01.setObjectName(u"block2_item01")
        self.verticalLayout_20 = QVBoxLayout(self.block2_item01)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_27 = QLabel(self.block2_item01)
        self.label_27.setObjectName(u"label_27")
        font1 = QFont()
        font1.setPointSize(14)
        self.label_27.setFont(font1)
        self.label_27.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_27.setWordWrap(True)

        self.verticalLayout_20.addWidget(self.label_27)

        self._20 = QHBoxLayout()
        self._20.setSpacing(0)
        self._20.setObjectName(u"_20")
        self.radioButton_58 = QRadioButton(self.block2_item01)
        self.radioButton_58.setObjectName(u"radioButton_58")
        self.radioButton_58.setFont(font1)

        self._20.addWidget(self.radioButton_58)

        self.radioButton_59 = QRadioButton(self.block2_item01)
        self.radioButton_59.setObjectName(u"radioButton_59")
        self.radioButton_59.setFont(font1)

        self._20.addWidget(self.radioButton_59)

        self.radioButton_60 = QRadioButton(self.block2_item01)
        self.radioButton_60.setObjectName(u"radioButton_60")
        self.radioButton_60.setFont(font1)

        self._20.addWidget(self.radioButton_60)


        self.verticalLayout_20.addLayout(self._20)


        self.gridLayout_3.addWidget(self.block2_item01, 0, 0, 1, 1)

        self.block2_item02 = QGroupBox(self.block2)
        self.block2_item02.setObjectName(u"block2_item02")
        self.verticalLayout_28 = QVBoxLayout(self.block2_item02)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.label_35 = QLabel(self.block2_item02)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setFont(font1)
        self.label_35.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_28.addWidget(self.label_35)

        self._28 = QHBoxLayout()
        self._28.setSpacing(0)
        self._28.setObjectName(u"_28")
        self.radioButton_82 = QRadioButton(self.block2_item02)
        self.radioButton_82.setObjectName(u"radioButton_82")
        self.radioButton_82.setFont(font1)

        self._28.addWidget(self.radioButton_82)

        self.radioButton_83 = QRadioButton(self.block2_item02)
        self.radioButton_83.setObjectName(u"radioButton_83")
        self.radioButton_83.setFont(font1)

        self._28.addWidget(self.radioButton_83)

        self.radioButton_84 = QRadioButton(self.block2_item02)
        self.radioButton_84.setObjectName(u"radioButton_84")
        self.radioButton_84.setFont(font1)

        self._28.addWidget(self.radioButton_84)


        self.verticalLayout_28.addLayout(self._28)


        self.gridLayout_3.addWidget(self.block2_item02, 1, 0, 1, 1)

        self.block2_item03 = QGroupBox(self.block2)
        self.block2_item03.setObjectName(u"block2_item03")
        self.verticalLayout_16 = QVBoxLayout(self.block2_item03)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_23 = QLabel(self.block2_item03)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font1)
        self.label_23.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_23.setWordWrap(True)

        self.verticalLayout_16.addWidget(self.label_23)

        self._16 = QHBoxLayout()
        self._16.setSpacing(0)
        self._16.setObjectName(u"_16")
        self.radioButton_46 = QRadioButton(self.block2_item03)
        self.radioButton_46.setObjectName(u"radioButton_46")
        self.radioButton_46.setFont(font1)

        self._16.addWidget(self.radioButton_46)

        self.radioButton_47 = QRadioButton(self.block2_item03)
        self.radioButton_47.setObjectName(u"radioButton_47")
        self.radioButton_47.setFont(font1)

        self._16.addWidget(self.radioButton_47)

        self.radioButton_48 = QRadioButton(self.block2_item03)
        self.radioButton_48.setObjectName(u"radioButton_48")
        self.radioButton_48.setFont(font1)

        self._16.addWidget(self.radioButton_48)


        self.verticalLayout_16.addLayout(self._16)


        self.gridLayout_3.addWidget(self.block2_item03, 2, 0, 1, 1)

        self.block2_item04 = QGroupBox(self.block2)
        self.block2_item04.setObjectName(u"block2_item04")
        self.verticalLayout_19 = QVBoxLayout(self.block2_item04)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_26 = QLabel(self.block2_item04)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font1)
        self.label_26.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_19.addWidget(self.label_26)

        self._19 = QHBoxLayout()
        self._19.setSpacing(0)
        self._19.setObjectName(u"_19")
        self.radioButton_55 = QRadioButton(self.block2_item04)
        self.radioButton_55.setObjectName(u"radioButton_55")
        self.radioButton_55.setFont(font1)

        self._19.addWidget(self.radioButton_55)

        self.radioButton_56 = QRadioButton(self.block2_item04)
        self.radioButton_56.setObjectName(u"radioButton_56")
        self.radioButton_56.setFont(font1)

        self._19.addWidget(self.radioButton_56)

        self.radioButton_57 = QRadioButton(self.block2_item04)
        self.radioButton_57.setObjectName(u"radioButton_57")
        self.radioButton_57.setFont(font1)

        self._19.addWidget(self.radioButton_57)


        self.verticalLayout_19.addLayout(self._19)


        self.gridLayout_3.addWidget(self.block2_item04, 3, 0, 1, 1)

        self.block2_item05 = QGroupBox(self.block2)
        self.block2_item05.setObjectName(u"block2_item05")
        self.verticalLayout_23 = QVBoxLayout(self.block2_item05)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_30 = QLabel(self.block2_item05)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font1)
        self.label_30.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_23.addWidget(self.label_30)

        self._23 = QHBoxLayout()
        self._23.setSpacing(0)
        self._23.setObjectName(u"_23")
        self.radioButton_67 = QRadioButton(self.block2_item05)
        self.radioButton_67.setObjectName(u"radioButton_67")
        self.radioButton_67.setFont(font1)

        self._23.addWidget(self.radioButton_67)

        self.radioButton_68 = QRadioButton(self.block2_item05)
        self.radioButton_68.setObjectName(u"radioButton_68")
        self.radioButton_68.setFont(font1)

        self._23.addWidget(self.radioButton_68)

        self.radioButton_69 = QRadioButton(self.block2_item05)
        self.radioButton_69.setObjectName(u"radioButton_69")
        self.radioButton_69.setFont(font1)

        self._23.addWidget(self.radioButton_69)


        self.verticalLayout_23.addLayout(self._23)


        self.gridLayout_3.addWidget(self.block2_item05, 4, 0, 1, 1)

        self.block2_item06 = QGroupBox(self.block2)
        self.block2_item06.setObjectName(u"block2_item06")
        self.verticalLayout_18 = QVBoxLayout(self.block2_item06)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_25 = QLabel(self.block2_item06)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font1)
        self.label_25.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_18.addWidget(self.label_25)

        self._18 = QHBoxLayout()
        self._18.setSpacing(0)
        self._18.setObjectName(u"_18")
        self.radioButton_52 = QRadioButton(self.block2_item06)
        self.radioButton_52.setObjectName(u"radioButton_52")
        self.radioButton_52.setFont(font1)

        self._18.addWidget(self.radioButton_52)

        self.radioButton_53 = QRadioButton(self.block2_item06)
        self.radioButton_53.setObjectName(u"radioButton_53")
        self.radioButton_53.setFont(font1)

        self._18.addWidget(self.radioButton_53)

        self.radioButton_54 = QRadioButton(self.block2_item06)
        self.radioButton_54.setObjectName(u"radioButton_54")
        self.radioButton_54.setFont(font1)

        self._18.addWidget(self.radioButton_54)


        self.verticalLayout_18.addLayout(self._18)


        self.gridLayout_3.addWidget(self.block2_item06, 5, 0, 1, 1)

        self.block2_item07 = QGroupBox(self.block2)
        self.block2_item07.setObjectName(u"block2_item07")
        self.verticalLayout_24 = QVBoxLayout(self.block2_item07)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.label_31 = QLabel(self.block2_item07)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font1)
        self.label_31.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_24.addWidget(self.label_31)

        self._24 = QHBoxLayout()
        self._24.setSpacing(0)
        self._24.setObjectName(u"_24")
        self.radioButton_70 = QRadioButton(self.block2_item07)
        self.radioButton_70.setObjectName(u"radioButton_70")
        self.radioButton_70.setFont(font1)

        self._24.addWidget(self.radioButton_70)

        self.radioButton_71 = QRadioButton(self.block2_item07)
        self.radioButton_71.setObjectName(u"radioButton_71")
        self.radioButton_71.setFont(font1)

        self._24.addWidget(self.radioButton_71)

        self.radioButton_72 = QRadioButton(self.block2_item07)
        self.radioButton_72.setObjectName(u"radioButton_72")
        self.radioButton_72.setFont(font1)

        self._24.addWidget(self.radioButton_72)


        self.verticalLayout_24.addLayout(self._24)


        self.gridLayout_3.addWidget(self.block2_item07, 6, 0, 1, 1)

        self.block2_item08 = QGroupBox(self.block2)
        self.block2_item08.setObjectName(u"block2_item08")
        self.verticalLayout_25 = QVBoxLayout(self.block2_item08)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.label_32 = QLabel(self.block2_item08)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setFont(font1)
        self.label_32.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_25.addWidget(self.label_32)

        self._25 = QHBoxLayout()
        self._25.setSpacing(0)
        self._25.setObjectName(u"_25")
        self.radioButton_73 = QRadioButton(self.block2_item08)
        self.radioButton_73.setObjectName(u"radioButton_73")
        self.radioButton_73.setFont(font1)

        self._25.addWidget(self.radioButton_73)

        self.radioButton_74 = QRadioButton(self.block2_item08)
        self.radioButton_74.setObjectName(u"radioButton_74")
        self.radioButton_74.setFont(font1)

        self._25.addWidget(self.radioButton_74)

        self.radioButton_75 = QRadioButton(self.block2_item08)
        self.radioButton_75.setObjectName(u"radioButton_75")
        self.radioButton_75.setFont(font1)

        self._25.addWidget(self.radioButton_75)


        self.verticalLayout_25.addLayout(self._25)


        self.gridLayout_3.addWidget(self.block2_item08, 7, 0, 1, 1)

        self.block2_item09 = QGroupBox(self.block2)
        self.block2_item09.setObjectName(u"block2_item09")
        self.verticalLayout_22 = QVBoxLayout(self.block2_item09)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.label_29 = QLabel(self.block2_item09)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font1)
        self.label_29.setAutoFillBackground(False)
        self.label_29.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_22.addWidget(self.label_29)

        self._22 = QHBoxLayout()
        self._22.setSpacing(0)
        self._22.setObjectName(u"_22")
        self.radioButton_64 = QRadioButton(self.block2_item09)
        self.radioButton_64.setObjectName(u"radioButton_64")
        self.radioButton_64.setFont(font1)

        self._22.addWidget(self.radioButton_64)

        self.radioButton_65 = QRadioButton(self.block2_item09)
        self.radioButton_65.setObjectName(u"radioButton_65")
        self.radioButton_65.setFont(font1)

        self._22.addWidget(self.radioButton_65)

        self.radioButton_66 = QRadioButton(self.block2_item09)
        self.radioButton_66.setObjectName(u"radioButton_66")
        self.radioButton_66.setFont(font1)

        self._22.addWidget(self.radioButton_66)


        self.verticalLayout_22.addLayout(self._22)


        self.gridLayout_3.addWidget(self.block2_item09, 8, 0, 1, 1)

        self.block2_item10 = QGroupBox(self.block2)
        self.block2_item10.setObjectName(u"block2_item10")
        self.verticalLayout_17 = QVBoxLayout(self.block2_item10)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_24 = QLabel(self.block2_item10)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font1)
        self.label_24.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_24.setWordWrap(False)

        self.verticalLayout_17.addWidget(self.label_24)

        self._17 = QHBoxLayout()
        self._17.setSpacing(0)
        self._17.setObjectName(u"_17")
        self.radioButton_49 = QRadioButton(self.block2_item10)
        self.radioButton_49.setObjectName(u"radioButton_49")
        self.radioButton_49.setFont(font1)

        self._17.addWidget(self.radioButton_49)

        self.radioButton_50 = QRadioButton(self.block2_item10)
        self.radioButton_50.setObjectName(u"radioButton_50")
        self.radioButton_50.setFont(font1)

        self._17.addWidget(self.radioButton_50)

        self.radioButton_51 = QRadioButton(self.block2_item10)
        self.radioButton_51.setObjectName(u"radioButton_51")
        self.radioButton_51.setFont(font1)

        self._17.addWidget(self.radioButton_51)


        self.verticalLayout_17.addLayout(self._17)


        self.gridLayout_3.addWidget(self.block2_item10, 9, 0, 1, 1)

        self.block2_item11 = QGroupBox(self.block2)
        self.block2_item11.setObjectName(u"block2_item11")
        self.verticalLayout_21 = QVBoxLayout(self.block2_item11)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.label_28 = QLabel(self.block2_item11)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font1)
        self.label_28.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_21.addWidget(self.label_28)

        self._21 = QHBoxLayout()
        self._21.setSpacing(0)
        self._21.setObjectName(u"_21")
        self.radioButton_61 = QRadioButton(self.block2_item11)
        self.radioButton_61.setObjectName(u"radioButton_61")
        self.radioButton_61.setFont(font1)

        self._21.addWidget(self.radioButton_61)

        self.radioButton_62 = QRadioButton(self.block2_item11)
        self.radioButton_62.setObjectName(u"radioButton_62")
        self.radioButton_62.setFont(font1)

        self._21.addWidget(self.radioButton_62)

        self.radioButton_63 = QRadioButton(self.block2_item11)
        self.radioButton_63.setObjectName(u"radioButton_63")
        self.radioButton_63.setFont(font1)

        self._21.addWidget(self.radioButton_63)


        self.verticalLayout_21.addLayout(self._21)


        self.gridLayout_3.addWidget(self.block2_item11, 10, 0, 1, 1)

        self.block2_item12 = QGroupBox(self.block2)
        self.block2_item12.setObjectName(u"block2_item12")
        self.verticalLayout_29 = QVBoxLayout(self.block2_item12)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.label_36 = QLabel(self.block2_item12)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setFont(font1)
        self.label_36.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_36.setWordWrap(True)

        self.verticalLayout_29.addWidget(self.label_36)

        self._29 = QHBoxLayout()
        self._29.setSpacing(0)
        self._29.setObjectName(u"_29")
        self.radioButton_85 = QRadioButton(self.block2_item12)
        self.radioButton_85.setObjectName(u"radioButton_85")
        self.radioButton_85.setFont(font1)

        self._29.addWidget(self.radioButton_85)

        self.radioButton_86 = QRadioButton(self.block2_item12)
        self.radioButton_86.setObjectName(u"radioButton_86")
        self.radioButton_86.setFont(font1)

        self._29.addWidget(self.radioButton_86)

        self.radioButton_87 = QRadioButton(self.block2_item12)
        self.radioButton_87.setObjectName(u"radioButton_87")
        self.radioButton_87.setFont(font1)

        self._29.addWidget(self.radioButton_87)


        self.verticalLayout_29.addLayout(self._29)


        self.gridLayout_3.addWidget(self.block2_item12, 11, 0, 1, 1)

        self.block2_item13 = QGroupBox(self.block2)
        self.block2_item13.setObjectName(u"block2_item13")
        self.verticalLayout_27 = QVBoxLayout(self.block2_item13)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.label_34 = QLabel(self.block2_item13)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setFont(font1)
        self.label_34.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_27.addWidget(self.label_34)

        self._27 = QHBoxLayout()
        self._27.setSpacing(0)
        self._27.setObjectName(u"_27")
        self.radioButton_79 = QRadioButton(self.block2_item13)
        self.radioButton_79.setObjectName(u"radioButton_79")
        self.radioButton_79.setFont(font1)

        self._27.addWidget(self.radioButton_79)

        self.radioButton_80 = QRadioButton(self.block2_item13)
        self.radioButton_80.setObjectName(u"radioButton_80")
        self.radioButton_80.setFont(font1)

        self._27.addWidget(self.radioButton_80)

        self.radioButton_81 = QRadioButton(self.block2_item13)
        self.radioButton_81.setObjectName(u"radioButton_81")
        self.radioButton_81.setFont(font1)

        self._27.addWidget(self.radioButton_81)


        self.verticalLayout_27.addLayout(self._27)


        self.gridLayout_3.addWidget(self.block2_item13, 12, 0, 1, 1)

        self.block2_item14 = QGroupBox(self.block2)
        self.block2_item14.setObjectName(u"block2_item14")
        self.verticalLayout_26 = QVBoxLayout(self.block2_item14)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.label_33 = QLabel(self.block2_item14)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setFont(font1)
        self.label_33.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_33.setWordWrap(True)

        self.verticalLayout_26.addWidget(self.label_33)

        self._26 = QHBoxLayout()
        self._26.setSpacing(0)
        self._26.setObjectName(u"_26")
        self.radioButton_76 = QRadioButton(self.block2_item14)
        self.radioButton_76.setObjectName(u"radioButton_76")
        self.radioButton_76.setFont(font1)

        self._26.addWidget(self.radioButton_76)

        self.radioButton_77 = QRadioButton(self.block2_item14)
        self.radioButton_77.setObjectName(u"radioButton_77")
        self.radioButton_77.setFont(font1)

        self._26.addWidget(self.radioButton_77)

        self.radioButton_78 = QRadioButton(self.block2_item14)
        self.radioButton_78.setObjectName(u"radioButton_78")
        self.radioButton_78.setFont(font1)

        self._26.addWidget(self.radioButton_78)


        self.verticalLayout_26.addLayout(self._26)


        self.gridLayout_3.addWidget(self.block2_item14, 13, 0, 1, 1)

        self.block2_item15 = QGroupBox(self.block2)
        self.block2_item15.setObjectName(u"block2_item15")
        self.verticalLayout_35 = QVBoxLayout(self.block2_item15)
        self.verticalLayout_35.setSpacing(0)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.label_42 = QLabel(self.block2_item15)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setFont(font1)
        self.label_42.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_42.setWordWrap(True)

        self.verticalLayout_35.addWidget(self.label_42)

        self._35 = QHBoxLayout()
        self._35.setSpacing(0)
        self._35.setObjectName(u"_35")
        self.radioButton_103 = QRadioButton(self.block2_item15)
        self.radioButton_103.setObjectName(u"radioButton_103")
        self.radioButton_103.setFont(font1)

        self._35.addWidget(self.radioButton_103)

        self.radioButton_104 = QRadioButton(self.block2_item15)
        self.radioButton_104.setObjectName(u"radioButton_104")
        self.radioButton_104.setFont(font1)

        self._35.addWidget(self.radioButton_104)

        self.radioButton_105 = QRadioButton(self.block2_item15)
        self.radioButton_105.setObjectName(u"radioButton_105")
        self.radioButton_105.setFont(font1)

        self._35.addWidget(self.radioButton_105)


        self.verticalLayout_35.addLayout(self._35)


        self.gridLayout_3.addWidget(self.block2_item15, 14, 0, 1, 1)

        self.block2_item16 = QGroupBox(self.block2)
        self.block2_item16.setObjectName(u"block2_item16")
        self.verticalLayout_34 = QVBoxLayout(self.block2_item16)
        self.verticalLayout_34.setSpacing(0)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.label_41 = QLabel(self.block2_item16)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setFont(font1)
        self.label_41.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_41.setWordWrap(True)

        self.verticalLayout_34.addWidget(self.label_41)

        self._34 = QHBoxLayout()
        self._34.setSpacing(0)
        self._34.setObjectName(u"_34")
        self.radioButton_100 = QRadioButton(self.block2_item16)
        self.radioButton_100.setObjectName(u"radioButton_100")
        self.radioButton_100.setFont(font1)

        self._34.addWidget(self.radioButton_100)

        self.radioButton_101 = QRadioButton(self.block2_item16)
        self.radioButton_101.setObjectName(u"radioButton_101")
        self.radioButton_101.setFont(font1)

        self._34.addWidget(self.radioButton_101)

        self.radioButton_102 = QRadioButton(self.block2_item16)
        self.radioButton_102.setObjectName(u"radioButton_102")
        self.radioButton_102.setFont(font1)

        self._34.addWidget(self.radioButton_102)


        self.verticalLayout_34.addLayout(self._34)


        self.gridLayout_3.addWidget(self.block2_item16, 15, 0, 1, 1)

        self.block2_item17 = QGroupBox(self.block2)
        self.block2_item17.setObjectName(u"block2_item17")
        self.verticalLayout_33 = QVBoxLayout(self.block2_item17)
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.label_40 = QLabel(self.block2_item17)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setFont(font1)
        self.label_40.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_40.setWordWrap(True)

        self.verticalLayout_33.addWidget(self.label_40)

        self._33 = QHBoxLayout()
        self._33.setSpacing(0)
        self._33.setObjectName(u"_33")
        self.radioButton_97 = QRadioButton(self.block2_item17)
        self.radioButton_97.setObjectName(u"radioButton_97")
        self.radioButton_97.setFont(font1)

        self._33.addWidget(self.radioButton_97)

        self.radioButton_98 = QRadioButton(self.block2_item17)
        self.radioButton_98.setObjectName(u"radioButton_98")
        self.radioButton_98.setFont(font1)

        self._33.addWidget(self.radioButton_98)

        self.radioButton_99 = QRadioButton(self.block2_item17)
        self.radioButton_99.setObjectName(u"radioButton_99")
        self.radioButton_99.setFont(font1)

        self._33.addWidget(self.radioButton_99)


        self.verticalLayout_33.addLayout(self._33)


        self.gridLayout_3.addWidget(self.block2_item17, 16, 0, 1, 1)

        self.block2_item18 = QGroupBox(self.block2)
        self.block2_item18.setObjectName(u"block2_item18")
        self.verticalLayout_32 = QVBoxLayout(self.block2_item18)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.label_39 = QLabel(self.block2_item18)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setFont(font1)
        self.label_39.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_39.setWordWrap(True)

        self.verticalLayout_32.addWidget(self.label_39)

        self._32 = QHBoxLayout()
        self._32.setSpacing(0)
        self._32.setObjectName(u"_32")
        self.radioButton_94 = QRadioButton(self.block2_item18)
        self.radioButton_94.setObjectName(u"radioButton_94")
        self.radioButton_94.setFont(font1)

        self._32.addWidget(self.radioButton_94)

        self.radioButton_95 = QRadioButton(self.block2_item18)
        self.radioButton_95.setObjectName(u"radioButton_95")
        self.radioButton_95.setFont(font1)

        self._32.addWidget(self.radioButton_95)

        self.radioButton_96 = QRadioButton(self.block2_item18)
        self.radioButton_96.setObjectName(u"radioButton_96")
        self.radioButton_96.setFont(font1)

        self._32.addWidget(self.radioButton_96)


        self.verticalLayout_32.addLayout(self._32)


        self.gridLayout_3.addWidget(self.block2_item18, 17, 0, 1, 1)

        self.block2_item19 = QGroupBox(self.block2)
        self.block2_item19.setObjectName(u"block2_item19")
        self.verticalLayout_31 = QVBoxLayout(self.block2_item19)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.label_38 = QLabel(self.block2_item19)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setFont(font1)
        self.label_38.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_38.setWordWrap(True)

        self.verticalLayout_31.addWidget(self.label_38)

        self._31 = QHBoxLayout()
        self._31.setSpacing(0)
        self._31.setObjectName(u"_31")
        self.radioButton_91 = QRadioButton(self.block2_item19)
        self.radioButton_91.setObjectName(u"radioButton_91")
        self.radioButton_91.setFont(font1)

        self._31.addWidget(self.radioButton_91)

        self.radioButton_92 = QRadioButton(self.block2_item19)
        self.radioButton_92.setObjectName(u"radioButton_92")
        self.radioButton_92.setFont(font1)

        self._31.addWidget(self.radioButton_92)

        self.radioButton_93 = QRadioButton(self.block2_item19)
        self.radioButton_93.setObjectName(u"radioButton_93")
        self.radioButton_93.setFont(font1)

        self._31.addWidget(self.radioButton_93)


        self.verticalLayout_31.addLayout(self._31)


        self.gridLayout_3.addWidget(self.block2_item19, 18, 0, 1, 1)

        self.block2_item20 = QGroupBox(self.block2)
        self.block2_item20.setObjectName(u"block2_item20")
        self.verticalLayout_30 = QVBoxLayout(self.block2_item20)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.label_37 = QLabel(self.block2_item20)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setFont(font1)
        self.label_37.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_37.setWordWrap(True)

        self.verticalLayout_30.addWidget(self.label_37)

        self._30 = QHBoxLayout()
        self._30.setSpacing(0)
        self._30.setObjectName(u"_30")
        self.radioButton_88 = QRadioButton(self.block2_item20)
        self.radioButton_88.setObjectName(u"radioButton_88")
        self.radioButton_88.setFont(font1)

        self._30.addWidget(self.radioButton_88)

        self.radioButton_89 = QRadioButton(self.block2_item20)
        self.radioButton_89.setObjectName(u"radioButton_89")
        self.radioButton_89.setFont(font1)

        self._30.addWidget(self.radioButton_89)

        self.radioButton_90 = QRadioButton(self.block2_item20)
        self.radioButton_90.setObjectName(u"radioButton_90")
        self.radioButton_90.setFont(font1)

        self._30.addWidget(self.radioButton_90)


        self.verticalLayout_30.addLayout(self._30)


        self.gridLayout_3.addWidget(self.block2_item20, 19, 0, 1, 1)


        self.gridLayout_2.addWidget(self.block2, 1, 0, 1, 1)

        self.block4 = QGroupBox(self.scrollAreaWidgetContents)
        self.block4.setObjectName(u"block4")
        self.block4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.gridLayout_5 = QGridLayout(self.block4)
        self.gridLayout_5.setSpacing(10)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(10, 10, 10, 10)
        self.block4_item01 = QGroupBox(self.block4)
        self.block4_item01.setObjectName(u"block4_item01")
        self.verticalLayout_56 = QVBoxLayout(self.block4_item01)
        self.verticalLayout_56.setSpacing(0)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.label_63 = QLabel(self.block4_item01)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setFont(font1)
        self.label_63.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_63.setWordWrap(True)

        self.verticalLayout_56.addWidget(self.label_63)

        self._56 = QHBoxLayout()
        self._56.setSpacing(0)
        self._56.setObjectName(u"_56")
        self.radioButton_166 = QRadioButton(self.block4_item01)
        self.radioButton_166.setObjectName(u"radioButton_166")
        self.radioButton_166.setFont(font1)

        self._56.addWidget(self.radioButton_166)

        self.radioButton_167 = QRadioButton(self.block4_item01)
        self.radioButton_167.setObjectName(u"radioButton_167")
        self.radioButton_167.setFont(font1)

        self._56.addWidget(self.radioButton_167)

        self.radioButton_169 = QRadioButton(self.block4_item01)
        self.radioButton_169.setObjectName(u"radioButton_169")
        self.radioButton_169.setFont(font1)

        self._56.addWidget(self.radioButton_169)

        self.radioButton_168 = QRadioButton(self.block4_item01)
        self.radioButton_168.setObjectName(u"radioButton_168")
        self.radioButton_168.setFont(font1)

        self._56.addWidget(self.radioButton_168)


        self.verticalLayout_56.addLayout(self._56)


        self.gridLayout_5.addWidget(self.block4_item01, 20, 0, 1, 1)

        self.block4_item02 = QGroupBox(self.block4)
        self.block4_item02.setObjectName(u"block4_item02")
        self.verticalLayout_69 = QVBoxLayout(self.block4_item02)
        self.verticalLayout_69.setSpacing(0)
        self.verticalLayout_69.setObjectName(u"verticalLayout_69")
        self.label_76 = QLabel(self.block4_item02)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setFont(font1)
        self.label_76.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_76.setWordWrap(True)

        self.verticalLayout_69.addWidget(self.label_76)

        self._69 = QHBoxLayout()
        self._69.setSpacing(0)
        self._69.setObjectName(u"_69")
        self.radioButton_218 = QRadioButton(self.block4_item02)
        self.radioButton_218.setObjectName(u"radioButton_218")
        self.radioButton_218.setFont(font1)

        self._69.addWidget(self.radioButton_218)

        self.radioButton_219 = QRadioButton(self.block4_item02)
        self.radioButton_219.setObjectName(u"radioButton_219")
        self.radioButton_219.setFont(font1)

        self._69.addWidget(self.radioButton_219)

        self.radioButton_220 = QRadioButton(self.block4_item02)
        self.radioButton_220.setObjectName(u"radioButton_220")
        self.radioButton_220.setFont(font1)

        self._69.addWidget(self.radioButton_220)

        self.radioButton_221 = QRadioButton(self.block4_item02)
        self.radioButton_221.setObjectName(u"radioButton_221")
        self.radioButton_221.setFont(font1)

        self._69.addWidget(self.radioButton_221)


        self.verticalLayout_69.addLayout(self._69)


        self.gridLayout_5.addWidget(self.block4_item02, 21, 0, 1, 1)

        self.block4_item03 = QGroupBox(self.block4)
        self.block4_item03.setObjectName(u"block4_item03")
        self.verticalLayout_68 = QVBoxLayout(self.block4_item03)
        self.verticalLayout_68.setSpacing(0)
        self.verticalLayout_68.setObjectName(u"verticalLayout_68")
        self.label_75 = QLabel(self.block4_item03)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setFont(font1)
        self.label_75.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_75.setWordWrap(True)

        self.verticalLayout_68.addWidget(self.label_75)

        self._68 = QHBoxLayout()
        self._68.setSpacing(0)
        self._68.setObjectName(u"_68")
        self.radioButton_214 = QRadioButton(self.block4_item03)
        self.radioButton_214.setObjectName(u"radioButton_214")
        self.radioButton_214.setFont(font1)

        self._68.addWidget(self.radioButton_214)

        self.radioButton_215 = QRadioButton(self.block4_item03)
        self.radioButton_215.setObjectName(u"radioButton_215")
        self.radioButton_215.setFont(font1)

        self._68.addWidget(self.radioButton_215)

        self.radioButton_216 = QRadioButton(self.block4_item03)
        self.radioButton_216.setObjectName(u"radioButton_216")
        self.radioButton_216.setFont(font1)

        self._68.addWidget(self.radioButton_216)

        self.radioButton_217 = QRadioButton(self.block4_item03)
        self.radioButton_217.setObjectName(u"radioButton_217")
        self.radioButton_217.setFont(font1)

        self._68.addWidget(self.radioButton_217)


        self.verticalLayout_68.addLayout(self._68)


        self.gridLayout_5.addWidget(self.block4_item03, 22, 0, 1, 1)

        self.block4_item04 = QGroupBox(self.block4)
        self.block4_item04.setObjectName(u"block4_item04")
        self.verticalLayout_67 = QVBoxLayout(self.block4_item04)
        self.verticalLayout_67.setSpacing(0)
        self.verticalLayout_67.setObjectName(u"verticalLayout_67")
        self.label_74 = QLabel(self.block4_item04)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setFont(font1)
        self.label_74.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_74.setWordWrap(True)

        self.verticalLayout_67.addWidget(self.label_74)

        self._67 = QHBoxLayout()
        self._67.setSpacing(0)
        self._67.setObjectName(u"_67")
        self.radioButton_210 = QRadioButton(self.block4_item04)
        self.radioButton_210.setObjectName(u"radioButton_210")
        self.radioButton_210.setFont(font1)

        self._67.addWidget(self.radioButton_210)

        self.radioButton_211 = QRadioButton(self.block4_item04)
        self.radioButton_211.setObjectName(u"radioButton_211")
        self.radioButton_211.setFont(font1)

        self._67.addWidget(self.radioButton_211)

        self.radioButton_212 = QRadioButton(self.block4_item04)
        self.radioButton_212.setObjectName(u"radioButton_212")
        self.radioButton_212.setFont(font1)

        self._67.addWidget(self.radioButton_212)

        self.radioButton_213 = QRadioButton(self.block4_item04)
        self.radioButton_213.setObjectName(u"radioButton_213")
        self.radioButton_213.setFont(font1)

        self._67.addWidget(self.radioButton_213)


        self.verticalLayout_67.addLayout(self._67)


        self.gridLayout_5.addWidget(self.block4_item04, 23, 0, 1, 1)

        self.block4_item05 = QGroupBox(self.block4)
        self.block4_item05.setObjectName(u"block4_item05")
        self.verticalLayout_66 = QVBoxLayout(self.block4_item05)
        self.verticalLayout_66.setSpacing(0)
        self.verticalLayout_66.setObjectName(u"verticalLayout_66")
        self.label_73 = QLabel(self.block4_item05)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setFont(font1)
        self.label_73.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_73.setWordWrap(True)

        self.verticalLayout_66.addWidget(self.label_73)

        self._66 = QHBoxLayout()
        self._66.setSpacing(0)
        self._66.setObjectName(u"_66")
        self.radioButton_206 = QRadioButton(self.block4_item05)
        self.radioButton_206.setObjectName(u"radioButton_206")
        self.radioButton_206.setFont(font1)

        self._66.addWidget(self.radioButton_206)

        self.radioButton_207 = QRadioButton(self.block4_item05)
        self.radioButton_207.setObjectName(u"radioButton_207")
        self.radioButton_207.setFont(font1)

        self._66.addWidget(self.radioButton_207)

        self.radioButton_208 = QRadioButton(self.block4_item05)
        self.radioButton_208.setObjectName(u"radioButton_208")
        self.radioButton_208.setFont(font1)

        self._66.addWidget(self.radioButton_208)

        self.radioButton_209 = QRadioButton(self.block4_item05)
        self.radioButton_209.setObjectName(u"radioButton_209")
        self.radioButton_209.setFont(font1)

        self._66.addWidget(self.radioButton_209)


        self.verticalLayout_66.addLayout(self._66)


        self.gridLayout_5.addWidget(self.block4_item05, 24, 0, 1, 1)

        self.block4_item06 = QGroupBox(self.block4)
        self.block4_item06.setObjectName(u"block4_item06")
        self.verticalLayout_65 = QVBoxLayout(self.block4_item06)
        self.verticalLayout_65.setSpacing(0)
        self.verticalLayout_65.setObjectName(u"verticalLayout_65")
        self.label_72 = QLabel(self.block4_item06)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setFont(font1)
        self.label_72.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_72.setWordWrap(True)

        self.verticalLayout_65.addWidget(self.label_72)

        self._65 = QHBoxLayout()
        self._65.setSpacing(0)
        self._65.setObjectName(u"_65")
        self.radioButton_202 = QRadioButton(self.block4_item06)
        self.radioButton_202.setObjectName(u"radioButton_202")
        self.radioButton_202.setFont(font1)

        self._65.addWidget(self.radioButton_202)

        self.radioButton_203 = QRadioButton(self.block4_item06)
        self.radioButton_203.setObjectName(u"radioButton_203")
        self.radioButton_203.setFont(font1)

        self._65.addWidget(self.radioButton_203)

        self.radioButton_204 = QRadioButton(self.block4_item06)
        self.radioButton_204.setObjectName(u"radioButton_204")
        self.radioButton_204.setFont(font1)

        self._65.addWidget(self.radioButton_204)

        self.radioButton_205 = QRadioButton(self.block4_item06)
        self.radioButton_205.setObjectName(u"radioButton_205")
        self.radioButton_205.setFont(font1)

        self._65.addWidget(self.radioButton_205)


        self.verticalLayout_65.addLayout(self._65)


        self.gridLayout_5.addWidget(self.block4_item06, 25, 0, 1, 1)

        self.block4_item07 = QGroupBox(self.block4)
        self.block4_item07.setObjectName(u"block4_item07")
        self.verticalLayout_64 = QVBoxLayout(self.block4_item07)
        self.verticalLayout_64.setSpacing(0)
        self.verticalLayout_64.setObjectName(u"verticalLayout_64")
        self.label_71 = QLabel(self.block4_item07)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setFont(font1)
        self.label_71.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_71.setWordWrap(True)

        self.verticalLayout_64.addWidget(self.label_71)

        self._64 = QHBoxLayout()
        self._64.setSpacing(0)
        self._64.setObjectName(u"_64")
        self.radioButton_198 = QRadioButton(self.block4_item07)
        self.radioButton_198.setObjectName(u"radioButton_198")
        self.radioButton_198.setFont(font1)

        self._64.addWidget(self.radioButton_198)

        self.radioButton_199 = QRadioButton(self.block4_item07)
        self.radioButton_199.setObjectName(u"radioButton_199")
        self.radioButton_199.setFont(font1)

        self._64.addWidget(self.radioButton_199)

        self.radioButton_200 = QRadioButton(self.block4_item07)
        self.radioButton_200.setObjectName(u"radioButton_200")
        self.radioButton_200.setFont(font1)

        self._64.addWidget(self.radioButton_200)

        self.radioButton_201 = QRadioButton(self.block4_item07)
        self.radioButton_201.setObjectName(u"radioButton_201")
        self.radioButton_201.setFont(font1)

        self._64.addWidget(self.radioButton_201)


        self.verticalLayout_64.addLayout(self._64)


        self.gridLayout_5.addWidget(self.block4_item07, 26, 0, 1, 1)

        self.block4_item08 = QGroupBox(self.block4)
        self.block4_item08.setObjectName(u"block4_item08")
        self.verticalLayout_63 = QVBoxLayout(self.block4_item08)
        self.verticalLayout_63.setSpacing(0)
        self.verticalLayout_63.setObjectName(u"verticalLayout_63")
        self.label_70 = QLabel(self.block4_item08)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setFont(font1)
        self.label_70.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_70.setWordWrap(True)

        self.verticalLayout_63.addWidget(self.label_70)

        self._63 = QHBoxLayout()
        self._63.setSpacing(0)
        self._63.setObjectName(u"_63")
        self.radioButton_194 = QRadioButton(self.block4_item08)
        self.radioButton_194.setObjectName(u"radioButton_194")
        self.radioButton_194.setFont(font1)

        self._63.addWidget(self.radioButton_194)

        self.radioButton_195 = QRadioButton(self.block4_item08)
        self.radioButton_195.setObjectName(u"radioButton_195")
        self.radioButton_195.setFont(font1)

        self._63.addWidget(self.radioButton_195)

        self.radioButton_196 = QRadioButton(self.block4_item08)
        self.radioButton_196.setObjectName(u"radioButton_196")
        self.radioButton_196.setFont(font1)

        self._63.addWidget(self.radioButton_196)

        self.radioButton_197 = QRadioButton(self.block4_item08)
        self.radioButton_197.setObjectName(u"radioButton_197")
        self.radioButton_197.setFont(font1)

        self._63.addWidget(self.radioButton_197)


        self.verticalLayout_63.addLayout(self._63)


        self.gridLayout_5.addWidget(self.block4_item08, 27, 0, 1, 1)

        self.block4_item09 = QGroupBox(self.block4)
        self.block4_item09.setObjectName(u"block4_item09")
        self.verticalLayout_62 = QVBoxLayout(self.block4_item09)
        self.verticalLayout_62.setSpacing(0)
        self.verticalLayout_62.setObjectName(u"verticalLayout_62")
        self.label_69 = QLabel(self.block4_item09)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setFont(font1)
        self.label_69.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_69.setWordWrap(True)

        self.verticalLayout_62.addWidget(self.label_69)

        self._62 = QHBoxLayout()
        self._62.setSpacing(0)
        self._62.setObjectName(u"_62")
        self.radioButton_190 = QRadioButton(self.block4_item09)
        self.radioButton_190.setObjectName(u"radioButton_190")
        self.radioButton_190.setFont(font1)

        self._62.addWidget(self.radioButton_190)

        self.radioButton_191 = QRadioButton(self.block4_item09)
        self.radioButton_191.setObjectName(u"radioButton_191")
        self.radioButton_191.setFont(font1)

        self._62.addWidget(self.radioButton_191)

        self.radioButton_192 = QRadioButton(self.block4_item09)
        self.radioButton_192.setObjectName(u"radioButton_192")
        self.radioButton_192.setFont(font1)

        self._62.addWidget(self.radioButton_192)

        self.radioButton_193 = QRadioButton(self.block4_item09)
        self.radioButton_193.setObjectName(u"radioButton_193")
        self.radioButton_193.setFont(font1)

        self._62.addWidget(self.radioButton_193)


        self.verticalLayout_62.addLayout(self._62)


        self.gridLayout_5.addWidget(self.block4_item09, 28, 0, 1, 1)

        self.block4_item10 = QGroupBox(self.block4)
        self.block4_item10.setObjectName(u"block4_item10")
        self.verticalLayout_60 = QVBoxLayout(self.block4_item10)
        self.verticalLayout_60.setSpacing(0)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.label_67 = QLabel(self.block4_item10)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setFont(font1)
        self.label_67.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_67.setWordWrap(True)

        self.verticalLayout_60.addWidget(self.label_67)

        self._60 = QHBoxLayout()
        self._60.setSpacing(0)
        self._60.setObjectName(u"_60")
        self.radioButton_182 = QRadioButton(self.block4_item10)
        self.radioButton_182.setObjectName(u"radioButton_182")
        self.radioButton_182.setFont(font1)

        self._60.addWidget(self.radioButton_182)

        self.radioButton_183 = QRadioButton(self.block4_item10)
        self.radioButton_183.setObjectName(u"radioButton_183")
        self.radioButton_183.setFont(font1)

        self._60.addWidget(self.radioButton_183)

        self.radioButton_184 = QRadioButton(self.block4_item10)
        self.radioButton_184.setObjectName(u"radioButton_184")
        self.radioButton_184.setFont(font1)

        self._60.addWidget(self.radioButton_184)

        self.radioButton_185 = QRadioButton(self.block4_item10)
        self.radioButton_185.setObjectName(u"radioButton_185")
        self.radioButton_185.setFont(font1)

        self._60.addWidget(self.radioButton_185)


        self.verticalLayout_60.addLayout(self._60)


        self.gridLayout_5.addWidget(self.block4_item10, 29, 0, 1, 1)

        self.block4_item11 = QGroupBox(self.block4)
        self.block4_item11.setObjectName(u"block4_item11")
        self.verticalLayout_61 = QVBoxLayout(self.block4_item11)
        self.verticalLayout_61.setSpacing(0)
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.label_68 = QLabel(self.block4_item11)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setFont(font1)
        self.label_68.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_68.setWordWrap(True)

        self.verticalLayout_61.addWidget(self.label_68)

        self._61 = QHBoxLayout()
        self._61.setSpacing(0)
        self._61.setObjectName(u"_61")
        self.radioButton_186 = QRadioButton(self.block4_item11)
        self.radioButton_186.setObjectName(u"radioButton_186")
        self.radioButton_186.setFont(font1)

        self._61.addWidget(self.radioButton_186)

        self.radioButton_187 = QRadioButton(self.block4_item11)
        self.radioButton_187.setObjectName(u"radioButton_187")
        self.radioButton_187.setFont(font1)

        self._61.addWidget(self.radioButton_187)

        self.radioButton_188 = QRadioButton(self.block4_item11)
        self.radioButton_188.setObjectName(u"radioButton_188")
        self.radioButton_188.setFont(font1)

        self._61.addWidget(self.radioButton_188)

        self.radioButton_189 = QRadioButton(self.block4_item11)
        self.radioButton_189.setObjectName(u"radioButton_189")
        self.radioButton_189.setFont(font1)

        self._61.addWidget(self.radioButton_189)


        self.verticalLayout_61.addLayout(self._61)


        self.gridLayout_5.addWidget(self.block4_item11, 30, 0, 1, 1)

        self.block4_item12 = QGroupBox(self.block4)
        self.block4_item12.setObjectName(u"block4_item12")
        self.verticalLayout_83 = QVBoxLayout(self.block4_item12)
        self.verticalLayout_83.setSpacing(0)
        self.verticalLayout_83.setObjectName(u"verticalLayout_83")
        self.label_90 = QLabel(self.block4_item12)
        self.label_90.setObjectName(u"label_90")
        self.label_90.setFont(font1)
        self.label_90.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_90.setWordWrap(True)

        self.verticalLayout_83.addWidget(self.label_90)

        self._83 = QHBoxLayout()
        self._83.setSpacing(0)
        self._83.setObjectName(u"_83")
        self.radioButton_273 = QRadioButton(self.block4_item12)
        self.radioButton_273.setObjectName(u"radioButton_273")
        self.radioButton_273.setFont(font1)

        self._83.addWidget(self.radioButton_273)

        self.radioButton_274 = QRadioButton(self.block4_item12)
        self.radioButton_274.setObjectName(u"radioButton_274")
        self.radioButton_274.setFont(font1)

        self._83.addWidget(self.radioButton_274)

        self.radioButton_275 = QRadioButton(self.block4_item12)
        self.radioButton_275.setObjectName(u"radioButton_275")
        self.radioButton_275.setFont(font1)

        self._83.addWidget(self.radioButton_275)

        self.radioButton_276 = QRadioButton(self.block4_item12)
        self.radioButton_276.setObjectName(u"radioButton_276")
        self.radioButton_276.setFont(font1)

        self._83.addWidget(self.radioButton_276)


        self.verticalLayout_83.addLayout(self._83)


        self.gridLayout_5.addWidget(self.block4_item12, 31, 0, 1, 1)

        self.block4_item13 = QGroupBox(self.block4)
        self.block4_item13.setObjectName(u"block4_item13")
        self.verticalLayout_82 = QVBoxLayout(self.block4_item13)
        self.verticalLayout_82.setSpacing(0)
        self.verticalLayout_82.setObjectName(u"verticalLayout_82")
        self.label_89 = QLabel(self.block4_item13)
        self.label_89.setObjectName(u"label_89")
        self.label_89.setFont(font1)
        self.label_89.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_89.setWordWrap(True)

        self.verticalLayout_82.addWidget(self.label_89)

        self._82 = QHBoxLayout()
        self._82.setSpacing(0)
        self._82.setObjectName(u"_82")
        self.radioButton_269 = QRadioButton(self.block4_item13)
        self.radioButton_269.setObjectName(u"radioButton_269")
        self.radioButton_269.setFont(font1)

        self._82.addWidget(self.radioButton_269)

        self.radioButton_270 = QRadioButton(self.block4_item13)
        self.radioButton_270.setObjectName(u"radioButton_270")
        self.radioButton_270.setFont(font1)

        self._82.addWidget(self.radioButton_270)

        self.radioButton_271 = QRadioButton(self.block4_item13)
        self.radioButton_271.setObjectName(u"radioButton_271")
        self.radioButton_271.setFont(font1)

        self._82.addWidget(self.radioButton_271)

        self.radioButton_272 = QRadioButton(self.block4_item13)
        self.radioButton_272.setObjectName(u"radioButton_272")
        self.radioButton_272.setFont(font1)

        self._82.addWidget(self.radioButton_272)


        self.verticalLayout_82.addLayout(self._82)


        self.gridLayout_5.addWidget(self.block4_item13, 32, 0, 1, 1)

        self.block4_item14 = QGroupBox(self.block4)
        self.block4_item14.setObjectName(u"block4_item14")
        self.verticalLayout_81 = QVBoxLayout(self.block4_item14)
        self.verticalLayout_81.setSpacing(0)
        self.verticalLayout_81.setObjectName(u"verticalLayout_81")
        self.label_88 = QLabel(self.block4_item14)
        self.label_88.setObjectName(u"label_88")
        self.label_88.setFont(font1)
        self.label_88.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_88.setWordWrap(True)

        self.verticalLayout_81.addWidget(self.label_88)

        self._81 = QHBoxLayout()
        self._81.setSpacing(0)
        self._81.setObjectName(u"_81")
        self.radioButton_265 = QRadioButton(self.block4_item14)
        self.radioButton_265.setObjectName(u"radioButton_265")
        self.radioButton_265.setFont(font1)

        self._81.addWidget(self.radioButton_265)

        self.radioButton_266 = QRadioButton(self.block4_item14)
        self.radioButton_266.setObjectName(u"radioButton_266")
        self.radioButton_266.setFont(font1)

        self._81.addWidget(self.radioButton_266)

        self.radioButton_267 = QRadioButton(self.block4_item14)
        self.radioButton_267.setObjectName(u"radioButton_267")
        self.radioButton_267.setFont(font1)

        self._81.addWidget(self.radioButton_267)

        self.radioButton_268 = QRadioButton(self.block4_item14)
        self.radioButton_268.setObjectName(u"radioButton_268")
        self.radioButton_268.setFont(font1)

        self._81.addWidget(self.radioButton_268)


        self.verticalLayout_81.addLayout(self._81)


        self.gridLayout_5.addWidget(self.block4_item14, 33, 0, 1, 1)

        self.block4_item15 = QGroupBox(self.block4)
        self.block4_item15.setObjectName(u"block4_item15")
        self.verticalLayout_80 = QVBoxLayout(self.block4_item15)
        self.verticalLayout_80.setSpacing(0)
        self.verticalLayout_80.setObjectName(u"verticalLayout_80")
        self.label_87 = QLabel(self.block4_item15)
        self.label_87.setObjectName(u"label_87")
        self.label_87.setFont(font1)
        self.label_87.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_87.setWordWrap(True)

        self.verticalLayout_80.addWidget(self.label_87)

        self._80 = QHBoxLayout()
        self._80.setSpacing(0)
        self._80.setObjectName(u"_80")
        self.radioButton_261 = QRadioButton(self.block4_item15)
        self.radioButton_261.setObjectName(u"radioButton_261")
        self.radioButton_261.setFont(font1)

        self._80.addWidget(self.radioButton_261)

        self.radioButton_262 = QRadioButton(self.block4_item15)
        self.radioButton_262.setObjectName(u"radioButton_262")
        self.radioButton_262.setFont(font1)

        self._80.addWidget(self.radioButton_262)

        self.radioButton_263 = QRadioButton(self.block4_item15)
        self.radioButton_263.setObjectName(u"radioButton_263")
        self.radioButton_263.setFont(font1)

        self._80.addWidget(self.radioButton_263)

        self.radioButton_264 = QRadioButton(self.block4_item15)
        self.radioButton_264.setObjectName(u"radioButton_264")
        self.radioButton_264.setFont(font1)

        self._80.addWidget(self.radioButton_264)


        self.verticalLayout_80.addLayout(self._80)


        self.gridLayout_5.addWidget(self.block4_item15, 34, 0, 1, 1)

        self.block4_item16 = QGroupBox(self.block4)
        self.block4_item16.setObjectName(u"block4_item16")
        self.verticalLayout_79 = QVBoxLayout(self.block4_item16)
        self.verticalLayout_79.setSpacing(0)
        self.verticalLayout_79.setObjectName(u"verticalLayout_79")
        self.label_86 = QLabel(self.block4_item16)
        self.label_86.setObjectName(u"label_86")
        self.label_86.setFont(font1)
        self.label_86.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_86.setWordWrap(True)

        self.verticalLayout_79.addWidget(self.label_86)

        self._79 = QHBoxLayout()
        self._79.setSpacing(0)
        self._79.setObjectName(u"_79")
        self.radioButton_257 = QRadioButton(self.block4_item16)
        self.radioButton_257.setObjectName(u"radioButton_257")
        self.radioButton_257.setFont(font1)

        self._79.addWidget(self.radioButton_257)

        self.radioButton_258 = QRadioButton(self.block4_item16)
        self.radioButton_258.setObjectName(u"radioButton_258")
        self.radioButton_258.setFont(font1)

        self._79.addWidget(self.radioButton_258)

        self.radioButton_259 = QRadioButton(self.block4_item16)
        self.radioButton_259.setObjectName(u"radioButton_259")
        self.radioButton_259.setFont(font1)

        self._79.addWidget(self.radioButton_259)

        self.radioButton_260 = QRadioButton(self.block4_item16)
        self.radioButton_260.setObjectName(u"radioButton_260")
        self.radioButton_260.setFont(font1)

        self._79.addWidget(self.radioButton_260)


        self.verticalLayout_79.addLayout(self._79)


        self.gridLayout_5.addWidget(self.block4_item16, 35, 0, 1, 1)

        self.block4_item17 = QGroupBox(self.block4)
        self.block4_item17.setObjectName(u"block4_item17")
        self.verticalLayout_78 = QVBoxLayout(self.block4_item17)
        self.verticalLayout_78.setSpacing(0)
        self.verticalLayout_78.setObjectName(u"verticalLayout_78")
        self.label_85 = QLabel(self.block4_item17)
        self.label_85.setObjectName(u"label_85")
        self.label_85.setFont(font1)
        self.label_85.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_85.setWordWrap(True)

        self.verticalLayout_78.addWidget(self.label_85)

        self._78 = QHBoxLayout()
        self._78.setSpacing(0)
        self._78.setObjectName(u"_78")
        self.radioButton_253 = QRadioButton(self.block4_item17)
        self.radioButton_253.setObjectName(u"radioButton_253")
        self.radioButton_253.setFont(font1)

        self._78.addWidget(self.radioButton_253)

        self.radioButton_254 = QRadioButton(self.block4_item17)
        self.radioButton_254.setObjectName(u"radioButton_254")
        self.radioButton_254.setFont(font1)

        self._78.addWidget(self.radioButton_254)

        self.radioButton_255 = QRadioButton(self.block4_item17)
        self.radioButton_255.setObjectName(u"radioButton_255")
        self.radioButton_255.setFont(font1)

        self._78.addWidget(self.radioButton_255)

        self.radioButton_256 = QRadioButton(self.block4_item17)
        self.radioButton_256.setObjectName(u"radioButton_256")
        self.radioButton_256.setFont(font1)

        self._78.addWidget(self.radioButton_256)


        self.verticalLayout_78.addLayout(self._78)


        self.gridLayout_5.addWidget(self.block4_item17, 36, 0, 1, 1)

        self.block4_item18 = QGroupBox(self.block4)
        self.block4_item18.setObjectName(u"block4_item18")
        self.verticalLayout_77 = QVBoxLayout(self.block4_item18)
        self.verticalLayout_77.setSpacing(0)
        self.verticalLayout_77.setObjectName(u"verticalLayout_77")
        self.label_84 = QLabel(self.block4_item18)
        self.label_84.setObjectName(u"label_84")
        self.label_84.setFont(font1)
        self.label_84.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_84.setWordWrap(True)

        self.verticalLayout_77.addWidget(self.label_84)

        self._77 = QHBoxLayout()
        self._77.setSpacing(0)
        self._77.setObjectName(u"_77")
        self.radioButton_249 = QRadioButton(self.block4_item18)
        self.radioButton_249.setObjectName(u"radioButton_249")
        self.radioButton_249.setFont(font1)

        self._77.addWidget(self.radioButton_249)

        self.radioButton_250 = QRadioButton(self.block4_item18)
        self.radioButton_250.setObjectName(u"radioButton_250")
        self.radioButton_250.setFont(font1)

        self._77.addWidget(self.radioButton_250)

        self.radioButton_251 = QRadioButton(self.block4_item18)
        self.radioButton_251.setObjectName(u"radioButton_251")
        self.radioButton_251.setFont(font1)

        self._77.addWidget(self.radioButton_251)

        self.radioButton_252 = QRadioButton(self.block4_item18)
        self.radioButton_252.setObjectName(u"radioButton_252")
        self.radioButton_252.setFont(font1)

        self._77.addWidget(self.radioButton_252)


        self.verticalLayout_77.addLayout(self._77)


        self.gridLayout_5.addWidget(self.block4_item18, 37, 0, 1, 1)

        self.block4_item19 = QGroupBox(self.block4)
        self.block4_item19.setObjectName(u"block4_item19")
        self.verticalLayout_76 = QVBoxLayout(self.block4_item19)
        self.verticalLayout_76.setSpacing(0)
        self.verticalLayout_76.setObjectName(u"verticalLayout_76")
        self.label_83 = QLabel(self.block4_item19)
        self.label_83.setObjectName(u"label_83")
        self.label_83.setFont(font1)
        self.label_83.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_83.setWordWrap(True)

        self.verticalLayout_76.addWidget(self.label_83)

        self._76 = QHBoxLayout()
        self._76.setSpacing(0)
        self._76.setObjectName(u"_76")
        self.radioButton_245 = QRadioButton(self.block4_item19)
        self.radioButton_245.setObjectName(u"radioButton_245")
        self.radioButton_245.setFont(font1)

        self._76.addWidget(self.radioButton_245)

        self.radioButton_246 = QRadioButton(self.block4_item19)
        self.radioButton_246.setObjectName(u"radioButton_246")
        self.radioButton_246.setFont(font1)

        self._76.addWidget(self.radioButton_246)

        self.radioButton_247 = QRadioButton(self.block4_item19)
        self.radioButton_247.setObjectName(u"radioButton_247")
        self.radioButton_247.setFont(font1)

        self._76.addWidget(self.radioButton_247)

        self.radioButton_248 = QRadioButton(self.block4_item19)
        self.radioButton_248.setObjectName(u"radioButton_248")
        self.radioButton_248.setFont(font1)

        self._76.addWidget(self.radioButton_248)


        self.verticalLayout_76.addLayout(self._76)


        self.gridLayout_5.addWidget(self.block4_item19, 38, 0, 1, 1)

        self.block4_item20 = QGroupBox(self.block4)
        self.block4_item20.setObjectName(u"block4_item20")
        self.verticalLayout_74 = QVBoxLayout(self.block4_item20)
        self.verticalLayout_74.setSpacing(0)
        self.verticalLayout_74.setObjectName(u"verticalLayout_74")
        self.label_81 = QLabel(self.block4_item20)
        self.label_81.setObjectName(u"label_81")
        self.label_81.setFont(font1)
        self.label_81.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_81.setWordWrap(True)

        self.verticalLayout_74.addWidget(self.label_81)

        self._74 = QHBoxLayout()
        self._74.setSpacing(0)
        self._74.setObjectName(u"_74")
        self.radioButton_241 = QRadioButton(self.block4_item20)
        self.radioButton_241.setObjectName(u"radioButton_241")
        self.radioButton_241.setFont(font1)

        self._74.addWidget(self.radioButton_241)

        self.radioButton_242 = QRadioButton(self.block4_item20)
        self.radioButton_242.setObjectName(u"radioButton_242")
        self.radioButton_242.setFont(font1)

        self._74.addWidget(self.radioButton_242)

        self.radioButton_243 = QRadioButton(self.block4_item20)
        self.radioButton_243.setObjectName(u"radioButton_243")
        self.radioButton_243.setFont(font1)

        self._74.addWidget(self.radioButton_243)

        self.radioButton_244 = QRadioButton(self.block4_item20)
        self.radioButton_244.setObjectName(u"radioButton_244")
        self.radioButton_244.setFont(font1)

        self._74.addWidget(self.radioButton_244)


        self.verticalLayout_74.addLayout(self._74)


        self.gridLayout_5.addWidget(self.block4_item20, 39, 0, 1, 1)

        self.block4_item21 = QGroupBox(self.block4)
        self.block4_item21.setObjectName(u"block4_item21")
        self.verticalLayout_73 = QVBoxLayout(self.block4_item21)
        self.verticalLayout_73.setSpacing(0)
        self.verticalLayout_73.setObjectName(u"verticalLayout_73")
        self.label_80 = QLabel(self.block4_item21)
        self.label_80.setObjectName(u"label_80")
        self.label_80.setFont(font1)
        self.label_80.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_80.setWordWrap(True)

        self.verticalLayout_73.addWidget(self.label_80)

        self._73 = QHBoxLayout()
        self._73.setSpacing(0)
        self._73.setObjectName(u"_73")
        self.radioButton_237 = QRadioButton(self.block4_item21)
        self.radioButton_237.setObjectName(u"radioButton_237")
        self.radioButton_237.setFont(font1)

        self._73.addWidget(self.radioButton_237)

        self.radioButton_238 = QRadioButton(self.block4_item21)
        self.radioButton_238.setObjectName(u"radioButton_238")
        self.radioButton_238.setFont(font1)

        self._73.addWidget(self.radioButton_238)

        self.radioButton_239 = QRadioButton(self.block4_item21)
        self.radioButton_239.setObjectName(u"radioButton_239")
        self.radioButton_239.setFont(font1)

        self._73.addWidget(self.radioButton_239)

        self.radioButton_240 = QRadioButton(self.block4_item21)
        self.radioButton_240.setObjectName(u"radioButton_240")
        self.radioButton_240.setFont(font1)

        self._73.addWidget(self.radioButton_240)


        self.verticalLayout_73.addLayout(self._73)


        self.gridLayout_5.addWidget(self.block4_item21, 40, 0, 1, 1)

        self.block4_item22 = QGroupBox(self.block4)
        self.block4_item22.setObjectName(u"block4_item22")
        self.verticalLayout_72 = QVBoxLayout(self.block4_item22)
        self.verticalLayout_72.setSpacing(0)
        self.verticalLayout_72.setObjectName(u"verticalLayout_72")
        self.label_79 = QLabel(self.block4_item22)
        self.label_79.setObjectName(u"label_79")
        self.label_79.setFont(font1)
        self.label_79.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_79.setWordWrap(True)

        self.verticalLayout_72.addWidget(self.label_79)

        self._72 = QHBoxLayout()
        self._72.setSpacing(0)
        self._72.setObjectName(u"_72")
        self.radioButton_233 = QRadioButton(self.block4_item22)
        self.radioButton_233.setObjectName(u"radioButton_233")
        self.radioButton_233.setFont(font1)

        self._72.addWidget(self.radioButton_233)

        self.radioButton_234 = QRadioButton(self.block4_item22)
        self.radioButton_234.setObjectName(u"radioButton_234")
        self.radioButton_234.setFont(font1)

        self._72.addWidget(self.radioButton_234)

        self.radioButton_235 = QRadioButton(self.block4_item22)
        self.radioButton_235.setObjectName(u"radioButton_235")
        self.radioButton_235.setFont(font1)

        self._72.addWidget(self.radioButton_235)

        self.radioButton_236 = QRadioButton(self.block4_item22)
        self.radioButton_236.setObjectName(u"radioButton_236")
        self.radioButton_236.setFont(font1)

        self._72.addWidget(self.radioButton_236)


        self.verticalLayout_72.addLayout(self._72)


        self.gridLayout_5.addWidget(self.block4_item22, 41, 0, 1, 1)

        self.block4_item23 = QGroupBox(self.block4)
        self.block4_item23.setObjectName(u"block4_item23")
        self.verticalLayout_71 = QVBoxLayout(self.block4_item23)
        self.verticalLayout_71.setSpacing(0)
        self.verticalLayout_71.setObjectName(u"verticalLayout_71")
        self.label_78 = QLabel(self.block4_item23)
        self.label_78.setObjectName(u"label_78")
        self.label_78.setFont(font1)
        self.label_78.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_78.setWordWrap(True)

        self.verticalLayout_71.addWidget(self.label_78)

        self._71 = QHBoxLayout()
        self._71.setSpacing(0)
        self._71.setObjectName(u"_71")
        self.radioButton_229 = QRadioButton(self.block4_item23)
        self.radioButton_229.setObjectName(u"radioButton_229")
        self.radioButton_229.setFont(font1)

        self._71.addWidget(self.radioButton_229)

        self.radioButton_230 = QRadioButton(self.block4_item23)
        self.radioButton_230.setObjectName(u"radioButton_230")
        self.radioButton_230.setFont(font1)

        self._71.addWidget(self.radioButton_230)

        self.radioButton_231 = QRadioButton(self.block4_item23)
        self.radioButton_231.setObjectName(u"radioButton_231")
        self.radioButton_231.setFont(font1)

        self._71.addWidget(self.radioButton_231)

        self.radioButton_232 = QRadioButton(self.block4_item23)
        self.radioButton_232.setObjectName(u"radioButton_232")
        self.radioButton_232.setFont(font1)

        self._71.addWidget(self.radioButton_232)


        self.verticalLayout_71.addLayout(self._71)


        self.gridLayout_5.addWidget(self.block4_item23, 42, 0, 1, 1)

        self.block4_item24 = QGroupBox(self.block4)
        self.block4_item24.setObjectName(u"block4_item24")
        self.verticalLayout_70 = QVBoxLayout(self.block4_item24)
        self.verticalLayout_70.setSpacing(0)
        self.verticalLayout_70.setObjectName(u"verticalLayout_70")
        self.label_77 = QLabel(self.block4_item24)
        self.label_77.setObjectName(u"label_77")
        self.label_77.setFont(font1)
        self.label_77.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_77.setWordWrap(True)

        self.verticalLayout_70.addWidget(self.label_77)

        self._70 = QHBoxLayout()
        self._70.setSpacing(0)
        self._70.setObjectName(u"_70")
        self.radioButton_222 = QRadioButton(self.block4_item24)
        self.radioButton_222.setObjectName(u"radioButton_222")
        self.radioButton_222.setFont(font1)

        self._70.addWidget(self.radioButton_222)

        self.radioButton_226 = QRadioButton(self.block4_item24)
        self.radioButton_226.setObjectName(u"radioButton_226")
        self.radioButton_226.setFont(font1)

        self._70.addWidget(self.radioButton_226)

        self.radioButton_227 = QRadioButton(self.block4_item24)
        self.radioButton_227.setObjectName(u"radioButton_227")
        self.radioButton_227.setFont(font1)

        self._70.addWidget(self.radioButton_227)

        self.radioButton_228 = QRadioButton(self.block4_item24)
        self.radioButton_228.setObjectName(u"radioButton_228")
        self.radioButton_228.setFont(font1)

        self._70.addWidget(self.radioButton_228)


        self.verticalLayout_70.addLayout(self._70)


        self.gridLayout_5.addWidget(self.block4_item24, 43, 0, 1, 1)


        self.gridLayout_2.addWidget(self.block4, 3, 0, 1, 1)

        self.block3 = QGroupBox(self.scrollAreaWidgetContents)
        self.block3.setObjectName(u"block3")
        self.block3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.gridLayout_4 = QGridLayout(self.block3)
        self.gridLayout_4.setSpacing(10)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(10, 10, 10, 10)
        self.block3_item01 = QGroupBox(self.block3)
        self.block3_item01.setObjectName(u"block3_item01")
        self.verticalLayout_36 = QVBoxLayout(self.block3_item01)
        self.verticalLayout_36.setSpacing(0)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.label_43 = QLabel(self.block3_item01)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setFont(font1)
        self.label_43.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_43.setWordWrap(True)

        self.verticalLayout_36.addWidget(self.label_43)

        self._36 = QHBoxLayout()
        self._36.setSpacing(0)
        self._36.setObjectName(u"_36")
        self.radioButton_106 = QRadioButton(self.block3_item01)
        self.radioButton_106.setObjectName(u"radioButton_106")
        self.radioButton_106.setFont(font1)

        self._36.addWidget(self.radioButton_106)

        self.radioButton_107 = QRadioButton(self.block3_item01)
        self.radioButton_107.setObjectName(u"radioButton_107")
        self.radioButton_107.setFont(font1)

        self._36.addWidget(self.radioButton_107)

        self.radioButton_108 = QRadioButton(self.block3_item01)
        self.radioButton_108.setObjectName(u"radioButton_108")
        self.radioButton_108.setFont(font1)

        self._36.addWidget(self.radioButton_108)


        self.verticalLayout_36.addLayout(self._36)


        self.gridLayout_4.addWidget(self.block3_item01, 0, 0, 1, 1)

        self.block3_item02 = QGroupBox(self.block3)
        self.block3_item02.setObjectName(u"block3_item02")
        self.verticalLayout_52 = QVBoxLayout(self.block3_item02)
        self.verticalLayout_52.setSpacing(0)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.label_59 = QLabel(self.block3_item02)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setFont(font1)
        self.label_59.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_52.addWidget(self.label_59)

        self._52 = QHBoxLayout()
        self._52.setSpacing(0)
        self._52.setObjectName(u"_52")
        self.radioButton_154 = QRadioButton(self.block3_item02)
        self.radioButton_154.setObjectName(u"radioButton_154")
        self.radioButton_154.setFont(font1)

        self._52.addWidget(self.radioButton_154)

        self.radioButton_155 = QRadioButton(self.block3_item02)
        self.radioButton_155.setObjectName(u"radioButton_155")
        self.radioButton_155.setFont(font1)

        self._52.addWidget(self.radioButton_155)

        self.radioButton_156 = QRadioButton(self.block3_item02)
        self.radioButton_156.setObjectName(u"radioButton_156")
        self.radioButton_156.setFont(font1)

        self._52.addWidget(self.radioButton_156)


        self.verticalLayout_52.addLayout(self._52)


        self.gridLayout_4.addWidget(self.block3_item02, 1, 0, 1, 1)

        self.block3_item03 = QGroupBox(self.block3)
        self.block3_item03.setObjectName(u"block3_item03")
        self.verticalLayout_42 = QVBoxLayout(self.block3_item03)
        self.verticalLayout_42.setSpacing(0)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.label_49 = QLabel(self.block3_item03)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setFont(font1)
        self.label_49.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_49.setWordWrap(True)

        self.verticalLayout_42.addWidget(self.label_49)

        self._42 = QHBoxLayout()
        self._42.setSpacing(0)
        self._42.setObjectName(u"_42")
        self.radioButton_124 = QRadioButton(self.block3_item03)
        self.radioButton_124.setObjectName(u"radioButton_124")
        self.radioButton_124.setFont(font1)

        self._42.addWidget(self.radioButton_124)

        self.radioButton_125 = QRadioButton(self.block3_item03)
        self.radioButton_125.setObjectName(u"radioButton_125")
        self.radioButton_125.setFont(font1)

        self._42.addWidget(self.radioButton_125)

        self.radioButton_126 = QRadioButton(self.block3_item03)
        self.radioButton_126.setObjectName(u"radioButton_126")
        self.radioButton_126.setFont(font1)

        self._42.addWidget(self.radioButton_126)


        self.verticalLayout_42.addLayout(self._42)


        self.gridLayout_4.addWidget(self.block3_item03, 2, 0, 1, 1)

        self.block3_item04 = QGroupBox(self.block3)
        self.block3_item04.setObjectName(u"block3_item04")
        self.verticalLayout_53 = QVBoxLayout(self.block3_item04)
        self.verticalLayout_53.setSpacing(0)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.label_60 = QLabel(self.block3_item04)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setFont(font1)
        self.label_60.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_53.addWidget(self.label_60)

        self._53 = QHBoxLayout()
        self._53.setSpacing(0)
        self._53.setObjectName(u"_53")
        self.radioButton_157 = QRadioButton(self.block3_item04)
        self.radioButton_157.setObjectName(u"radioButton_157")
        self.radioButton_157.setFont(font1)

        self._53.addWidget(self.radioButton_157)

        self.radioButton_158 = QRadioButton(self.block3_item04)
        self.radioButton_158.setObjectName(u"radioButton_158")
        self.radioButton_158.setFont(font1)

        self._53.addWidget(self.radioButton_158)

        self.radioButton_159 = QRadioButton(self.block3_item04)
        self.radioButton_159.setObjectName(u"radioButton_159")
        self.radioButton_159.setFont(font1)

        self._53.addWidget(self.radioButton_159)


        self.verticalLayout_53.addLayout(self._53)


        self.gridLayout_4.addWidget(self.block3_item04, 3, 0, 1, 1)

        self.block3_item05 = QGroupBox(self.block3)
        self.block3_item05.setObjectName(u"block3_item05")
        self.verticalLayout_54 = QVBoxLayout(self.block3_item05)
        self.verticalLayout_54.setSpacing(0)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.label_61 = QLabel(self.block3_item05)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setFont(font1)
        self.label_61.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_54.addWidget(self.label_61)

        self._54 = QHBoxLayout()
        self._54.setSpacing(0)
        self._54.setObjectName(u"_54")
        self.radioButton_160 = QRadioButton(self.block3_item05)
        self.radioButton_160.setObjectName(u"radioButton_160")
        self.radioButton_160.setFont(font1)

        self._54.addWidget(self.radioButton_160)

        self.radioButton_161 = QRadioButton(self.block3_item05)
        self.radioButton_161.setObjectName(u"radioButton_161")
        self.radioButton_161.setFont(font1)

        self._54.addWidget(self.radioButton_161)

        self.radioButton_162 = QRadioButton(self.block3_item05)
        self.radioButton_162.setObjectName(u"radioButton_162")
        self.radioButton_162.setFont(font1)

        self._54.addWidget(self.radioButton_162)


        self.verticalLayout_54.addLayout(self._54)


        self.gridLayout_4.addWidget(self.block3_item05, 4, 0, 1, 1)

        self.block3_item06 = QGroupBox(self.block3)
        self.block3_item06.setObjectName(u"block3_item06")
        self.verticalLayout_41 = QVBoxLayout(self.block3_item06)
        self.verticalLayout_41.setSpacing(0)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.label_48 = QLabel(self.block3_item06)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setFont(font1)
        self.label_48.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_41.addWidget(self.label_48)

        self._41 = QHBoxLayout()
        self._41.setSpacing(0)
        self._41.setObjectName(u"_41")
        self.radioButton_121 = QRadioButton(self.block3_item06)
        self.radioButton_121.setObjectName(u"radioButton_121")
        self.radioButton_121.setFont(font1)

        self._41.addWidget(self.radioButton_121)

        self.radioButton_122 = QRadioButton(self.block3_item06)
        self.radioButton_122.setObjectName(u"radioButton_122")
        self.radioButton_122.setFont(font1)

        self._41.addWidget(self.radioButton_122)

        self.radioButton_123 = QRadioButton(self.block3_item06)
        self.radioButton_123.setObjectName(u"radioButton_123")
        self.radioButton_123.setFont(font1)

        self._41.addWidget(self.radioButton_123)


        self.verticalLayout_41.addLayout(self._41)


        self.gridLayout_4.addWidget(self.block3_item06, 5, 0, 1, 1)

        self.block3_item07 = QGroupBox(self.block3)
        self.block3_item07.setObjectName(u"block3_item07")
        self.verticalLayout_37 = QVBoxLayout(self.block3_item07)
        self.verticalLayout_37.setSpacing(0)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.label_44 = QLabel(self.block3_item07)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setFont(font1)
        self.label_44.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_37.addWidget(self.label_44)

        self._37 = QHBoxLayout()
        self._37.setSpacing(0)
        self._37.setObjectName(u"_37")
        self.radioButton_109 = QRadioButton(self.block3_item07)
        self.radioButton_109.setObjectName(u"radioButton_109")
        self.radioButton_109.setFont(font1)

        self._37.addWidget(self.radioButton_109)

        self.radioButton_110 = QRadioButton(self.block3_item07)
        self.radioButton_110.setObjectName(u"radioButton_110")
        self.radioButton_110.setFont(font1)

        self._37.addWidget(self.radioButton_110)

        self.radioButton_111 = QRadioButton(self.block3_item07)
        self.radioButton_111.setObjectName(u"radioButton_111")
        self.radioButton_111.setFont(font1)

        self._37.addWidget(self.radioButton_111)


        self.verticalLayout_37.addLayout(self._37)


        self.gridLayout_4.addWidget(self.block3_item07, 6, 0, 1, 1)

        self.block3_item08 = QGroupBox(self.block3)
        self.block3_item08.setObjectName(u"block3_item08")
        self.verticalLayout_45 = QVBoxLayout(self.block3_item08)
        self.verticalLayout_45.setSpacing(0)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.label_52 = QLabel(self.block3_item08)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setFont(font1)
        self.label_52.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_45.addWidget(self.label_52)

        self._45 = QHBoxLayout()
        self._45.setSpacing(0)
        self._45.setObjectName(u"_45")
        self.radioButton_133 = QRadioButton(self.block3_item08)
        self.radioButton_133.setObjectName(u"radioButton_133")
        self.radioButton_133.setFont(font1)

        self._45.addWidget(self.radioButton_133)

        self.radioButton_134 = QRadioButton(self.block3_item08)
        self.radioButton_134.setObjectName(u"radioButton_134")
        self.radioButton_134.setFont(font1)

        self._45.addWidget(self.radioButton_134)

        self.radioButton_135 = QRadioButton(self.block3_item08)
        self.radioButton_135.setObjectName(u"radioButton_135")
        self.radioButton_135.setFont(font1)

        self._45.addWidget(self.radioButton_135)


        self.verticalLayout_45.addLayout(self._45)


        self.gridLayout_4.addWidget(self.block3_item08, 7, 0, 1, 1)

        self.block3_item09 = QGroupBox(self.block3)
        self.block3_item09.setObjectName(u"block3_item09")
        self.verticalLayout_38 = QVBoxLayout(self.block3_item09)
        self.verticalLayout_38.setSpacing(0)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.label_45 = QLabel(self.block3_item09)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setFont(font1)
        self.label_45.setAutoFillBackground(False)
        self.label_45.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_38.addWidget(self.label_45)

        self._38 = QHBoxLayout()
        self._38.setSpacing(0)
        self._38.setObjectName(u"_38")
        self.radioButton_112 = QRadioButton(self.block3_item09)
        self.radioButton_112.setObjectName(u"radioButton_112")
        self.radioButton_112.setFont(font1)

        self._38.addWidget(self.radioButton_112)

        self.radioButton_113 = QRadioButton(self.block3_item09)
        self.radioButton_113.setObjectName(u"radioButton_113")
        self.radioButton_113.setFont(font1)

        self._38.addWidget(self.radioButton_113)

        self.radioButton_114 = QRadioButton(self.block3_item09)
        self.radioButton_114.setObjectName(u"radioButton_114")
        self.radioButton_114.setFont(font1)

        self._38.addWidget(self.radioButton_114)


        self.verticalLayout_38.addLayout(self._38)


        self.gridLayout_4.addWidget(self.block3_item09, 8, 0, 1, 1)

        self.block3_item10 = QGroupBox(self.block3)
        self.block3_item10.setObjectName(u"block3_item10")
        self.verticalLayout_44 = QVBoxLayout(self.block3_item10)
        self.verticalLayout_44.setSpacing(0)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.label_51 = QLabel(self.block3_item10)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setFont(font1)
        self.label_51.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_51.setWordWrap(False)

        self.verticalLayout_44.addWidget(self.label_51)

        self._44 = QHBoxLayout()
        self._44.setSpacing(0)
        self._44.setObjectName(u"_44")
        self.radioButton_130 = QRadioButton(self.block3_item10)
        self.radioButton_130.setObjectName(u"radioButton_130")
        self.radioButton_130.setFont(font1)

        self._44.addWidget(self.radioButton_130)

        self.radioButton_131 = QRadioButton(self.block3_item10)
        self.radioButton_131.setObjectName(u"radioButton_131")
        self.radioButton_131.setFont(font1)

        self._44.addWidget(self.radioButton_131)

        self.radioButton_132 = QRadioButton(self.block3_item10)
        self.radioButton_132.setObjectName(u"radioButton_132")
        self.radioButton_132.setFont(font1)

        self._44.addWidget(self.radioButton_132)


        self.verticalLayout_44.addLayout(self._44)


        self.gridLayout_4.addWidget(self.block3_item10, 9, 0, 1, 1)

        self.block3_item11 = QGroupBox(self.block3)
        self.block3_item11.setObjectName(u"block3_item11")
        self.verticalLayout_46 = QVBoxLayout(self.block3_item11)
        self.verticalLayout_46.setSpacing(0)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.label_53 = QLabel(self.block3_item11)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setFont(font1)
        self.label_53.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_46.addWidget(self.label_53)

        self._46 = QHBoxLayout()
        self._46.setSpacing(0)
        self._46.setObjectName(u"_46")
        self.radioButton_136 = QRadioButton(self.block3_item11)
        self.radioButton_136.setObjectName(u"radioButton_136")
        self.radioButton_136.setFont(font1)

        self._46.addWidget(self.radioButton_136)

        self.radioButton_137 = QRadioButton(self.block3_item11)
        self.radioButton_137.setObjectName(u"radioButton_137")
        self.radioButton_137.setFont(font1)

        self._46.addWidget(self.radioButton_137)

        self.radioButton_138 = QRadioButton(self.block3_item11)
        self.radioButton_138.setObjectName(u"radioButton_138")
        self.radioButton_138.setFont(font1)

        self._46.addWidget(self.radioButton_138)


        self.verticalLayout_46.addLayout(self._46)


        self.gridLayout_4.addWidget(self.block3_item11, 10, 0, 1, 1)

        self.block3_item12 = QGroupBox(self.block3)
        self.block3_item12.setObjectName(u"block3_item12")
        self.verticalLayout_40 = QVBoxLayout(self.block3_item12)
        self.verticalLayout_40.setSpacing(0)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.label_47 = QLabel(self.block3_item12)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setFont(font1)
        self.label_47.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_47.setWordWrap(True)

        self.verticalLayout_40.addWidget(self.label_47)

        self._40 = QHBoxLayout()
        self._40.setSpacing(0)
        self._40.setObjectName(u"_40")
        self.radioButton_118 = QRadioButton(self.block3_item12)
        self.radioButton_118.setObjectName(u"radioButton_118")
        self.radioButton_118.setFont(font1)

        self._40.addWidget(self.radioButton_118)

        self.radioButton_119 = QRadioButton(self.block3_item12)
        self.radioButton_119.setObjectName(u"radioButton_119")
        self.radioButton_119.setFont(font1)

        self._40.addWidget(self.radioButton_119)

        self.radioButton_120 = QRadioButton(self.block3_item12)
        self.radioButton_120.setObjectName(u"radioButton_120")
        self.radioButton_120.setFont(font1)

        self._40.addWidget(self.radioButton_120)


        self.verticalLayout_40.addLayout(self._40)


        self.gridLayout_4.addWidget(self.block3_item12, 11, 0, 1, 1)

        self.block3_item13 = QGroupBox(self.block3)
        self.block3_item13.setObjectName(u"block3_item13")
        self.verticalLayout_47 = QVBoxLayout(self.block3_item13)
        self.verticalLayout_47.setSpacing(0)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.label_54 = QLabel(self.block3_item13)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setFont(font1)
        self.label_54.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_47.addWidget(self.label_54)

        self._47 = QHBoxLayout()
        self._47.setSpacing(0)
        self._47.setObjectName(u"_47")
        self.radioButton_139 = QRadioButton(self.block3_item13)
        self.radioButton_139.setObjectName(u"radioButton_139")
        self.radioButton_139.setFont(font1)

        self._47.addWidget(self.radioButton_139)

        self.radioButton_140 = QRadioButton(self.block3_item13)
        self.radioButton_140.setObjectName(u"radioButton_140")
        self.radioButton_140.setFont(font1)

        self._47.addWidget(self.radioButton_140)

        self.radioButton_141 = QRadioButton(self.block3_item13)
        self.radioButton_141.setObjectName(u"radioButton_141")
        self.radioButton_141.setFont(font1)

        self._47.addWidget(self.radioButton_141)


        self.verticalLayout_47.addLayout(self._47)


        self.gridLayout_4.addWidget(self.block3_item13, 12, 0, 1, 1)

        self.block3_item14 = QGroupBox(self.block3)
        self.block3_item14.setObjectName(u"block3_item14")
        self.verticalLayout_51 = QVBoxLayout(self.block3_item14)
        self.verticalLayout_51.setSpacing(0)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.label_58 = QLabel(self.block3_item14)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setFont(font1)
        self.label_58.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_58.setWordWrap(True)

        self.verticalLayout_51.addWidget(self.label_58)

        self._51 = QHBoxLayout()
        self._51.setSpacing(0)
        self._51.setObjectName(u"_51")
        self.radioButton_151 = QRadioButton(self.block3_item14)
        self.radioButton_151.setObjectName(u"radioButton_151")
        self.radioButton_151.setFont(font1)

        self._51.addWidget(self.radioButton_151)

        self.radioButton_152 = QRadioButton(self.block3_item14)
        self.radioButton_152.setObjectName(u"radioButton_152")
        self.radioButton_152.setFont(font1)

        self._51.addWidget(self.radioButton_152)

        self.radioButton_153 = QRadioButton(self.block3_item14)
        self.radioButton_153.setObjectName(u"radioButton_153")
        self.radioButton_153.setFont(font1)

        self._51.addWidget(self.radioButton_153)


        self.verticalLayout_51.addLayout(self._51)


        self.gridLayout_4.addWidget(self.block3_item14, 13, 0, 1, 1)

        self.block3_item15 = QGroupBox(self.block3)
        self.block3_item15.setObjectName(u"block3_item15")
        self.verticalLayout_55 = QVBoxLayout(self.block3_item15)
        self.verticalLayout_55.setSpacing(0)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.label_62 = QLabel(self.block3_item15)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setFont(font1)
        self.label_62.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_62.setWordWrap(True)

        self.verticalLayout_55.addWidget(self.label_62)

        self._55 = QHBoxLayout()
        self._55.setSpacing(0)
        self._55.setObjectName(u"_55")
        self.radioButton_163 = QRadioButton(self.block3_item15)
        self.radioButton_163.setObjectName(u"radioButton_163")
        self.radioButton_163.setFont(font1)

        self._55.addWidget(self.radioButton_163)

        self.radioButton_164 = QRadioButton(self.block3_item15)
        self.radioButton_164.setObjectName(u"radioButton_164")
        self.radioButton_164.setFont(font1)

        self._55.addWidget(self.radioButton_164)

        self.radioButton_165 = QRadioButton(self.block3_item15)
        self.radioButton_165.setObjectName(u"radioButton_165")
        self.radioButton_165.setFont(font1)

        self._55.addWidget(self.radioButton_165)


        self.verticalLayout_55.addLayout(self._55)


        self.gridLayout_4.addWidget(self.block3_item15, 14, 0, 1, 1)

        self.block3_item16 = QGroupBox(self.block3)
        self.block3_item16.setObjectName(u"block3_item16")
        self.verticalLayout_39 = QVBoxLayout(self.block3_item16)
        self.verticalLayout_39.setSpacing(0)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.label_46 = QLabel(self.block3_item16)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setFont(font1)
        self.label_46.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_46.setWordWrap(True)

        self.verticalLayout_39.addWidget(self.label_46)

        self._39 = QHBoxLayout()
        self._39.setSpacing(0)
        self._39.setObjectName(u"_39")
        self.radioButton_115 = QRadioButton(self.block3_item16)
        self.radioButton_115.setObjectName(u"radioButton_115")
        self.radioButton_115.setFont(font1)

        self._39.addWidget(self.radioButton_115)

        self.radioButton_116 = QRadioButton(self.block3_item16)
        self.radioButton_116.setObjectName(u"radioButton_116")
        self.radioButton_116.setFont(font1)

        self._39.addWidget(self.radioButton_116)

        self.radioButton_117 = QRadioButton(self.block3_item16)
        self.radioButton_117.setObjectName(u"radioButton_117")
        self.radioButton_117.setFont(font1)

        self._39.addWidget(self.radioButton_117)


        self.verticalLayout_39.addLayout(self._39)


        self.gridLayout_4.addWidget(self.block3_item16, 15, 0, 1, 1)

        self.block3_item17 = QGroupBox(self.block3)
        self.block3_item17.setObjectName(u"block3_item17")
        self.verticalLayout_43 = QVBoxLayout(self.block3_item17)
        self.verticalLayout_43.setSpacing(0)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.label_50 = QLabel(self.block3_item17)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setFont(font1)
        self.label_50.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_50.setWordWrap(True)

        self.verticalLayout_43.addWidget(self.label_50)

        self._43 = QHBoxLayout()
        self._43.setSpacing(0)
        self._43.setObjectName(u"_43")
        self.radioButton_127 = QRadioButton(self.block3_item17)
        self.radioButton_127.setObjectName(u"radioButton_127")
        self.radioButton_127.setFont(font1)

        self._43.addWidget(self.radioButton_127)

        self.radioButton_128 = QRadioButton(self.block3_item17)
        self.radioButton_128.setObjectName(u"radioButton_128")
        self.radioButton_128.setFont(font1)

        self._43.addWidget(self.radioButton_128)

        self.radioButton_129 = QRadioButton(self.block3_item17)
        self.radioButton_129.setObjectName(u"radioButton_129")
        self.radioButton_129.setFont(font1)

        self._43.addWidget(self.radioButton_129)


        self.verticalLayout_43.addLayout(self._43)


        self.gridLayout_4.addWidget(self.block3_item17, 16, 0, 1, 1)

        self.block3_item18 = QGroupBox(self.block3)
        self.block3_item18.setObjectName(u"block3_item18")
        self.verticalLayout_49 = QVBoxLayout(self.block3_item18)
        self.verticalLayout_49.setSpacing(0)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.label_56 = QLabel(self.block3_item18)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setFont(font1)
        self.label_56.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_56.setWordWrap(True)

        self.verticalLayout_49.addWidget(self.label_56)

        self._49 = QHBoxLayout()
        self._49.setSpacing(0)
        self._49.setObjectName(u"_49")
        self.radioButton_145 = QRadioButton(self.block3_item18)
        self.radioButton_145.setObjectName(u"radioButton_145")
        self.radioButton_145.setFont(font1)

        self._49.addWidget(self.radioButton_145)

        self.radioButton_146 = QRadioButton(self.block3_item18)
        self.radioButton_146.setObjectName(u"radioButton_146")
        self.radioButton_146.setFont(font1)

        self._49.addWidget(self.radioButton_146)

        self.radioButton_147 = QRadioButton(self.block3_item18)
        self.radioButton_147.setObjectName(u"radioButton_147")
        self.radioButton_147.setFont(font1)

        self._49.addWidget(self.radioButton_147)


        self.verticalLayout_49.addLayout(self._49)


        self.gridLayout_4.addWidget(self.block3_item18, 17, 0, 1, 1)


        self.gridLayout_2.addWidget(self.block3, 2, 0, 1, 1)

        self.block1 = QGroupBox(self.scrollAreaWidgetContents)
        self.block1.setObjectName(u"block1")
        self.block1.setStyleSheet(u"")
        self.block1.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.gridLayout = QGridLayout(self.block1)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.block1_item11 = QGroupBox(self.block1)
        self.block1_item11.setObjectName(u"block1_item11")
        self.verticalLayout_9 = QVBoxLayout(self.block1_item11)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_16 = QLabel(self.block1_item11)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font1)
        self.label_16.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_9.addWidget(self.label_16)

        self._48 = QHBoxLayout()
        self._48.setSpacing(0)
        self._48.setObjectName(u"_48")
        self.radioButton_25 = QRadioButton(self.block1_item11)
        self.radioButton_25.setObjectName(u"radioButton_25")
        self.radioButton_25.setFont(font1)

        self._48.addWidget(self.radioButton_25)

        self.radioButton_26 = QRadioButton(self.block1_item11)
        self.radioButton_26.setObjectName(u"radioButton_26")
        self.radioButton_26.setFont(font1)

        self._48.addWidget(self.radioButton_26)

        self.radioButton_27 = QRadioButton(self.block1_item11)
        self.radioButton_27.setObjectName(u"radioButton_27")
        self.radioButton_27.setFont(font1)

        self._48.addWidget(self.radioButton_27)


        self.verticalLayout_9.addLayout(self._48)


        self.gridLayout.addWidget(self.block1_item11, 10, 0, 1, 1)

        self.block1_item01 = QGroupBox(self.block1)
        self.block1_item01.setObjectName(u"block1_item01")
        self.verticalLayout = QVBoxLayout(self.block1_item01)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_8 = QLabel(self.block1_item01)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)
        self.label_8.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_8)

        self._9 = QFrame(self.block1_item01)
        self._9.setObjectName(u"_9")
        self._1 = QHBoxLayout(self._9)
        self._1.setSpacing(0)
        self._1.setObjectName(u"_1")
        self.radioButton = QRadioButton(self._9)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setFont(font1)

        self._1.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self._9)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setFont(font1)

        self._1.addWidget(self.radioButton_2)

        self.radioButton_3 = QRadioButton(self._9)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setFont(font1)

        self._1.addWidget(self.radioButton_3)


        self.verticalLayout.addWidget(self._9)


        self.gridLayout.addWidget(self.block1_item01, 0, 0, 1, 1)

        self.block1_item10 = QGroupBox(self.block1)
        self.block1_item10.setObjectName(u"block1_item10")
        self.verticalLayout_10 = QVBoxLayout(self.block1_item10)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_17 = QLabel(self.block1_item10)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font1)
        self.label_17.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_17.setWordWrap(False)

        self.verticalLayout_10.addWidget(self.label_17)

        self._10 = QHBoxLayout()
        self._10.setSpacing(0)
        self._10.setObjectName(u"_10")
        self.radioButton_28 = QRadioButton(self.block1_item10)
        self.radioButton_28.setObjectName(u"radioButton_28")
        self.radioButton_28.setFont(font1)

        self._10.addWidget(self.radioButton_28)

        self.radioButton_29 = QRadioButton(self.block1_item10)
        self.radioButton_29.setObjectName(u"radioButton_29")
        self.radioButton_29.setFont(font1)

        self._10.addWidget(self.radioButton_29)

        self.radioButton_30 = QRadioButton(self.block1_item10)
        self.radioButton_30.setObjectName(u"radioButton_30")
        self.radioButton_30.setFont(font1)

        self._10.addWidget(self.radioButton_30)


        self.verticalLayout_10.addLayout(self._10)


        self.gridLayout.addWidget(self.block1_item10, 9, 0, 1, 1)

        self.block1_item09 = QGroupBox(self.block1)
        self.block1_item09.setObjectName(u"block1_item09")
        self.verticalLayout_11 = QVBoxLayout(self.block1_item09)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_18 = QLabel(self.block1_item09)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font1)
        self.label_18.setAutoFillBackground(False)
        self.label_18.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_11.addWidget(self.label_18)

        self._11 = QHBoxLayout()
        self._11.setSpacing(0)
        self._11.setObjectName(u"_11")
        self.radioButton_31 = QRadioButton(self.block1_item09)
        self.radioButton_31.setObjectName(u"radioButton_31")
        self.radioButton_31.setFont(font1)

        self._11.addWidget(self.radioButton_31)

        self.radioButton_32 = QRadioButton(self.block1_item09)
        self.radioButton_32.setObjectName(u"radioButton_32")
        self.radioButton_32.setFont(font1)

        self._11.addWidget(self.radioButton_32)

        self.radioButton_33 = QRadioButton(self.block1_item09)
        self.radioButton_33.setObjectName(u"radioButton_33")
        self.radioButton_33.setFont(font1)

        self._11.addWidget(self.radioButton_33)


        self.verticalLayout_11.addLayout(self._11)


        self.gridLayout.addWidget(self.block1_item09, 8, 0, 1, 1)

        self.block1_item14 = QGroupBox(self.block1)
        self.block1_item14.setObjectName(u"block1_item14")
        self.verticalLayout_12 = QVBoxLayout(self.block1_item14)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_19 = QLabel(self.block1_item14)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font1)
        self.label_19.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_19.setWordWrap(True)

        self.verticalLayout_12.addWidget(self.label_19)

        self._12 = QHBoxLayout()
        self._12.setSpacing(0)
        self._12.setObjectName(u"_12")
        self.radioButton_34 = QRadioButton(self.block1_item14)
        self.radioButton_34.setObjectName(u"radioButton_34")
        self.radioButton_34.setFont(font1)

        self._12.addWidget(self.radioButton_34)

        self.radioButton_35 = QRadioButton(self.block1_item14)
        self.radioButton_35.setObjectName(u"radioButton_35")
        self.radioButton_35.setFont(font1)

        self._12.addWidget(self.radioButton_35)

        self.radioButton_36 = QRadioButton(self.block1_item14)
        self.radioButton_36.setObjectName(u"radioButton_36")
        self.radioButton_36.setFont(font1)

        self._12.addWidget(self.radioButton_36)


        self.verticalLayout_12.addLayout(self._12)


        self.gridLayout.addWidget(self.block1_item14, 13, 0, 1, 1)

        self.block1_item02 = QGroupBox(self.block1)
        self.block1_item02.setObjectName(u"block1_item02")
        self.verticalLayout_2 = QVBoxLayout(self.block1_item02)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_9 = QLabel(self.block1_item02)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)
        self.label_9.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.label_9)

        self._2 = QHBoxLayout()
        self._2.setSpacing(0)
        self._2.setObjectName(u"_2")
        self.radioButton_4 = QRadioButton(self.block1_item02)
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setFont(font1)

        self._2.addWidget(self.radioButton_4)

        self.radioButton_5 = QRadioButton(self.block1_item02)
        self.radioButton_5.setObjectName(u"radioButton_5")
        self.radioButton_5.setFont(font1)

        self._2.addWidget(self.radioButton_5)

        self.radioButton_6 = QRadioButton(self.block1_item02)
        self.radioButton_6.setObjectName(u"radioButton_6")
        self.radioButton_6.setFont(font1)

        self._2.addWidget(self.radioButton_6)


        self.verticalLayout_2.addLayout(self._2)


        self.gridLayout.addWidget(self.block1_item02, 1, 0, 1, 1)

        self.block1_item03 = QGroupBox(self.block1)
        self.block1_item03.setObjectName(u"block1_item03")
        self.block1_item3 = QVBoxLayout(self.block1_item03)
        self.block1_item3.setSpacing(0)
        self.block1_item3.setObjectName(u"block1_item3")
        self.label_10 = QLabel(self.block1_item03)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font1)
        self.label_10.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.block1_item3.addWidget(self.label_10)

        self._3 = QHBoxLayout()
        self._3.setSpacing(0)
        self._3.setObjectName(u"_3")
        self.radioButton_7 = QRadioButton(self.block1_item03)
        self.radioButton_7.setObjectName(u"radioButton_7")
        self.radioButton_7.setFont(font1)

        self._3.addWidget(self.radioButton_7)

        self.radioButton_8 = QRadioButton(self.block1_item03)
        self.radioButton_8.setObjectName(u"radioButton_8")
        self.radioButton_8.setFont(font1)

        self._3.addWidget(self.radioButton_8)

        self.radioButton_9 = QRadioButton(self.block1_item03)
        self.radioButton_9.setObjectName(u"radioButton_9")
        self.radioButton_9.setFont(font1)

        self._3.addWidget(self.radioButton_9)


        self.block1_item3.addLayout(self._3)


        self.gridLayout.addWidget(self.block1_item03, 2, 0, 1, 1)

        self.block1_item04 = QGroupBox(self.block1)
        self.block1_item04.setObjectName(u"block1_item04")
        self.verticalLayout_4 = QVBoxLayout(self.block1_item04)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_11 = QLabel(self.block1_item04)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font1)
        self.label_11.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_4.addWidget(self.label_11)

        self._4 = QHBoxLayout()
        self._4.setSpacing(0)
        self._4.setObjectName(u"_4")
        self.radioButton_10 = QRadioButton(self.block1_item04)
        self.radioButton_10.setObjectName(u"radioButton_10")
        self.radioButton_10.setFont(font1)

        self._4.addWidget(self.radioButton_10)

        self.radioButton_11 = QRadioButton(self.block1_item04)
        self.radioButton_11.setObjectName(u"radioButton_11")
        self.radioButton_11.setFont(font1)

        self._4.addWidget(self.radioButton_11)

        self.radioButton_12 = QRadioButton(self.block1_item04)
        self.radioButton_12.setObjectName(u"radioButton_12")
        self.radioButton_12.setFont(font1)

        self._4.addWidget(self.radioButton_12)


        self.verticalLayout_4.addLayout(self._4)


        self.gridLayout.addWidget(self.block1_item04, 3, 0, 1, 1)

        self.block1_item05 = QGroupBox(self.block1)
        self.block1_item05.setObjectName(u"block1_item05")
        self.verticalLayout_5 = QVBoxLayout(self.block1_item05)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_12 = QLabel(self.block1_item05)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font1)
        self.label_12.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_5.addWidget(self.label_12)

        self._5 = QHBoxLayout()
        self._5.setSpacing(0)
        self._5.setObjectName(u"_5")
        self.radioButton_13 = QRadioButton(self.block1_item05)
        self.radioButton_13.setObjectName(u"radioButton_13")
        self.radioButton_13.setFont(font1)

        self._5.addWidget(self.radioButton_13)

        self.radioButton_14 = QRadioButton(self.block1_item05)
        self.radioButton_14.setObjectName(u"radioButton_14")
        self.radioButton_14.setFont(font1)

        self._5.addWidget(self.radioButton_14)

        self.radioButton_15 = QRadioButton(self.block1_item05)
        self.radioButton_15.setObjectName(u"radioButton_15")
        self.radioButton_15.setFont(font1)

        self._5.addWidget(self.radioButton_15)


        self.verticalLayout_5.addLayout(self._5)


        self.gridLayout.addWidget(self.block1_item05, 4, 0, 1, 1)

        self.block1_item06 = QGroupBox(self.block1)
        self.block1_item06.setObjectName(u"block1_item06")
        self.verticalLayout_6 = QVBoxLayout(self.block1_item06)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_13 = QLabel(self.block1_item06)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font1)
        self.label_13.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_6.addWidget(self.label_13)

        self._6 = QHBoxLayout()
        self._6.setSpacing(0)
        self._6.setObjectName(u"_6")
        self.radioButton_16 = QRadioButton(self.block1_item06)
        self.radioButton_16.setObjectName(u"radioButton_16")
        self.radioButton_16.setFont(font1)

        self._6.addWidget(self.radioButton_16)

        self.radioButton_17 = QRadioButton(self.block1_item06)
        self.radioButton_17.setObjectName(u"radioButton_17")
        self.radioButton_17.setFont(font1)

        self._6.addWidget(self.radioButton_17)

        self.radioButton_18 = QRadioButton(self.block1_item06)
        self.radioButton_18.setObjectName(u"radioButton_18")
        self.radioButton_18.setFont(font1)

        self._6.addWidget(self.radioButton_18)


        self.verticalLayout_6.addLayout(self._6)


        self.gridLayout.addWidget(self.block1_item06, 5, 0, 1, 1)

        self.block1_item07 = QGroupBox(self.block1)
        self.block1_item07.setObjectName(u"block1_item07")
        self.verticalLayout_7 = QVBoxLayout(self.block1_item07)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_14 = QLabel(self.block1_item07)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font1)
        self.label_14.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_7.addWidget(self.label_14)

        self._7 = QHBoxLayout()
        self._7.setSpacing(0)
        self._7.setObjectName(u"_7")
        self.radioButton_19 = QRadioButton(self.block1_item07)
        self.radioButton_19.setObjectName(u"radioButton_19")
        self.radioButton_19.setFont(font1)

        self._7.addWidget(self.radioButton_19)

        self.radioButton_20 = QRadioButton(self.block1_item07)
        self.radioButton_20.setObjectName(u"radioButton_20")
        self.radioButton_20.setFont(font1)

        self._7.addWidget(self.radioButton_20)

        self.radioButton_21 = QRadioButton(self.block1_item07)
        self.radioButton_21.setObjectName(u"radioButton_21")
        self.radioButton_21.setFont(font1)

        self._7.addWidget(self.radioButton_21)


        self.verticalLayout_7.addLayout(self._7)


        self.gridLayout.addWidget(self.block1_item07, 6, 0, 1, 1)

        self.block1_item08 = QGroupBox(self.block1)
        self.block1_item08.setObjectName(u"block1_item08")
        self.verticalLayout_8 = QVBoxLayout(self.block1_item08)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_15 = QLabel(self.block1_item08)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font1)
        self.label_15.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_8.addWidget(self.label_15)

        self._8 = QHBoxLayout()
        self._8.setSpacing(0)
        self._8.setObjectName(u"_8")
        self.radioButton_22 = QRadioButton(self.block1_item08)
        self.radioButton_22.setObjectName(u"radioButton_22")
        self.radioButton_22.setFont(font1)

        self._8.addWidget(self.radioButton_22)

        self.radioButton_23 = QRadioButton(self.block1_item08)
        self.radioButton_23.setObjectName(u"radioButton_23")
        self.radioButton_23.setFont(font1)

        self._8.addWidget(self.radioButton_23)

        self.radioButton_24 = QRadioButton(self.block1_item08)
        self.radioButton_24.setObjectName(u"radioButton_24")
        self.radioButton_24.setFont(font1)

        self._8.addWidget(self.radioButton_24)


        self.verticalLayout_8.addLayout(self._8)


        self.gridLayout.addWidget(self.block1_item08, 7, 0, 1, 1)

        self.block1_item12 = QGroupBox(self.block1)
        self.block1_item12.setObjectName(u"block1_item12")
        self.verticalLayout_15 = QVBoxLayout(self.block1_item12)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_22 = QLabel(self.block1_item12)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font1)
        self.label_22.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_22.setWordWrap(True)

        self.verticalLayout_15.addWidget(self.label_22)

        self._15 = QHBoxLayout()
        self._15.setSpacing(0)
        self._15.setObjectName(u"_15")
        self.radioButton_43 = QRadioButton(self.block1_item12)
        self.radioButton_43.setObjectName(u"radioButton_43")
        self.radioButton_43.setFont(font1)

        self._15.addWidget(self.radioButton_43)

        self.radioButton_44 = QRadioButton(self.block1_item12)
        self.radioButton_44.setObjectName(u"radioButton_44")
        self.radioButton_44.setFont(font1)

        self._15.addWidget(self.radioButton_44)

        self.radioButton_45 = QRadioButton(self.block1_item12)
        self.radioButton_45.setObjectName(u"radioButton_45")
        self.radioButton_45.setFont(font1)

        self._15.addWidget(self.radioButton_45)


        self.verticalLayout_15.addLayout(self._15)


        self.gridLayout.addWidget(self.block1_item12, 11, 0, 1, 1)

        self.block1_item13 = QGroupBox(self.block1)
        self.block1_item13.setObjectName(u"block1_item13")
        self.verticalLayout_13 = QVBoxLayout(self.block1_item13)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_20 = QLabel(self.block1_item13)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font1)
        self.label_20.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_13.addWidget(self.label_20)

        self._13 = QHBoxLayout()
        self._13.setSpacing(0)
        self._13.setObjectName(u"_13")
        self.radioButton_37 = QRadioButton(self.block1_item13)
        self.radioButton_37.setObjectName(u"radioButton_37")
        self.radioButton_37.setFont(font1)

        self._13.addWidget(self.radioButton_37)

        self.radioButton_38 = QRadioButton(self.block1_item13)
        self.radioButton_38.setObjectName(u"radioButton_38")
        self.radioButton_38.setFont(font1)

        self._13.addWidget(self.radioButton_38)

        self.radioButton_39 = QRadioButton(self.block1_item13)
        self.radioButton_39.setObjectName(u"radioButton_39")
        self.radioButton_39.setFont(font1)

        self._13.addWidget(self.radioButton_39)


        self.verticalLayout_13.addLayout(self._13)


        self.gridLayout.addWidget(self.block1_item13, 12, 0, 1, 1)


        self.gridLayout_2.addWidget(self.block1, 0, 0, 1, 1)

        self.warning = QLabel(self.scrollAreaWidgetContents)
        self.warning.setObjectName(u"warning")
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        self.warning.setFont(font2)
        self.warning.setAlignment(Qt.AlignCenter)
        self.warning.setWordWrap(True)

        self.gridLayout_2.addWidget(self.warning, 4, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.exitWithoutSave_button = QPushButton(self.centralwidget)
        self.exitWithoutSave_button.setObjectName(u"exitWithoutSave_button")
        self.exitWithoutSave_button.setGeometry(QRect(100, 670, 231, 41))
        self.exitWithoutSave_button.setFont(font)
        self.exitWithoutSave_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.exitWithoutSave_button.setMouseTracking(True)
        self.exitWithoutSave_button.setTabletTracking(False)
        self.exitWithoutSave_button.setStyleSheet(u"QPushButton{\n"
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
        self.exitWithoutSave_button.setCheckable(False)
        self.exitWithoutSave_button.setAutoDefault(False)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.saveData_button.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.block2.setTitle(QCoreApplication.translate("MainWindow", u"II. \u0421\u043e\u0446\u0438\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 1: \u041a\u0430\u0436\u0435\u0442\u0441\u044f, \u0447\u0442\u043e \u043d\u0430\u0445\u043e\u0434\u0438\u0442\u0441\u044f \u0432 \u0440\u0430\u043a\u043e\u0432\u0438\u043d\u0435 \u2013 \u0432\u044b \u043d\u0435 \u043c\u043e\u0436\u0435\u0442\u0435 \u0434\u043e\u0441\u0442\u0443\u0447\u0430\u0442\u044c\u0441\u044f \u0434\u043e \u043d\u0435\u0433\u043e/\u043d\u0435\u0435?", None))
        self.radioButton_58.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430", None))
        self.radioButton_59.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u043e\u0433\u0434\u0430", None))
        self.radioButton_60.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0442", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 2: \u0418\u0433\u043d\u043e\u0440\u0438\u0440\u0443\u0435\u0442 \u0434\u0440\u0443\u0433\u0438\u0445 \u043b\u044e\u0434\u0435\u0439?", None))
        self.radioButton_82.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430", None))
        self.radioButton_83.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u043e\u0433\u0434\u0430", None))
        self.radioButton_84.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0442", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 3: \u041f\u0440\u0430\u043a\u0442\u0438\u0447\u0435\u0441\u043a\u0438 \u043d\u0435 \u043e\u0431\u0440\u0430\u0449\u0430\u0435\u0442 \u0432\u043d\u0438\u043c\u0430\u043d\u0438\u0435, \u0435\u0441\u043b\u0438 \u043a \u043d\u0435\u043c\u0443/\u043a \u043d\u0435\u0439 \u043e\u0431\u0440\u0430\u0449\u0430\u044e\u0442\u0441\u044f?", None))
        self.radioButton_46.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430", None))
        self.radioButton_47.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u043e\u0433\u0434\u0430", None))
        self.radioButton_48.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0442", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 4: \u041d\u0435 \u0441\u043a\u043b\u043e\u043d\u0435\u043d \u043a \u0441\u043e\u0432\u043c\u0435\u0441\u0442\u043d\u043e\u0439 \u0434\u0435\u044f\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u0438?", None))
        self.radioButton_55.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430", None))
        self.radioButton_56.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u043e\u0433\u0434\u0430", None))
        self.radioButton_57.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0442", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 5: \u0417\u0440\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u043a\u043e\u043d\u0442\u0430\u043a\u0442 \u043e\u0442\u0441\u0443\u0442\u0441\u0442\u0432\u0443\u0435\u0442?", None))
        self.radioButton_67.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430", None))
        self.radioButton_68.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u043e\u0433\u0434\u0430", None))
        self.radioButton_69.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0442", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 6: \u041f\u0440\u0435\u0434\u043f\u043e\u0447\u0438\u0442\u0430\u0435\u0442 \u043e\u0441\u0442\u0430\u0432\u0430\u0442\u044c\u0441\u044f \u0432 \u043e\u0434\u0438\u043d\u043e\u0447\u0435\u0441\u0442\u0432\u0435?", None))
        self.radioButton_52.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430", None))
        self.radioButton_53.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u043e\u0433\u0434\u0430", None))
        self.radioButton_54.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0442", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 7: \u041d\u0435 \u043f\u0440\u043e\u044f\u0432\u043b\u044f\u0435\u0442 \u043f\u0440\u0438\u0432\u044f\u0437\u0430\u043d\u043d\u043e\u0441\u0442\u0438?", None))
        self.radioButton_70.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430", None))
        self.radioButton_71.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u043e\u0433\u0434\u0430", None))
        self.radioButton_72.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0442", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 8: \u041d\u0435 \u0437\u0434\u043e\u0440\u043e\u0432\u0430\u0435\u0442\u0441\u044f \u0441 \u0440\u043e\u0434\u0438\u0442\u0435\u043b\u044f\u043c\u0438?", None))
        self.radioButton_73.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430", None))
        self.radioButton_74.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u043e\u0433\u0434\u0430", None))
        self.radioButton_75.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0442", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 9: \u0418\u0437\u0431\u0435\u0433\u0430\u0435\u0442 \u043a\u043e\u043d\u0442\u0430\u043a\u0442\u043e\u0432 \u0441 \u043e\u043a\u0440\u0443\u0436\u0430\u044e\u0449\u0438\u043c\u0438?", None))
        self.radioButton_64.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430", None))
        self.radioButton_65.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u043e\u0433\u0434\u0430", None))
        self.radioButton_66.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0442", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 10: \u0418\u043c\u0438\u0442\u0430\u0446\u0438\u044f \u043e\u0442\u0441\u0443\u0442\u0441\u0442\u0432\u0443\u0435\u0442?", None))
        self.radioButton_49.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430", None))
        self.radioButton_50.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u043e\u0433\u0434\u0430", None))
        self.radioButton_51.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0442", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 11 : \u041d\u0435 \u043b\u044e\u0431\u0438\u0442 \u043f\u0440\u0438\u043a\u043e\u0441\u043d\u043e\u0432\u0435\u043d\u0438\u0439/\u043e\u0431\u044a\u044f\u0442\u0438\u0439?", None))
        self.radioButton_61.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430", None))
        self.radioButton_62.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u043e\u0433\u0434\u0430", None))
        self.radioButton_63.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0442", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 12: \u041d\u0435 \u0434\u0435\u043b\u0438\u0442\u0441\u044f, \u0443\u043a\u0430\u0437\u0430\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u0436\u0435\u0441\u0442 \u043e\u0442\u0441\u0443\u0442\u0441\u0442\u0432\u0443\u0435\u0442?", None))
        self.radioButton_85.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430", None))
        self.radioButton_86.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u043e\u0433\u0434\u0430", None))
        self.radioButton_87.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0442", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 13: \u041d\u0435 \u043c\u0430\u0448\u0435\u0442 \u0440\u0443\u043a\u043e\u0439 `\u0434\u043e \u0441\u0432\u0438\u0434\u0430\u043d\u0438\u044f`?", None))
        self.radioButton_79.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430", None))
        self.radioButton_80.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u043e\u0433\u0434\u0430", None))
        self.radioButton_81.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0442", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 14: \u041d\u0435\u043f\u043e\u0441\u043b\u0443\u0448\u043d\u044b\u0439/\u043d\u0435\u043f\u043e\u043a\u043b\u0430\u0434\u0438\u0441\u0442\u044b\u0439?", None))
        self.radioButton_76.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430", None))
        self.radioButton_77.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u043e\u0433\u0434\u0430", None))
        self.radioButton_78.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0442", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 15: \u0418\u0441\u043f\u044b\u0442\u044b\u0432\u0430\u0435\u0442 \u043f\u0440\u0438\u0441\u0442\u0443\u043f\u044b \u0433\u043d\u0435\u0432\u0430, \u0440\u0430\u0437\u0434\u0440\u0430\u0436\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u0438?", None))
        self.radioButton_103.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430", None))
        self.radioButton_104.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u043e\u0433\u0434\u0430", None))
        self.radioButton_105.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0442", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 16: \u041d\u0435\u0434\u043e\u0441\u0442\u0430\u0442\u043e\u043a \u0434\u0440\u0443\u0437\u0435\u0439/\u043d\u0435\u0442 \u043a\u043e\u043c\u043f\u0430\u043d\u0438\u0438?", None))
        self.radioButton_100.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430", None))
        self.radioButton_101.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u043e\u0433\u0434\u0430", None))
        self.radioButton_102.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0442", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 17: \u0420\u0435\u0434\u043a\u043e \u0443\u043b\u044b\u0431\u0430\u0435\u0442\u0441\u044f?", None))
        self.radioButton_97.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430", None))
        self.radioButton_98.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u043e\u0433\u0434\u0430", None))
        self.radioButton_99.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0442", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 18: \u041d\u0435 \u043f\u043e\u043d\u0438\u043c\u0430\u0435\u0442 \u0447\u0443\u0432\u0441\u0442\u0432 \u0434\u0440\u0443\u0433\u0438\u0445 \u043b\u044e\u0434\u0435\u0439?", None))
        self.radioButton_94.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430", None))
        self.radioButton_95.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u043e\u0433\u0434\u0430", None))
        self.radioButton_96.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0442", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 19: \u0411\u0435\u0437\u0440\u0430\u0437\u043b\u0438\u0447\u0435\u043d, \u0435\u0441\u043b\u0438 \u0435\u043c\u0443 \u0432\u044b\u0440\u0430\u0436\u0430\u044e\u0442 \u0441\u0438\u043c\u043f\u0430\u0442\u0438\u044e?", None))
        self.radioButton_91.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430", None))
        self.radioButton_92.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u043e\u0433\u0434\u0430", None))
        self.radioButton_93.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0442", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 20: \u041d\u0435 \u0440\u0435\u0430\u0433\u0438\u0440\u0443\u0435\u0442 \u043d\u0430 \u0443\u0445\u043e\u0434 \u0440\u043e\u0434\u0438\u0442\u0435\u043b\u0435\u0439?", None))
        self.radioButton_88.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430", None))
        self.radioButton_89.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u043e\u0433\u0434\u0430", None))
        self.radioButton_90.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0442", None))
        self.block4.setTitle(QCoreApplication.translate("MainWindow", u"IV. \u0417\u0434\u043e\u0440\u043e\u0432\u044c\u0435/\u0424\u0438\u0437\u0438\u0447\u0435\u0441\u043a\u043e\u0435 \u0440\u0430\u0437\u0432\u0438\u0442\u0438\u0435/\u041f\u043e\u0432\u0435\u0434\u0435\u043d\u0438\u0435", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 1: \u041d\u043e\u0447\u043d\u043e\u0435 \u043d\u0435\u0434\u0435\u0440\u0436\u0430\u043d\u0438\u0435 \u043c\u043e\u0447\u0438?", None))
        self.radioButton_166.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435 \u043f\u0440\u043e\u0431\u043b\u0435\u043c\u0430", None))
        self.radioButton_167.setText(QCoreApplication.translate("MainWindow", u"\u041b\u0451\u0433\u043a\u0430\u044f \u043f\u0440\u043e\u0431\u043b.", None))
        self.radioButton_169.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0440\u0435\u0434\u043d\u044f\u044f \u043f\u0440\u043e\u0431\u043b.", None))
        self.radioButton_168.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0435\u0440\u044c\u0451\u0437\u043d\u0430\u044f \u043f\u0440\u043e\u0431\u043b.", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 2: \u041c\u043e\u0447\u0438\u0442\u0441\u044f \u0432 \u0448\u0442\u0430\u043d\u044b/\u043f\u0430\u043c\u043f\u0435\u0440\u0441\u044b?", None))
        self.radioButton_218.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435 \u043f\u0440\u043e\u0431\u043b\u0435\u043c\u0430", None))
        self.radioButton_219.setText(QCoreApplication.translate("MainWindow", u"\u041b\u0451\u0433\u043a\u0430\u044f \u043f\u0440\u043e\u0431\u043b.", None))
        self.radioButton_220.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0440\u0435\u0434\u043d\u044f\u044f \u043f\u0440\u043e\u0431\u043b.", None))
        self.radioButton_221.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0435\u0440\u044c\u0451\u0437\u043d\u0430\u044f \u043f\u0440\u043e\u0431\u043b.", None))
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 3: \u041a\u0430\u043a\u0430\u0435\u0442 \u0432 \u0448\u0442\u0430\u043d\u044b/\u043f\u0430\u043c\u043f\u0435\u0440\u0441\u044b?", None))
        self.radioButton_214.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435 \u043f\u0440\u043e\u0431\u043b\u0435\u043c\u0430", None))
        self.radioButton_215.setText(QCoreApplication.translate("MainWindow", u"\u041b\u0451\u0433\u043a\u0430\u044f \u043f\u0440\u043e\u0431\u043b.", None))
        self.radioButton_216.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0440\u0435\u0434\u043d\u044f\u044f \u043f\u0440\u043e\u0431\u043b.", None))
        self.radioButton_217.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0435\u0440\u044c\u0451\u0437\u043d\u0430\u044f \u043f\u0440\u043e\u0431\u043b.", None))
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 4: \u041f\u043e\u043d\u043e\u0441\u044b?", None))
        self.radioButton_210.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435 \u043f\u0440\u043e\u0431\u043b\u0435\u043c\u0430", None))
        self.radioButton_211.setText(QCoreApplication.translate("MainWindow", u"\u041b\u0451\u0433\u043a\u0430\u044f \u043f\u0440\u043e\u0431\u043b.", None))
        self.radioButton_212.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0440\u0435\u0434\u043d\u044f\u044f \u043f\u0440\u043e\u0431\u043b.", None))
        self.radioButton_213.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0435\u0440\u044c\u0451\u0437\u043d\u0430\u044f \u043f\u0440\u043e\u0431\u043b.", None))
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 5: \u0417\u0430\u043f\u043e\u0440\u044b?", None))
        self.radioButton_206.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435 \u043f\u0440\u043e\u0431\u043b\u0435\u043c\u0430", None))
        self.radioButton_207.setText(QCoreApplication.translate("MainWindow", u"\u041b\u0451\u0433\u043a\u0430\u044f \u043f\u0440\u043e\u0431\u043b.", None))
        self.radioButton_208.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0440\u0435\u0434\u043d\u044f\u044f \u043f\u0440\u043e\u0431\u043b.", None))
        self.radioButton_209.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0435\u0440\u044c\u0451\u0437\u043d\u0430\u044f \u043f\u0440\u043e\u0431\u043b.", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 6: \u041f\u0440\u043e\u0431\u043b\u0435\u043c\u044b \u0441\u043e \u0441\u043d\u043e\u043c?", None))
        self.radioButton_202.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435 \u043f\u0440\u043e\u0431\u043b\u0435\u043c\u0430", None))
        self.radioButton_203.setText(QCoreApplication.translate("MainWindow", u"\u041b\u0451\u0433\u043a\u0430\u044f \u043f\u0440\u043e\u0431\u043b.", None))
        self.radioButton_204.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0440\u0435\u0434\u043d\u044f\u044f \u043f\u0440\u043e\u0431\u043b.", None))
        self.radioButton_205.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0435\u0440\u044c\u0451\u0437\u043d\u0430\u044f \u043f\u0440\u043e\u0431\u043b.", None))
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 7: \u0415\u0441\u0442 \u0441\u043b\u0438\u0448\u043a\u043e\u043c \u043c\u043d\u043e\u0433\u043e/\u0441\u043b\u0438\u0448\u043a\u043e\u043c \u043c\u0430\u043b\u043e?", None))
        self.radioButton_198.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435 \u043f\u0440\u043e\u0431\u043b\u0435\u043c\u0430", None))
        self.radioButton_199.setText(QCoreApplication.translate("MainWindow", u"\u041b\u0451\u0433\u043a\u0430\u044f \u043f\u0440\u043e\u0431\u043b.", None))
        self.radioButton_200.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0440\u0435\u0434\u043d\u044f\u044f \u043f\u0440\u043e\u0431\u043b.", None))
        self.radioButton_201.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0435\u0440\u044c\u0451\u0437\u043d\u0430\u044f \u043f\u0440\u043e\u0431\u043b.", None))
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 8: \u0415\u0441\u0442 \u043e\u0447\u0435\u043d\u044c \u043e\u0433\u0440\u0430\u043d\u0438\u0447\u0435\u043d\u043d\u044b\u0439 \u043d\u0430\u0431\u043e\u0440 \u043f\u0440\u043e\u0434\u0443\u043a\u0442\u043e\u0432?", None))
        self.radioButton_194.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435 \u043f\u0440\u043e\u0431\u043b\u0435\u043c\u0430", None))
        self.radioButton_195.setText(QCoreApplication.translate("MainWindow", u"\u041b\u0451\u0433\u043a\u0430\u044f \u043f\u0440\u043e\u0431\u043b.", None))
        self.radioButton_196.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0440\u0435\u0434\u043d\u044f\u044f \u043f\u0440\u043e\u0431\u043b.", None))
        self.radioButton_197.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0435\u0440\u044c\u0451\u0437\u043d\u0430\u044f \u043f\u0440\u043e\u0431\u043b.", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 9: \u0413\u0438\u043f\u0435\u0440\u0430\u043a\u0442\u0438\u0432\u043d\u043e\u0441\u0442\u044c?", None))
        self.radioButton_190.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435 \u043f\u0440\u043e\u0431\u043b\u0435\u043c\u0430", None))
        self.radioButton_191.setText(QCoreApplication.translate("MainWindow", u"\u041b\u0451\u0433\u043a\u0430\u044f \u043f\u0440\u043e\u0431\u043b.", None))
        self.radioButton_192.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0440\u0435\u0434\u043d\u044f\u044f \u043f\u0440\u043e\u0431\u043b.", None))
        self.radioButton_193.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0435\u0440\u044c\u0451\u0437\u043d\u0430\u044f \u043f\u0440\u043e\u0431\u043b.", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 10: \u0410\u043f\u043f\u0430\u0442\u0438\u044f?", None))
        self.radioButton_182.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435 \u043f\u0440\u043e\u0431\u043b\u0435\u043c\u0430", None))
        self.radioButton_183.setText(QCoreApplication.translate("MainWindow", u"\u041b\u0451\u0433\u043a\u0430\u044f \u043f\u0440\u043e\u0431\u043b.", None))
        self.radioButton_184.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0440\u0435\u0434\u043d\u044f\u044f \u043f\u0440\u043e\u0431\u043b.", None))
        self.radioButton_185.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0435\u0440\u044c\u0451\u0437\u043d\u0430\u044f \u043f\u0440\u043e\u0431\u043b.", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 11: \u0411\u044c\u0435\u0442 \u0438\u043b\u0438 \u0440\u0430\u043d\u0438\u0442 \u0441\u0430\u043c \u0441\u0435\u0431\u044f?", None))
        self.radioButton_186.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435 \u043f\u0440\u043e\u0431\u043b\u0435\u043c\u0430", None))
        self.radioButton_187.setText(QCoreApplication.translate("MainWindow", u"\u041b\u0451\u0433\u043a\u0430\u044f \u043f\u0440\u043e\u0431\u043b.", None))
        self.radioButton_188.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0440\u0435\u0434\u043d\u044f\u044f \u043f\u0440\u043e\u0431\u043b.", None))
        self.radioButton_189.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0435\u0440\u044c\u0451\u0437\u043d\u0430\u044f \u043f\u0440\u043e\u0431\u043b.", None))
        self.label_90.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 12: \u0411\u044c\u0435\u0442 \u0438\u043b\u0438 \u0440\u0430\u043d\u0438\u0442 \u0441\u0430\u043c \u0434\u0440\u0443\u0433\u0438\u0445?", None))
        self.radioButton_273.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435 \u043f\u0440\u043e\u0431\u043b\u0435\u043c\u0430", None))
        self.radioButton_274.setText(QCoreApplication.translate("MainWindow", u"\u041b\u0451\u0433\u043a\u0430\u044f \u043f\u0440\u043e\u0431\u043b.", None))
        self.radioButton_275.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0440\u0435\u0434\u043d\u044f\u044f \u043f\u0440\u043e\u0431\u043b.", None))
        self.radioButton_276.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0435\u0440\u044c\u0451\u0437\u043d\u0430\u044f \u043f\u0440\u043e\u0431\u043b.", None))
        self.label_89.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 13: \u041b\u043e\u043c\u0430\u0435\u0442 \u0438 \u0440\u0430\u0437\u0431\u0440\u0430\u0441\u044b\u0432\u0430\u0435\u0442 \u0432\u0441\u0435 \u0432\u043e\u043a\u0440\u0443\u0433?", None))
        self.radioButton_269.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435 \u043f\u0440\u043e\u0431\u043b\u0435\u043c\u0430", None))
        self.radioButton_270.setText(QCoreApplication.translate("MainWindow", u"\u041b\u0451\u0433\u043a\u0430\u044f \u043f\u0440\u043e\u0431\u043b.", None))
        self.radioButton_271.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0440\u0435\u0434\u043d\u044f\u044f \u043f\u0440\u043e\u0431\u043b.", None))
        self.radioButton_272.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0435\u0440\u044c\u0451\u0437\u043d\u0430\u044f \u043f\u0440\u043e\u0431\u043b.", None))
        self.label_88.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 14: \u0427\u0443\u0432\u0441\u0442\u0432\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c \u043a \u0437\u0432\u0443\u043a\u0430\u043c?", None))
        self.radioButton_265.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435 \u043f\u0440\u043e\u0431\u043b\u0435\u043c\u0430", None))
        self.radioButton_266.setText(QCoreApplication.translate("MainWindow", u"\u041b\u0451\u0433\u043a\u0430\u044f \u043f\u0440\u043e\u0431\u043b.", None))
        self.radioButton_267.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0440\u0435\u0434\u043d\u044f\u044f \u043f\u0440\u043e\u0431\u043b.", None))
        self.radioButton_268.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0435\u0440\u044c\u0451\u0437\u043d\u0430\u044f \u043f\u0440\u043e\u0431\u043b.", None))
        self.label_87.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 15: \u0422\u0440\u0435\u0432\u043e\u0436\u043d\u043e\u0441\u0442\u044c/\u0441\u0442\u0440\u0430\u0445?", None))
        self.radioButton_261.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435 \u043f\u0440\u043e\u0431\u043b\u0435\u043c\u0430", None))
        self.radioButton_262.setText(QCoreApplication.translate("MainWindow", u"\u041b\u0451\u0433\u043a\u0430\u044f \u043f\u0440\u043e\u0431\u043b.", None))
        self.radioButton_263.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0440\u0435\u0434\u043d\u044f\u044f \u043f\u0440\u043e\u0431\u043b.", None))
        self.radioButton_264.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0435\u0440\u044c\u0451\u0437\u043d\u0430\u044f \u043f\u0440\u043e\u0431\u043b.", None))
        self.label_86.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 16: \u041f\u043e\u0434\u0430\u0432\u043b\u0435\u043d\u043d\u043e\u0441\u0442\u044c/\u0441\u043b\u0435\u0437\u044b?", None))
        self.radioButton_257.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435 \u043f\u0440\u043e\u0431\u043b\u0435\u043c\u0430", None))
        self.radioButton_258.setText(QCoreApplication.translate("MainWindow", u"\u041b\u0451\u0433\u043a\u0430\u044f \u043f\u0440\u043e\u0431\u043b.", None))
        self.radioButton_259.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0440\u0435\u0434\u043d\u044f\u044f \u043f\u0440\u043e\u0431\u043b.", None))
        self.radioButton_260.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0435\u0440\u044c\u0451\u0437\u043d\u0430\u044f \u043f\u0440\u043e\u0431\u043b.", None))
        self.label_85.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 17: \u041f\u0440\u0438\u043f\u0430\u0434\u043a\u0438?", None))
        self.radioButton_253.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435 \u043f\u0440\u043e\u0431\u043b\u0435\u043c\u0430", None))
        self.radioButton_254.setText(QCoreApplication.translate("MainWindow", u"\u041b\u0451\u0433\u043a\u0430\u044f \u043f\u0440\u043e\u0431\u043b.", None))
        self.radioButton_255.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0440\u0435\u0434\u043d\u044f\u044f \u043f\u0440\u043e\u0431\u043b.", None))
        self.radioButton_256.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0435\u0440\u044c\u0451\u0437\u043d\u0430\u044f \u043f\u0440\u043e\u0431\u043b.", None))
        self.label_84.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 18: \u041d\u0430\u0432\u044f\u0437\u0447\u0438\u0432\u0430\u044f \u0440\u0435\u0447\u044c?", None))
        self.radioButton_249.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435 \u043f\u0440\u043e\u0431\u043b\u0435\u043c\u0430", None))
        self.radioButton_250.setText(QCoreApplication.translate("MainWindow", u"\u041b\u0451\u0433\u043a\u0430\u044f \u043f\u0440\u043e\u0431\u043b.", None))
        self.radioButton_251.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0440\u0435\u0434\u043d\u044f\u044f \u043f\u0440\u043e\u0431\u043b.", None))
        self.radioButton_252.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0435\u0440\u044c\u0451\u0437\u043d\u0430\u044f \u043f\u0440\u043e\u0431\u043b.", None))
        self.label_83.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 19: \u041d\u0435\u0438\u0437\u043c\u0435\u043d\u043d\u044b\u0439 \u043f\u043e\u0440\u044f\u0434\u043e\u043a \u0434\u0435\u0439\u0441\u0442\u0432\u0438\u0439?", None))
        self.radioButton_245.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435 \u043f\u0440\u043e\u0431\u043b\u0435\u043c\u0430", None))
        self.radioButton_246.setText(QCoreApplication.translate("MainWindow", u"\u041b\u0451\u0433\u043a\u0430\u044f \u043f\u0440\u043e\u0431\u043b.", None))
        self.radioButton_247.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0440\u0435\u0434\u043d\u044f\u044f \u043f\u0440\u043e\u0431\u043b.", None))
        self.radioButton_248.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0435\u0440\u044c\u0451\u0437\u043d\u0430\u044f \u043f\u0440\u043e\u0431\u043b.", None))
        self.label_81.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 20: \u0412\u043e\u043f\u043b\u0438 \u0438 \u043a\u0440\u0438\u043a\u0438?", None))
        self.radioButton_241.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435 \u043f\u0440\u043e\u0431\u043b\u0435\u043c\u0430", None))
        self.radioButton_242.setText(QCoreApplication.translate("MainWindow", u"\u041b\u0451\u0433\u043a\u0430\u044f \u043f\u0440\u043e\u0431\u043b.", None))
        self.radioButton_243.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0440\u0435\u0434\u043d\u044f\u044f \u043f\u0440\u043e\u0431\u043b.", None))
        self.radioButton_244.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0435\u0440\u044c\u0451\u0437\u043d\u0430\u044f \u043f\u0440\u043e\u0431\u043b.", None))
        self.label_80.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 21: \u041f\u043e\u0442\u0440\u0435\u0431\u043d\u043e\u0441\u0442\u044c \u0432 \u043e\u0434\u043d\u043e\u043e\u0431\u0440\u0430\u0437\u0438\u0438?", None))
        self.radioButton_237.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435 \u043f\u0440\u043e\u0431\u043b\u0435\u043c\u0430", None))
        self.radioButton_238.setText(QCoreApplication.translate("MainWindow", u"\u041b\u0451\u0433\u043a\u0430\u044f \u043f\u0440\u043e\u0431\u043b.", None))
        self.radioButton_239.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0440\u0435\u0434\u043d\u044f\u044f \u043f\u0440\u043e\u0431\u043b.", None))
        self.radioButton_240.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0435\u0440\u044c\u0451\u0437\u043d\u0430\u044f \u043f\u0440\u043e\u0431\u043b.", None))
        self.label_79.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 22: \u041f\u043e\u0441\u0442\u043e\u044f\u043d\u043d\u0430\u044f \u0432\u043e\u0437\u0431\u0443\u0436\u0434\u0435\u043d\u043d\u043e\u0441\u0442\u044c?", None))
        self.radioButton_233.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435 \u043f\u0440\u043e\u0431\u043b\u0435\u043c\u0430", None))
        self.radioButton_234.setText(QCoreApplication.translate("MainWindow", u"\u041b\u0451\u0433\u043a\u0430\u044f \u043f\u0440\u043e\u0431\u043b.", None))
        self.radioButton_235.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0440\u0435\u0434\u043d\u044f\u044f \u043f\u0440\u043e\u0431\u043b.", None))
        self.radioButton_236.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0435\u0440\u044c\u0451\u0437\u043d\u0430\u044f \u043f\u0440\u043e\u0431\u043b.", None))
        self.label_78.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 23: \u041d\u0435\u0447\u0443\u0432\u0441\u0442\u0432\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c \u043a \u0431\u043e\u043b\u0438?", None))
        self.radioButton_229.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435 \u043f\u0440\u043e\u0431\u043b\u0435\u043c\u0430", None))
        self.radioButton_230.setText(QCoreApplication.translate("MainWindow", u"\u041b\u0451\u0433\u043a\u0430\u044f \u043f\u0440\u043e\u0431\u043b.", None))
        self.radioButton_231.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0440\u0435\u0434\u043d\u044f\u044f \u043f\u0440\u043e\u0431\u043b.", None))
        self.radioButton_232.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0435\u0440\u044c\u0451\u0437\u043d\u0430\u044f \u043f\u0440\u043e\u0431\u043b.", None))
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 24: \u041a\u043e\u043d\u0446\u0435\u043d\u0442\u0440\u0430\u0446\u0438\u044f \u043d\u0430 \u043e\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u043d\u044b\u0445 \u043f\u0440\u0435\u0434\u043c\u0435\u0442\u0430\u0445/\u0442\u0435\u043c\u0430\u0445?", None))
        self.radioButton_222.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435 \u043f\u0440\u043e\u0431\u043b\u0435\u043c\u0430", None))
        self.radioButton_226.setText(QCoreApplication.translate("MainWindow", u"\u041b\u0451\u0433\u043a\u0430\u044f \u043f\u0440\u043e\u0431\u043b.", None))
        self.radioButton_227.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0440\u0435\u0434\u043d\u044f\u044f \u043f\u0440\u043e\u0431\u043b.", None))
        self.radioButton_228.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0435\u0440\u044c\u0451\u0437\u043d\u0430\u044f \u043f\u0440\u043e\u0431\u043b.", None))
        self.block3.setTitle(QCoreApplication.translate("MainWindow", u"III. \u0421\u0435\u043d\u0441\u043e\u0440\u043d\u044b\u0435 \u043d\u0430\u0432\u044b\u043a\u0438/\u041f\u043e\u0437\u043d\u0430\u0432\u0430\u0442\u0435\u043b\u044c\u043d\u044b\u0435 \u0441\u043f\u043e\u0441\u043e\u0431\u043d\u043e\u0441\u0442\u0438", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 1: \u041e\u0442\u043a\u043b\u0438\u043a\u0430\u0435\u0442\u0441\u044f \u043d\u0430 \u0441\u043e\u0431\u0441\u0442\u0432\u0435\u043d\u043d\u043e\u0435 \u0438\u043c\u044f?", None))
        self.radioButton_106.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430", None))
        self.radioButton_107.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u043e\u0433\u0434\u0430", None))
        self.radioButton_108.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0442", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 2: \u0420\u0435\u0430\u0433\u0438\u0440\u0443\u0435\u0442 \u043d\u0430 \u043f\u043e\u0445\u0432\u0430\u043b\u0443?", None))
        self.radioButton_154.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430", None))
        self.radioButton_155.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u043e\u0433\u0434\u0430", None))
        self.radioButton_156.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0442", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 3: \u0421\u043c\u043e\u0442\u0440\u0438\u0442 \u043d\u0430 \u043b\u044e\u0434\u0435\u0439 \u0438 \u0436\u0438\u0432\u043e\u0442\u043d\u044b\u0445?", None))
        self.radioButton_124.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430", None))
        self.radioButton_125.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u043e\u0433\u0434\u0430", None))
        self.radioButton_126.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0442", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 4: \u0421\u043c\u043e\u0442\u0440\u0438\u0442 \u043d\u0430 \u043a\u0430\u0440\u0442\u0438\u043d\u043a\u0438 (\u0438 \u0442\u0435\u043b\u0435\u0432\u0438\u0437\u043e\u0440)?", None))
        self.radioButton_157.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430", None))
        self.radioButton_158.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u043e\u0433\u0434\u0430", None))
        self.radioButton_159.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0442", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 5: \u0423\u043c\u0435\u0435\u0442 \u0440\u0438\u0441\u043e\u0432\u0430\u0442\u044c, \u0440\u0430\u0441\u043a\u0440\u0430\u0448\u0438\u0432\u0430\u0442\u044c, \u043c\u0430\u0441\u0442\u0435\u0440\u0438\u0442\u044c?", None))
        self.radioButton_160.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430", None))
        self.radioButton_161.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u043e\u0433\u0434\u0430", None))
        self.radioButton_162.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0442", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 6: \u041f\u0440\u0430\u0432\u0438\u043b\u044c\u043d\u043e \u0438\u0433\u0440\u0430\u0435\u0442 \u0441 \u0438\u0433\u0440\u0443\u0448\u043a\u0430\u043c\u0438?", None))
        self.radioButton_121.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430", None))
        self.radioButton_122.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u043e\u0433\u0434\u0430", None))
        self.radioButton_123.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0442", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 7: \u0412\u044b\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u043b\u0438\u0446\u0430 \u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0443\u0435\u0442 \u0441\u0438\u0442\u0443\u0430\u0446\u0438\u0438?", None))
        self.radioButton_109.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430", None))
        self.radioButton_110.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u043e\u0433\u0434\u0430", None))
        self.radioButton_111.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0442", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 8: \u041f\u043e\u043d\u0438\u043c\u0430\u0435\u0442 \u043f\u0440\u043e\u0438\u0441\u0445\u043e\u0434\u044f\u0449\u0435\u0435 \u043d\u0430 \u0442\u0435\u043b\u0435\u044d\u043a\u0440\u0430\u043d\u0435?", None))
        self.radioButton_133.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430", None))
        self.radioButton_134.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u043e\u0433\u0434\u0430", None))
        self.radioButton_135.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0442", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 9: \u041f\u043e\u043d\u0438\u043c\u0430\u0435\u0442 \u043e\u0431\u044a\u044f\u0441\u043d\u0435\u043d\u0438\u044f?", None))
        self.radioButton_112.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430", None))
        self.radioButton_113.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u043e\u0433\u0434\u0430", None))
        self.radioButton_114.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0442", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 10: \u041e\u0441\u043e\u0437\u043d\u0430\u0435\u0442 \u043e\u043a\u0440\u0443\u0436\u0430\u044e\u0449\u0443\u044e \u0441\u0440\u0435\u0434\u0443?", None))
        self.radioButton_130.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430", None))
        self.radioButton_131.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u043e\u0433\u0434\u0430", None))
        self.radioButton_132.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0442", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 11 :  \u041e\u0441\u043e\u0437\u043d\u0430\u0435\u0442 \u043e\u043f\u0430\u0441\u043d\u043e\u0441\u0442\u044c?", None))
        self.radioButton_136.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430", None))
        self.radioButton_137.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u043e\u0433\u0434\u0430", None))
        self.radioButton_138.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0442", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 12: \u041f\u0440\u043e\u044f\u0432\u043b\u044f\u0435\u0442 \u0432\u043e\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435?", None))
        self.radioButton_118.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430", None))
        self.radioButton_119.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u043e\u0433\u0434\u0430", None))
        self.radioButton_120.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0442", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 13: \u041f\u0440\u043e\u044f\u0432\u043b\u044f\u0435\u0442 \u0438\u043d\u0438\u0446\u0438\u0430\u0442\u0438\u0432\u0443?", None))
        self.radioButton_139.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430", None))
        self.radioButton_140.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u043e\u0433\u0434\u0430", None))
        self.radioButton_141.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0442", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 14: \u0423\u043c\u0435\u0435\u0442 \u0441\u0430\u043c\u043e\u0441\u0442\u043e\u044f\u0442\u0435\u043b\u044c\u043d\u043e \u043e\u0434\u0435\u0432\u0430\u0442\u044c\u0441\u044f?", None))
        self.radioButton_151.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430", None))
        self.radioButton_152.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u043e\u0433\u0434\u0430", None))
        self.radioButton_153.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0442", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 15: \u041f\u0440\u043e\u044f\u0432\u043b\u044f\u0435\u0442 \u043b\u044e\u0431\u043e\u043f\u044b\u0442\u0441\u0442\u0432\u043e, \u0437\u0430\u0438\u043d\u0442\u0435\u0440\u0435\u0441\u043e\u0432\u0430\u043d\u043d\u043e\u0441\u0442\u044c?", None))
        self.radioButton_163.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430", None))
        self.radioButton_164.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u043e\u0433\u0434\u0430", None))
        self.radioButton_165.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0442", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 16: \u0421\u043c\u0435\u043b\u044b\u0439 \u2014 \u0438\u0441\u0441\u043b\u0435\u0434\u0443\u0435\u0442 \u043e\u043a\u0440\u0443\u0436\u0430\u044e\u0449\u0435\u0435?", None))
        self.radioButton_115.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430", None))
        self.radioButton_116.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u043e\u0433\u0434\u0430", None))
        self.radioButton_117.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0442", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 17: \u0410\u0434\u0435\u043a\u0432\u0430\u0442\u043d\u043e \u0432\u043e\u0441\u043f\u0440\u0438\u043d\u0438\u043c\u0430\u0435\u0442 \u043e\u043a\u0440\u0443\u0436\u0430\u044e\u0449\u0435\u0435, \u043d\u0435 \u0443\u0445\u043e\u0434\u0438\u0442 \u0432 \u0441\u0435\u0431\u044f?", None))
        self.radioButton_127.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430", None))
        self.radioButton_128.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u043e\u0433\u0434\u0430", None))
        self.radioButton_129.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0442", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 18: \u0421\u043c\u043e\u0442\u0440\u0438\u0442 \u0442\u0443\u0434\u0430, \u043a\u0443\u0434\u0430 \u0441\u043c\u043e\u0442\u0440\u044f\u0442 \u0434\u0440\u0443\u0433\u0438\u0435?", None))
        self.radioButton_145.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430", None))
        self.radioButton_146.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u043e\u0433\u0434\u0430", None))
        self.radioButton_147.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0442", None))
        self.block1.setTitle(QCoreApplication.translate("MainWindow", u"I. \u0420\u0435\u0447\u044c/\u042f\u0437\u044b\u043a/\u041a\u043e\u043c\u043c\u0443\u043d\u0438\u043a\u0430\u0442\u0438\u0432\u043d\u044b\u0435 \u043d\u0430\u0432\u044b\u043a\u0438", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 11 : \u0420\u0435\u0447\u044c \u0447\u0430\u0449\u0435 \u0432\u0441\u0435\u0433\u043e \u043e\u0441\u043c\u044b\u0441\u043b\u0435\u043d\u043d\u0430/\u043b\u043e\u0433\u0438\u0447\u043d\u0430", None))
        self.radioButton_25.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430", None))
        self.radioButton_26.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u043e\u0433\u0434\u0430", None))
        self.radioButton_27.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0442", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 1: \u0417\u043d\u0430\u0435\u0442 \u0441\u043e\u0431\u0441\u0442\u0432\u0435\u043d\u043d\u043e\u0435 \u0438\u043c\u044f?", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u043e\u0433\u0434\u0430", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0442", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 10: \u0417\u0430\u0434\u0430\u0435\u0442 \u043e\u0441\u043c\u044b\u0441\u043b\u0435\u043d\u043d\u044b\u0435 \u0432\u043e\u043f\u0440\u043e\u0441\u044b?", None))
        self.radioButton_28.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430", None))
        self.radioButton_29.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u043e\u0433\u0434\u0430", None))
        self.radioButton_30.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0442", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 9: \u041e\u0431\u044a\u044f\u0441\u043d\u044f\u0435\u0442, \u0447\u0442\u043e \u043e\u043d/\u043e\u043d\u0430 \u0445\u043e\u0447\u0435\u0442?", None))
        self.radioButton_31.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430", None))
        self.radioButton_32.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u043e\u0433\u0434\u0430", None))
        self.radioButton_33.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0442", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 14: \u0418\u043c\u0435\u0435\u0442 \u043d\u043e\u0440\u043c\u0430\u043b\u044c\u043d\u044b\u0435 \u043a\u043e\u043c\u043c\u0443\u043d\u0438\u043a\u0430\u0442\u0438\u0432\u043d\u044b\u0435 \u043d\u0430\u0432\u044b\u043a\u0438 \u0434\u043b\u044f \u0441\u0432\u043e\u0435\u0433\u043e \u0432\u043e\u0437\u0440\u0430\u0441\u0442\u0430?", None))
        self.radioButton_34.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430", None))
        self.radioButton_35.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u043e\u0433\u0434\u0430", None))
        self.radioButton_36.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0442", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 2: \u0420\u0435\u0430\u0433\u0438\u0440\u0443\u0435\u0442 \u043d\u0430 \u2018\u043d\u0435\u0442\u2019 \u0438\u043b\u0438 \u2018\u0441\u0442\u043e\u043f\u2019?", None))
        self.radioButton_4.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430", None))
        self.radioButton_5.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u043e\u0433\u0434\u0430", None))
        self.radioButton_6.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0442", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 3: \u041c\u043e\u0436\u0435\u0442 \u0432\u044b\u043f\u043e\u043b\u043d\u044f\u0442\u044c \u043d\u0435\u043a\u043e\u0442\u043e\u0440\u044b\u0435 \u043a\u043e\u043c\u0430\u043d\u0434\u044b?", None))
        self.radioButton_7.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430", None))
        self.radioButton_8.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u043e\u0433\u0434\u0430", None))
        self.radioButton_9.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0442", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 4: \u041c\u043e\u0436\u0435\u0442 \u0441\u043a\u0430\u0437\u0430\u0442\u044c \u043e\u0434\u043d\u043e \u0441\u043b\u043e\u0432\u043e?", None))
        self.radioButton_10.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430", None))
        self.radioButton_11.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u043e\u0433\u0434\u0430", None))
        self.radioButton_12.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0442", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 5: \u041c\u043e\u0436\u0435\u0442 \u0441\u043a\u0430\u0437\u0430\u0442\u044c 2 \u0441\u043b\u043e\u0432\u0430 \u043f\u043e\u0434\u0440\u044f\u0434?", None))
        self.radioButton_13.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430", None))
        self.radioButton_14.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u043e\u0433\u0434\u0430", None))
        self.radioButton_15.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0442", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 6: \u041c\u043e\u0436\u0435\u0442 \u0441\u043a\u0430\u0437\u0430\u0442\u044c 2 \u0441\u043b\u043e\u0432\u0430 \u043f\u043e\u0434\u0440\u044f\u0434?", None))
        self.radioButton_16.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430", None))
        self.radioButton_17.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u043e\u0433\u0434\u0430", None))
        self.radioButton_18.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0442", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 7: \u0417\u043d\u0430\u0435\u0442 10 \u0438\u043b\u0438 \u0431\u043e\u043b\u044c\u0448\u0435 \u0441\u043b\u043e\u0432?", None))
        self.radioButton_19.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430", None))
        self.radioButton_20.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u043e\u0433\u0434\u0430", None))
        self.radioButton_21.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0442", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 8: \u0418\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0435\u0442 \u0432 \u0440\u0435\u0447\u0438 \u043f\u0440\u0435\u0434\u043b\u043e\u0436\u0435\u043d\u0438\u044f \u0438\u0437 4 \u0438 \u0431\u043e\u043b\u0435\u0435 \u0441\u043b\u043e\u0432?", None))
        self.radioButton_22.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430", None))
        self.radioButton_23.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u043e\u0433\u0434\u0430", None))
        self.radioButton_24.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0442", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 12: \u0427\u0430\u0441\u0442\u043e \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0435\u0442 \u043f\u0440\u0435\u0434\u043b\u043e\u0436\u0435\u043d\u0438\u044f, \u0432\u044b\u0441\u0442\u0440\u043e\u0435\u043d-\u043d\u044b\u0435 \u0432 \u043b\u043e\u0433\u0438\u0447\u0435\u0441\u043a\u043e\u0439 \u043f\u043e\u0441\u043b\u0435\u0434\u043e\u0432\u0430\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u0438", None))
        self.radioButton_43.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430", None))
        self.radioButton_44.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u043e\u0433\u0434\u0430", None))
        self.radioButton_45.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0442", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 13: \u041f\u043e\u0434\u0434\u0435\u0440\u0436\u0438\u0432\u0430\u0435\u0442 \u0440\u0430\u0437\u0433\u043e\u0432\u043e\u0440?", None))
        self.radioButton_37.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430", None))
        self.radioButton_38.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u043e\u0433\u0434\u0430", None))
        self.radioButton_39.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0442", None))
        self.warning.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0432\u0435\u0440\u0448\u0438\u0442\u0435  \u0442\u0435\u0441\u0442 \u0441 \u0441\u043e\u0445\u0440\u0430\u043d\u0435\u043d\u0438\u0435\u043c \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u043e\u0432, \u0435\u0441\u043b\u0438 \u0445\u043e\u0442\u0438\u0442\u0435, \u0447\u0442\u043e\u0431\u044b \u043e\u043d\u0438 \u0431\u044b\u043b\u0438 \u0437\u0430\u043f\u0438\u0441\u0430\u043d\u044b \u0432 \u043e\u0431\u0449\u0435\u0435 \u0434\u0435\u043b\u043e \u0440\u0435\u0431\u0451\u043d\u043a\u0430. \u0418\u043d\u0430\u0447\u0435 \u0432\u044b \u043c\u043e\u0436\u0435\u0442\u0435 \u0432\u044b\u0439\u0442\u0438 \u0431\u0435\u0437 \u0441\u043e\u0445\u0440\u0430\u043d\u0435\u043d\u0438\u044f.\u2028\u2028\u041f\u043e\u0441\u043b\u0435 \u0437\u0430\u0432\u0435\u0440\u0448\u0435\u043d\u0438\u044f \u0441 \u0441\u043e\u0445\u0440\u0430\u043d\u0435\u043d\u0438\u0435\u043c \u0432\u0430\u043c \u0431\u0443\u0434\u0435\u0442 \u043f\u0440\u0435\u0434\u043b\u043e\u0436\u0435\u043d\u043e \u043e\u0437\u043d\u0430\u043a"
                        "\u043e\u043c\u0438\u0442\u044c\u0441\u044f \u0441 \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u0430\u043c\u0438 \u0442\u0435\u0441\u0442\u0430.", None))
        self.exitWithoutSave_button.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0439\u0442\u0438 \u0431\u0435\u0437 \u0441\u043e\u0445\u0440\u0430\u043d\u0435\u043d\u0438\u044f", None))
    # retranslateUi

