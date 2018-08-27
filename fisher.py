# _*_ encoding:utf-8 _*_
from app import init_app

__author__ = 'xiao'
__date__ = '2018/8/17 11:04'

"""
入口
参数会被作为Flask对象的标识
"""

"""
    这里路径 /hello/ 会兼容/hello 实质上是flask在接收到/hello请求时会做会返回301状态码  跳转到/hello/
    这样做的原因在于保持url唯一性  这里涉及到SEO
"""

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


# 注册路由的第二种方式
app.add_url_rule("/hello/", view_func=hello)

print(app.config)
"""
app = init_app()

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
    print("启动的app id {}".format(id(app)))

    app.run(host="0.0.0.0", port=8080, debug=app.config["DEBUG"])
