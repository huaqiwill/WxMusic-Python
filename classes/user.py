from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base  # ORM(对象关系映射)的基类

Base = declarative_base()


# class User(Base):
#     def __init__(self):
#         self.__tablename = "user"
#         self.id = Column(Integer, primary_key=True)
#         self.name = Column(String(20), default=None, nullable=False, comment="用户名")
#         self.phone = Column(String(20), default=None, nullable=False, comment="电话")

#     def __repr__(self):
#         # __repr__函数定义该类返回的字符串内容
#         return f"User Name {self.name},phone {self.phone}"
