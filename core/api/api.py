"""
@ Class-Name: KuWo
@ Author: Cunfu Peng
@ Date: 2021/11/08
@ Last-Edit-Time: 2021/11
@ Version: 1.2
音乐API，所有音乐源必须根据接口实现API
"""
from abc import ABCMeta, abstractmethod


class Api(object):
    __metaclass__ = ABCMeta

    def __init__(self) -> None:
        pass

    @abstractmethod
    def sourceList():
        pass

    # 获取歌曲详细信息
    @abstractmethod
    def musicInfoGet():
        pass

    @abstractmethod
    def recommendList():
        pass

    @abstractmethod
    def songList():
        pass

    # 单曲搜索，歌单搜索
    @abstractmethod
    def searchSingle(self, **kwargs):
        # 通过歌曲名称搜索
        if kwargs.get("name") is not None:
            pass
        # 通过歌手名称搜索
        if kwargs.get("author") is not None:
            pass
        # 搜索歌单
        if kwargs.get("listname") is not None:
            pass

    @abstractmethod
    def musicLrcGetById():
        pass

    @abstractmethod
    def musicUrlGetById():
        pass

    @abstractmethod
    def musicSourceGetByUrl():
        pass

    @abstractmethod
    def albumPicUrlGetById():
        pass
