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
    Py_Initialize();   //初始化

        if(!Py_IsInitialized())
            return;
        PyRun_SimpleString("print('hello python from Qt')");
    //QDebug(strTemp.toLatin1());
}

