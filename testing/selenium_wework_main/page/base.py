#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/17 16:29
# @Author : zhangmin
# @File : base.py
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class BasePage:
    _driver = None
    _base_url = ""

    def __init__(self, driver: webdriver):
        if driver is None:
            options = Options()
            options.debugger_address = "127.0.0.1:9222"
            self._driver = webdriver.Chrome(options=options)

        else:
            self._driver = driver

        if self._base_url != "":
            self._driver.get(self._base_url)

    def find(self, by, locator):
        return self._driver.find_element(by, locator)

    def finds(self, by, locator):
        return self._driver.find_elements(by, locator)