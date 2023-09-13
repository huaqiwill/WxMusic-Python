# @File:
# @Author: CunFu Peng
# @Created: 2023-8-21
# @Updated:
# @Version: 1.0

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QLabel


class WxPicture(QLabel):
    myLabelSignal = pyqtSignal(str)
    myLabelDoubleClickSignal = pyqtSignal(str)

    def __int__(self):
        super(WxPicture, self).__init__()

    def mouseDoubleClickEvent(self, e):  # 双击
        sigContent = self.objectName()
        self.myLabelDoubleClickSignal.emit(sigContent)

    def mousePressEvent(self, e):  # 单击
        sigContent = self.objectName()
        self.myLabelSignal.emit(sigContent)

    def leaveEvent(self, e):  # 鼠标离开label
        print("leaveEvent")

    def enterEvent(self, e):  # 鼠标移入label
        print("enterEvent")
