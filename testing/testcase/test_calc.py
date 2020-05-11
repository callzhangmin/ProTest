#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/7 21:17
# @Author : zhangmin
# @File : test_calc.py


from python.calc import Calc
import pytest
import yaml

class TestCalc:
    def setup(self):
        self.calc = Calc()

    @pytest.mark.parametrize("data1,data2,expect",yaml.safe_load(open('../datas/add.yaml')))
    def calc_add(self,data1,data2,expect):
        result = self.calc.add(data1,data2)
        assert expect == result


if __name__ == '__main__':
    pytest.main()
