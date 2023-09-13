# @File:
# @Author: CunFu Peng
# @Created: 2023-8-21
# @Updated:
# @Version: 1.0

import qtawesome
from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QPushButton


class WxButton(QPushButton):
    def __init__(self, parent, rect: QRect = None, text: str = None):
        super().__init__(parent)
        if rect is not None:
            self.setGeometry(rect)
        if text is not None:
            self.setText(text)

    def setQtFontIcon(self, icon_name, icon_color):
        style_icon = qtawesome.icon(icon_name, color=icon_color)  # 搜索
        self.setIcon(style_icon)
