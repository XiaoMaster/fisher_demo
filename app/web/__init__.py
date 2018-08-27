# _*_ encoding:utf-8 _*_
from flask import Blueprint

__author__ = 'xiao'
__date__ = '2018/8/23 09:38'

# 蓝图
web_blue_print = Blueprint("web", __name__)

from . import book
from . import user
