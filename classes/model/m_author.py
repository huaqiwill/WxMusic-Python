# @File:
# @Author: CunFu Peng
# @Created: 2023-8-21
# @Updated:
# @Version: 1.0
class IAuthor(object):
    def __init__(self, author):
        self.name = getattr(author, "name", None)
        self.id = getattr(author, "id", None)
        self.sex = getattr(author, "sex", None)
        self.age = getattr(author, "age", None)
        self.birthDate = getattr(author, "birthDate", None)
