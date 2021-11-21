import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton, QLabel


class Calculator(QWidget):
    def __init__(self):
        super(Calculator, self).__init__()

        self.vbox = QVBoxLayout(self)
        self.hbox_input = QHBoxLayout()
        self.hbox_clear = QHBoxLayout()
        self.hbox_first = QHBoxLayout()
        self.hbox_second = QHBoxLayout()
        self.hbox_third = QHBoxLayout()
        self.hbox_fourth = QHBoxLayout()
        self.hbox_fifth = QHBoxLayout()
        self.hbox_result = QHBoxLayout()
        self.hbox_info = QHBoxLayout()

        self.vbox.addLayout(self.hbox_input)
        self.vbox.addLayout(self.hbox_clear)
        self.vbox.addLayout(self.hbox_first)
        self.vbox.addLayout(self.hbox_second)
        self.vbox.addLayout(self.hbox_third)
        self.vbox.addLayout(self.hbox_fourth)
        self.vbox.addLayout(self.hbox_fifth)
        self.vbox.addLayout(self.hbox_result)
        self.vbox.addLayout(self.hbox_info)

        self.input = QLineEdit(self)
        self.hbox_input.addWidget(self.input)

        self.b_c = QPushButton("CLEAR", self)
        self.hbox_clear.addWidget(self.b_c)

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

        self.b_multiply = QPushButton("*", self)
        self.hbox_third.addWidget(self.b_multiply)

        self.b_unminus = QPushButton("+/-", self)
        self.hbox_fourth.addWidget(self.b_unminus)

        self.b_0 = QPushButton("0", self)
        self.hbox_fourth.addWidget(self.b_0)

        self.b_point = QPushButton(".", self)
        self.hbox_fourth.addWidget(self.b_point)

        self.b_divide = QPushButton("/", self)
        self.hbox_fourth.addWidget(self.b_divide)

        self.b_result = QPushButton("=", self)
        self.hbox_result.addWidget(self.b_result)

        self.info = QLabel(self)
        self.hbox_info.addWidget(self.info)

        self.b_plus.clicked.connect(lambda: self._operation("+"))
        self.b_minus.clicked.connect(lambda: self._operation("-"))
        self.b_multiply.clicked.connect(lambda: self._operation("*"))
        self.b_divide.clicked.connect(lambda: self._operation("/"))
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

        self.b_point.clicked.connect(lambda: self._point())
        self.b_c.clicked.connect(self._clear)
        self.b_unminus.clicked.connect(lambda: self._uminus())

    def _button(self, param):
        line = self.input.text()
        self.info.setText("")
        self.input.setText(line + param)

    def _point(self):
        line = self.input.text()
        if "." in line:
            self.input.setText(line)
        else:
            if line == '':
                line = '0'
            self.input.setText(line + ".")

    def _uminus(self):
        line = self.input.text()
        try:
            if float(line) == 0.0:
                self.input.setText(line)
            else:
                self.input.setText("-" + line)
        except ValueError:
            self.info.setText("wrong input")


    def _clear(self):
        self.input.setText("")
        self.info.setText("")

    def _operation(self, op):
        try:
            self.num_1 = float(self.input.text())
        except ValueError:
            self.info.setText(str("wrong input"))
        else:
            self.op = op
            self.input.setText("")

    def _result(self):
        try:
            self.num_2 = float(self.input.text())
        except ValueError:
            self.info.setText(str("wrong input"))
        else:
            if self.op == "+":
                self.input.setText(str(self.num_1 + self.num_2))
            elif self.op == '-':
                self.input.setText(str(self.num_1 - self.num_2))
            elif self.op == '*':
                self.input.setText(str(self.num_1 * self.num_2))
            elif self.op == '/':
                try:
                    self.input.setText(str(self.num_1 / self.num_2))
                except ZeroDivisionError:
                    self.info.setText("cannot be divided by zero")
                    self.input.setText("")


app = QApplication(sys.argv)

win = Calculator()
win.show()

sys.exit(app.exec_())
