# _*_ encoding:utf-8 _*_
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from flask_sqlalchemy import SQLAlchemy
__author__ = 'xiao'
__date__ = '2018/8/23 11:42'

db = SQLAlchemy()

class Book(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    author = Column(String(30), default="未名")
    binding = Column(String(20))
    publisher = Column(String(50))
    price = Column(String(20))
    page = Column(Integer)
    pubdate = Column(String(20))
    isbn = Column(String(15), nullable=False, unique=True)
    summary = Column(String(1000))
    image = Column(String(50))
