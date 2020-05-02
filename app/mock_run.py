# -*- coding:utf-8 -*-
__author__ = "leo"

import json

from flask import Flask
from util.handle_json import handle_json

app = Flask(__name__)


@app.route("/mock", methods=["POST"])
def mock_data(request):
    """模拟数据"""
    return_data = {
        "message": None
    }

    mock_data = handle_json.read_json()
    url = request.form.get("url")
    data = request.form.get("data")
    try:
        data = json.loads(data)
        mock_data[url] = data
    except Exception as e:
        return_data["message"] = "传递的数据不是 json 格式"
        return json.dumps(return_data)

    try:
        handle_json.write_value(mock_data, file_name="/config/user_data.json")
    except Exception as e:
        return_data["message"] = "写入数据失败"
        json.dumps(return_data)

    return_data["message"] = "写入成功~"
    return json.dumps(return_data)


if __name__ == '__main__':
    app.run(debug=True)
