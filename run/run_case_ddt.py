# -*- coding:utf-8 -*-
__author__ = "leo"

import json
import os
import time
import unittest

import ddt
import HTMLTestRunner_PY3

from base.base_request import request
from config import settings
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
        # 用例的编号
        case_id = data[settings.CASE_ID]
        # 是否执行
        is_run = data[settings.IS_RUN]
        # 行号
        i = excel_data.get_row_number(case_id)

        if is_run == "yes":
            # 依赖信息
            is_depend = data[settings.IS_DEPEND]
            # 头信息内容
            data1 = json.loads(data[settings.DATA1])
            try:
                if is_depend:
                    """获取依赖数据"""
                    # 依赖关键字
                    depend_key = data[settings.DEPEND_KEY]
                    depend_data = condition_data.get_data(is_depend)
                    data1[depend_key] = depend_data
                # 请求方式
                method = data[settings.METHOD]
                # 接口
                url = data[settings.URL]
                # 是否携带 cookies 或者写入 cookies
                cookie_method = data[settings.COOKIE_METHOD]
                # 是否携带头信息
                is_header = data[settings.IS_HEADER]
                # 预期结果的形式
                excepted_method = data[settings.EXCEPTED_METHOD]
                # 预期结果
                excepted_result = data[settings.EXCEPTED_RESULT]

                # 携带 cookies 时的操作
                if cookie_method == "yes":
                    cookie = handle_cookie.get_cookie_value("app")
                # 写入 cookies 时的操作
                if cookie_method == "write":
                    get_cookie = {"is_cookie": "app"}
                # 是否携带头信息
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
                        excel_data.excel_write_data(i, settings.RESULT, "case 通过")
                    except Exception as e:
                        excel_data.excel_write_data(i, settings.RESULT, "case 失败")
                        excel_data.excel_write_data(i, settings.DATA, json.dumps(res))
                        raise e

                if excepted_method == "error_code":
                    try:
                        self.assertEqual(str(excepted_result), str(code))
                        excel_data.excel_write_data(i, settings.RESULT, "case 通过")
                    except Exception as e:
                        excel_data.excel_write_data(i, settings.RESULT, "case 失败")
                        excel_data.excel_write_data(i, settings.DATA, json.dumps(res))
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
                            excel_data.excel_write_data(i, settings.RESULT, "case 通过")
                        except Exception as e:
                            excel_data.excel_write_data(i, settings.RESULT, "case 失败")
                            excel_data.excel_write_data(i, settings.DATA, json.dumps(res))
                            raise e
            except Exception as e:
                excel_data.excel_write_data(i, settings.RESULT, "case 失败")
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
