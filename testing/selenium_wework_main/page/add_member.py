#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/17 15:08
# @Author : zhangmin
# @File : add_member.py
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from testing.selenium_wework_main.page.base import BasePage


class AddMember(BasePage):
    def add_member(self):
        sleep(2)
        self._driver.find_element(By.ID, 'username').send_keys("azhangmin")
        self._driver.find_element(By.ID, 'memberAdd_acctid').send_keys("zhangmin")
        self._driver.find_element(By.ID, 'memberAdd_phone').send_keys("15088748900")
        self._driver.find_element(By.CSS_SELECTOR, '.js_btn_save').click()
        sleep(5)
        return True

    def get_member(self):
        elements = self._driver.find_elements(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
        return [element.get_attribute("title") for element in elements]
