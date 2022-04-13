#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QFile>
#include <QProcess>
#include <QStringList>

#undef slots
#include <cmath>
#include <Python.h>


#define slots Q_SLOTS
MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
}

MainWindow::~MainWindow()
{
    delete ui;
}


void MainWindow::on_pushButton_clicked()
{
    MainWindow::ui->textEdit_2->setText("");
    QString str = MainWindow::ui->textEdit->toPlainText();
    QFile out("test.py");
    if (out.open(QIODevice::WriteOnly|QIODevice::Text)){
        out.write(str.toUtf8());
        out.close();
    }
    QProcess p(0);
    p.start("cmd", QStringList()<<"/c"<<"python test.py");
    p.waitForStarted();
    p.waitForFinished();
    QString strTemp=QString::fromLocal8Bit(p.readAllStandardOutput());  //获得输出
    if(strTemp==""){
        strTemp=QString::fromLocal8Bit(p.readAllStandardError());
    }
    MainWindow::ui->textEdit_2->setText(strTemp);

    Py_Initialize();
       //如果初始化失败，返回
       if(!Py_IsInitialized())
       {
           qDebug()<<"erro1";
       }
       //加载模块，模块名称为myModule，就是myModule.py文件
       PyObject *pModule = PyImport_ImportModule("sum.py");
       //如果加载失败，则返回
       if(!pModule)
       {
           qDebug()<<"erro2";
       }
       //加载函数greatFunc
       PyObject * pFuncHello = PyObject_GetAttrString(pModule, "add");
       //如果失败则返回
       if(!pFuncHello)
       {
           qDebug()<<"erro3";
       }
       //调用函数
       PyObject_CallFunction(pFuncHello, NULL);
       //退出
       Py_Finalize();
}

