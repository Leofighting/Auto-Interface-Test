# -*- coding:utf-8 -*-
__author__ = "leo"


class ConditionData:
    def split_data(self, data):
        result = data.split(">")
        case_id = result[0]
        rule_data = result[1]
        return case_id, rule_data
