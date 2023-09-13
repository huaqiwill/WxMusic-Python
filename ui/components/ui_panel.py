# @File:
# @Author: CunFu Peng
# @Created: 2023-8-21
# @Updated:
# @Version: 1.0

from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QLabel


class WxPanel(QLabel):
    def __init__(self, parent, rect: QRect):
        super().__init__(parent)
        self.setGeometry(rect)
