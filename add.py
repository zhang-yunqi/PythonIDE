import sys
from PyQt5 import uic
from PyQt5.Qt import *
app = QApplication(sys.argv)

class File(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("input.ui",self)
        self.setWindowFlags(Qt.WindowMinMaxButtonsHint|Qt.FramelessWindowHint)
        self.enter.clicked.connect(self.set_input)
    def set_input(self):
        with open("filename.txt","w+")as codes:
            codes.write(self.inputs.text())
        self.close()

files=File()
files.show()

sys.exit(app.exec_())