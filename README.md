## 接口自动化测试

#### 整体架构

> 逻辑控制层
>
> - `ddt`库：数据驱动
> - `unittest`库：自动化测试框架
> - `requests库：HTTP客户端库`
> - `openpyxl`库：处理 Excel 文件
>
> 持久层
>
> - Excel：保存用例信息
> - logging 库：日志记录
>
> 展示层
>
> - `HTMLTestRunner_PY3` 库：输出测试报告
>
> 其他：
>
> - `Flask`：`Web` 应用框架
> - Fiddler：抓包工具，获取与校验接口
> - git：代码管理
> - mock 库：模拟接口数据



#### 整体目录结构

> `app`：运用 Flask 框架开发的简易数据输入平台
>
> base：用例基类，处理基础配置
>
> case：测试用例，使用 Excel 保存
>
> `config`：基础配置信息，保存cookie，header，user_data 等 `json` 格式数据
>
> report：保存测试报告 HTML 文件
>
> run：测试执行文件
>
> templates：前端页面 HTML 文件
>
> unit：数据处理
>
> - `condition_data.py`：处理 前置条件 数据
> - `handle_cookie.py`：处理 cookie 数据
> - `handle_excel.py`：处理 Excel 文件数据
> - `handle_header.py`：处理请求头 信息
> - `handle_json.py`：处理 `json` 文件数据
> - `handle_result.py`：处理 结果 数据

