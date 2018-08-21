# _*_ encoding:utf-8 _*_
__author__ = 'xiao'
__date__ = '2018/8/21 16:19'
import requests


# urllib  python 自带的http请求库
# requests 第三方请求库
class Http:
    def get(self, url, return_json=True):
        r = requests.get(url)
        if return_json:
            return r.json()
        else:
            return r.text
