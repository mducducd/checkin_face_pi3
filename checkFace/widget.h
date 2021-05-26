#ifndef WIDGET_H
#define WIDGET_H

#include <QWidget>

namespace Ui {
class Widget;
}

class Widget : public QWidget
{
    Q_OBJECT

public:
    explicit Widget(QWidget *parent = nullptr);
    ~Widget();

private slots:
    void on_pushButton_clicked();
private slots:
    void timer_timeout();
    //void on_pushButton_2_clicked();
    void on_yes_clicked();

    void on_no_clicked();

    void on_vantay_clicked();

    void on_yes_windowTitleChanged(const QString &title);

    void on_fp_clicked();

    void on_comeBack_clicked();

private:
    Ui::Widget *ui;
};

#endif // WIDGET_H
