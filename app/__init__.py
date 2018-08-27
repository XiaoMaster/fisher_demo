# _*_ encoding:utf-8 _*_
from flask import Flask

from app.models.book import db

__author__ = 'xiao'
__date__ = '2018/8/23 09:34'


def init_app():
    app = Flask(__name__)

    print("app id {}".format(id(app)))

    # 导入配置文件路径
    app.config.from_object("app.setting")
    app.config.from_object("app.secure")

    register_blue_print(app)

    db.init_app(app)
    db.create_all(app=app)

    return app


def register_blue_print(app):
    from app.web import web_blue_print
    app.register_blueprint(web_blue_print)
