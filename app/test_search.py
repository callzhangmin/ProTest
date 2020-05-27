#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/24 15:09
# @Author : zhangmin
# @File : test_search.py
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestWeiXin:
    def setup(self):
        self.desired_caps = {}
        self.desired_caps['platformName'] = 'Android'
        self.desired_caps['platformVersion'] = '6.0.1'
        self.desired_caps['deviceName'] = '127.0.0.1:7555'
        self.desired_caps['appPackage'] = 'com.tencent.wework'
        self.desired_caps['noReset'] = "true"
        self.desired_caps['appActivity'] = '.launch.LaunchSplashActivity'
        self.desired_caps['skipServerInstallation'] = True
        self.desired_caps['skipDeviceInitialization'] = True
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_addcontact(self):
        print("添加联系人")
        self.driver.find_element(MobileBy.XPATH, "//*android.widget.TextView[@text='通讯录']").click()
        self.driver.find_element(MobileBy.XPATH, "//*android.widget.TextView[@text='添加成员']").click()
        self.driver.find_element(MobileBy.XPATH, "//*android.widget.TextView[@text='手动输入添加']").click()
        self.driver.find_element(MobileBy.XPATH, "//*android.widget.TextView[@text='姓名　']/..//*[@class='android.widget.EditText']").send_keys(
            "张敏")
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[@text='性别']/..//*[contains(@class, 'TextView') and @text='男']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[@text='手机　']/..//*[contains(@class, 'EditText')]").send_keys("15397399245")
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[@text='邮箱　']/..//*[contains(@class, 'EditText')]").send_keys("531474715@163.com")
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/gvk").click()
        sleep(1)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成功']")
    def test_delcontact(self):
        print('删除联系人')
        self.driver.find_element(MobileBy.XPATH,"//*[@text='通讯录']").click()
        els2 = driver.find_elements_by_id("drb")
        els3 = driver.find_elements_by_id("drb[1]")
        els4 = driver.find_elements_by_xpath("//*android.widget.TextView[@text='通讯录']")


