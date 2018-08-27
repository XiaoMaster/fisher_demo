# _*_ encoding:utf-8 _*_
import json

from flask import request, jsonify
from app.forms.book import SearchForm
from . import web_blue_print
from yushu_book import YuShuBook

import helper

__author__ = 'xiao'
__date__ = '2018/8/21 17:46'


@web_blue_print.route("/book/search")
def search():
    """
    搜索书籍
    :param q: 搜索关键字  或  isbn
    :param page:
    """
    search_validator = SearchForm(request.args)

    if search_validator.validate():

        q = search_validator.q.data.strip()
        page = search_validator.page.data

        isbn_or_key = helper.verify_isbn_or_word(q)
        if isbn_or_key == "isbn":
            result = YuShuBook.search_by_isbn(q)
        else:
            result = YuShuBook.search_by_keyword(q, page)

        return json.dumps(result), 200, {"content-type": "application/json"}
    else:
        return jsonify(search_validator.errors)
