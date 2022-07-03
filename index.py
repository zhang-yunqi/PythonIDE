from PyQt5 import uic
from PyQt5.Qt import *
import sys,os,subprocess
app = QApplication(sys.argv)
INPUTS=""
last_dir="./"
class Ins(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("input.ui",self)
        self.setWindowFlags(Qt.WindowMinMaxButtonsHint|Qt.FramelessWindowHint)
        self.enter.clicked.connect(self.set_input)
    def set_input(self):
            global INPUTS
            INPUTS=self.inputs.text()
            self.close()
        
            


ins=Ins()


class Out(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("out.ui",self)
        self.setWindowFlags(Qt.FramelessWindowHint|Qt.WindowMinMaxButtonsHint)
        self.x.clicked.connect(self.close)
    def out(self,output):
        self.outputing.setText(output)


out=Out()

class Ui(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('untitled.ui', self)
        self.open.clicked.connect(self.open_file)
        self.run.clicked.connect(self.run_file)
        self.setins.clicked.connect(self.setin)
        self.add.clicked.connect(self.add_file)
        m=QFontMetrics(self.code.font())
        self.code.setTabStopWidth(4*m.width(" "))

    def open_file(self):
        self.directory = QFileDialog.getOpenFileName(self,"选取文件","/","*.py")
        self.directory=self.directory[0]
        st=0
        for i in range(0,len(self.directory)):
            if self.directory[i]=='/':
                st=i
        self.file_name.setText(str(self.directory[st+1:]))
        with open(self.directory,"r+") as codes:
            self.code.setText(codes.read())
        self.directory = QFileDialog.getExistingDirectory(self,"选择文件夹",last_dir)
        self.code.setEnabled(True)
        self.run.setEnabled(True)
        self.setins.setEnabled(True)

    def run_file(self):
        with open(self.directory,"w")as codes:
            codes.write(self.code.toPlainText())
        re=subprocess.Popen(["python "+self.directory+" "+INPUTS],shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        #self.animation_run()
        stdout, stderr = re.communicate()
        if re.returncode ==0:
            out.out( strout.deode("utf-8"))
        else:
            out.out(stderr.decode("utf-8"))
        out.show()
    def setin(self):
        ins.show()
    def add_file(self):
        global FILE,last_dir
        self.directory = QFileDialog.getExistingDirectory(self,"选择文件夹",last_dir)
        last_dir=self.directory
        os.system("python ./add.py")
        with open("filename.txt","r")as name:
            self.directory+="/"
            self.directory+=name.read()
        os.system("touch "+self.directory)
        
        

ui=Ui()
ui.show()
    
sys.exit(app.exec_())
