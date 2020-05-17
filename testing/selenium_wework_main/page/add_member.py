#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/17 15:08
# @Author : zhangmin
# @File : add_member.py
from selenium.webdriver.common.by import By

from testing.selenium_wework_main.page.base import BasePage


class AddMember(BasePage):
    def add_member(self):
        self.find(By.ID,'username').send_keys('张敏')
        self.find(By.ID,'memberAdd_english_name').send_keys('小张')
        self.find(By.ID, 'memberAdd_acctid').send_keys('NIUKOU')
        self.find_radio("1").click()
        self.find(By.ID,'memberAdd_phone').send_keys('11111111111')
        self.find(By.CSS_SELECTOR, '.js_btn_save').click()