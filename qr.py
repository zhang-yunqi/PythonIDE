import sys,os,threading
from PyQt5 import uic
from PyQt5.Qt import *

app = QApplication(sys.argv)

class File(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("input.ui",self)
        self.setWindowFlags(Qt.FramelessWindowHint|Qt.WindowStaysOnTopHint)
        self.enter.clicked.connect(self.set_input)
    def set_input(self):
        with open("filename.txt","w+")as codes:
            codes.write(self.inputs.text())
        self.close()

files=File()

def opening():
    files.show()
    
t=threading.Thread(target=opening)
t.start()
t.join()
print(1)
sys.exit(app.exec_())
