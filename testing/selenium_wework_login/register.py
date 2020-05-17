#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/17 14:35
# @Author : zhangmin
# @File : register.py
from selenium.webdriver.remote.webdriver import WebDriver


class Register:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    def register(self):
        self._driver.find_element()
