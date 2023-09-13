# @File:
# @Author: CunFu Peng
# @Created: 2021/09/18
# @Updated:
# @Version: 1.0

from PyQt5 import QtCore, QtGui, QtWidgets
import ctypes


class WxWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        # 设置任务栏常驻图标
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(
            "myappid")

        # 设置窗口大小
        self.setFixedSize(1244, 788)

        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        # self.setWindowOpacity(0.99)  # 设置窗口透明度
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # 隐藏边框

        # 设置圆角边框
        self.bmp = QtGui.QBitmap(1244, 788)  # 这里将window size引入，否则无效果！
        self.bmp.fill()
        self.Painter = QtGui.QPainter(self.bmp)
        self.Painter.setPen(QtCore.Qt.NoPen)
        self.Painter.setBrush(QtCore.Qt.black)
        self.Painter.drawRoundedRect(self.bmp.rect(), 10, 10)  # 倒边角为5px
        self.setMask(self.bmp)  # 切记将self.bmp Mark到window

    # ===================== # ===================== #
    # 无边框的拖动 事件重写
    # ===
    def mouseMoveEvent(self, e: QtGui.QMouseEvent):  # 重写移动事件
        if self._isTracking:
            self._endPos = e.pos() - self._startPos
            self.move(self.pos() + self._endPos)

    def mousePressEvent(self, e: QtGui.QMouseEvent):
        if e.button() == QtCore.Qt.LeftButton:
            self._isTracking = True
            self._startPos = QtCore.QPoint(e.x(), e.y())

    def mouseReleaseEvent(self, e: QtGui.QMouseEvent):
        if e.button() == QtCore.Qt.LeftButton:
            self._isTracking = False
            self._startPos = None
            self._endPos = None

    # ===================== # ===================== #
