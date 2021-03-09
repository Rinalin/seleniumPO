#!/user/bin/env python
# -*- coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self,driver:WebDriver=None):
        if driver == None:
            option = Options()
            option.debugger_address = '127.0.0.1:9222'
            self.driver = webdriver.Chrome(options=option)
            self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
            self.driver.implicitly_wait(5)
        else:
            self.driver = driver

        base_url = ''
        if base_url !='':
            self.driver.get(base_url)

    def wait(self,by,locator):
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable((by,locator)))
