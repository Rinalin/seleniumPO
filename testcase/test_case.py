#!/user/bin/env python
# -*- coding:utf-8 -*-
from PO_shizhan.page.index_page import IndexPage


class TestCase:
    def setup(self):
        self.index = IndexPage()

    def test_add_member(self):
        user_name = '0002'
        user_acct = '0002'
        user_phone = '13100010002'

        turn_add_member = self.index.goto_add_member()
        turn_add_member.add_member(user_name,user_acct,user_phone)
        names = turn_add_member.get_member()
        assert user_name in names