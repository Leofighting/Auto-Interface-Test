# -*- coding:utf-8 -*-
__author__ = "leo"

import json

import requests

from config import settings
from util.handle_cookie import handle_cookie


class BaseRequest:
    """基础配置"""

    @staticmethod
    def send_post(url, data, cookie=None, get_cookie=None, header=None):
        """发送post请求"""
        response = requests.post(url=url, data=data, cookies=cookie, headers=header)

        if get_cookie:
            cookie_value_jar = response.cookies
            cookie_value = requests.utils.dict_from_cookiejar(cookie_value_jar)
            handle_cookie.write_cookie(cookie_value, get_cookie["is_cookie"])
        res = response.text
        return res

    @staticmethod
    def send_get(url, data, cookie=None, get_cookie=None, header=None):
        """发送 get 请求"""
        response = requests.get(url=url, params=data, cookies=cookie, headers=header)

        if get_cookie:
            cookie_value_jar = response.cookies
            cookie_value = requests.utils.dict_from_cookiejar(cookie_value_jar)
            handle_cookie.write_cookie(cookie_value, get_cookie["is_cookie"])
        res = response.text

        return res

    def run_main(self, method, url, data, cookie=None, get_cookie=None, header=None):
        """执行主方法"""
        base_url = settings.HOST
        if "http" not in url:
            url = base_url + url
        if method == "post":
            res = self.send_post(url, data, cookie, get_cookie, header)
        else:
            res = self.send_get(url, data, cookie, get_cookie, header)
        try:
            res = json.loads(res)
        except:
            print("结果是一个 text")
        return res


request = BaseRequest()
