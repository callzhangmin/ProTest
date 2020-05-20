#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/19 23:42
# @Author : zhangmin
# @File : apptestdemo.py
from appium import webdriver
import pytest
from selenium.webdriver.common.by import By


desired_caps = {}
desired_caps['platformName'] = 'Android'     # 安卓系统
desired_caps['platformVersion'] = '6.0.1'      # 连接的设备Android版本
desired_caps['deviceName'] = '127.0.0.1:7555'      # 我的手机设备名称
desired_caps['appPackage'] = 'com.xueqiu.android'  # 雪球app的包名
desired_caps['appActivity'] = '.view.WelcomeActivityAlias'  #  app 的主 activity（启动的第一个页面）
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)  # 连通过 ip 和端口 连接模拟器
driver.find_element(By.CSS_SELECTOR,".android.widget.RelativeLayout:nth-child(3)").click()
