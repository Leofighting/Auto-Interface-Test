# -*- coding:utf-8 -*-
__author__ = "leo"

import json

from util.handle_json import handle_json


class MockServer:

    def request(self, flow):
        request_data = flow.request
        self.request_url = request_data.url
        request_pr = request_data.query
        request_form = request_data.urlencoded_form

    def response(self, flow):
        if "imooc" in self.request_url or "mukewang" in self.request_url:
            response_data = flow.response
            host = self.request_url.split(".com")
            url = host[1]

            if "?" in url:
                url = url.split("?")[0]

            data = json.dumps(handle_json.get_value(url))
            response_data.set_text(data)


addons = [
    MockServer()
]