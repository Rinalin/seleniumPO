#!/user/bin/env python
# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from PO_shizhan.page.basepage import BasePage


class AddMember(BasePage):
    def add_member(self,user_name,user_acct,user_phone):
        #name
        self.driver.find_element(By.CSS_SELECTOR,'#username').send_keys(user_name)
        #acct
        self.driver.find_element(By.CSS_SELECTOR,'#memberAdd_acctid').send_keys(user_acct)
        #phone
        self.driver.find_element(By.CSS_SELECTOR,'#memberAdd_phone').send_keys(user_phone)
        self.driver.find_element(By.XPATH,"//a[text()='保存']").click()
        #保存后获取列表成员名称

    def get_member(self):
        self.wait(By.CSS_SELECTOR,'.ww_checkbox')
        member_eles = self.driver.find_elements(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
        names = []
        for member_ele in member_eles:
            name = member_ele.get_attribute('title')
            names.append(name)
        return names