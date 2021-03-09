#!/user/bin/env python
# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from PO_shizhan.page.add_member import AddMember
from PO_shizhan.page.basepage import BasePage


class IndexPage(BasePage):
    base_url = "https://work.weixin.qq.com/wework_admin/frame#index"
    def goto_add_member(self):
        self.driver.find_element(By.XPATH,"//div[@class='index_service_cnt js_service_list']/a/div").click()
        return AddMember(self.driver)
