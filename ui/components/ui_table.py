# @File:
# @Author: CunFu Peng
# @Created: 2023-8-21
# @Updated:
# @Version: 1.0

from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QTableWidget, QAbstractItemView, QHeaderView

from utils import LoggerHelper


class WxTable(QTableWidget):
    def __init__(self, parent, rect: QRect = None):
        super().__init__(parent)
        self._parent = parent

        if rect is not None:
            self.setGeometry(rect)

        # self.a.setGeometry(800, 250, 300, 460)
        # self.setGeometry(800, 210, 300, 500)
        # self.setColumnCount(2)
        # self.setColumnWidth(0, 130)
        # self.setColumnWidth(1, 120)
        # self.setHorizontalHeaderLabels(["歌曲名", "歌手"])
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 设置不可编辑
        self.setSelectionBehavior(QAbstractItemView.SelectRows)  # 设置整行选中
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)  # 使用户无法调整，
        self.verticalHeader().setSectionResizeMode(QHeaderView.Fixed)  # 固定单元格尺寸
        # self.verticalHeader().setVisible(False)  # 隐藏垂直表头
        # self.horizontalHeader().setVisible(False)  # 隐藏水平表头
        # self.verticalScrollBar().setHidden(True)  # 隐藏垂直滚动条
        # self.horizontalScrollBar().setHidden(True)  # 隐藏水平滚动条

        self.event_()

    def event_(self):
        self.clicked(self.event_playMusic)

    def setShow(self):
        if self.isVisible():
            LoggerHelper.debug("not show")
            self.setVisible(False)
        else:
            LoggerHelper.debug("show")
            self.setVisible(True)

    def event_playMusic(self):
        # playlist = Player.playlist(self._parent.path.songDB + "\\songlist.db")
        # playlist.index = self.a.currentRow() + 1
        #
        # song_id = playlist.getLocalMusicInfo()[1]
        # song_id = "1456890009"
        # music_path = "http://music.163.com/song/media/outer/url?id={0}.mp3".format(
        #     song_id
        # )
        # print(music_path)
        # Player.music(self._parent).play(music_path, "url")
        pass
