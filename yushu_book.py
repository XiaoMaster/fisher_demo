# _*_ encoding:utf-8 _*_
from flask import current_app

from httper import Http

__author__ = 'xiao'
__date__ = '2018/8/21 16:53'


class YuShuBook:
    per_page = 15
    isbn_url = "http://t.yushu.im/v2/book/isbn/{}"
    keyword_url = "http://t.yushu.im/v2/book/search?q={}&count={}&start={}"

    @classmethod
    def search_by_isbn(cls, isbn):
        url = cls.isbn_url.format(isbn)
        result = Http.get(url)
        return result

    @classmethod
    def search_by_keyword(cls, keyword, page=1):
        url = cls.keyword_url.format(keyword, current_app.config["PER_PAGE"], cls.calculate_start(page))
        result = Http.get(url)
        return result

    @classmethod
    def calculate_start(cls, page):
        return (page - 1) * current_app.config["PER_PAGE"]
