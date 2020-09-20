# -*- coding:utf-8 -*-
# ================================
# @Time   : 2020/9/20 14:42
# @File   : basePage.py
# @Author : WU
# ================================
from selenium import webdriver
from selenium.webdriver.common.by import By


class Page:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *ele):
        # if mode == 'id':
        #     self.element = self.driver.find_element(By.ID, ele)
        # elif mode == 'className':
        #     self.element = self.driver.find_element(By.CLASS_NAME, ele)
        # elif mode == 'xpath':
        #     self.element = self.driver.find_element(By.XPATH, ele)
        return self.driver.find_element(By.ID, ele)

    def send_keys(self, ele, keyword):
        return self.find_element(ele).send_keys(keyword)

    def click_button(self, ele):
        return self.find_element(ele).click()

    def open_url(self, url):
        return self.driver.get(url)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.find_element()
