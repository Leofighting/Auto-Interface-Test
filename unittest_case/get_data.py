# -*- coding:utf-8 -*-
__author__ = "leo"

import json

from mitmproxy import http

from util.handle_json import handle_json


class GetData:
    def request(self, flow):
        request_data = flow.request
        self.request_url = request_data.url
        request_pr = request_data.query
        request_form = request_data.urlencoded_form
        # print("url:===> ", self.request_url)
        # print("pr====> ", request_pr)
        # print("request_form====> ", request_form)

    def response(self, flow):
        if "imooc" in self.request_url or "mukewang" in self.request_url:
            response_data = flow.response
            host = self.request_url.split(".com")
            base_url = host[0]
            path_url = host[1]
            if "?" in path_url:
                path_url = path_url.split("?")[0]

            data = json.dumps(handle_json.get_value(path_url))

            response_data.set_text(data)

            # response_header = response_data.headers
            # content_type = response_header["Content-Type"]
            # if "application/json" in content_type or "image/jpeg" in content_type:
            #     print("这是图片文字")
            # else:
            #     print("content-type===> ", content_type)
            #     print("code===> ", response_data.status_code)
            #     print("response===> ", response_data.text)


addons = [
    GetData()
]
