'''
信号和槽
定义信号
定义槽
'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QMainWindow


class UIMain(QMainWindow):
    clicked = pyqtSignal()

    def __init__(self):
        super(QMainWindow, self).__init__()
        w = QWidget()
        button = QPushButton()
        button.setText("你说话啊")
        button.clicked.connect(self.clicked.emit)
        h = QHBoxLayout()
        h.addWidget(button)
        w.setLayout(h)
        self.setCentralWidget(w)

def handle():
    print("Hello World")

if __name__ == "__main__":
    clicked = pyqtSignal()
    app = QApplication(sys.argv)
    print("程序正在启动中...")
    win = UIMain()
    win.clicked.connect(handle)
    win.show()
    print("启动成功！")
    sys.exit(app.exec_())
    
    
