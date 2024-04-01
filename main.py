import sys

from PySide6.QtCore import QSize, Qt
# Импорт необходимых для работы классов
from PySide6.QtWidgets import QApplication, QMainWindow, QGroupBox, QRadioButton, QMessageBox

# Импорт необходимых нарисованных окон
from Teremok2_HelloWindow import Ui_TeremokFirstWindow
from Teremok2_MainWindow import Ui_MainWindow
from Teremok2_TestAtek impogit rt Ui_TestWindow
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
        # Объявление суммы баллов теста
        import functools
        ballResult = 0

        # 14 вопросов
        # 20 вопросов
        # 18 вопросов
        # 24 вопросов
        # да, иногда, нет = 2, 1, 0 соответственно
        # не проблема, лёг. проблема, ср.проблема, серьёзная проблема = 0, 1, 2, 3 соответственно

        # Ищем потомков типа QGroupBox(4 бокса с вопросами и сам бокс вопроса с ответами)
        childrens = self.findChildren(QGroupBox)
        # Блоки с вопросами
        questBlocks = []
        block1 = []
        block2 = []
        block3 = []
        block4 = []
        questBlocks.append(block1)
        questBlocks.append(block2)
        questBlocks.append(block3)
        questBlocks.append(block4)
        # Перебор найденных потомков QGroupBox
        # вопрос имеет название "block1_item02", где block1 - секция вопросов, item02 - номер вопроса
        for child in childrens:
            if "block1_" in child.objectName():
                block1.append(child)
            elif "block2_" in child.objectName():
                block2.append(child)
            elif "block3_" in child.objectName():
                block3.append(child)
            elif "block4_" in child.objectName():
                block4.append(child)

        # Сортировка листов вопросов по номеру вопроса
        def MyFunc(item):
            return int(item.objectName()[-2:])
        for block in questBlocks:
            block.sort(key=MyFunc)
        # block1.sort(key=MyFunc)
        # block2.sort(key=MyFunc)
        # block3.sort(key=MyFunc)
        # block4.sort(key=MyFunc)

        # ----------------------------------------------------------------- рабочий блок кода
        # Результаты ответов на вопросы
        # Например, 201 = 1 вопрос: Да, 2 вопрос: Нет, 3 вопрос: Иногда
        # блоки 1, 2, 3, 4
        for j in range(0, 4):
            curBlock = questBlocks[j]
            resStr = ""
            for i in range(0, len(curBlock)):
                # print(f'Вопрос {block1[i].objectName()}:')
                questionRadioButtons = curBlock[i].findChildren(QRadioButton)
                isQuestAnswered = False
                # Условие для 4ого блока вопросов из-за различия ответов на вопрос
                if j != 3:
                    # Перебор радиоКнопок в текущем вопросе
                    for radioButton in questionRadioButtons:
                        if radioButton.isChecked():
                            isQuestAnswered = True
                            if radioButton.text() == "Да":
                                resStr += "2"
                                # print(radioButton.text())
                            elif radioButton.text() == "Иногда":
                                resStr += "1"
                                # print(radioButton.text())
                            elif radioButton.text() == "Нет":
                                resStr += "0"
                                # print(radioButton.text())
                else:
                    # Перебор радиоКнопок в текущем вопросе
                    for radioButton in questionRadioButtons:
                        if radioButton.isChecked():
                            isQuestAnswered = True
                            if radioButton.text() == "Не проблема":
                                resStr += "0"
                                # print(radioButton.text())
                            elif radioButton.text() == "Лёгкая пробл.":
                                resStr += "1"
                                # print(radioButton.text())
                            elif radioButton.text() == "Средняя пробл.":
                                resStr += "2"
                                # print(radioButton.text())
                            elif radioButton.text() == "Серьёзная пробл.":
                                resStr += "3"
                                # print(radioButton.text())
                if not(isQuestAnswered):
                    #вызов диалогового окна
                    text = f'Блок {j+1}: не отвечен вопрос № {i+1}'
                    DialogMsg("Ошибка", text)
                    break
            if not(isQuestAnswered):
                break
            balls = functools.reduce(lambda a,b: int(a) + int(b), resStr)
            ballResult += balls
        # ----------------------------------------------------------------- рабочий блок кода

        # Если на все вопросы ответили
        if isQuestAnswered:
            # Закрытие окна тестирования
            self.close()
            # Открытие окна результатов тестирования с выведением количества баллов
            self.window = ResultsTestWindow()
            self.window.ui.results_QLE.setText(str(ballResult))
            self.window.show()

# Метод вызова диалогового окна
def DialogMsg(title, text):
    error = QMessageBox()
    error.setWindowTitle(title)
    error.setText(text)
    error.setIcon(QMessageBox.Warning)
    error.exec()

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
        resSum = int(self.ui.results_QLE.text())
        print(f'Распечатано. Ваш результат составляет: {resSum} баллов')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FirstWindow()
    window.show()

    sys.exit(app.exec())