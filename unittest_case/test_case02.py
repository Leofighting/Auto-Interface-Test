# -*- coding:utf-8 -*-
__author__ = "leo"

import unittest
import requests

url = "http://www.imooc.com"
data = {
    "username": "1111",
    "password": "2222"
}


class TestCase02(unittest.TestCase):

    def setUp(self) -> None:
        print("case 开始执行")

    def tearDown(self) -> None:
        print("case 结束")

    @classmethod
    def setUpClass(cls) -> None:
        print("case 类开始执行")

    @classmethod
    def tearDownClass(cls) -> None:
        print("case类 结束执行")

    def test_01(self):
        # res = requests.get(url=url, params=data).json()
        data1 = {
            "user": "123"
        }
        self.assertDictEqual(data1, data)
        print("case01")

    def test_02(self):
        print("case02")

    def test_03(self):
        print("case03")
        flag = True
        self.assertFalse(flag)

    def test_04(self):
        flag = False
        self.assertFalse(flag)
        print("case04")

    def test_05(self):
        print("case05")

    def test_06(self):
        print("case06")


if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    # suite.addTest(TestCase01("test_05"))
    # suite.addTest(TestCase01("test_02"))
    # suite.addTest(TestCase01("test_03"))
    tests = [TestCase01("test_05"), TestCase01("test_02"), TestCase01("test_06")]
    suite.addTests(tests)
    runner = unittest.TextTestRunner()
    runner.run(suite)
