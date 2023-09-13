# @File:
# @Author: CunFu Peng
# @Created: 2023-8-21
# @Updated:
# @Version: 1.0

class IAlbum(object):
    def __init__(self, album):
        self.id = getattr(album, "id", None)
        self.picId = getattr(album, "picId", None)
        self.picUrl = getattr(album, "picUrl", None)
        self.name = getattr(album, "name", None)
