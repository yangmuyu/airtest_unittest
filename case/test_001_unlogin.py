# -*- coding:utf-8 -*-
import unittest
from BeautifulReport import BeautifulReport
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
import logging
logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR) #屏蔽非错误日志
import sys
root_path = os.path.abspath(__file__)
root_path = '/'.join(root_path.split('/')[:-2])
sys.path.append(root_path)
from common import *

PACKAGE_NAME = "com.tencent.mm" #微信

class test_001_unlogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
        sleep(2)
        start_app(PACKAGE_NAME)

    @classmethod
    def tearDownClass(cls):
        stop_app(PACKAGE_NAME)

    def setUp(self):
        sleep(5)

    def tearDown(self):
        sleep(2)

    def save_img(self, img_name):
        snapshot(img_name)

    @BeautifulReport.add_test_img('test01enter_unlogin') #运行失败时截图保存到测试报告
    @retry(max_n=2) #运行失败时重试max_n次
    def test01enter_unlogin(self):
        '''your test case 1'''
        #self.poco(text="通讯录").click()
        keyevent("HOME")

    @BeautifulReport.add_test_img('test02enter_unlogin')
    @retry(max_n=2)
    def test02enter_unlogin(self):
        '''your test case 2'''
        #self.poco(text="我").click()
        keyevent("HOME")

if __name__ == "__main__":
    unittest.main(verbosity=2)