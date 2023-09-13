
"""
@ Class-Name: KuWo
@ Author: Cunfu Peng
@ Date: 2021/11/08
@ Last-Edit-Time: 2021/11
@ Version: 1.2
酷我音乐API
"""
from core.api.api import Api
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
}

class KuWo(Api):
    def get_recommond():
        url = "http://www.kuwo.cn/rankList"
        global headers
        requests.get(url,headers=headers)

    def get_songlist():
        pass
    
    def single_search():
        pass
    
    def get_childlist():
        pass

    