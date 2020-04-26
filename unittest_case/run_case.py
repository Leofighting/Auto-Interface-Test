# -*- coding:utf-8 -*-
__author__ = "leo"

import os
import unittest

# from unittest_case.test_case01 import TestCase01
# from unittest_case.test_case02 import TestCase02
# from unittest_case.test_case03 import TestCase03
#
# case01 = unittest.TestLoader().loadTestsFromTestCase(TestCase01)
# case02 = unittest.TestLoader().loadTestsFromTestCase(TestCase02)
# case03 = unittest.TestLoader().loadTestsFromTestCase(TestCase03)
#
# suite = unittest.TestSuite([case01, case02, case03])
# unittest.TextTestRunner().run(suite)

case_path = os.getcwd()
print(case_path)

discover = unittest.defaultTestLoader.discover(case_path)
unittest.TextTestRunner().run(discover)