#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: zhanghanwen
import os
import time
import unittest
import HTMLTestRunner
from testcases.login_test import RanzhiLogin

if __name__ == '__main__':
    suite = unittest.TestSuite()#创建一个测试套，测试套是用来装测试用例的对象
    loader = unittest.TestLoader()#加载器，用来加载对象
    suite.addTests(loader.discover('testcases', pattern='*.py'))  # 在指定的目录下匹配模式，满足的都自动添加到suite
    # suite.addTests(loader.loadTestsFromTestCase(RanzhiLogin))  # 把测试类中的测试用例添加到suite里

    # 如果没有reports目录，就自动创建一个
    if not os.path.exists("./reports"):
        os.makedirs("./reports")
    if not os.path.exists("./screenshots"):
        os.makedirs('./screenshots')

    fp = file('./reports/test_result_%s.html' % time.strftime("%Y-%m-%d %H-%M-%S"), 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u"然之登录测试结果",
        description=u"详细信息如下"
    )
    runner.run(suite)
    fp.close()
