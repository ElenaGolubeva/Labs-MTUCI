import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton

# Создание класса
class Calculator(QWidget):
    def __init__(self):
        # Задание осей
        super(Calculator, self).__init__()
        self.vbox = QVBoxLayout(self)
        self.hbox_input = QHBoxLayout()
        self.hbox_first = QHBoxLayout()
        self.hbox_second = QHBoxLayout()
        self.hbox_third = QHBoxLayout()
        self.hbox_forth = QHBoxLayout()
        self.hbox_result = QHBoxLayout()

        self.vbox.addLayout(self.hbox_input)
        self.vbox.addLayout(self.hbox_first)
        self.vbox.addLayout(self.hbox_second)
        self.vbox.addLayout(self.hbox_third)
        self.vbox.addLayout(self.hbox_forth)
        self.vbox.addLayout(self.hbox_result)
        self.input = QLineEdit(self)
        self.hbox_input.addWidget(self.input)

        # Создание виджетов
        self.b_1 = QPushButton("1", self)
        self.hbox_first.addWidget(self.b_1)

        self.b_2 = QPushButton("2", self)
        self.hbox_first.addWidget(self.b_2)

        self.b_3 = QPushButton("3", self)
        self.hbox_first.addWidget(self.b_3)

        self.b_plus = QPushButton("+", self)
        self.hbox_first.addWidget(self.b_plus)

        self.b_4 = QPushButton("4", self)
        self.hbox_second.addWidget(self.b_4)

        self.b_5 = QPushButton("5", self)
        self.hbox_second.addWidget(self.b_5)

        self.b_6 = QPushButton("6", self)
        self.hbox_second.addWidget(self.b_6)

        self.b_minus = QPushButton("-", self)
        self.hbox_second.addWidget(self.b_minus)

        self.b_7 = QPushButton("7", self)
        self.hbox_third.addWidget(self.b_7)

        self.b_8 = QPushButton("8", self)
        self.hbox_third.addWidget(self.b_8)

        self.b_9 = QPushButton("9", self)
        self.hbox_third.addWidget(self.b_9)

        self.b_del = QPushButton("/", self)
        self.hbox_third.addWidget(self.b_del)

        self.b_clean = QPushButton("C", self)
        self.hbox_forth.addWidget(self.b_clean)

        self.b_0 = QPushButton("0", self)
        self.hbox_forth.addWidget(self.b_0)

        self.b_umn = QPushButton("*", self)
        self.hbox_forth.addWidget(self.b_umn)

        self.b_point = QPushButton(".", self)
        self.hbox_forth.addWidget(self.b_point)

        self.b_result = QPushButton("=", self)
        self.hbox_result.addWidget(self.b_result)
        # Нажатие на кнопки
        self.b_plus.clicked.connect(lambda: self._operation("+"))
        self.b_minus.clicked.connect(lambda: self._operation("-"))
        self.b_del.clicked.connect(lambda: self._operation("/"))
        self.b_umn.clicked.connect(lambda: self._operation("*"))
        self.b_clean.clicked.connect(self._clean)
        self.b_result.clicked.connect(self._result)

        self.b_1.clicked.connect(lambda: self._button("1"))
        self.b_2.clicked.connect(lambda: self._button("2"))
        self.b_3.clicked.connect(lambda: self._button("3"))
        self.b_4.clicked.connect(lambda: self._button("4"))
        self.b_5.clicked.connect(lambda: self._button("5"))
        self.b_6.clicked.connect(lambda: self._button("6"))
        self.b_7.clicked.connect(lambda: self._button("7"))
        self.b_8.clicked.connect(lambda: self._button("8"))
        self.b_9.clicked.connect(lambda: self._button("9"))
        self.b_0.clicked.connect(lambda: self._button("0"))
        self.b_point.clicked.connect(lambda: self._button("."))

    # Ввод в строку цифр
    def _button(self, param):
        line = self.input.text()
        self.input.setText(line + param)

    # Очищение строки
    def _clean(self):
        line = ""
        self.input.setText(line)

    # Ввод в строку математических операций
    def _operation(self, op):
        if self.input.text() == ".":
            self.input.setText(str('Error'))
        else:
            self.num_1 = float(self.input.text())
            self.op = op
            self.input.setText("")

    # Вывод результата
    def _result(self):
        self.num_2 = float(self.input.text())
        if self.op == "+":
            self.input.setText(str(self.num_1 + self.num_2))
        if self.op == "-":
            self.input.setText(str(self.num_1 - self.num_2))
        if self.op == "/":
            if self.num_2 == 0:
                self.input.setText(str('Error'))
            else:
                self.input.setText(str(self.num_1 / self.num_2))
        if self.op == "*":
            self.input.setText(str(self.num_1 * self.num_2))


app = QApplication(sys.argv)
win = Calculator()
win.show()
sys.exit(app.exec_())

