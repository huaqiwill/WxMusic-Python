# @File: settings.py 日志工具
# @Author: CunFu Peng
# @Created: 2021-11-15
# @Updated: 2023
# @Version: 2.1

import settings as settings
import os
import time

_basePath = os.getcwd()
_curPath = _basePath + "/logs/"


# 日志工具
class LoggerHelper:
    # 输出到日志文件
    @staticmethod
    def log(msg):
        print(msg)
        t = time.time()
        f = open(file=_curPath + t + ".log", mode="a")
        f.write(t + " " + msg)
        f.close()

    # 错误日志
    @staticmethod
    def error(msg, log=False):
        print(msg)
        if log:
            LoggerHelper.log(msg)

    # 调试日志
    @staticmethod
    def debug(msg, log=False):
        if settings.DEBUG:
            print(msg)
        if log:
            LoggerHelper.log(msg)

    # 普通日志
    @staticmethod
    def info(msg, log=False):
        print(msg)
        if log:
            LoggerHelper.log(msg)

    # 警告消息
    @staticmethod
    def warn(msg, log=False):
        print(msg)
        if log:
            LoggerHelper.log(msg)
