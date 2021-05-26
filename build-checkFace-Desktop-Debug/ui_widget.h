/********************************************************************************
** Form generated from reading UI file 'widget.ui'
**
** Created by: Qt User Interface Compiler version 5.11.3
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_WIDGET_H
#define UI_WIDGET_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QLabel>
#include <QtWidgets/QPlainTextEdit>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_Widget
{
public:
    QPushButton *pushButton;
    QLabel *time;
    QPlainTextEdit *id;
    QLabel *label;
    QLabel *true_2;
    QLabel *boder;
    QPushButton *yes;
    QPushButton *no;
    QPushButton *fp;
    QPushButton *comeBack;

    void setupUi(QWidget *Widget)
    {
        if (Widget->objectName().isEmpty())
            Widget->setObjectName(QStringLiteral("Widget"));
        Widget->resize(320, 480);
        Widget->setStyleSheet(QStringLiteral("background-color: rgb(0, 0, 0);"));
        pushButton = new QPushButton(Widget);
        pushButton->setObjectName(QStringLiteral("pushButton"));
        pushButton->setGeometry(QRect(70, 410, 91, 71));
        pushButton->setStyleSheet(QLatin1String("color: rgb(100, 100, 100);\n"
"font: 75 italic 17pt \"PibotoLt\";\n"
"border:5px solid rgb(100,100,100);"));
        time = new QLabel(Widget);
        time->setObjectName(QStringLiteral("time"));
        time->setGeometry(QRect(0, 0, 81, 51));
        time->setStyleSheet(QLatin1String("color: rgb(0, 255, 0);\n"
"font:18pt \"Quicksand\";"));
        id = new QPlainTextEdit(Widget);
        id->setObjectName(QStringLiteral("id"));
        id->setGeometry(QRect(0, 360, 321, 51));
        id->setAutoFillBackground(true);
        id->setStyleSheet(QStringLiteral("font: 75 30pt \"Quicksand\";"));
        label = new QLabel(Widget);
        label->setObjectName(QStringLiteral("label"));
        label->setGeometry(QRect(-50, 50, 371, 301));
        true_2 = new QLabel(Widget);
        true_2->setObjectName(QStringLiteral("true_2"));
        true_2->setGeometry(QRect(80, 0, 241, 51));
        true_2->setStyleSheet(QLatin1String("\n"
"color: rgb(0, 255, 0);\n"
"font: 18pt \"Quicksand\";"));
        boder = new QLabel(Widget);
        boder->setObjectName(QStringLiteral("boder"));
        boder->setGeometry(QRect(0, 50, 321, 311));
        boder->setStyleSheet(QLatin1String("\n"
"border:10px solid rgb(0,255,0);"));
        yes = new QPushButton(Widget);
        yes->setObjectName(QStringLiteral("yes"));
        yes->setGeometry(QRect(0, 410, 71, 71));
        yes->setStyleSheet(QLatin1String("color: rgb(0, 255, 0);\n"
"font: 75 italic 30pt \"PibotoLt\";\n"
"border:5px solid rgb(0,255,0);"));
        no = new QPushButton(Widget);
        no->setObjectName(QStringLiteral("no"));
        no->setGeometry(QRect(250, 410, 71, 71));
        no->setStyleSheet(QLatin1String("color: rgb(255, 0, 0);\n"
"font: 75 italic 30pt \"PibotoLt\";\n"
"border:5px solid rgb(255,0,0);"));
        fp = new QPushButton(Widget);
        fp->setObjectName(QStringLiteral("fp"));
        fp->setGeometry(QRect(160, 410, 91, 71));
        fp->setStyleSheet(QLatin1String("color: rgb(0, 100, 255);\n"
"font: 75 italic 15pt \"PibotoLt\";\n"
"border:5px solid rgb(0,100,255);"));
        comeBack = new QPushButton(Widget);
        comeBack->setObjectName(QStringLiteral("comeBack"));
        comeBack->setGeometry(QRect(78, 419, 171, 51));
        comeBack->setStyleSheet(QLatin1String("color: rgb(0, 255, 0);\n"
"font: 75 italic 20pt \"PibotoLt\";\n"
"border:5px solid rgb(0,255,0);"));

        retranslateUi(Widget);

        QMetaObject::connectSlotsByName(Widget);
    } // setupUi

    void retranslateUi(QWidget *Widget)
    {
        Widget->setWindowTitle(QApplication::translate("Widget", "Widget", nullptr));
        pushButton->setText(QApplication::translate("Widget", "ADD", nullptr));
        time->setText(QString());
        label->setText(QString());
        true_2->setText(QString());
        boder->setText(QString());
        yes->setText(QApplication::translate("Widget", "YES", nullptr));
        no->setText(QApplication::translate("Widget", "NO", nullptr));
        fp->setText(QApplication::translate("Widget", "FP", nullptr));
        comeBack->setText(QApplication::translate("Widget", "COME BACK", nullptr));
    } // retranslateUi

};

namespace Ui {
    class Widget: public Ui_Widget {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_WIDGET_H
