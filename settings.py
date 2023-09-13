# @File: settings.py 配置文件
# @Author: CunFu Peng
# @Created: 2021-11-15
# @Updated: 2023
# @Version: 2.1

# 是否为调试版
DEBUG = True


# 字体配置信息
class Font:
    size = 0
    color = "white"

    # 字体颜色预设
    class Color:
        white = 0
        black = 1


FONT_SIZE = 14  # 字体大小
# ["白色","蓝色","黑色","红色"]
FONT_COLOR = "white"  # 字体颜色
FONT_FAMILY = "微软雅黑"  # 字体名称

# 背景颜色
BK_COLOR = 1
# 主题颜色
THEME_COLOR = 0

# 开机自启动
START_OPEN = True
# 显示歌词
SHOW_LRC = True
# 图标颜色
NAV_ICON_COLOR = "black"


class Resource(object):
    pass
