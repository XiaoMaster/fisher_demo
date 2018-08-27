# _*_ encoding:utf-8 _*_

import requests

__author__ = 'xiao'
__date__ = '2018/8/21 16:19'


# urllib  python 自带的http请求库
# requests 第三方请求库

class Http:
    # Http(object)
    @staticmethod
    def get(url, return_json=True):
        r = requests.get(url)
        if r.status_code != 200:
            return {} if return_json else ""
        return r.json() if return_json else r.text
