# -*- coding:utf-8 -*-
__author__ = "leo"

import os

from util.handle_json import handle_json


class HandleCookie:
    def get_cookie_value(self, cookie_key):
        data = handle_json.read_json("/config/cookie.json")
        return data[cookie_key]

    def write_cookie(self, new_data, cookie_key):
        data = handle_json.read_json("/config/cookie.json")
        data[cookie_key] = new_data
        handle_json.write_value(data)


handle_cookie = HandleCookie()
