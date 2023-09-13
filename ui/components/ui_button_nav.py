# @File:
# @Author: CunFu Peng
# @Created: 2023-8-21
# @Updated:
# @Version: 1.0

import qtawesome
from PyQt5.QtWidgets import QPushButton


class WxNavButton(QPushButton):
    def __init__(self, text, parent):
        super().__init__(text, parent)

    def setQtFontIcon(self, icon_name, icon_color):
        style_icon = qtawesome.icon(icon_name, icon_color)  # 搜索
        self.setIcon(style_icon)

    def styleNormal(self):
        stylesheet = """
                QPushButton{
                    border:none;
                    color:black;
                    font-size:18px;
                    background-color:#eee;
                    height:155px;
                    font-family:"微软雅黑";
                }
                QPushButton:hover{
                    background-color:#ccc;
                }"""
        self.setStyleSheet(stylesheet)

    def styleFocus(self):
        stylesheet_focus = """
                QPushButton{
                    border:none;
                    color:black;
                    font-size:18px;
                    background-color:#ccc;
                    height:155px;
                    font-family:"微软雅黑";
                }
                QPushButton:hover{
                    background-color:#ccc;
                }"""
        self.setStyleSheet(stylesheet_focus)
