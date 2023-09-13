"""
Create-Date: 2021/11/11
Author: Peng
Last-Edit-Date: 2021/11
"""

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from core import PlayMode
from ui.components import WxCtrlButton, WxLabel, WxPanel, WxProgress
from utils import LoggerHelper


# 代码底部播放器
class WxPlayer:
    previous = pyqtSignal()
    play = pyqtSignal()
    pause = pyqtSignal()
    next = pyqtSignal()
    progressValueChanged = pyqtSignal()
    
    def __init__(self, parent):
        self._parent = parent
        self.bottom = WxPanel(self._parent, QRect(100, 718, 1144, 70))

        # 歌曲播放信息区域
        self.infoArea = WxPanel(self.bottom, QRect(0, 0, 1130, 70))

        # 歌曲播放控制区域
        self.ctrlArea = WxPanel(self.bottom, QRect(870, 2, 150, 24))

        # 歌曲播放播放区域
        self.playArea = WxPanel(self.bottom, QRect(1005, 10, 132, 50))

        # 专辑（小）图片
        self.infoPic = QLabel(self.infoArea)
        self.infoPic.setGeometry(7, 7, 58, 58)
        self.infoPic.setStyleSheet("""
                QLabel { 
                    background-color:green;
                }
                """)

        # 歌曲 标题
        self.infoTitle = WxLabel(self.infoArea, QRect(78, 7, 500, 24), "年轮 - 张碧晨")
        self.infoTitle.setStyleSheet("""
                QLabel {
                    font-family:"微软雅黑";
                }
                """)

        # 歌曲 播放进度
        self.infoProgress = WxProgress(self.infoArea)
        self.infoProgress.setGeometry(78, 36, 890, 10)

        # 歌曲 歌词
        self.infoLrc = WxLabel(self.infoArea, QRect(170, 48, 180, 16), "是有缘却无分")
        self.infoLrc.setStyleSheet("""
                QLabel {
                    font-family:"微软雅黑";
                }
                """)

        # 歌曲 当前播放时间
        self.infoTimeStart = WxLabel(self.infoArea, QRect(78, 48, 60, 16), "02:21")
        self.infoTimeStart.setStyleSheet("""
                QLabel {
                    font-family:"微软雅黑";
                }
                """)

        # 歌曲 总时间
        self.infoTimeEnd = WxLabel(self.infoArea, QRect(920, 48, 60, 16), "03:45")
        self.infoTimeEnd.setStyleSheet("""
                QLabel {
                    font-family:"微软雅黑";
                }
                """)
        
        '''
        控制区域：添加到收藏列表、声音、播放列表
        '''
        
        layoutMenu = QHBoxLayout()
        
        # style_icon = qtawesome.icon('fa5s.arrow-right',color=123555) # 顺序
        # style_icon = qtawesome.icon('fa5s.sync-alt',color=123555) # 循环
        # style_icon = qtawesome.icon('fa5s.random',color=123555) # 随机
        # self.ctrl_playmode.setIcon(style_icon)
        # style_icon = qtawesome.icon('fa5s.volume-mute',color=123555) # 静音

        # 控制 播放模式
        self.ctrlPlayMode = WxCtrlButton(self.ctrlArea, QRect(0, 0, 24, 24))
        self.ctrlPlayMode.setQtFontIcon("fa5s.arrow-right", "black")
        self.ctrlPlayMode.setStyleSheet(
            """
        QPushButton { 
            border:none;
            border-radius:15px;
            background-color:rgb(209,232,247);
        } 
        QPushButton:hover { 
            background-color:rgb(129,191,233);
        }
        """
        )
        layoutMenu.addWidget(self.ctrlPlayMode)

        # 控制 添加到
        self.ctrlAddTo = WxCtrlButton(self.ctrlArea, QRect(28, 0, 24, 24))
        self.ctrlAddTo.setQtFontIcon("fa5s.plus", "black")
        self.ctrlAddTo.clicked.connect(self.handleAddTo)
        self.ctrlAddTo.setStyleSheet(
            """
        QPushButton {
            background-color:rgb(209,232,247);
            border:none;
            border-radius:15px;
        } 
        QPushButton:hover {
            background-color:rgb(129,191,233);
        }
        """
        )
        layoutMenu.addWidget(self.ctrlAddTo)

        # 控制 声音
        self.ctrlVoice = WxCtrlButton(self.ctrlArea, QRect(54, 0, 24, 24))
        self.ctrlVoice.setQtFontIcon("fa5s.volume-down", "balck")  # 有声音
        self.ctrlVoice.clicked.connect()
        self.ctrlVoice.setStyleSheet(
            """
        QPushButton {
            background-color:rgb(209,232,247);
            border:none;
            border-radius:15px;
        } 
        QPushButton:hover {
            background-color:rgb(129,191,233);
        }"""
        )
        layoutMenu.addWidget(self.ctrlVoice)

        # 歌曲列表
        self.ctrlPlaylist = WxCtrlButton(self.ctrlArea, QRect(80, 0, 24, 24))
        self.ctrlPlaylist.setQtFontIcon("fa5s.bars", "black")  # 列表
        self.ctrlPlaylist.clicked.connect()
        self.ctrlPlaylist.setStyleSheet(
            """
        QPushButton {
            background-color:rgb(209,232,247);
            border:none;
            border-radius:15px;
        } 
        QPushButton:hover {
            background-color:rgb(129,191,233);
        }
        """
        )
        layoutMenu.addWidget(self.ctrlPlaylist)
    
        
        '''
        控制区域：播放、暂停、上一首、下一首
        '''
            
        layoutControl =  QHBoxLayout()
        
        # 控制 上一首
        self.playPrevieous = WxCtrlButton(self.playArea, QRect(0, 16, 32, 32))
        self.playPrevieous.setQtFontIcon("fa5s.angle-double-left", "black")
        self.playPrevieous.click.connect(self.emitPrevious)
        self.playPrevieous.setStyleSheet(
            """
        QPushButton{
            border:none;
            border-radius:15px;
            background-color:rgb(209,232,247);
        }
        QPushButton:hover{
            background-color:rgb(129,191,233);
        }
        """
        )
        layoutControl.addWidget(self.playPrevieous)

        # 控制 播放
        self.playPause = WxCtrlButton(self.playArea, QRect(40, 0, 48, 48))
        self.playPause.setQtFontIcon("fa5s.play", "black")
        self.playPause.clicked.connect(self.emitPlayPause)
        self.playPause.setStyleSheet(
            """
        QPushButton{
            border:none;
            border-radius:22px;
            background-color:rgb(209,232,247);
        }
        QPushButton:hover{
            background-color:rgb(129,191,233);
        }
        """
        )
        layoutControl.addWidget(self.playPrevieous)

        # 控制 下一首
        self.playNext = WxCtrlButton(self.playArea, QRect(96, 16, 32, 32))
        self.playNext.setQtFontIcon("fa5s.angle-double-right", "black")
        self.playNext.clicked.connect(self.emitNext)
        self.playNext.setStyleSheet(
            """
        QPushButton{
            background-color:rgb(209,232,247);
            border:none;
            border-radius:15px;
        }
        QPushButton:hover{
            background-color:rgb(129,191,233);
        }
        """
        )
        
    def emitPrevious(self):
        self.previous.emit()
    
    def emitPlayPause(self):
        self.play.emit()
    
    def emitNext(self):
        self.next.emit()
    
    
    def handleAddTo():
        pass
    
