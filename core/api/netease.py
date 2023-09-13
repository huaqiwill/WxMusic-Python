"""
@ Class-Name: KuWo
@ Author: Cunfu Peng
@ Date: 2021/11/08
@ Last-Edit-Time: 2021/11
@ Version: 1.2
网易云音乐API
"""

import requests
import json
import csv
from bs4 import BeautifulSoup
from core.api.api import Api
from classes.model import IAlbum, IAuthor, IMusic


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
}


class Netease(Api):
    """
    net_recommond_dic = {
    "飙升榜": "https://music.163.com/discover/toplist?id=19723756",
    "新歌榜": "https://music.163.com/discover/toplist?id=3779629",
    "原创榜": "https://music.163.com/discover/toplist?id=2884035",
    "热歌榜": "https://music.163.com/discover/toplist?id=3778678"
    }
    """

    def SourceList():
        # 音乐源
        music_source_lists = {
            "网易云": {
                "热歌榜": "https://music.163.com/discover/toplist?id=3778678",
                "新歌榜": "https://music.163.com/discover/toplist?id=3779629",
                "原创榜": "https://music.163.com/discover/toplist?id=2884035",
                "飙升榜": "https://music.163.com/discover/toplist?id=19723756",
            },
            "酷狗": {
                "飙升榜": "https://www.kugou.com/yy/rank/home/1-6666.html?from=rank",
                "TOP500": "https://www.kugou.com/yy/rank/home/1-8888.html?from=rank",
                "抖音热歌榜": "https://www.kugou.com/yy/rank/home/1-52144.html?from=rank",
                "快手热歌榜": "https://www.kugou.com/yy/rank/home/1-52767.html?from=rank",
                "国风新歌榜": "https://www.kugou.com/yy/rank/home/1-33161.html?from=rank",
                "电音热歌榜": "https://www.kugou.com/yy/rank/home/1-33160.html?from=rank",
                "影视金曲榜": "https://www.kugou.com/yy/rank/home/1-33163.html?from=rank",
            },
            "QQ": {
                "飙升榜": "https://y.qq.com/n/ryqq/toplist/62",
                "热歌榜": "https://y.qq.com/n/ryqq/toplist/26",
                "新歌榜": "https://y.qq.com/n/ryqq/toplist/27",
                "国风热歌榜": "https://y.qq.com/n/ryqq/toplist/65",
            },
            "酷我": {
                "飙升榜": "http://www.kuwo.cn/rankList",
                "热歌榜": "http://www.kuwo.cn/rankList",
                "新歌榜": "http://www.kuwo.cn/rankList",
            },
        }
        return music_source_lists

    # 获取音乐推荐列表
    def recommendList(
            url: str = "https://music.163.com/discover/toplist?id=3778678",
    ):
        '''
        返回数据格式
        rst_songlist = net_music().get_recommoned()
        duration = rst_songlist[0]["duration"]
        name =  rst_songlist[0]["name"]
        id = rst_songlist[0]["id"]

        albumn =  rst_songlist[0]["album"]
        albumn_picurl = albumn["picUrl"]
        albumn_id = albumn["id"]
        albumn_name = albumn["name"]

        artists =  rst_songlist[0]["artists"]
        artists_id = artists[0]["id"]
        artists_name = artists[0]["id"]
        '''
        # url = "https://music.163.com/discover/toplist?id=3778678"
        global headers
        html = requests.get(url, headers=headers).content
        # tree = etree.HTML(rst).xpath("@id=song-list-pre-cache/textarea/text()")
        soup = BeautifulSoup(html, "html.parser", from_encoding="utf-8").find(
            attrs={"id": "song-list-pre-data"}
        )
        return json.loads(soup.get_text())

    def songList(page: int, cat: str):
        '''
        获取歌单
        cat = [
            "全部",
            {"语种":["日语","韩语","欧美","粤语"]},
            {"风格":["流行","摇滚","民谣","民族","电子","爵士","乡村","古典","古风"]},
            {"场景":["清晨","夜晚","学习","工作","旅行","散步","酒吧"]},
            {"情感":["怀旧","清新","浪漫","治愈","伤感","思念"]},
            {"主题":["KTV","影视原声","校园","经典","翻唱","游戏"]}
        ]
        '''
        url = "https://music.163.com/discover/playlist"
        page *= 35
        params = {
            "order": "hot",
            "cat": cat,
            "limit": "35",
            "offset": str(page)
        }

        global headers
        html = requests.get(url, headers=headers, params=params).content

        # 方法一，解析了再返回  测试使用
        # soups = BeautifulSoup(html,"html.parser",from_encoding="utf-8").find(attrs={"id":"m-pl-container"}).find_all("li")
        # print(soups.__len__())

        # 方法二：在外部使用正则解析 优点：速度更快
        soups = (
            BeautifulSoup(html, "html.parser", from_encoding="utf-8")
            .find(attrs={"id": "m-pl-container"})
            .find_all("li")
        )
        print(soups.__len__())

        musics = list[IAlbum]()
        for soup in soups:
            music = IAlbum()
            img = soup.find("img")
            music.img = img.get("src")
            name = soup.find("a")
            music.href = name.get("href")
            music.title = name.get("title")
            musics.append(music)
        return musics

    def searchSingle(name: str, song_num: int = 100) -> list:
        '''
        单曲搜索

        数据返回格式
        id = data[0]["id"]
        name = data[0]["name"]
        alias = data[0]["alias"]
        duration = data[0]["duration"]

        artists = data[0]["artists"]
        artists_id = artists[0]["id"]
        artists_name = artists[0]["name"]

        album = data[0]["album"]
        album_id = album["id"]
        album_picId = album["picId"]
        album_name = album["name"]
        '''
        url = (
            'http://music.163.com/api/search/get/web?csrf_token=hlpretag=&hlposttag=&s={"'
            + name
            + '"}'
            "&type=1&offset=0&total=true&limit=" + str(song_num)
        )

        data = requests.get(url, headers=headers).json()["result"]["songs"]

        music_list = list[IMusic]()

        for song in data:
            m = IMusic()
            m.id = data.get("id")
            m.name = song.get("name")
            m.alias = song.get("alias")
            m.duration = song.get("duration")
            m.authors.append(IAuthor(song[0].get("album")))

        return music_list

    # 获取歌单中的歌曲信息
    def get_childlist(url: str):
        # url = "https://music.163.com/playlist?id=6733647208"
        global headers
        html = requests.get(url=url, headers=headers).content
        soups = (
            BeautifulSoup(html, "html.parser", from_encoding="utf-8")
            .find(attrs={"class": "f-hide"})
            .find_all("a")
        )

        # for soup in soups:
        #     href = soup.get("href")
        #     title = soup.get_text()

        return soups

    def musicLrcGetById():
        '''
        获取音乐歌词
        '''
        br = "96000"
        # 通过urls获取歌词
        url = "http://music.163.com/api/song/media?id={0}".format(song_id)
        rst = requests.get(url).json()["lyric"]
        return rst

    def get_musicUrl_byId(song_id: str):
        '''获取音乐地址'''
        url = "http://music.163.com/song/media/outer/url?id={0}.mp3".format(
            song_id)
        return url

    # 通过音乐url获取音乐资源并写到文件
    def get_musicSource_byUrl(song_url: str, file_name: str) -> bool:
        """
        此处详细注释：
        1. 音乐通过GET外链，返回状态码为302
        2. 从Response Headers中获取Location的值才是真正的音乐地址
        3. GET新的链接

        为什么Python可以通过修改Headers就直接爬取到资源？
            因为其内部对其使用了重定向。
        """
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36",
            "Accept": "image/gif, image/x-xbitmap, image/jpeg, image/pjpeg, application/x-shockwave-flash, application/vnd.ms-excel, application/vnd.ms-powerpoint, application/msword, */*",
            "Content-Type": "application/x-www-form-urlencoded",
        }
        rst = requests.get(song_url, headers=headers).content
        # print(rst["Location"])
        with open(file_name, mode="wb") as f:
            f.write(rst)
        return True

    def get_album_picUrl_byPicId(pic_id: str):
        # 暂未实现该方法

        return pic_id
