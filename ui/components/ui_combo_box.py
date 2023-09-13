# @File:
# @Author: CunFu Peng
# @Created: 2023-8-21
# @Updated:
# @Version: 1.0

from PyQt5.QtWidgets import QComboBox


class WxComboBox(QComboBox):
    def __init__(self, parent):
        super().__init__(parent)
