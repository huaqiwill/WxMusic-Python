# @File:
# @Author: CunFu Peng
# @Created: 2021-11-24
# @Updated:
# @Version: 2.1
# 这是个无界面播放器，可以控制音乐上一首，下一首，音乐的播放进度和速度等

from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl
import random
from classes.model import IMusic, SourceFrom


# 播放模式
class PlayMode:
    Order = 0  # 顺序播放
    Random = 1  # 随机播放
    Circulate = 2  # 循环播放


class Player(object):
    def __init__(self, parent):
        # 播放列表，列表中放入 Music 对象
        self._playList = []
        # 当前播放的歌曲索引
        self._currentIndex = 0
        # 当前播放歌曲的进度
        self._progress = 0
        # 当前播放歌曲的速度
        self._speed = 1  # 速度的值控制在 0.5~1.5 之间，超出不生效
        # 当前播放器模式
        self._playMode = 1  # 三个模式，值只能为 1,2,3
        # 当前播放器音量
        self._volume = 50

        self._minCount = 0
        self._maxCount = 0
        # 当前播放状态是否为已暂停
        self._isPause = False
        # PyQt5多媒体播放对象
        self._media = QMediaPlayer(parent)

    # 播放音乐
    def play(self):
        if self._isPause:
            # 如果暂停状态，则播放
            self._media.play()
            self._isPause = False
        else:
            # 如果播放状态，则暂停
            self._isPause = True
            self._media.stop()
            music = IMusic(self._playList[self._currentIndex])
            url = None
            if music.sourceFrom == SourceFrom.Native:
                url = QUrl.fromLocalFile(music.path)
            if music.sourceFrom == SourceFrom.Url:
                url = QUrl(music.url)

            self._media.setMedia(QMediaContent(url))
            self._media.setVolume(self._volume)
            self._media.play()

    # 暂停音乐的播放，保留进度条
    def pause(self) -> None:  # 暂停
        """
        暂停
        """
        self._media.pause()
        self._isPause = True

    # 停止播放音乐，音乐进度条清空
    def stop(self) -> None:
        """
        停止
        """
        self._media.stop()

    # 当前的播放状态，是否正在播放音乐
    def isPlaying(self):
        return ~self._isPause

    # 下一首
    def next(self) -> None:
        if self._playMode == PlayMode.Order \
                or self._playMode == PlayMode.Circulate:  # 顺序播放和循环播放
            if self._currentIndex != self._maxCount:
                self._currentIndex += 1

        if self._playMode == PlayMode.Random:  # 随机播放
            self._currentIndex = random.randint(
                self._minCount - 1, self._maxCount + 1)

    # 上一首
    def previous(self) -> None:
        if self._playMode == PlayMode.Circulate \
                or self._playMode == PlayMode.Order:  # 顺序播放和循环播放
            if self._currentIndex != self._minCount:
                self._currentIndex -= 1

        if self._playMode == PlayMode.Circulate:  # 随机播放
            self._currentIndex = random.randint(
                self._minCount - 1, self._maxCount + 1)

    # 设置和获取当前进度
    def progress(self, progress: int = None):
        if progress is None:
            return self._progress
        else:
            self._progress = progress

    # 设置和获取播放进度
    def speed(self, speed: int = None):
        if speed is None:
            return self._speed
        else:
            self._speed = speed

    # 设置或获取当前播放音乐的索引，调用 play 方法后可播放
    def currentIndex(self, currentIndex: int = None):
        if currentIndex is None:
            return self._currentIndex
        self._currentIndex = currentIndex

    def current(self):
        return self._playList[self._currentIndex]

    # 设置和获取当前播放模式
    def playMode(self, playMode: PlayMode = None):
        if playMode is None:
            return self._playMode
        else:
            self._playMode = playMode

    # 设置和获取当前音量大小，范围 0-100
    def volume(self, volume: int = None):
        if volume is None:
            return self._volume
        else:
            self._volume = volume

    def playlist(self, play_list: list[IMusic]):
        if play_list is None:
            return self._playList
        self._playList = play_list
        self._maxCount = self._playList.__len__()

    # 添加音乐到播放列表
    def musicAdd(self, music: IMusic) -> None:  # 增
        """
        增
        1. object path：传入一个对象，例如{"sourcefrom":"native","path":"C:\\test.mp3"}，{"sourcefrom":"url","path":"http://test.com/test.mp3"}
            sourcefrom：可供选择的有两个值（"native"和"url"）
        """
        self._playList.append(music)
        self._maxCount = self._playList.__len__()

    # 从播放列表中删除音乐
    def musicRemove(self, index: int) -> None:  # 删
        """
        删
        1. int index：索引
        """
        self._playList.pop(index)
        self._maxCount = self._playList.__len__()

    # 获取播放列表中某音乐的歌曲信息
    def musicGet(self, index: int = -1):  # 查
        """
        查
        1. int index：默认为-1，返回全部。
            不为1则返回索引所在的值

        返回值：默认返回列表，否则返回对象{"sourcefrom":" ","path":" "}
        """
        if index == -1:
            return self._playList
        return self._playList[index]

    # 插入播放列表
    def musicInsert(self, index, path: object) -> None:  # 插
        """
        插
        1. int index：插入索引
        2. object path：传入一个对象，例如{"sourcefrom":"native","path":"C:\\test.mp3"}，{"sourcefrom":"url","path":"http://test.com/test.mp3"}
            sourcefrom：可供选择的有两个值（"native"和"url"）
        """
        self._playList.insert(index, path)
        self._maxCount = self._playList.__len__()
