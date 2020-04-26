# -*- coding:utf-8 -*-
__author__ = "leo"

from util.handle_json import handle_json


class HandleHeader:
    def get_header(self):
        data = handle_json.read_json("/config/header.json")
        return data


handle_header = HandleHeader()
