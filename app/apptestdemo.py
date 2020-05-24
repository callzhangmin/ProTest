#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/19 23:42
# @Author : zhangmin
# @File : apptestdemo.py
import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestXueQiu:
    def setup(self):
        self.desired_caps = {}
        self.desired_caps['platformName'] = 'Android'  # 安卓系统
        self.desired_caps['platformVersion'] = '6.0.1'  # 连接的设备Android版本
        self.desired_caps['deviceName'] = '127.0.0.1:7555'  # 我的手机设备名称
        self.desired_caps['appPackage'] = 'com.xueqiu.android'  # 雪球app的包名
        self.desired_caps['appActivity'] = '.view.WelcomeActivityAlias'  # app 的主 activity（启动的第一个页面）
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps)  # 连通过 ip 和端口 连接模拟器
        self.desired_caps['noReset'] = "true"
        self.desired_caps['dontStopAppOnReset'] = 'true'
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.parametrize('searchkey,text,type', [
        ('alibaba', '阿里巴巴', 'BABA'),
        ('xiaomi', '小米集团-W', '01810')
    ])
    def test_search(self,searchkey,text,type):
        try:
            self.driver.find_element(MobileBy.ID,'com.xueqiu.android:id/tv_search').click()
            self.driver.find_element(MobileBy.ID,'com.xueqiu.android:id/search_input_text').send_keys(searchkey)
        except EnvironmentError as e:
            print(e)
