# -*- coding:utf-8 -*-
__author__ = "leo"

from util.handle_json import handle_json
from deepdiff import DeepDiff


class HandleResult:
    def get_result(self, url, code):
        data = handle_json.get_value(url, "/config/code_message.json")
        if data:
            for item in data:
                message = item.get(str(code))
                if message:
                    return message

        return None

    def get_json_result(self, dict1, dict2):
        if isinstance(dict1, dict) and isinstance(dict2, dict):
            cmp_dict = DeepDiff(dict1, dict2, ignore_order=True).to_dict()
            # print(cmp_dict)
            if cmp_dict.get("dictionary_item_added") or cmp_dict.get("dictionary_item_removed"):
                return False
            else:
                return True

        return False

    def get_result_json(self, url, status):
        data = handle_json.get_value(url, "/config/result.json")
        if data:
            for item in data:
                message = item.get(status)
                if message:
                    return message
        return None


handle_result = HandleResult()
# dict1 = {"111": "123", "222": "222"}
# dict2 = {"222": "222"}
# print(handle_result.get_json_result(dict1, None))

# print(handle_result.get_result_json("api3/newcourseskill", "sucess"))
