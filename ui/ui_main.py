# @File: settings.py 多语言支持
# @Author: CunFu Peng
# @Created: 2021-11-15
# @Updated: 2023-8-20
# @Version: 2.1

import requests
from PyQt5 import QtWidgets, QtGui

from core.api import Api
from core import Player, PlayMode
from classes.model import IMusic
from ui.components import WxWindow
from ui.widgets import WxPlayer, WxNavbar, WxControl, WxCenter
from utils import LoggerHelper


# 程序主窗口，程序控制枢纽
class WxMain(WxWindow):
    # 本对象的实例
    __instance = None

    # python的单例模式实现
    # def __new__(cls, *args, **kwargs):
    #     if cls.__instance is None:
    #         cls.__instance = object.__new__(cls)
    #     return cls.__instance

    def __init__(self):
        super().__init__()

        # self.wxNavBar = WxNavbar(self)
        # self.wxNavBar.clicked.connect()
        self.wxControl = WxControl(self)
        self.wxControl.minWindow.connect(self.showMinimized)
        self.wxControl.closeWindow.connect(self.close)
        # self.wxPlayer = WxPlayer(self)
        
        # self.center = WxCenter(self)
        # self.player = Player(self)
        # self.music = MusicApi()

        # self.event_()

    def event_(self):
        self.wxNavBar.clicked.connect()
        self.wxPlayer.previous.connect()
        self.wxPlayer.play.connect()
        self.wxPlayer.pause.connect()
        self.wxPlayer.next.connect()
        
        self.wxPlayer.ctrlPlaylist.clicked(self.event_playList)
        self.wxPlayer.ctrlAddTo.clicked(self.event_addMusic)
        self.wxPlayer.ctrlVoice.clicked(self.event_ctrlVoice)
        self.wxPlayer.ctrlPlayMode.clicked(self.event_playMode)
        self.wxPlayer.playPrevieous.clicked(self.event_playUp)
        self.wxPlayer.playPause.clicked(self.event_playPause)
        self.wxPlayer.playNext.clicked(self.event_playNext)
        # self.bottom.info_pic.mousePressEvent(QtGui.QMouseEvent())
        self.wxPlayer.infoProgress.valueChanged(self.event_sliderValueChanged)

        self.center.songinfo.clicked(self.event_addToPlaylist)
        self.center.rocking.clicked(self.event_rockingClicked)

    def event_addToPlaylist(self):
        row = self.center.songinfo.currentRow()

        music = IMusic(row)

        LoggerHelper.debug(music.name + "" + music.authorName + "" + "" + music.duration + "" + music.albumName)

        row = self.center.playlist_base.right_list.rowCount()

        self.center.playlist_base.right_list.setRowCount(row + 1)
        self.center.playlist_base.right_list.setItem(
            row, 0, QtWidgets.QTableWidgetItem(music.name))
        self.center.playlist_base.right_list.setItem(
            row, 1, QtWidgets.QTableWidgetItem(music.authorName))
        self.center.playlist_base.right_list.setItem(
            row, 2, QtWidgets.QTableWidgetItem(music.albumName))
        self.center.playlist_base.right_list.setItem(
            row, 3, QtWidgets.QTableWidgetItem(music.duration))

        LoggerHelper.debug(music.id + " " + music.url)

        self.wxPlayer.play()

        ic_map = QtGui.QPixmap(75, 75)
        ic_map.loadFromData(requests.get(music.pic).content)
        ic_map = ic_map.scaledToWidth(75).scaledToHeight(75)
        self.wxPlayer.infoPic.setPixmap(ic_map)

        self.wxPlayer.infoTitle.setText(music.name + " - " + music.authorName)
        self.wxPlayer.infoTimeEnd.setText(music.duration)
        self.wxPlayer.infoTimeStart.setText("00:00")

        # self.time_count_duration = 0

        # _thread.start_new_thread(self.durationAdd)

    # def durationAdd(self):
    #     self.time_count_duration += 1000;
    #     duration = netease.net_music.durationToString(self.time_count_duration)
    #     self.parent.bottom.info_time_1.setText(duration)
    #     # time.sleep(1000)
    #     print(1)
    #     self.durationAdd()

    def event_rockingClicked(self):
        index = self.center.rocking.currentRow()
        LoggerHelper.debug("rocking - 点击:" + str(index))

        if index == 0 or index == 5 or index == 13 or index == 18:
            return

        if index == 1:
            LoggerHelper.debug("网易 - 热歌榜 - 1")
            rst_songlist = WxMain().music.Recommend()

            self.center.setSonginfoContent(rst_songlist)
            return

        if index == 2:
            LoggerHelper.debug("网易 - 新歌榜 - 2")
            # CODE
            rst_songlist = WxMain().music.Recommend()
            self.center.setSonginfoContent(rst_songlist)
            return

        if index == 3:
            LoggerHelper.debug("网易 - 原创榜 - 3")
            rst_songlist = WxMain().music.Recommend()
            self.center.setSonginfoContent(rst_songlist)
            return

        if index == 4:
            LoggerHelper.debug("网易 - 飙升榜 - 4")
            # CODE
            rst_songlist = WxMain().music.Recommend()
            self.center.setSonginfoContent(rst_songlist)
            return

    def event_infoPicMouseDown(self):
        LoggerHelper.debug("info-pic 接收 鼠标按钮下 消息")

    def event_sliderValueChanged(self):
        LoggerHelper.debug("滑动条的值改变")
        self.wxPlayer.progress()

    def event_playList(self):
        LoggerHelper.debug("显示播放列表窗口")

    def event_addMusic(self):
        LoggerHelper.debug("显示添加到窗口")

    def event_ctrlVoice(self):
        LoggerHelper.debug("调节音量")
        play_voice = 0
        if play_voice == 0:
            LoggerHelper.debug("静音")
            self.wxPlayer.ctrlVoice.setQtFontIcon("fa5s.volume-off", "black")
        else:
            LoggerHelper.debug("非静音")
            self.wxPlayer.ctrlVoice.setQtFontIcon("fa5s.volume", "black")

    def event_playMode(self):
        LoggerHelper.debug("播放模式")

        if self.wxPlayer.playMode() == PlayMode.Order:
            LoggerHelper.debug("顺序播放")
            WxMain().wxPlayer.playMode(PlayMode.Random)
            # 设置图标
            self.wxPlayer.ctrlPlayMode.setQtFontIcon("fa5s.axe", "black")
            return

        if self.wxPlayer.playMode() == PlayMode.Random:
            LoggerHelper.debug("随机播放")
            self.wxPlayer.playMode(PlayMode.Circulate)
            # 设置图标
            self.wxPlayer.ctrlPlayMode.setQtFontIcon("fa5s.atom-alt", "black")
            return

        if self.wxPlayer.playMode() == PlayMode.Circulate:
            LoggerHelper.debug("循环播放")
            self.wxPlayer.playMode(PlayMode.Order)
            # 设置图标
            self.wxPlayer.ctrlPlayMode.setQtFontIcon("fa5s.pause", "black")
            return

    def event_playUp(self):
        LoggerHelper.debug("上一首")
        self.wxPlayer.previous()

    def event_playPause(self):
        LoggerHelper.debug("播放暂停")

        if WxMain().wxPlayer.isPlaying():
            LoggerHelper.debug("暂停")
            WxMain().wxPlayer.pause()
            # 设置播放图标
            self.wxPlayer.playPause.setQtFontIcon("fa5s.play", "black")
        else:
            LoggerHelper.debug("播放")
            WxMain().wxPlayer.play()
            # 设置暂停图标
            self.wxPlayer.playPause.setQtFontIcon("fa5s.pause", "black")

    def event_playNext(self):
        LoggerHelper.debug("下一首")
        self.wxPlayer.next()
