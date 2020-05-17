#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/17 16:29
# @Author : zhangmin
# @File : base.py
from time import sleep

from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    _driver = None
    _base_url = ""
    """
    隐性等待:implicitly_wait(xx),隐形等待是设置了一个最长等待时间，如果在规定时间内网页加载完成，则执行下一步，否则一直等到时间截止，然后执行下一步。
    显性等待:WebDriverWait,配合该类的until()和until_not()方法,程序每隔xx秒看一眼，如果条件成立了，则执行下一步，否则继续等待，直到超过设置的最长时间，然后抛出TimeoutException
    selenium的expected_conditions模块一般也简称EC，收集了一系列的场景判断方法
    """

    def __init__(self, driver: WebDriver = None):
        if driver is None:
            # options = Options()
            # options.debugger_address = "127.0.0.1:9222"
            self._driver = webdriver.Chrome()
            self._driver.implicitly_wait(3)  # 隐式等待
        else:
            self._driver = driver

        if self._base_url != "":
            self._driver.get(self._base_url)


    def find(self, by, locator):
        return self._driver.find_element(by, locator)

    def finds(self, by, locator):
        return self._driver.find_elements(by, locator)

    def wait_for_click(self, locator, time=10):
        try:
            WebDriverWait(self._driver, time).until(EC.element_to_be_clickable(locator))
        except TimeoutException as e:
            print(e)
        except NoSuchElementException as e:
            print(e)
        except Exception as e:
            print(e)

    def wait_for_elem(self, conditions, time=10):
        try:
            WebDriverWait(self._driver, time).until(conditions)
        except TimeoutException as e:
            print(e)
        except NoSuchElementException as e:
            print(e)
        except Exception as e:
            print(e)

    def find_radio(self, value):
        self._driver.find_element_by_xpath("//input[@value=%s]" % value)
