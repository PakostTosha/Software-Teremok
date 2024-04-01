import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QGroupBox

from Teremok2_HelloWindow import Ui_TeremokFirstWindow
from Teremok2_MainWindow import Ui_MainWindow
from Teremok2_TestAtek import Ui_TestWindow
from Teremok2_ResultsTest import Ui_Form

class FirstWindow(QMainWindow):
    # Конструктор класса
    def __init__(self):
        # Позволяет QT настраивать
        super(FirstWindow, self).__init__()
        # Установка дизайна из файла
        self.ui = Ui_TeremokFirstWindow()
        self.ui.setupUi(self)

        # Закрытие первого окна по клику
        self.ui.close_button.clicked.connect(self.close_FirstWindow)
        # Открытие главного окна по клику
        self.ui.openSys_button.clicked.connect(self.open_MainWindow)

    # Функция закрытия окна
    def close_FirstWindow(self):
        self.close()
    # Функция открытия главного окна
    def open_MainWindow(self):
        self.close_FirstWindow()
        self.window = MainWindow()
        self.window.show()

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Открытие окна теста
        self.ui.startTest_button.clicked.connect(self.open_TestWindow)

    def open_TestWindow(self, s):
        self.window = TestWindow()
        self.window.show()

class TestWindow(QMainWindow):
    def __init__(self):
        super(TestWindow, self).__init__()
        self.ui = Ui_TestWindow()
        self.ui.setupUi(self)
        # Кнопка выйти без сохранения
        self.ui.exitWithoutSave_button.clicked.connect(self.close)
        # Кнопка подсчёта и сохранения результатов тестирования
        self.ui.saveData_button.clicked.connect(self.saveResultsTest)

    # Функция подсчёта и сохранения результатов тестирования
    def saveResultsTest(self):
        # Подсчёт результатов по блокам
        # 14 вопросов
        # 20 вопросов
        # 18 вопросов
        # 24 вопросов
        # да, иногда, нет = 2, 1, 0 соответственно
        # не проблема, лёг. проблема, ср.проблема, серьёзная проблема = 0, 1, 2, 3 соответственно
        sum = 0

        # Обработка одного вопроса
        if (self.ui.radioButton.isChecked()): sum += 1
        elif (self.ui.radioButton_2.isChecked()): sum += 2
        elif (self.ui.radioButton_3.isChecked()): sum += 3
        childrens = self.findChildren(QGroupBox)
        # print(childrens[0].title())
        block2 = []
        for child in childrens:
            block2.append(child)

        print(block2)



        # items = [QGroupBox for QGroupBox in self.findChildren(QGroupBox)]
        # for item in items:
        #     print(f'{item.objectName()} ---->{item.children()}')


        # Закрытие окна тестирования
        # self.close()
        # Открытие окна результатов тестирования с выведением количества баллов
        # self.window = ResultsTestWindow()
        # self.window.show()

class ResultsTestWindow(QMainWindow):
    def __init__(self):
        super(ResultsTestWindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # Кнопка OK, закрывающая результаты теста
        self.ui.OK_button.clicked.connect(self.close)
        # Кнопка Распечатать результаты, печатающая результаты теста
        self.ui.printResults_button.clicked.connect(self.printResults)

    def printResults(self):
        resSum = 15
        print("Распечатано. Ваш результат составляет: " + str(resSum) + " баллов")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FirstWindow()
    window.show()

    sys.exit(app.exec())