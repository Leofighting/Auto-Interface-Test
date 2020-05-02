# -*- coding:utf-8 -*-
__author__ = "leo"

import os
import json

base_path = os.path.dirname(os.getcwd())


class HandleJson:
    """处理 json 文件"""

    @staticmethod
    def read_json(file_name=None):
        """
        读取 json 文件
        :param file_name: 文件名
        :return: json 文件内容
        """
        if file_name is None:
            file_path = base_path + "/config/user_data.json"
        else:
            file_path = base_path + file_name
        with open(file_path, encoding="utf-8") as f:
            data = json.load(f)

        return data

    def get_value(self, key, file_name=None):
        """
        根据关键字，在 json 文件获取对应值
        :param key: 关键字
        :param file_name: 文件名
        :return: 对应的值
        """
        data = self.read_json(file_name)
        return data.get(key)

    @staticmethod
    def write_value(data, file_name=None):
        """
        向 json 文件写入内容
        :param data: 内容
        :param file_name: 文件名
        :return:
        """
        if file_name is None:
            path = base_path + "/config/cookie.json"
        else:
            path = base_path + file_name
        data_value = json.dumps(data)
        with open(path, "w") as f:
            f.write(data_value)


handle_json = HandleJson()
