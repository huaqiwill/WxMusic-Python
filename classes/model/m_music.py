# @File:
# @Author: CunFu Peng
# @Created: 2023-8-21
# @Updated:
# @Version: 1.0

from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from classes.model.m_album import IAlbum

from classes.model.m_author import IAuthor

# Base = declarative_base()


# class SQLUser(Base):
#     __tablename = "user"
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     name = Column(String(20))
#     url = Column(String(255))


class SourceFrom:
    Native = 0
    Url = 1


class IMusic(object):
    id: int
    name: str
    duration: int
    authors: list[IAuthor]
    url: str
    path: str
    albums: list[IAlbum]
    pic: str
    alias: str
    albumName: str
    authorName: str
    sourceFrom: str
    path: str

    def __init__(self, music):
        # 编号
        self.id = getattr(music, "id", None)
        # 歌曲名称
        self.name = getattr(music, "name", None)
        # 歌曲时长
        self.duration = getattr(music, "duration", None)
        # 作者
        self.authors = getattr(music, "authors", None)
        # 歌曲的下载地址
        self.url = getattr(music, "url", None)
        # 歌曲在本地的路径
        self.path = getattr(music, "path", None)
        # 歌曲的所属专辑
        self.albums = getattr(music, "albums", None)
        # 歌曲的封面
        self.pic = getattr(music, "pic", None)
        #
        self.alias = getattr(music, "alias", None)
        self.albumName = getattr(music, "albumName", None)
        self.authorName = getattr(music, "authorName", None)
        self.sourceFrom = getattr(music, "sourceFrom", None)
        self.path = getattr(music, "path", None)
