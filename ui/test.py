from PyQt5.QtQuick import QQuickView
from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtQml, QtQuick
import sys
import os

str = "windows.qml"

path = os.getcwd() + "\\ui\\qml\\" + str
if not os.path.exists(path):
    print("文件不存在")
else:
    print("文件存在")
app = QtWidgets.QApplication(sys.argv)
engine = QtQml.QQmlApplicationEngine(path)  # 显示window界面
sys.exit(app.exec_())
