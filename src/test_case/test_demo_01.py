# -*- coding:utf-8 -*-
# ================================
# @Time   : 2020/9/20 13:22
# @File   : test_demo_01.py
# @Author : WU
# ================================
import pytest


class TestDemo01:

    @pytest.fixture()
    def setup_init(self):
        print('开始测试。。。')
        yield
        print('测试结束。。。')

    def add(self, a, b):
        return a + b

    def test_case_01(self, setup_init):
        assert 2 == self.add(1, 1)

    def test_case_02(self, setup_init):
        assert 2 == self.add(1, 2)


if __name__ == '__main__':
    pytest.main(['-q', 'test_demo_01.py'])
