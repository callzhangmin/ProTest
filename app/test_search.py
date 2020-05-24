#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/24 15:09
# @Author : zhangmin
# @File : test_search.py
from appium import webdriver


class TestWeiXin:
    def setup(self):
        self.desired_caps = {}
        self.desired_caps['platformName'] = 'Android'
        self.desired_caps['platformVersion'] = '6.0.1'
        self.desired_caps['deviceName'] = '127.0.0.1:7555'
        self.desired_caps['appPackage'] = 'com.tencent.wework'
        self.desired_caps['appActivity'] = '.launch.LaunchSplashActivity'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver = quit()

    def test_add(self):
        pass
