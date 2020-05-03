# -*- coding:utf-8 -*-
__author__ = "leo"

import json

from util.handle_excel import excel_data
from jsonpath_rw import parse


class ConditionData:
    """前置条件数据处理"""

    @staticmethod
    def split_data(data):
        """数据切分"""
        result = data.split(">")
        case_id = result[0]
        rule_data = result[1]
        return case_id, rule_data

    def depend_data(self, data):
        """依赖数据"""
        case_id = self.split_data(data)[0]
        row_number = excel_data.get_row_number(case_id)
        row_data = excel_data.get_cell_value(row_number, 14)
        return row_data

    @staticmethod
    def get_depend_data(key, data):
        """获取依赖字段"""
        data = json.loads(data)
        json_exe = parse(key)
        result = json_exe.find(data)
        return [item.value for item in result][0]

    def get_data(self, data):
        """获取依赖数据"""
        res_data = self.depend_data(data)
        rule_data = self.split_data(data)[1]
        return self.get_depend_data(rule_data, res_data)


condition_data = ConditionData()
