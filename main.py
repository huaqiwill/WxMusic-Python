"""
Project: wxMusic
File: main.py 这是程序的启动文件
Author: CunFu Peng
Created: 2021-09-18
Updated: 2021-11-24
Version: 2.1
五音助手

一款集优秀的音乐播放器，并且内置酷狗音乐、网易云音乐、等源
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui import WxMain
from ui.components import WxWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    print("程序正在启动中...")
    win = WxMain()
    win.show()
    print("启动成功！")
    sys.exit(app.exec_())
