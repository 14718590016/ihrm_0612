import os
import unittest
import time

import HTMLTestRunner_PY3

import app
from script.test_emp_params import TestIHRMEmployeeParams
from script.test_login_params import TestIHRMEmployeeParams02

# 2 创建测试套件
suite = unittest.TestSuite()
# 3 将测试用例添加到测试套件（csript里的两个文件的类名）
suite.addTest(unittest.makeSuite(TestIHRMEmployeeParams))
suite.addTest(unittest.makeSuite(TestIHRMEmployeeParams02))
# 4 定义生成测试报告在哪个目录和报告名称
report_path = app.BASE_DIR + "/report/ihrm{}.html".format(time.strftime('%Y%m%d %H%M%S'))
# report_path = app.BASE_DIR + "/report/ihrm.html"
# 5 使用HTMLTestRunner_PY3生成测试报告
with open(report_path, mode='wb') as f:
    # 实例化HTMLTestRunner_PY3
    runner = HTMLTestRunner_PY3.HTMLTestRunner(f, verbosity=1, title="ihrm系统部门接口测试",
                                               description="我们的IHRM的部门接口测试报告")
    # 使用实例化的runner运行测试套件，生成测试报告
    runner.run(suite)

