# -*- coding:utf-8 -*-
# ================================
# @Time   : 2020/9/20 0:43
# @File   : conftest.py
# @Author : WU
# ================================
import pytest
from selenium import webdriver


@pytest.fixture()
def driver_init():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.close()
