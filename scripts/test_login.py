import os
import sys
sys.path.append(os.getcwd())

import pytest

from page.page_login import PageLogin


def get_data():
    return [("13811110000", "123456"), ("13823456789", "0000")]


class TestLogin(object):
    # 初始化
    def setup_class(self):
        # 实例化pagelogin
        self.login = PageLogin()

    # 结束
    def teardown_class(self):
        self.login.driver.quit()

    # 登陆测试方法
    @pytest.mark.parametrize("phone,pwd", get_data())
    def test_login(self, phone, pwd):
        self.login.page_login(phone, pwd)

if __name__ == '__main__':
    pytest.main("-s test_login.py")
