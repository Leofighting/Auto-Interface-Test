# -*- coding:utf-8 -*-
__author__ = "leo"

from util.handle_json import handle_json
from deepdiff import DeepDiff


class HandleResult:
    """结果处理"""

    @staticmethod
    def get_result(url, code):
        """
        获取结果
        :param url: url连接
        :param code: 对应结果的编码
        :return: 返回结果信息
        """
        data = handle_json.get_value(url, "/config/code_message.json")
        if data:
            for item in data:
                message = item.get(str(code))
                if message:
                    return message

        return None

    @staticmethod
    def get_json_result(dict1, dict2):
        """对比两个字典是否发生变更"""
        # 先判断两个传入值是否为字典
        if isinstance(dict1, dict) and isinstance(dict2, dict):
            cmp_dict = DeepDiff(dict1, dict2, ignore_order=True).to_dict()
            if cmp_dict.get("dictionary_item_added") or cmp_dict.get("dictionary_item_removed"):
                return False
            else:
                return True

        return False

    @staticmethod
    def get_result_json(url, status):
        """
        获取结果
        :param url: url 接口
        :param status: 状态码
        :return: json格式的结果
        """
        data = handle_json.get_value(url, "/config/result.json")
        if data:
            for item in data:
                message = item.get(status)
                if message:
                    return message
        return None


handle_result = HandleResult()
