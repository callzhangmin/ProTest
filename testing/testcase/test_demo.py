#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/14 20:31
# @Author : zhangmin
# @File : test_demo.py



import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestDemo():

    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_demo(self):
        self.driver.get("https://home.testing-studio.com/")
        # self.driver.find_element(By.ID, 'menu_contacts').click(
        sleep(5)
if __name__ == '__main__':
    pytest.main()