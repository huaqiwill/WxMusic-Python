# @File: settings.py 多语言支持
# @Author: CunFu Peng
# @Created: 2021/11/11
# @Updated: 2023-8-20
# @Version: 2.1

import os
import requests
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRect
from ui.components import WxTab, WxTable, WxButton
from classes.model import IMusic
from utils import LoggerHelper


# 中部区
class WxCenter:
    def __init__(self, parent):
        self._parent = parent

        self._center = QtWidgets.QLabel(self._parent)  # [-0-]
        self._center.setGeometry(100, 52, 1144, 660)
        # self.center.setStyleSheet("QLabel{background-color:rgb(209,232,247);}")

        # 中部
        self.tab = WxTab(self._center, QRect(6, 0, 1129, 660))  # [-1-]
        self.tab.addItem("1", " 发现")
        self.tab.addItem("2", " 下载")
        self.tab.addItem("3", " 发现")
        self.tab.addItem("4", " 下载")
        self.tab.addItem("5", " 列表")
        self.tab.addItem("6", " 本地")
        self.tab.addItem("7", " 设置")

        # 发现
        self.found = WxTab(self.tab.getItem("1"), QRect(0, 0, 1129, 660))  # [-3-]
        # 推荐，歌单，搜索
        self.found.addItem("a", "推荐")
        self.found.addItem("b", "歌单")
        self.found.addItem("c", "搜索")

        # 下载
        self.download = WxTable(self.found.getItem("a"), QRect(0, 0, 1129, 648))  # [-3-]
        self.download.setColumnCount(4)
        self.download.setHorizontalHeaderLabels(["歌曲名", "歌手", "下载状态", "下载进度"])
        self.download.setColumnWidth(0, 420)
        self.download.setColumnWidth(1, 180)
        self.download.setColumnWidth(2, 110)
        self.download.setColumnWidth(3, 360)

        # 本地
        self.native = WxTable(self.tab.getItem("b"), QRect(70, 0, 1029, 630))  # [-3-]
        self.native.setColumnCount(3)
        self.native.setHorizontalHeaderLabels(["歌曲名", "时长", "操作"])
        self.native.setColumnWidth(0, 745)
        self.native.setColumnWidth(1, 105)
        self.native.setColumnWidth(2, 120)
        self.native.setStyleSheet(
            """
            QTableView,QTabWidget::pane {
                border:none;
                selection-background-color:rgb(52,152,200);
                selection-color:#40E0D0;
                alternate-background-color:#525252;
                gridline-color:#fff;
            }
            """
        )

        w = 80
        h = 80

        # 排行榜 歌单列表
        self.rocking = WxTable(self.tab.getItem("1"), QRect(0, 0, 262, 630))  # [-5-]
        self.rocking.verticalHeader().setVisible(False)  # 隐藏垂直表头
        self.rocking.horizontalHeader().setVisible(False)  # 隐藏水平表头
        self.rocking.verticalScrollBar().setHidden(True)  # 隐藏垂直滚动条
        self.rocking.horizontalScrollBar().setHidden(True)  # 隐藏水平滚动条
        self.rocking.setColumnCount(1)
        self.rocking.setColumnWidth(0, 255)
        self.rocking.setStyleSheet("""
            QTableWidget{
                border:none;
                gridline-color:#fff;
            }
            """)

        # ========================================
        # Qss界面美化3：QTableWidget美化
        # https://blog.csdn.net/parkchorong/article/details/102661052

        self.rocking.setStyleSheet(
            """
            /*tabelwidget*/
            QTableWidget{
                color:#000;
                background:#fff;
                border:0;
                /*alternate-background-color:#525252;*//*交错颜色*/
                /*gridline-color:#242424;*/
            }

            /*选中item*/
            QTableWidget::item:selected{
                color:#fff;
                /*background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #484848,stop:1 #383838);*/

                background-color:#666;
            }

            /*悬浮item*/
            QTableWidget::item:hover{
                /*background:#5B5B5B;*/
            }

            /*表头*/
            QHeaderView::section{
                text-align:center;
                background:#5E5E5E;
                padding:3px;
                margin:0px;
                color:#DCDCDC;
                border:1px solid #242424;
                border-left-width:0;
            }

            /*表右侧的滑条*/
            QScrollBar:vertical{
                background:#484848;
                padding:0px;
                border-radius:6px;
                max-width:12px;
            }

            /*滑块*/
            QScrollBar::handle:vertical{
                background:#CCCCCC;
                }
                /*
                滑块悬浮，按下*/
                QScrollBar::handle:hover:vertical,QScrollBar::handle:pressed:vertical{
                background:#A7A7A7;
                }
                /*
                滑块已经划过的区域*/
                QScrollBar::sub-page:vertical{
                background:444444;
            }

            /*
            滑块还没有划过的区域*/
            QScrollBar::add-page:vertical{
                background:5B5B5B;
            }

            /*页面下移的按钮*/
            QScrollBar::add-line:vertical{
                background:none;
            }

            /*页面上移的按钮*/
            QScrollBar::sub-line:vertical{
                background:none;
            }
            """
        )
        # ========================================

        music_source_list = [
            "• 网易云",
            "  热歌榜",
            "  新歌榜",
            "  原创榜",
            "  飙升榜",
            "• 酷狗",
            "  飙升榜",
            "  TOP500",
            "  抖音热歌榜",
            "  快手热歌榜",
            "  国风新歌榜",
            "  电音热歌榜",
            "  影视金曲榜",
            "• QQ",
            "  飙升榜",
            "  热歌榜",
            "  新歌榜",
            "  国风热歌榜",
            "• 酷我",
            "  飙升榜",
            "  热歌榜",
            "  新歌榜",
        ]

        self.rocking.setRowCount(music_source_list.__len__())
        for i in range(0, music_source_list.__len__()):
            self.rocking.setItem(i, 0, QtWidgets.QTableWidgetItem(music_source_list[i]))

        self.rocking.item(0, 0).setFont(QtGui.QFont("微软雅黑", 12))
        self.rocking.item(5, 0).setFont(QtGui.QFont("微软雅黑", 12))
        self.rocking.item(13, 0).setFont(QtGui.QFont("微软雅黑", 12))
        self.rocking.item(18, 0).setFont(QtGui.QFont("微软雅黑", 12))

        # 设置不可选中
        self.rocking.item(0, 0).setFlags(QtCore.Qt.ItemIsSelectable)
        self.rocking.item(5, 0).setFlags(QtCore.Qt.ItemIsSelectable)
        self.rocking.item(13, 0).setFlags(QtCore.Qt.ItemIsSelectable)
        self.rocking.item(18, 0).setFlags(QtCore.Qt.ItemIsSelectable)

        # self.rocking.setItem(0,0,QtWidgets.QTableWidgetItem("网易云"))
        # self.rocking.setItem(1,0,QtWidgets.QTableWidgetItem("酷狗"))
        # self.rocking.setItem(2,0,QtWidgets.QTableWidgetItem("酷我"))
        # self.rocking.setItem(3,0,QtWidgets.QTableWidgetItem("QQ"))

        del w, h

        # 音乐信息
        self.songinfo = WxTable(self.tab.getItem("2"), QRect(243, 0, 886, 630))  # [-5-]
        self.songinfo.setColumnCount(5)
        self.songinfo.setHorizontalHeaderLabels(["歌曲名", "歌手", "时长", "专辑", "操作"])
        self.songinfo.setColumnWidth(0, 320)
        self.songinfo.setColumnWidth(1, 150)
        self.songinfo.setColumnWidth(2, 90)
        self.songinfo.setColumnWidth(3, 150)
        self.songinfo.setColumnWidth(4, 120)
        self.songinfo.setStyleSheet(
            """
            QTableView,QTabWidget::pane{ 
                border:none;
                selection-background-color:rgb(52,152,200);
                selection-color:white;
                alternate-background-color:#505050;
                gridline-color:#fff;
            }"""
        )

        # 歌单
        self.songlist = WxTable(self.tab.getItem("1"), QRect(0, 0, 1129, 630))  # [-5-]
        # self.songlist.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)  # 设置整行选中
        self.songlist.verticalHeader().setVisible(False)  # 隐藏垂直表头
        self.songlist.horizontalHeader().setVisible(False)  # 隐藏水平表头
        self.songlist.setStyleSheet(
            """
            QTableWidget{
            color:#000;
            background:#fff;
            border:0;
            }

            /*选中item*/
            QTableWidget::item:selected{
                color:#fff;
                background-color:#eee;
                border:0;
                outline:0;
            }

            /*悬浮item*/
            QTableWidget::item:hover{

            }
            """
        )

        # 搜索
        self.search = WxTable(self.tab.getItem("0"), QRect(0, 0, 1129, 630))  # [-5-]
        self.search.setColumnCount(5)
        self.search.setHorizontalHeaderLabels(["歌曲名", "歌手", "专辑", "时长", "操作"])
        self.search.setColumnWidth(0, 420)
        self.search.setColumnWidth(1, 180)
        self.search.setColumnWidth(2, 260)
        self.search.setColumnWidth(3, 110)
        self.search.setColumnWidth(4, 100)
        self.search.setStyleSheet(
            """
            QTableWidget{
                color:#000;
                background:#fff;
                border:0;
            }

            /*选中item*/
            QTableWidget::item:selected{
                color:#fff;
                background-color:rgb(36,172,242);
            }

            /*悬浮item*/
            QTableWidget::item:hover{

            }
            """
        )
        self.native_base = NativeBase(self)
        self.playlist_base = WxPlaylist(self)
        self.setting_base = WxSettings(self)

        # ====================================================================
        # 热歌榜
        rst_songlist = WxMain().music.Recommend()

        row = rst_songlist.__len__()
        self.songinfo.setRowCount(row)
        self.addOpration(self.songinfo, row, 4)

        for i in range(0, row):
            music = IMusic(rst_songlist[i])
            self.songinfo.setItem(
                i, 0, QtWidgets.QTableWidgetItem(music.name))
            self.songinfo.setItem(
                i, 1, QtWidgets.QTableWidgetItem(music.authorName))
            self.songinfo.setItem(
                i, 2, QtWidgets.QTableWidgetItem(music.duration))
            self.songinfo.setItem(
                i, 3, QtWidgets.QTableWidgetItem(music.albumName))

        # ====================================================================
        # 歌单

        soups = WxMain().music.songlist()
        self.songlist.setColumnCount(6)

        for i in range(0, 6):
            self.songlist.setColumnWidth(i, 185)

        self.songlist.setRowCount(int(soups.__len__() / 6) + 1)
        # find,get方法继承来自BeautifulSoup,由方法get_songlist()返回

        for i in range(0, soups.__len__()):
            img = soups[i].find("img")
            name = soups[i].find("a")
            img = img.get("src")
            href = name.get("href")
            title = name.get("title")

            w_pic = QtWidgets.QLabel()
            map = QtGui.QPixmap(130, 130)
            map.loadFromData(requests.get(img).content)
            w_pic.setPixmap(map)

            w_title = QtWidgets.QLabel()
            w_title.setFont(QtGui.QFont("微软雅黑", 10))
            w_title.setText(title)

            layout = QtWidgets.QVBoxLayout()
            layout.addWidget(w_pic)
            layout.addWidget(w_title)

            w_lb = QtWidgets.QLabel(self.songlist)
            w_lb.setLayout(layout)

            a = i % 6
            b = int(i / 6)
            self.songlist.setCellWidget(b, a, w_lb)

            # self.songlist.setItem(i,1,QtWidgets.QTableWidgetItem(href))
            # self.songlist.setItem(i,2,QtWidgets.QTableWidgetItem(img))

            self.songlist.setRowHeight(i, 185)

    def setSonginfoContent(self, rst_songlist: list):
        row = rst_songlist.__len__()

        self.songinfo.setRowCount(row)
        self.addOpration(self.songinfo, row)

        for i in range(0, row):
            music = IMusic(rst_songlist[i])
            self.songinfo.setItem(
                i, 0, QtWidgets.QTableWidgetItem(music.name))
            self.songinfo.setItem(
                i, 1, QtWidgets.QTableWidgetItem(music.authorName))
            self.songinfo.setItem(
                i, 2, QtWidgets.QTableWidgetItem(music.duration))
            self.songinfo.setItem(
                i, 3, QtWidgets.QTableWidgetItem(music.albumName))

    def addOpration(self, parent, row: int, column: int):

        for i in range(0, row):
            la = QtWidgets.QLabel()
            ctrl_1 = QtWidgets.QPushButton(la)
            ctrl_1.setGeometry(0, 0, 30, 30)

            ctrl_2 = QtWidgets.QPushButton(la)
            ctrl_2.setGeometry(30, 0, 30, 30)

            ctrl_3 = QtWidgets.QPushButton(la)
            ctrl_3.setGeometry(60, 0, 30, 30)

            self.songinfo.setCellWidget(i, column, la)

            # event
            ctrl_1.clicked(lambda: self.event_ctrlPlay1(i))
            ctrl_2.clicked(lambda: self.event_ctrlPlay2(i))
            ctrl_3.clicked(lambda: self.event_ctrlPlay3(i))
            # style

    def event_ctrlPlay1(self, n: int):
        row = self.songinfo.currentRow()
        LoggerHelper.debug("songinfo - ctrl-1-play - " + str(n))

    def event_ctrlPlay2(self, n: int):
        row = self.songinfo.currentRow()
        LoggerHelper.debug("songinfo - ctrl-2-play - " + str(n))

    def event_ctrlPlay3(self, n: int):
        row = self.songinfo.currentRow()
        LoggerHelper.debug("songinfo - ctrl-3-play - " + str(n))


# from ui_main import mainwin


class NativeBase:
    def __init__(self, parent):
        self.browser_btn = WxButton(parent, QRect(0, 30, 60, 30), "浏览")
        self.browser_btn.setStyleSheet(
            """
            QPushButton{
                border:0;
                background-color:rgb(10,133,217);
                color:white;
            }

            QPushButton:hover{
                background-color:rgb(77,210,168);
            }
            """
        )

        self.open_btn = WxButton(parent, QRect(0, 60, 60, 30), "添加")
        self.open_btn.setStyleSheet(
            """
            QPushButton{
                border:0;
                background-color:rgb(10,133,217);
                color:white;
            }

            QPushButton:hover{
                background-color:rgb(77,210,168);
            }

            """
        )

        self.delete_btn = WxButton(parent, QRect(0, 90, 60, 30), "删除")
        self.delete_btn.setStyleSheet(
            """
            QPushButton{
                border:0;
                background-color:rgb(10,133,217);
                color:white;
            }

            QPushButton:hover{
                background-color:rgb(77,210,168);
            }
            """
        )

        self.event()

    def event(self):
        self.browser_btn.clicked(lambda: self.browser_clicked())
        self.open_btn.clicked(lambda: self.open_clicked())
        self.delete_btn.clicked(lambda: self.delete_clicked())

    def browser_clicked(self):
        print("浏览")
        # 选择文件夹 对话框
        dir = QtWidgets.QFileDialog.getExistingDirectory(
            self._parent._parent, "请选择包含音乐的文件夹："
        )
        files = self.EnumFiles(dir)
        for file in files:
            print(file)

    def open_clicked(self):
        print("添加")
        # 文件另存为
        # 对话框
        # QFileDialog.getSaveFileName()

        # 文件另存为
        # 对话框
        #
        # QFileDialog.getSaveFileName()

        # 选择文件 对话框
        file_name = QtWidgets.QFileDialog.getOpenFileName(
            self._parent._parent, "选取音频文件", os.getcwd(), "mp3文件(*.mp3);;所有文件(*.*)"
        )[0]
        print(file_name)

    def delete_clicked(self):
        print("删除")

    # 枚举文件
    def EnumFiles(self, path: str, isPath: bool = True):
        files = os.listdir(path)
        if isPath:
            for i in range(0, files.__len__()):
                files[i] = path + "/" + files[i]
        return files


class WxPlaylist(object):
    def __init__(self, parent):
        self._parent = parent

        # 左侧_列表
        self.left_list = WxTable(self._parent, QRect(0, 0, 100, 650))
        self.left_list.verticalHeader().setVisible(False)  # 隐藏垂直表头
        self.left_list.horizontalHeader().setVisible(False)  # 隐藏水平表头
        self.left_list.verticalScrollBar().setHidden(True)  # 隐藏垂直滚动条
        self.left_list.horizontalScrollBar().setHidden(True)  # 隐藏水平滚动条
        self.left_list.setColumnCount(1)
        self.left_list.setRowCount(3)
        self.left_list.setItem(0, 0, QtWidgets.QTableWidgetItem("我的列表"))
        self.left_list.setItem(1, 0, QtWidgets.QTableWidgetItem("播放列表"))
        self.left_list.setItem(2, 0, QtWidgets.QTableWidgetItem("我的收藏"))
        self.left_list.item(0, 0).setFont(QtGui.QFont("微软雅黑", 12))
        # 所有单元格不可选中
        self.left_list.item(0, 0).setFlags(QtCore.Qt.ItemIsSelectable)
        self.left_list.setStyleSheet("""
            QTableWidget{
                border:0;
            }
            """)

        # 右侧_列表
        self.right_list = WxTable(self._parent, QRect(102, 0, 1020, 650))
        self.right_list.setColumnCount(5)
        self.right_list.setHorizontalHeaderLabels(["歌曲名", "歌手", "专辑", "时长", "操作"])
        self.right_list.setColumnWidth(0, 250)
        self.right_list.setColumnWidth(1, 180)
        self.right_list.setColumnWidth(2, 220)
        self.right_list.setColumnWidth(3, 120)
        self.right_list.setColumnWidth(4, 100)


class WxSettings(object):
    def __init__(self, parent):
        self._parent = parent

        # ==== 基本设置

        # 1.开机自启动
        self.check_startSelf = QtWidgets.QCheckBox(self._parent)
        self.check_startSelf.setText("开机自启动")
        self.check_startSelf.setGeometry(0, 0, 80, 24)

        # 2.靠边隐藏
        self.check_hideSelf = QtWidgets.QCheckBox(self._parent)
        self.check_hideSelf.setText("靠边隐藏")
        self.check_hideSelf.setGeometry(0, 30, 80, 24)

        # 1.主题设置

        self.theme_style = 1

        # 2.动画设置

        self.animation = 1

        # === 播放设置

        # === 搜索设置
