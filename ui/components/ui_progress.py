# @File:
# @Author: CunFu Peng
# @Created: 2023-8-21
# @Updated:
# @Version: 1.0


"""
1、 QProgressBar基本用法
m_pConnectProBar = new QProgressBar;
m_pConnectProBar->setRange(0,100); //设置进度条最小值和最大值(取值范围)
m_pConnectProBar->setMinimum(0); //设置进度条最小值
m_pConnectProBar->setMaximum(100); //设置进度条最大值
m_pConnectProBar->setValue(50);  //设置当前的运行值
m_pConnectProBar->reset(); //让进度条重新回到开始
m_pConnectProBar->setOrientation(Qt::Horizontal);  //水平方向
m_pConnectProBar->setOrientation(Qt::Vertical);  //垂直方向
m_pConnectProBar->setAlignment(Qt::AlignVCenter);  // 对齐方式
m_pConnectProBar->setTextVisible(false); //隐藏进度条文本
m_pConnectProBar->setFixedSize(258,5);   //进度条固定大小
m_pConnectProBar->setInvertedAppearance(true); //true:反方向  false:正方向
m_pConnectProBar->setVisible(false);  //false:隐藏进度条  true:显示进度条

[2]信号
QSlider常用的信号有以下这几个信号:

移动滑动条时发出的信号:

void sliderMoved(int value)
其传递的参数为当前滑动条所对应的数值

点击滑动条时所发出的信号:
void sliderPressed()

释放时所发出的信号:
void sliderReleased()

数值改变时所发出的信号：
void valueChanged(int value)
"""
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QSlider


class WxProgress(QSlider):
    def __init__(self, parent):
        super().__init__(parent)
        self.setOrientation(Qt.Horizontal)  # 设置为水平滑块条
