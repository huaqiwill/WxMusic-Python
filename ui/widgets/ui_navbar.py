'''
Create-Date: 2021/11/11
Author: Peng
Last-Edit-Date: 2021/11
'''

from PyQt5 import QtWidgets
from ui.components import WxNavButton
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import *


class NavItem:
    text: str
    icon: str
    iconColor: str


class WxNavbar:
    '''
    导航栏
    传入参数，导航栏显示字符串即可


        # 导航栏 发现
        self.found = WxNavButton(" 发现", self.nav)
        self.found.setGeometry(x, y * 0, w, h)
        # self.found.setQtFontIcon("fa5s.search", "black")

        # 导航栏 下载
        self.download = WxNavButton(" 下载", self.nav)
        self.download.setGeometry(x, y * 1, w, h)
        # self.download.setQtFontIcon("fa5s.bars", "black")

        # 导航栏 列表
        self.list = WxNavButton(" 列表", self.nav)
        self.list.setGeometry(x, y * 2, w, h)
        # self.list.setQtFontIcon("fa5s.file", "black")

        # 导航栏 本地
        self.native = WxNavButton(" 本地", self.nav)
        self.native.setGeometry(x, y * 3, w, h)
        # self.native.setQtFontIcon("fa5s.arrow-circle-down", "black")

        # 导航栏 设置
        self.set = WxNavButton(" 设置", self.nav)
        self.set.setGeometry(x, y * 4, w, h)
        # self.set.setQtFontIcon("fa5s.cog", "black")
    '''
    clicked = pyqtSignal(int)
    _selectedIndex = -1

    def __init__(self, parent, navs: list[NavItem]):
        self._parent = parent

        layout = QVBoxLayout()

        self.nav = QtWidgets.QLabel(self._parent)
        self.nav.setGeometry(0, 0, 100, 788)
        self.nav.setStyleSheet("""
            QLabel { 
                background-color:#eee;
            }
            QPushButton { 
                border:none;
                color:black;
                font-size:18px;
                background-color:#eee;
                height:155px;
                font-family:"微软雅黑";
            }
            QPushButton:hover { 
                background-color:#ccc;
            }
            """)

        x = 0
        y = 52
        w = 100
        h = 52

        idx = 0
        self.nav_items = list[WxNavButton]()
        for nav in range(navs):
            item = WxNavButton(nav.text, self.nav)
            item.setGeometry(x, y * idx, w, h)
            item.setQtFontIcon(nav.icon, nav.iconColor)
            item.click.connect(self.emitClickSignal)
            layout.addWidget(item)
            idx += 1
            self.nav_items.append(item)

        del x, y, w, h


    def emitClickSignal(self, e):
        
        self.clicked[int].emit(self._selectedIndex)

    def setIndexStyle(self, n: int):
        idx = 0
        for item in self.nav_items:
            item.styleNormal()
            if idx == n:
                item.styleFocus()
            idx += 1
