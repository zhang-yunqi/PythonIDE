# encoding: utf-8
import requests, sys
from PyQt5.Qt import *

app = QApplication(sys.argv)


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        self.setWindowTitle("get test")
        self.resize(300, 500)
        self.move(300, 200)
        self.set_up_ui()
        self.show()
        self.text_t = "+"

    def set_up_ui(self):
        self.and1 = QTextEdit(self)
        self.and1.move(10, 10)
        self.and1.setStyleSheet("font-size : 25px")
        text1 = QPushButton(self)
        text1.resize(40, 40)
        text1.setText("+")
        text1.move(10, 40)
        text1.setStyleSheet("font-size : 40px")
        text1.clicked.connect(self.t1)
        text2 = QPushButton(self)
        text2.resize(40, 40)
        text2.setText("-")
        text2.move(60, 40)
        text2.setStyleSheet("font-size : 40px")
        text2.clicked.connect(self.t2)
        text3 = QPushButton(self)
        text3.resize(40, 40)
        text3.setText("*")
        text3.move(110, 40)
        text3.setStyleSheet("font-size : 40px")
        text3.clicked.connect(self.t3)
        text4 = QPushButton(self)
        text4.resize(40, 40)
        text4.setText("/")
        text4.move(160, 40)
        text4.setStyleSheet("font-size : 40px")
        text4.clicked.connect(self.t4)
        self.and2 = QTextEdit(self)
        self.and2.move(10, 80)
        self.and2.setStyleSheet("font-size : 25px")
        button = QPushButton(self)
        button.move(10, 110)
        button.setText("=")
        button.setStyleSheet("font-size : 25px")
        button.clicked.connect(self.click)
        self.re = QLabel(self)
        self.re.move(10, 150)
        self.re.setText("")
        self.re.setStyleSheet("font-size : 25px")
        self.text = QLabel(self)
        self.text.resize(40, 40)
        self.text.setText("")
        self.text.move(120, 10)
        self.text.setStyleSheet("font-size : 40px")
        # print(self.text_t)

    def click(self):
        data = {"code": self.text_t, "num1": self.and1.toPlainText().encode("utf-8"),
                "num2": self.and2.toPlainText().encode("utf-8")}
        #print(data)
        url = "http://192.168.1.19"
        response = requests.get(url, data=data)
        answer = response.json()["answer"]
        self.re.setText(str(answer))

    def t1(self):
        self.text_t = "+"
        self.text.setText("+")
        #print(self.text_t)

    def t2(self):
        self.text_t = "-"
        self.text.setText("-")
        #print(self.text_t)

    def t3(self):
        self.text_t = "*"
        self.text.setText("*")
        #print(self.text_t)

    def t4(self):
        self.text_t = "/"
        self.text.setText("/")
        print("/")
        # print(self.ty)


ui = UI()
sys.exit(app.exec_())
