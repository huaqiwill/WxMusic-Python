# @File: settings.py 数据库管理
# @Author: CunFu Peng
# @Created: 2021-11-15
# @Updated: 2023-8-20
# @Version: 2.1

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from PyQt5.QtSql import QSql
from sqlalchemy.ext.declarative import declarative_base
from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session
from sqlalchemy import select


class Base(DeclarativeBase):
    pass


# class User(Base):
#     __tablename = "user"
#     id: Mapped[int] = mapped_column(primary_key=True)
#     name: Mapped[str] = mapped_column(String(30))


# 数据库管理工具
class DbHelper(object):
    base = declarative_base()

    def __init__(self):
        self._engine = create_engine("sqlite:///D:/date2.db", echo=True)
        self._session = Session(self._engine)
        self.base.metadata.create_all(self._engine)

    def commit(self):
        self.session.commit()

    # 获取会话
    @property
    def session(self):
        return self._session

    # def get_users(self, where):
    #     stmt = select(User).where()
    #     return self.session.scalar(stmt)

    # def get_user(self):
    #     stmt = select(User).where()
    #     return self.session.scalar(stmt).one()

    # def add_user(self, user: User):
    #     self.session.add(user)

    # def remove_user(self, user_id):
    #     user = self.session.get(User, user_id)
        