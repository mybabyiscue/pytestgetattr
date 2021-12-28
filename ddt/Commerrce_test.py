# coding:utf8


# @Time:    2021/12/23 21:46
# @Auth:    xiejun
# @filename: 
import time

import allure
import pytest

from Web.webkeys import Webkey
from lib.read_yaml import readyaml

@allure.feature('电商项目Web自动化测试')
class TestComm:
    """
    电商项目PO封装
    """

    @allure.title('打开浏览器')
    @classmethod
    def setup_class(cls):
        """
        构造函数，创建对象的时候会执行
        :return:
        """
        cls.web = Webkey()
        cls.web.openbrowser()

    @allure.story('登录')
    @pytest.mark.parametrize('listcases',readyaml('./lib/cases.yaml')['loginpage'])
    def test_login(self,listcases):
        try:
            allure.dynamic.title(listcases['title'])
            allure.description(listcases['description'])
        except Exception as e:
            pass
        """
        登录成功的用例
        :return:
        """
        #利用反射机制
        testcases = listcases['cases']
        for cases in testcases:
            listcase = list(cases.values())
            with allure.step(listcase[0]):
                func = getattr(self.web,listcase[1])
                values = listcase[2:]
                func(*values)

    @classmethod
    def teardown_class(cls):
         cls.web.closebrower()




if __name__ == "__main__":
    pytest.main('-sv')
