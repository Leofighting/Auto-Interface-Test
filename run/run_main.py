# -*- coding:utf-8 -*-
__author__ = "leo"

import json

from base.base_request import request
from util.condition_data import condition_data
from util.handle_excel import excel_data
from util.handle_header import handle_header
from util.handle_result import handle_result
from util.handle_cookie import handle_cookie


class RunMain:
    """主运行文件"""

    @staticmethod
    def run_case():
        """运行用例"""
        rows = excel_data.get_rows()

        for i in range(2, rows + 1):
            data = excel_data.get_rows_value(i)
            cookie = None
            get_cookie = None
            header = None
            depend_data = None
            is_run = data[2]

            if is_run == "yes":
                is_depend = data[3]
                data1 = json.loads(data[7])
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
                    if message == config_message:
                        excel_data.excel_write_data(i, 13, "case 通过")
                    else:
                        excel_data.excel_write_data(i, 13, "case 失败")
                        excel_data.excel_write_data(i, 14, json.dumps(res))

                if excepted_method == "error_code":
                    if str(excepted_result) == str(code):
                        excel_data.excel_write_data(i, 13, "case 通过")
                    else:
                        excel_data.excel_write_data(i, 13, "case 失败")
                        excel_data.excel_write_data(i, 14, json.dumps(res))

                if excepted_method == "json":
                    if code == 1000:
                        status = "sucess"
                    else:
                        status = "error"
                    expected_result = handle_result.get_result_json(url, status)
                    result = handle_result.get_json_result(res, expected_result)
                    if result:
                        excel_data.excel_write_data(i, 13, "case 通过")
                    else:
                        excel_data.excel_write_data(i, 13, "case 失败")
                        excel_data.excel_write_data(i, 14, json.dumps(res))


if __name__ == '__main__':
    run = RunMain()
    run.run_case()
