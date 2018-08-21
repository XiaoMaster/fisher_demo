# _*_ encoding:utf-8 _*_
__author__ = 'xiao'
__date__ = '2018/8/17 11:04'

from flask import Flask
from flask import make_response
import helper

"""
入口
参数会被作为Flask对象的标识
"""
app = Flask(__name__)

"""
    这里路径 /hello/ 会兼容/hello 实质上是flask在接收到/hello请求时会做会返回301状态码  跳转到/hello/
    这样做的原因在于保持url唯一性  这里涉及到SEO
"""


# 注册路由的第一种方式
# @app.route("/hello/")
def hello():
    # num = 1/0

    response = make_response("<html><p style='color:red'>Hello Flask 哈哈哈</p></html>", 200)
    response.headers = {
        'content-type': 'text/html;charset=utf-8',
    }
    return response


@app.route("/book/search/<q>/<page>")
def search(q, page):
    """
    搜索书籍
    :param q: 搜索关键字  或  isbn
    :param page:
    """
    isbn_or_key = helper.verify_isbn_or_word(q)


# 注册路由的第二种方式
app.add_url_rule("/hello/", view_func=hello)

# 导入配置文件路径
app.config.from_object("config")

print(app.config)

# 生产环境下  nginx+uwsgi   通过uwsgi加载fisher模块启动  因此不会执行app.run
# 如果不加if判断  uwsgi一旦加载fisher模块便会额外启动服务器
if __name__ == "__main__":
    # debug 开启调试模式   修改代码自动重启服务器  会将异常显示到浏览器中
    # host="0.0.0.0" 指定可以通过任意地址访问 非 localhost 、127.0.0.1
    """
     * Debug mode: on
     * Running on http://127.0.0.1:8080/ (Press CTRL+C to quit)
     * Restarting with stat
     * Debugger is active!
     * Debugger PIN: 180-447-295
    """
    app.run(host="0.0.0.0", port=8080, debug=app.config["DEBUG"])
