"""
@ Class-Name: QQ
@ Author: Cunfu Peng
@ Date: 2021/11/08
@ Last-Edit-Time: 2021/11
@ Version: 1.2
QQ音乐API
"""
from core.api.api import Api
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
}

class QQ(Api):
    def sourceList():
        pass

    def searchSingle(self, **kwargs):
        return super().searchSingle(**kwargs)
    
    def songList():
        pass
    
    