# @File:
# @Author: CunFu Peng
# @Created: 2023-8-21
# @Updated:
# @Version: 1.0

import qtawesome
from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QPushButton

#按钮
class WxCtrlButton(QPushButton):
    def __init__(self, parent, rect: QRect = None):
        super().__init__(parent)
        if rect is not None:
            self.setGeometry(28, 0, 24, 24)

    def setQtFontIcon(self, icon_name, icon_color):
        style_icon = qtawesome.icon(icon_name, color=icon_color)  # 添加到
        self.setIcon(style_icon)
