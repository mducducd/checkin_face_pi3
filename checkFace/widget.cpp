#include "widget.h"
#include "ui_widget.h"
#include<QFileDialog>
#include <QTextStream>
#include <QTime>
#include <QDate>
#include <QTimer>
#include <QProcess>
#include <QDebug>
#include <QMessageBox>
#include <QJsonDocument>
#include<QJsonArray>
#include<QJsonObject>
#include<QMovie>
#include<QFile>
#include "widget.h"
#include <QApplication>
//void readJson()
//   {
//      QString val;
//      QFile file;
//      file.setFileName("db.json");
//      file.open(QIODevice::ReadOnly | QIODevice::Text);
//      val = file.readAll();
//      file.close();
//      qWarning() << val;
//      QJsonDocument d = QJsonDocument::fromJson(val.toUtf8());
//      QJsonObject sett2 = d.object();
//      QJsonValue value = sett2.value(QString("appName"));
//      qDebug() << value;
//}
//void xoa(){
//    QTextStream out(stdout);
//    QString filename = "option.txt";
//    QFile file(filename);
//    if(file.open(QIODevice::WriteOnly))
//    {
//        QTextStream out(&file);
//        out << " ";
//    }
//}
//void writeJson(QString ID,QString NAME,QString TIME)
//{
//    // Open the 1.json file in the main directory by reading and writing. If the file does not exist, it will be created automatically.
//        QFile file("db.json");
//        if(!file.open(QIODevice::Append)) {
//            qDebug() << "File open error";
//        } else {
//            qDebug() <<"File open!";
//        }
//     // Insert a key-value pair using the QJsonObject object.
//        QJsonObject jsonObject;
//        jsonObject.insert("ID", ID);
//        jsonObject.insert("NAME", NAME);
//        jsonObject.insert("TIME", TIME);

//     // Set the json object using QJsonDocument
//        QJsonDocument jsonDoc;
//        jsonDoc.setObject(jsonObject);

//     // Write json to the file as text and close the file.
//        file.write(jsonDoc.toJson());
//        file.close();

//        qDebug() << "Write to file";


//}
//void no(){
//    QTextStream out(stdout);
//    QString filename = "/home/pi/build-checkFace-Desktop-Debug/log_data/option.txt";
//    QFile file(filename);
//    if(file.open(QIODevice::WriteOnly))
//    {
//        QTextStream out(&file);
//        out << "0";
//    }
//}
//void yes(){
//    QTextStream out(stdout);
//    QString filename = "/home/pi/build-checkFace-Desktop-Debug/log_data/option.txt";
//    QFile file(filename);
//    if(file.open(QIODevice::WriteOnly))
//    {
//        QTextStream out(&file);
//        out << "1";
//    }
//}
//void write(){
//    QTextStream out(stdout);
//    QString filename = "/home/pi/build-checkFace-Desktop-Debug/log_data/notification.txt";
//    QFile file(filename);
//    if(file.open(QIODevice::WriteOnly))
//    {
//        QTextStream out(&file);
//        out << "";
//    }
//}

//void Widget::on_yes_clicked()
//{
//    yes();
//}

//void Widget::on_no_clicked()
//{
//    no();
//}

//void writeSwitch()
//{
//    QTextStream out(stdout);
//    QString filename = "/home/pi/build-checkFace-Desktop-Debug/log_data/switch.txt";
//    QFile file(filename);
//    if(file.open(QIODevice::WriteOnly))
//    {
//        QTextStream out(&file);
//        out << "1" << endl;
//    }

//}


////time
//QTimer *timer;
//QTimer *timer_id_name;
//QString nhap;
//QString timeht;

////dangky
//void Widget::on_pushButton_clicked()
//{
////xoa();
//writeSwitch();
////ui->yes->show();
////ui->no->show();
// QTime dieTime = QTime::currentTime().addSecs(4000);
// while(QTime::currentTime() < dieTime)
//     QCoreApplication::processEvents(QEventLoop::AllEvents,100);

//}



////vantay
//void Widget::on_vantay_clicked()
//{

//}
////GUI
//Widget::Widget(QWidget *parent) :
//    QWidget(parent),
//    ui(new Ui::Widget)
//{

//    ui->setupUi(this);
//    ui->pushButton->hide();
//    ui->fp->hide();
//    ui->yes->hide();
//    ui->no->hide();
//    //add .gif
//    QMovie * movie = new QMovie("/home/pi/build-checkFace-Desktop-Debug/img2/WwUV.gif");
//    ui->label->setMovie(movie);
//   movie->start();



//   //set time hien tai


//    QTextStream out(stdout);
//    //set time
//       QDate cd = QDate::currentDate();
//       QTime ct = QTime::currentTime();
//       QString thu = timeht.mid(0,3);
//       if(thu == "Mon") thu = "Thứ Hai";
//       if(thu == "Tue") thu = "Thứ Ba";
//       if(thu == "Wed") thu = "Thứ Tư";
//       if(thu == "Thu") thu = "Thứ Năm";
//       if(thu == "Fri") thu = "Thứ Sáu";
//       if(thu == "Sat") thu = "Thứ Bảy";
//       if(thu == "Sun") thu = "Chủ Nhật";
//       QString date = QDate::currentDate().toString("dd.MM.yyyy");

//       ui->true_2->setText(thu+" "+date);
//       ui->boder->hide();
//       out << "Current date is: " << cd.toString() << endl;
//       out << "Current time is: " << ct.toString() << endl;
//       ui->pushButton->hide();
//       ui->fp->hide();
//       ui->comeBack->hide();

//     //load realtime
//       timer = new QTimer(this);
//       timer->setInterval(1000);
//       connect(timer,SIGNAL(timeout()),this,SLOT(timer_timeout()));
//       timer->start();
//       ui->id->setStyleSheet("color: rgb(0, 255, 0);\nfont: 16pt;");
//}

//    //funcition realtime++
//void Widget::timer_timeout(){
//      ui->id->setStyleSheet("color: rgb(0, 255, 0);\nfont: 16pt;");
////    QTextStream out(stdout);
//////    foreach(QString x,strings);
//////    QString sx= readAllStandardOutput();
//////    QString stderr= readAllStandardError();
////    qDebug() << "" << endl;
////    //out << stderr << endl;
//       ui->id->setCursor(Qt::BlankCursor);

//    //set time
//     ui->true_2->setStyleSheet("color: rgb(0, 255, 0);\nfont: 18pt;");
//     ui->time->setStyleSheet("color: rgb(0, 255, 0);\nfont: 18pt;");
//    QDate cd = QDate::currentDate();
//    QString ct = QTime::currentTime().toString("hh:mm");
//    ui->time->setText("  "+ct);
//    timeht= cd.toString();

//    //set thoi gian tieng viet
//    QString thu = timeht.mid(0,3);
//    if(thu == "Mon") thu = "Thứ Hai";
//    if(thu == "Tue") thu = "Thứ Ba";
//    if(thu == "Wed") thu = "Thứ Tư";
//    if(thu == "Thu") thu = "Thứ Năm";
//    if(thu == "Fri") thu = "Thứ Sáu";
//    if(thu == "Sat") thu = "Thứ Bảy";
//    if(thu == "Sun") thu = "Chủ Nhật";
//    QString date = QDate::currentDate().toString("dd.MM.yyyy");

//    ui->true_2->setText("  "+thu+" "+date);

//     //set id,name
//    QString data = "/home/pi/build-checkFace-Desktop-Debug/log_data/notification.txt";
//     QFile file (data);
//     if(!file.open(QFile::ReadOnly|QFile::Text))
//     {
//         QMessageBox::warning (this,"title","file not open");
//     }
//     QTextStream in (&file);
//     QString text = in.readAll();
//     QString dang_Ky_thanh_cong = text.right(6);

////     QString dataS = "/home/pi/build-checkFace-Desktop-Debug/log_data/switch.txt";
////      QFile fileS (dataS);
////      if(!fileS.open(QFile::ReadOnly|QFile::Text))
////      {
////          QMessageBox::warning (this,"title","file not open");
////      }
////      QTextStream inS (&fileS);
////      QString textS = inS.readAll();
////      QString dang_Ky_thanh_congS = text.right(6);


//     QString checkfalse = " không tim thấy ";
//     QString Nobody = "";
//     QString WarmUp = "vui lòng chờ";
//     QString Enroll = "Starting the Camera...";
//     QString noFace = "không phát hiện bất cứ khuôn mặt nào";
//     QString error = "lỗi, quay lại chế độ nhận dạng";
//     QString yesno = "ban muốn sử dụng ảnh này để đăng ký (y/n)?";
//     QString id ="ID";
//     QString deTayVaoCamBien ="vui lòng để tay vào cam biến";

////     ui->yes->hide();
////     ui->no->hide();




//     //3 truong hop
//     if (dang_Ky_thanh_cong == yesno)
//     {
//         ui->comeBack->hide();
//         ui->yes->show();
//         ui->no->hide();
//     }
//     if(text == checkfalse)
//     {
//         ui->comeBack->hide();
//         ui->yes->hide();
//         ui->no->hide();
//          ui->boder->show();
//            ui->id->setStyleSheet("color: rgb(255, 0, 0);\nfont: 16pt;");
//          ui->id->show();
//          ui->boder->setStyleSheet("border:11px solid rgb(255,0,0);");
//          ui->label->hide();
//          ui->pushButton->setText("Đăng ký");
//          ui->pushButton->show();
//          ui->fp->setText("FP");
//          ui->fp->show();
//          //ui->id->setStyleSheet("color: rgb(255, 0, 0);");
//          ui->id->setPlainText(text);


//     }
//     else if(text == Nobody)
//     {
//         ui->comeBack->hide();
//         write();
//         ui->pushButton->hide();
//         ui->fp->hide();
//         ui->yes->hide();
//         ui->no->hide();
//         ui->id->setStyleSheet("color: rgb(0, 255, 0);\nfont: 16pt;");
//         ui->id->setPlainText("vui lòng nhìn vào máy ảnh"+text);
//         ui->label->hide();
//         ui->boder->setStyleSheet("border:11px solid rgb(255,255,255);");
//         ui->boder->hide();



//     }
//    else if(text == WarmUp)
//     {
//         ui->comeBack->hide();
//         ui->pushButton->hide();
//         ui->fp->hide();
//         ui->yes->hide();
//         ui->no->hide();
//         ui->id->setStyleSheet("color: rgb(0, 255, 0);\nfont: 16pt;");
//            ui->id->show();
//            ui->boder->hide();
////            ui->id->setStyleSheet("color: rgb(0, 255, 0);");
//            ui->id->setPlainText(text);
//            ui->true_2->show();
//            ui->pushButton->hide();

//        }
//     else if (text == noFace)
//     {
//         ui->comeBack->hide();
//         ui->pushButton->show();
//         ui->fp->show();
//         ui->yes->hide();
//         ui->no->hide();
//         ui->id->setStyleSheet("color: rgb(0, 255, 0);\nfont: 15pt;");
//         ui->id->setPlainText(text+"\n ban co muốn đăng ký ?");

//     }
//     else if (text == error)
//     {
//         ui->comeBack->hide();
//         ui->yes->hide();
//         ui->no->hide();
//         ui->boder->show();
//         ui->id->setStyleSheet("color: rgb(0, 255, 0);\nfont: 16pt;");
//         ui->id->show();
//         ui->boder->setStyleSheet("border:11px solid rgb(255,0,0);");
//         ui->label->hide();
//         ui->id->setStyleSheet("color: rgb(255, 0, 0);");


//     }
//     else if (text == yesno)
//     {
//         ui->comeBack->hide();
//         ui->yes->show();
//         ui->no->show();
//         ui->id->setStyleSheet("color: rgb(0, 255, 0);\nfont: 16pt;");
//         ui->id->show();
//         ui->id->setPlainText(text);
//         ui->label->hide();
//         ui->boder->show();
//         ui->boder->setStyleSheet("border:11px solid rgb(0,255,0);");
//         ui->id->setStyleSheet("color: rgb(0, 255, 0);");
//     }
//    else if (text == deTayVaoCamBien){
//             ui->comeBack->hide();
////             ui->comeBack->show();
//             ui->yes->hide();
//             ui->no->hide();
//             ui->id->setStyleSheet("color: rgb(0, 255, 0);\nfont: 16pt;");
//             ui->id->setPlainText(text);
//             ui->id->show();
//             ui->pushButton->hide();
//             ui->fp->hide();
//             ui->label->hide();
//             ui->boder->show();
//             ui->boder->setStyleSheet("border:11px solid rgb(0,255,0);");
//             ui->id->setStyleSheet("color: rgb(0, 255, 0);");
//}
//     else {
//         ui->comeBack->hide();
//         ui->yes->hide();
//         ui->no->hide();
//         ui->id->setStyleSheet("color: rgb(0, 255, 0);\nfont: 16pt;");
//         ui->id->show();
//         ui->pushButton->hide();
//         ui->fp->hide();
//         ui->label->hide();
//         ui->boder->show();
//         ui->boder->setStyleSheet("border:11px solid rgb(0,255,0);");
//         //ui->id->setStyleSheet("color: rgb(0, 255, 0);");
//         ui->id->setPlainText(text);
//         }
//     file.flush();
//     file.close();


//}




//    //function resetname

//Widget::~Widget()
//{
//    delete ui;
//}




//void Widget::on_yes_windowTitleChanged(const QString &title)
//{

//}

//void Widget::on_fp_clicked()
//{
//    QTextStream out(stdout);
//    QString filename = "/home/pi/build-checkFace-Desktop-Debug/log_data/switch.txt";
//    QFile file(filename);
//    if(file.open(QIODevice::WriteOnly))
//    {
//        QTextStream out(&file);
//        out << "2" << endl;
//    }

//     file.flush();
//     file.close();
//}

//void Widget::on_comeBack_clicked()
//{
//    QTextStream out(stdout);
//    QString filename = "/home/pi/build-checkFace-Desktop-Debug/log_data/switch.txt";
//    QFile file(filename);
//    if(file.open(QIODevice::WriteOnly))
//    {
//        QTextStream out(&file);
//        out << "0" << endl;
//    }

//     file.flush();
//     file.close();
//}

void no(){
    QTextStream out(stdout);
    QString filename = "/home/pi/build-checkFace-Desktop-Debug/log_data/option.txt";
    QFile file(filename);
    if(file.open(QIODevice::WriteOnly))
    {
        QTextStream out(&file);
        out << "0";
    }
}
void yes(){
    QTextStream out(stdout);
    QString filename = "/home/pi/build-checkFace-Desktop-Debug/log_data/option.txt";
    QFile file(filename);
    if(file.open(QIODevice::WriteOnly))
    {
        QTextStream out(&file);
        out << "1";
    }
}
void write(){
    QTextStream out(stdout);
    QString filename = "/home/pi/build-checkFace-Desktop-Debug/log_data/notification.txt";
    QFile file(filename);
    if(file.open(QIODevice::WriteOnly))
    {
        QTextStream out(&file);
        out << "";
    }
}

void Widget::on_yes_clicked()
{
    yes();
}

void Widget::on_no_clicked()
{
    no();
}

void writeSwitch()
{
    QTextStream out(stdout);
    QString filename = "/home/pi/build-checkFace-Desktop-Debug/log_data/switch.txt";
    QFile file(filename);
    if(file.open(QIODevice::WriteOnly))
    {
        QTextStream out(&file);
        out << "1" << endl;
    }

}


//time
QTimer *timer;
QTimer *timer_id_name;
QString nhap;
QString timeht;

//dangky
void Widget::on_pushButton_clicked()
{
//xoa();
writeSwitch();
//ui->yes->show();
//ui->no->show();
 QTime dieTime = QTime::currentTime().addSecs(4000);
 while(QTime::currentTime() < dieTime)
     QCoreApplication::processEvents(QEventLoop::AllEvents,100);

}



//vantay
void Widget::on_vantay_clicked()
{

}
//GUI
Widget::Widget(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Widget)
{

    ui->setupUi(this);
    ui->pushButton->hide();
    ui->fp->hide();
    ui->yes->hide();
    ui->no->hide();
    //add .gif
    QMovie * movie = new QMovie("/home/pi/build-checkFace-Desktop-Debug/img2/WwUV.gif");
    ui->label->setMovie(movie);
   movie->start();



   //set time hien tai


    QTextStream out(stdout);
    //set time
       QDate cd = QDate::currentDate();
       QTime ct = QTime::currentTime();
       QString thu = timeht.mid(0,3);
       if(thu == "Mon") thu = "Thứ Hai";
       if(thu == "Tue") thu = "Thứ Ba";
       if(thu == "Wed") thu = "Thứ Tư";
       if(thu == "Thu") thu = "Thứ Năm";
       if(thu == "Fri") thu = "Thứ Sáu";
       if(thu == "Sat") thu = "Thứ Bảy";
       if(thu == "Sun") thu = "Chủ Nhật";
       QString date = QDate::currentDate().toString("dd.MM.yyyy");

       ui->true_2->setText(thu+" "+date);
       ui->boder->hide();
       out << "Current date is: " << cd.toString() << endl;
       out << "Current time is: " << ct.toString() << endl;
       ui->pushButton->hide();
       ui->fp->hide();
       ui->comeBack->hide();

     //load realtime
       timer = new QTimer(this);
       timer->setInterval(1000);
       connect(timer,SIGNAL(timeout()),this,SLOT(timer_timeout()));
       timer->start();
       ui->id->setStyleSheet("color: rgb(0, 255, 0);\nfont: 16pt;");
}

    //funcition realtime++
void Widget::timer_timeout(){
      ui->id->setStyleSheet("color: rgb(0, 255, 0);\nfont: 16pt;");
//    QTextStream out(stdout);
////    foreach(QString x,strings);
////    QString sx= readAllStandardOutput();
////    QString stderr= readAllStandardError();
//    qDebug() << "" << endl;
//    //out << stderr << endl;
       ui->id->setCursor(Qt::BlankCursor);

    //set time
     ui->true_2->setStyleSheet("color: rgb(0, 255, 0);\nfont: 18pt;");
     ui->time->setStyleSheet("color: rgb(0, 255, 0);\nfont: 18pt;");
    QDate cd = QDate::currentDate();
    QString ct = QTime::currentTime().toString("hh:mm");
    ui->time->setText("  "+ct);
    timeht= cd.toString();

    //set thoi gian tieng viet
    QString thu = timeht.mid(0,3);
    if(thu == "Mon") thu = "Thứ Hai";
    if(thu == "Tue") thu = "Thứ Ba";
    if(thu == "Wed") thu = "Thứ Tư";
    if(thu == "Thu") thu = "Thứ Năm";
    if(thu == "Fri") thu = "Thứ Sáu";
    if(thu == "Sat") thu = "Thứ Bảy";
    if(thu == "Sun") thu = "Chủ Nhật";
    QString date = QDate::currentDate().toString("dd.MM.yyyy");

    ui->true_2->setText("  "+thu+" "+date);

     //set id,name
    QString data = "/home/pi/build-checkFace-Desktop-Debug/log_data/notification.txt";
     QFile file (data);
     if(!file.open(QFile::ReadOnly|QFile::Text))
     {
         QMessageBox::warning (this,"title","file not open");
     }
     QTextStream in (&file);
     QString text = in.readAll();
     QString dang_Ky_thanh_cong = text.right(6);

//     QString dataS = "/home/pi/build-checkFace-Desktop-Debug/log_data/switch.txt";
//      QFile fileS (dataS);
//      if(!fileS.open(QFile::ReadOnly|QFile::Text))
//      {
//          QMessageBox::warning (this,"title","file not open");
//      }
//      QTextStream inS (&fileS);
//      QString textS = inS.readAll();
//      QString dang_Ky_thanh_congS = text.right(6);


     QString checkfalse = " không tim thấy ";
     QString Nobody = "";
     QString WarmUp = "Vui lòng chờ";
     QString Enroll = "Starting the Camera...";
     QString noFace = "Ảnh không đủ tiêu chuẩn";
     QString error = "Lỗi, quay lại chế độ nhận dạng";
     QString yesno = "Sử dụng ảnh này để đăng ký (y/n)?";
     QString id ="ID";
     QString deTayVaoCamBien ="Đặt tay vào cảm biến";

//     ui->yes->hide();
//     ui->no->hide();




     //3 truong hop
     if (dang_Ky_thanh_cong == yesno)
     {
         ui->comeBack->hide();
         ui->yes->show();
         ui->no->hide();
     }
     if(text == checkfalse)
     {
         ui->comeBack->hide();
         ui->yes->hide();
         ui->no->hide();
          ui->boder->show();
            ui->id->setStyleSheet("color: rgb(255, 0, 0);\nfont: 16pt;");
          ui->id->show();
          ui->boder->setStyleSheet("border:11px solid rgb(255,0,0);");
          ui->label->hide();
          ui->pushButton->setText("Đăng ký");
          ui->pushButton->show();
          ui->fp->setText("FP");
          ui->fp->show();
          //ui->id->setStyleSheet("color: rgb(255, 0, 0);");
          ui->id->setPlainText(text);


     }
     else if(text == Nobody)
     {
         ui->comeBack->hide();
         write();
         ui->pushButton->show();
         ui->fp->show();
         ui->yes->hide();
         ui->no->hide();
         ui->id->setStyleSheet("color: rgb(0, 255, 0);\nfont: 16pt;");
         ui->id->setPlainText("");
         ui->label->hide();
         ui->boder->setStyleSheet("border:11px solid rgb(255,255,255);");
         ui->boder->hide();



     }
    else if(text == WarmUp)
     {
         ui->comeBack->hide();
         ui->pushButton->hide();
         ui->fp->hide();
         ui->yes->hide();
         ui->no->hide();
         ui->id->setStyleSheet("color: rgb(0, 255, 0);\nfont: 16pt;");
            ui->id->show();
            ui->boder->hide();
//            ui->id->setStyleSheet("color: rgb(0, 255, 0);");
            ui->id->setPlainText(text);
            ui->true_2->show();
            ui->pushButton->hide();

        }
     else if (text == noFace)
     {
         ui->comeBack->hide();
         ui->pushButton->show();
         ui->fp->show();
         ui->yes->hide();
         ui->no->hide();
         ui->id->setStyleSheet("color: rgb(0, 255, 0);\nfont: 15pt;");
         ui->id->setPlainText(text);

     }
     else if (text == error)
     {
         ui->comeBack->hide();
         ui->yes->hide();
         ui->no->hide();
         ui->boder->show();
         ui->id->setStyleSheet("color: rgb(0, 255, 0);\nfont: 16pt;");
         ui->id->show();
         ui->id->setPlainText(text);
         ui->boder->setStyleSheet("border:11px solid rgb(255,0,0);");
         ui->label->hide();
         ui->id->setStyleSheet("color: rgb(255, 0, 0);");


     }
     else if (text == yesno)
     {
         ui->comeBack->hide();
         ui->yes->show();
         ui->no->show();
         ui->id->setStyleSheet("color: rgb(0, 255, 0);\nfont: 16pt;");
         ui->id->show();
         ui->id->setPlainText(text);
         ui->label->hide();
         ui->boder->show();
         ui->boder->setStyleSheet("border:11px solid rgb(0,255,0);");
         ui->id->setStyleSheet("color: rgb(0, 255, 0);");
     }
    else if (text == deTayVaoCamBien){
             ui->comeBack->hide();
//             ui->comeBack->show();
             ui->yes->hide();
             ui->no->hide();
             ui->id->setStyleSheet("color: rgb(0, 255, 0);\nfont: 16pt;");
             ui->id->setPlainText(text);
             ui->id->show();
             ui->pushButton->hide();
             ui->fp->hide();
             ui->label->hide();
             ui->boder->show();
             ui->boder->setStyleSheet("border:11px solid rgb(0,255,0);");
             ui->id->setStyleSheet("color: rgb(0, 255, 0);");
}
     else {
         ui->comeBack->hide();
         ui->yes->hide();
         ui->no->hide();
         ui->id->setStyleSheet("color: rgb(0, 255, 0);\nfont: 16pt;");
         ui->id->show();
         ui->pushButton->hide();
         ui->fp->hide();
         ui->label->hide();
         ui->boder->show();
         ui->boder->setStyleSheet("border:11px solid rgb(0,255,0);");
         //ui->id->setStyleSheet("color: rgb(0, 255, 0);");
         ui->id->setPlainText(text);
         }
     file.flush();
     file.close();


}




    //function resetname

Widget::~Widget()
{
    delete ui;
}




void Widget::on_yes_windowTitleChanged(const QString &title)
{

}

void Widget::on_fp_clicked()
{
    QTextStream out(stdout);
    QString filename = "/home/pi/build-checkFace-Desktop-Debug/log_data/switch.txt";
    QFile file(filename);
    if(file.open(QIODevice::WriteOnly))
    {
        QTextStream out(&file);
        out << "2" << endl;
    }

     file.flush();
     file.close();
}

void Widget::on_comeBack_clicked()
{
    QTextStream out(stdout);
    QString filename = "/home/pi/build-checkFace-Desktop-Debug/log_data/switch.txt";
    QFile file(filename);
    if(file.open(QIODevice::WriteOnly))
    {
        QTextStream out(&file);
        out << "0" << endl;
    }

     file.flush();
     file.close();
}
