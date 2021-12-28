'''
    Basepage类是POM中的基类，主要用于提供常用的函数，为页面对象进行服务
    Selenium常用函数：
        元素定位
        输入
        点击
        访问URl
        等待
        关闭
'''
from time import sleep

from selenium import webdriver


class BasePage:
    # 虚构driver对象
    driver = webdriver.Chrome()
    #构造函数
    def __init__(self,driver):
        self.driver=driver


    # 访问url
    def visit(self):
        self.driver.get(self.url)

    # 元素定位
    #loc 表示定位方法和定位的值，打包成元组形式
    def locator(self, loc):
        return self.driver.find_element(*loc)

    # 输入
    def input_(self, loc, txt):
        self.locator(loc).send_keys(txt)

    # 点击
    def click(self, loc):
        self.locator(loc).click()

    # 等待
    def wait(self, time_):
        sleep(time_)
    # 关闭
