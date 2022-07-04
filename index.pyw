from PyQt5 import uic
from PyQt5.Qt import *
import sys
import os
import subprocess
import platform
plat = platform.system().lower()

codeing = {"linux": "utf-8", "windows": "gbk"}
cmd = {"linux": "touch", "windows": "echo >"}
app = QApplication(sys.argv)
with open("datas", "r") as data:
    INPUTS = data.readline()[:-1]
    last_dir = data.readline()[:-1]
    python_path = data.readline()[:-1]


def save_data(INPUTS, last_dir):
    with open("datas", "w") as data:
        data.write(INPUTS+"\n")
        data.write(last_dir+"\n")
        data.write(python_path+"\n")


class Ins(QWidget):
    def __init__(self):
        super().__init__()
        global INPUTS, last_dir
        uic.loadUi("input.ui", self)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.enter.clicked.connect(self.set_input)
        self.inputs.setText(INPUTS)

    def set_input(self):
        global INPUTS, last_dir
        INPUTS = self.inputs.text()
        save_data(INPUTS, last_dir)
        self.close()


ins = Ins()


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


class Out(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("out.ui", self)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.x.clicked.connect(self.close)

    def out(self, output):
        self.outputing.setText(output)


out = Out()


class Ui(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('untitled.ui', self)
        self.open.clicked.connect(self.open_file)
        self.run.clicked.connect(self.run_file)
        self.setins.clicked.connect(self.setin)
        self.add.clicked.connect(self.add_file)
        m = QFontMetrics(self.code.font())
        self.code.setTabStopWidth(4*m.width(" "))

    def open_file(self):
        global last_dir
        self.directory = QFileDialog.getOpenFileName(
            self, "选取文件", last_dir, "*.py *.pyw")
        self.directory = self.directory[0]
        self.load_file()

    def run_file(self):
        with open(self.directory, "w")as codes:
            codes.write(self.code.toPlainText())
        if plat=="linux":
            re = subprocess.Popen([python_path+" "+self.directory+" "+INPUTS],
                              shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        else:
            re = subprocess.Popen("cd " + self.directory[:self.st]+" & "+python_path+" "+self.directory[self.st+1:]+" "+INPUTS,
                              shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        stdout, stderr = re.communicate()
        if re.returncode == 0:
            out.out(stdout.decode(codeing[plat]))
        else:
            out.out(stderr.decode(codeing[plat]))
        out.show()

    def setin(self):
        ins.show()

    def add_file(self):
        global FILE, last_dir
        self.directory = QFileDialog.getExistingDirectory(
            self, "选择文件夹", last_dir)
        last_dir = self.directory
        if self.directory == '':
            massage.show("请选择正确的文件")
        else:
            os.system("python ./add.py")
            with open("filename.txt", "r+")as name:
                title = name.read()
                if title[-3:] != ".py" or title[-4:] != ".pyw":
                    title += ".py"
                if title == '':

                    massage.show("请选择正确的文件")
                else:
                    self.directory += ("/"+title)
                    os.system(cmd[plat]+" "+self.directory)
                    self.load_file()

    def load_file(self):
        if self.directory == '':
            massage.show("请选择正确的文件")
        else:
            global last_dir, INPUTS
            self.st = 0
            for i in range(0, len(self.directory)):
                if self.directory[i] == '/':
                    self.st = i
            last_dir = self.directory[:self.st]
            save_data(INPUTS, last_dir)
            self.file_name.setText(str(self.directory[self.st+1:]))
            with open(self.directory, "r+") as codes:
                self.code.setText(codes.read())
            self.code.setEnabled(True)
            self.run.setEnabled(True)
            self.setins.setEnabled(True)


ui = Ui()
ui.show()

sys.exit(app.exec_())
