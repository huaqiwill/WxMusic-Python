# @File: settings.py 音乐辅助工具
# @Author: CunFu Peng
# @Created: 2021-11-15
# @Updated: 2023
# @Version: 2.1

class TFyMusicHelper(object):

    # 将整数的duration转换为字符串，以（分：秒）的形式返回
    @staticmethod
    def durationToString(duration: int):
        duration = int(duration / 1000)
        sec = duration % 60
        min_ = int((duration - sec) / 60)
        sec = "00" + str(sec)
        min_ = "00" + str(min_)
        sec = sec[sec.__len__() - 2:]
        min_ = min_[min_.__len__() - 2:]
        return min_ + ":" + sec

    @staticmethod
    def stringToDuration(durationString: str):
        return 0
