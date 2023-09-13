# @File:
# @Author: CunFu Peng
# @Created: 2023-8-21
# @Updated:
# @Version: 1.0

from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QTabWidget, QWidget


class WxTab(QTabWidget):
    def __init__(self, parent, rect: QRect = None):
        super().__init__(parent)
        if rect is not None:
            self.setGeometry(rect)
        self.tabBar().hide()  # 隐藏表头
        self.setStyleSheet("""
            QTabWidget{ 
                border:none;
                font-size:16px;
                font-family:"微软雅黑";
            }
            """)
        self.items = []

    def addItem(self, key: str, name: str):
        d = {"key": key, "name": name, "widget": QWidget()}
        self.items.append(d)
        self.addTab(d.get("widget"), d.get("name"))

    def getItem(self, key: str):
        for i in self.items:
            if i.get("key") == key:
                return i.get("widget")
        return None
