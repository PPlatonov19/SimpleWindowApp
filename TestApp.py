#подключение необходимых модулей и файлов
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QRadioButton, QMessageBox, QLineEdit
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont
from inStr import *
#создание первого окна
class FScreen(QWidget):
    #комплектация методов(удобство и практичность)
    def __init__(self):
        super().__init__()
        self.set_appear()#устанавливает внешний вид окна
        self.initUI()#создаёт и настраевает тексты, кнопки, строки и др.
        self.connects()#соединяет обозначения и задачи
        self.show()#отображает окно

    def set_appear(self):
        #название окна
        self.setWindowTitle(txt_title_1)
        #размеры
        self.resize(win_width, win_height)
    
    def initUI(self):
        #присвоение/отображение слов, предложений, обозначений
        self.text = QLabel(txt_hello, alignment = Qt.AlignCenter)#Align(место) - отвечает за расположение текста
        self.instruction1 = QLabel(txt_instruction, alignment = Qt.AlignCenter)#Center/Right/Left
        self.instruction2 = QLabel(txt_hint)
        self.button = QPushButton(txt_next)
        #добавление строчек ввода
        self.answer = QLineEdit(txt_hintanswer)
        #лайауты - отвечают за красивое размещение всего того, что вы сделали
        self.VLayout = QVBoxLayout()
        self.VLayout.addWidget(self.text)
        self.VLayout.addWidget(self.instruction1)
        self.VLayout.addWidget(self.instruction2)
        self.VLayout.addWidget(self.answer)
        self.VLayout.addWidget(self.button)
        self.setLayout(self.VLayout)

    def connects(self):
        #привязка задачи к кнопке в окне
        self.button.clicked.connect(self.next_win)
    #переход от одного окна к другому и передачу переменных
    def next_win(self):
        self.asd = SScreen(self.answer.text())
        self.hide()

#создание второго окна
class SScreen(QWidget):
    #комплектация методов(удобство и практичность)
    def __init__(self):
        super().__init__()
        self.answer = answer
        self.set_appear()#устанавливает внешний вид окна
        self.initUI()#создаёт и настраевает тексты, кнопки, строки и др.
        self.connects()#соединяет обозначения и задачи
        self.show()#отображает окно

    def set_appear(self):
        #название окна
        self.setWindowTitle(txt_title_2)
        #размеры
        self.resize(win_width, win_height)

    def initUI(self):
        #тексты
        self.text1 = QLabel(txt_1)
        self.text2 = QLabel(txt_2)
        self.answer_0 = QLabel(self.answer)
        #лайауты
        self.VLayout = QVBoxLayout()
        self.VLayout.addWidget(self.text1)
        self.VLayout.addWidget(self.answer_0)
        self.VLayout.addWidget(self.text2)
        self.setLayout(self.VLayout)

app = QApplication([])
mw = FScreen()
app.exec_()