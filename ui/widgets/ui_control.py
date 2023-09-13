"""
Create-Date: 2021/11/11
Author:Cunfu Peng
Last-Edit-Date: 2021/11
"""

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from ui.components import WxButton, WxPanel
from utils import TFyMusicHelper
from classes.model import IMusic


# 顶部区域
class WxControl:
    closeWindow = pyqtSignal()
    minWindow = pyqtSignal()

    def __init__(self, parent):
        self._parent = parent
        self.ui()
        # self.event()

    def ui(self):
        self.top = QLabel(self._parent)
        self.top.setGeometry(100, 0, 1144, 52)

        # 顶部 歌曲源区域 组合框
        self.top_sourcefrom = WxPanel(self.top, QRect(6, 6, 76, 50))

        self.sourcefrom = QComboBox(self.top_sourcefrom)
        self.sourcefrom.setGeometry(0, 2, 76, 36)
        self.sourcefrom.addItem(" 网易云")
        self.sourcefrom.addItem(" 酷狗")
        self.sourcefrom.addItem(" QQ")
        self.sourcefrom.addItem(" 酷我")
        self.sourcefrom.setCurrentIndex(0)
        self.sourcefrom.setStyleSheet(
            """
            QComboBox{
                border:none;
                font-family:"微软雅黑";
                font-size:12px;
                color:black;
                border-radius:5px;
            }

            QComboBox QAbstractItemView{
                border:0;
            }

            QComboBox::drop-down {
                subcontrol-origin: padding;
                subcontrol-position: top right;
                width: 30px;
                border-left-width: 0px;
                border-left-color: gray;
                border-left-style: solid;
                border-top-right-radius: 10px;
                border-bottom-right-radius: 10px;
            }

            QComboBox::down-arrow {    
                border-image: url(:/image/down.png);
            }

            QComboBox::down-arrow:hover {    
                border-image: url(:/image/up.png);

            }

            QComboBox::down-arrow:pressed {   
                border-image: url(:/image/up.png);
            }
            """
        )

        # == 顶部 搜索区域 ==
        self.top_search = WxPanel(self.top, QRect(86, 6, 500, 50))
        self.top_search.setStyleSheet(
            """
            QLineEdit{ 
                border:none;
                color:black;
                background-color:#ddd;
                font-size:14px;
                font-family:微软雅黑;
                padding-left:8px;
                border-top-left-radius:5px;
                border-bottom-left-radius:5px;
            }
            QPushButton { 
                border:none;
                background-color:#ddd;
                border-top-right-radius:5px;
                border-bottom-right-radius:5px;
            }
            QPushButton:hover { 
                background-color:#ccc;
            }
            """
        )

        # 顶部搜索框
        self.searchbox = QLineEdit(self.top_search)
        self.searchbox.setGeometry(0, 2, 300, 36)
        self.searchbox.setPlaceholderText("Search for something...")

        # 顶部搜索按钮
        self.searchbtn = WxButton(self.top_search, QRect(300, 2, 50, 36))
        self.searchbtn.setQtFontIcon("fa5s.search", 156456)

        # == 顶部 控制区域 ==
        self.top_ctrl = WxPanel(self.top, QRect(1060, 10, 80, 50))

        # 最小化按钮
        self.mini = WxButton(self.top_ctrl, QRect(4, 4, 24, 24))
        self.mini.setQtFontIcon("fa5s.minus", "white")
        self.mini.clicked.connect(lambda: self.minWindow.emit())
        self.mini.setStyleSheet(
            """
            QPushButton {
                border:none;
                border-radius:12px;
                background-color:#4caf50;
            } 
            QPushButton:hover { 
                background-color:#388e3c;
            }
            """
        )

        # 关闭按钮
        self.close = WxButton(self.top_ctrl, QRect(36, 4, 24, 24))
        self.close.setQtFontIcon("fa5s.times", "white")
        self.close.clicked.connect(lambda:self.closeWindow.emit())
        self.close.setStyleSheet(
            """
            QPushButton {
                border:none;
                border-radius:12px;
                background-color:red;
            } 
            QPushButton:hover {
                background-color:rgb(210,0,0);
            }
            """
        )

        self.searchbtn.clicked.connect(self.event_searchMusic)

    def event_searchMusic(self):
        name = self.searchbox.text()
        if name != "":
            WxMain().center.found.setCurrentIndex(2)
            sch_rsts = WxMain().music.search(name=name)
            WxMain().center.search.setRowCount(sch_rsts.__len__())

            for i in range(0, sch_rsts.__len__()):
                music = IMusic(sch_rsts[i])
                print(music)

                self._parent._center.search.setItem(
                    i, 0, QtWidgets.QTableWidgetItem(music.name))
                self._parent._center.search.setItem(
                    i, 1, QtWidgets.QTableWidgetItem(music.authorName))
                WxMain().center.search.setItem(
                    i, 2, QtWidgets.QTableWidgetItem(music.albumName))
                WxMain().center.search.setItem(
                    i, 3, QtWidgets.QTableWidgetItem(
                        TFyMusicHelper.durationToString(music.duration)))
