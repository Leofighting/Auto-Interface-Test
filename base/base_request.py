# -*- coding:utf-8 -*-
__author__ = "leo"

import json

import requests

from util.handle_ini import handle_ini
from util.handle_json import handle_json
from util.handle_cookie import handle_cookie


class BaseRequest:
    def send_post(self, url, data, cookie=None, get_cookie=None, header=None):
        response = requests.post(url=url, data=data, cookies=cookie, headers=header)

        if get_cookie:
            cookie_value_jar = response.cookies
            cookie_value = requests.utils.dict_from_cookiejar(cookie_value_jar)
            handle_cookie.write_cookie(cookie_value, get_cookie["is_cookie"])
        res = response.text
        return res

    def send_get(self, url, data, cookie=None, get_cookie=None, header=None):
        response = requests.get(url=url, params=data, cookies=cookie, headers=header)

        if get_cookie:
            cookie_value_jar = response.cookies
            cookie_value = requests.utils.dict_from_cookiejar(cookie_value_jar)
            handle_cookie.write_cookie(cookie_value, get_cookie["is_cookie"])
        res = response.text

        return res

    def run_main(self, method, url, data, cookie=None, get_cookie=None, header=None):
        base_url = handle_ini.get_value("host")
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
