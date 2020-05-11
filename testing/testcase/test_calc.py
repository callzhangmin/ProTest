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

    @pytest.mark.parametrize('num1,num2,expect', yaml.safe_load(open('../datas/add.yml')))
    def calc_add(self, num1, num2, expect):
        result = self.calc.add(num1, num2)
        assert expect == result

    @pytest.mark.parametrize('num1,num2,expect',yaml.safe_load(open('../datas/sub.yml')))
    def calc_sub(self, num1, num2, expect):
        result = self.calc.sub(num1, num2)
        assert expect == result

    @pytest.mark.parametrize('num1,num2,expect', yaml.safe_load(open('../datas/mul.yml')))
    def calc_mul(self, num1, num2, expect):
        result = self.calc.mul(num1, num2)
        assert expect == result

    @pytest.mark.parametrize('num1,num2,expect', yaml.safe_load(open('../datas/div.yml')))
    def calc_div(self, num1, num2, expect):
        result = self.calc.div(num1, num2)
        assert expect == result

if __name__ == '__main__':
    pytest.main()
