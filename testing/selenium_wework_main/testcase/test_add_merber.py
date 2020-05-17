#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/17 15:31
# @Author : zhangmin
# @File : test_add_merber.py

from testing.selenium_wework_main.page.main import Main


class TestAddMember:
    def setup(self):
        self.main = Main()

    def test_addmember(self):
        add_member = self.main.goto_add_member().add_member()
        assert "azhangmin" in add_member.get_member()

    # def test_addmember1(self):
    #     add_member1 = self.main.goto_member().add_member()
    #     assert "azhangmin" in add_member1.get_member()

