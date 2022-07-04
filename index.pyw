from PyQt5 import uic
from PyQt5.Qt import *
import sys
import os,subprocess,platform,threading
plat = platform.system().lower()

codeing = {"linux": "utf-8", "windows": "gbk"}
cmd = {"linux": "touch", "windows": "echo #coding:utf-8 >"}
app = QApplication(sys.argv)
with open("datas", "r") as data:
    last_dir = data.readline()[:-1]
    python_path = data.readline()[:-1]

def save_data(last_dir):
    with open("datas", "w") as data:
        data.write(last_dir+"\n")
        data.write(python_path+"\n")

    def set_input(self):
        global last_dir
        save_data(last_dir)
        self.close()
        
class Massage(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("massage.ui", self)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.enter.clicked.connect(self.back)

    def back(self):
        self.close()

    def show(self, mess):
        self.massage.setText(mess)
        super().show()


massage = Massage()

class Ui(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('untitled.ui', self)
        self.open.clicked.connect(self.open_file)
        self.run.clicked.connect(self.run_file)
        self.add.clicked.connect(self.add_file)
        m = QFontMetrics(self.code.font())
        self.code.setTabStopWidth(4*m.width(" "))

    def open_file(self):
        global last_dir
        self.directory = QFileDialog.getOpenFileName(
            self, "选取文件", last_dir, "*.py *.pyw")
        self.directory = self.directory[0]
        self.load_file()
        with open(self.directory, "r+",encoding = " utf-8 ") as codes:
            self.code.setText(codes.read())
        self.code.setEnabled(True)
        self.run.setEnabled(True)
    def run_file(self):
        with open(self.directory, "w")as codes:
            codes.write(self.code.toPlainText())
        os.system("cmd/K python "+self.directory)

    def add_file(self):
        global FILE, last_dir,t
        self.directory = QFileDialog.getExistingDirectory(
            self, "选择文件夹", last_dir)
        last_dir = self.directory
        if self.directory == '':
            massage.show("请选择正确的文件")
        else:
            title, okPressed = QInputDialog.getText(self, "file name","file name:", QLineEdit.Normal, "")
            title = str(title)
            if title[-3:] != ".py" or title[-4:] != ".pyw":
                title += ".py"
            if okPressed==True:
                self.directory += ("/"+title)
                os.system(cmd[plat]+" "+self.directory)
                self.load_file()
            else:
                massage.show("请选择正确的文件")
            with open(self.directory, "r+") as codes:
                self.code.setText(codes.read())
            self.code.setEnabled(True)
            self.run.setEnabled(True)
                    

    def load_file(self):
        if self.directory == '':
            massage.show("请选择正确的文件")
        else:
            global last_dir
            self.st = 0
            for i in range(0, len(self.directory)):
                if self.directory[i] == '/':
                    self.st = i
            last_dir = self.directory[:self.st]
            save_data(last_dir)
            self.file_name.setText(str(self.directory[self.st+1:]))
            


ui = Ui()
ui.show()

sys.exit(app.exec_())
