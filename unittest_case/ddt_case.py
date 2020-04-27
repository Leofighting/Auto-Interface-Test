# -*- coding:utf-8 -*-
__author__ = "leo"

import unittest

from ddt import data, ddt

test_data = [[1, 2, 3, 4], [3, 4, 5, 56], [4, 5, 6, 7]]

@ddt
class TestCase01(unittest.TestCase):
    def setUp(self) -> None:
        print("开始")

    def tearDown(self) -> None:
        print("结束")

    @data(*test_data)
    def test_01(self, data1):
        num1, num2, num3, num4 = data1
        print("this is test", num1, num2, num3, num4)


if __name__ == '__main__':
    unittest.main()
