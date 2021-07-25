# -*- coding:utf-8 -*-
import unittest
import os
from BeautifulReport import BeautifulReport
import time
root_path = os.getcwd()

case_file = "test_*.py"

def allTest():
    cur_path = os.path.dirname(os.path.realpath(__file__))
    casepath = os.path.join(cur_path, "case")
    suite = unittest.TestLoader().discover(
        start_dir=casepath,  # 文件地址
        pattern=case_file,  # 文件类型
        top_level_dir=None)
    return suite

def run():
    #unittest.TextTestRunner(verbosity=2).run(allTest())

    result = BeautifulReport(allTest())
    nowtime = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
    result.report(filename='测试报告' + nowtime, description='测试报告', report_dir='report', theme='theme_default')

if __name__ == "__main__":
    run()