# -*- coding:utf-8 -*-
# ================================
# @Time   : 2020/9/20 22:12
# @File   : testSearch.py
# @Author : WU
# ================================
import time
import pytest

from src.page_obj.searchPage import HomePage


class TestSearch:

    def test_search(self, driver_init):
        home = HomePage(driver_init)
        home.baidu_search('自动化测试')
        time.sleep(1)
        assert '自动化' in driver_init.title

    @pytest.mark.skip
    def test_search2(self, driver_init):
        pass


if __name__ == '__main__':
    pytest.main(['-s', 'testSearch.py'])
