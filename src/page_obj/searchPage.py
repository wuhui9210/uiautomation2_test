# -*- coding:utf-8 -*-
# ================================
# @Time   : 2020/9/20 17:51
# @File   : searchPage.py
# @Author : WU
# ================================
import time

from src.page_obj.basePage import Page


class HomePage(Page):

    def baidu_search(self, keyword):
        print('打开百度')
        self.open_url('http://www.baidu.com')
        time.sleep(2)
        print('输入关键字', keyword)
        self.send_keys('kw', keyword)
        print('点击百度一下')
        self.click_button('su')
