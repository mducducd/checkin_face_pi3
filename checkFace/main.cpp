#include "widget.h"
#include <QApplication>
#include <QProcess>
#include<QFileDialog>
#include <QTextStream>
#include <QMessageBox>
#include <debug/debug.h>
void reset(){
    QTextStream out(stdout);
    QString filename = "/home/pi/build-checkFace-Desktop-Debug/log_data/option.txt";
    QFile file(filename);
    if(file.open(QIODevice::WriteOnly))
    {
        QTextStream out(&file);
        out << "" << endl;
    }
    QTextStream out1(stdout);
    QString filename1 = "/home/pi/build-checkFace-Desktop-Debug/log_data/option.txt";
    QFile file1(filename1);
    if(file.open(QIODevice::WriteOnly))
    {
        QTextStream out(&file);
        out1 << "" << endl;
    }
}
void writeSwitch0()
{
    QTextStream out(stdout);
    QString filename = "/home/pi/build-checkFace-Desktop-Debug/log_data/switch.txt";
    QFile file(filename);
    if(file.open(QIODevice::WriteOnly))
    {
        QTextStream out(&file);
        out << "0" ;
    }

}
int main(int argc, char *argv[])
{
    reset();
    writeSwitch0();
    QApplication a(argc, argv);
    Widget w;
    w.setWindowFlags(Qt::Window | Qt::FramelessWindowHint);
    w.move(0,0);
    w.show();

    //hide mouse

    a.setOverrideCursor(QCursor(Qt::BlankCursor));

    //open camera
    QProcess process;
    process.setProcessChannelMode(QProcess::MergedChannels);
    QString exe = "python3 utils/main.py";
    process.start(exe);
    return a.exec();
}
