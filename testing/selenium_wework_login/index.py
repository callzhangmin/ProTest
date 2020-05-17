#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/17 14:25
# @Author : zhangmin
# @File : index.py
from selenium import webdriver
class Index:
    def __init__(self):
        self._driver = webdriver.Chrome()
