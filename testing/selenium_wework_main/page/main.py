#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/17 14:57
# @Author : zhangmin
# @File : main.py
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from testing.selenium_wework_main.page.add_member import AddMember
from testing.selenium_wework_main.page.base import BasePage


class Main(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame"
    def goto_add_member(self):
        self._driver.find_element(By.CSS_SELECTOR, '.index_service_cnt_itemWrap:nth-child(1)').click()
        return AddMember(self._driver)

    def goto_member(self):
        self._driver.find_element(By.ID,"menu_contacts").click()
        return AddMember(self._driver)