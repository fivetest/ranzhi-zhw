#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: zhanghanwen
from selenium import webdriver
import unittest
import ddt,time
from lib.utils import captureScreen #从其他人家下加的某文件中引用某个函数

def get_data():
    L = []
    data_file = 'data/test_data.txt'

    fp = open(data_file,'r')
    for line in fp.readlines():   #readlines 读取多行全部行，readline（）  读取某一行
        tmp = line.strip().split(',')
        L.append(tmp)
    fp.close()
    return L

@ddt.ddt  # 声明这个类要使用ddt要进行数据驱动
class RanzhiLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost/ranzhi/www"

    def tearDown(self):
        self.driver.quit()

    @ddt.unpack
    @ddt.data(*get_data())
    def test_login_test(self,username, password, type):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("account").clear()
        driver.find_element_by_id("account").send_keys(username)
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(password)
        driver.find_element_by_id("submit").click()
        time.sleep(3)
        captureScreen(driver)
        # 下面的str(type) 强制类型转换把传进来的type转换成字符串，防止TYPE类型是真 和==后的真有冲突
        if str(type) == 'True':
            self.assertEqual(u'然之协同',driver.title,u'断言标题必须是然之协同')
            self.assertIn(u'退出', driver.page_source, u'断言页面中包含退出')
            ad_text = driver.find_element_by_xpath("//div[@id='home']/nav/div/ul/li/a").text
            self.assertIn('admin', ad_text)
        else:
            # 登录失败，会弹出提示框
            self.assertIn(u'登录失败', driver.page_source)



