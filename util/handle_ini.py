# -*- coding:utf-8 -*-
__author__ = "leo"

import os

import configparser


class HandleIni:
    def load_ini(self):
        base_path = os.path.dirname(os.getcwd())
        file_path = base_path + "/config/server.ini"
        cf = configparser.ConfigParser()
        cf.read(file_path, encoding="utf-8")
        return cf

    def get_value(self, key, section=None):
        if section is None:
            section = "server"
        cf = self.load_ini()
        try:
            data = cf.get(section, key)
        except:
            print("没有获取到值")
            data = None
        return data


handle_ini = HandleIni()
