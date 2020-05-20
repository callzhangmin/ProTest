#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/17 14:57
# @Author : zhangmin
# @File : main.py
from selenium.webdriver.common.by import By
from testing.selenium_wework_main.page.add_member import AddMember
from testing.selenium_wework_main.page.base import BasePage


class Main(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame"

    def goto_addmember(self):
        """
        :nth-child(n) 选择器匹配属于其父元素的第 N 个子元素，不论元素的类型。
        """
        self.find(By.CSS_SELECTOR,".index_service_cnt_itemWrap:nth-child(1)").click()
        return AddMember(self._driver)
