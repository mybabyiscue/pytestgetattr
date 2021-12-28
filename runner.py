# coding:utf8


# @Time:    2021/12/27 23:26
# @Auth:    xiejun
# @filename:
import os

import pytest

if __name__ == "__main__":
    pytest.main(['-sv', 'ddt/Commerrce_test.py', '--alluredir', './result'])
    os.system('allure generate ./result/ -o ./report_allure/ --clean')
