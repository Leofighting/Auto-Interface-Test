# -*- coding:utf-8 -*-
__author__ = "leo"

import json
import os
import time
import unittest

import ddt
import HTMLTestRunner_PY3

from base.base_request import request
from util.condition_data import condition_data
from util.handle_cookie import handle_cookie
from util.handle_excel import excel_data
from util.handle_header import handle_header
from util.handle_result import handle_result

test_data = excel_data.get_excel_data()


@ddt.ddt
class TestRunCaseDdt(unittest.TestCase):
    """以数据驱动运行测试"""

    @ddt.data(*test_data)
    def test_main_case(self, data):
        """测试用例"""
        cookie = None
        get_cookie = None
        header = None
        depend_data = None
        case_id = data[0]
        is_run = data[2]
        i = excel_data.get_row_number(case_id)

        if is_run == "yes":
            is_depend = data[3]
            data1 = json.loads(data[7])
            try:
                if is_depend:
                    """获取依赖数据"""
                    depend_key = data[4]
                    depend_data = condition_data.get_data(is_depend)
                    data1[depend_key] = depend_data

                method = data[6]
                url = data[5]

                cookie_method = data[8]
                is_header = data[9]
                excepted_method = data[10]
                excepted_result = data[11]

                if cookie_method == "yes":
                    cookie = handle_cookie.get_cookie_value("app")

                if cookie_method == "write":
                    get_cookie = {"is_cookie": "app"}

                if is_header == "yes":
                    header = handle_header.get_header()

                res = request.run_main(method=method, url=url, data=data1,
                                       cookie=cookie, get_cookie=get_cookie, header=header)

                code = res["errorCode"]
                message = res["errorDesc"]
                if excepted_method == "mec":
                    config_message = handle_result.get_result(url, code)
                    try:
                        self.assertEqual(message, config_message)
                        excel_data.excel_write_data(i, 13, "case 通过")
                    except Exception as e:
                        excel_data.excel_write_data(i, 13, "case 失败")
                        excel_data.excel_write_data(i, 14, json.dumps(res))
                        raise e

                if excepted_method == "error_code":
                    try:
                        self.assertEqual(str(excepted_result), str(code))
                        excel_data.excel_write_data(i, 13, "case 通过")
                    except Exception as e:
                        excel_data.excel_write_data(i, 13, "case 失败")
                        excel_data.excel_write_data(i, 14, json.dumps(res))
                        raise e

                if excepted_method == "json":
                    if code == 1000:
                        status = "sucess"
                    else:
                        status = "error"
                    expected_result = handle_result.get_result_json(url, status)
                    result = handle_result.get_json_result(res, expected_result)
                    if result:
                        try:
                            self.assertTrue(result)
                            excel_data.excel_write_data(i, 13, "case 通过")
                        except Exception as e:
                            excel_data.excel_write_data(i, 13, "case 失败")
                            excel_data.excel_write_data(i, 14, json.dumps(res))
                            raise e
            except Exception as e:
                excel_data.excel_write_data(i, 13, "case 失败")
                raise e


if __name__ == '__main__':
    base_path = os.path.dirname(os.getcwd())
    case_path = os.getcwd()
    discover = unittest.defaultTestLoader.discover(case_path, pattern="run_case*.py")
    file_name = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
    html_file = base_path + "/report/" + file_name + "_report.html"

    with open(html_file, "wb") as f:
        runner = HTMLTestRunner_PY3.HTMLTestRunner(stream=f, title="Leo Report",
                                                   description="An Interface Test Report~~")
        runner.run(discover)
