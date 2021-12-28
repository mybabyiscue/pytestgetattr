# coding:utf8


# @Time:    2021/12/23 22:11
# @Auth:    xiejun
# @filename:
import time

from selenium import webdriver


class Webkey:

    def __init__(self):
        """
        构造函数，创建必要的实例变量
        """
        self.driver = None

    def openbrowser(self,br='gc'):
        """
        打开浏览器
        :param br: gc=谷歌；ff=Firefox；ie=IE
       :return:
        """
        if br == 'gc':
            self.driver = webdriver.Chrome()
        elif br == 'ff':
            self.driver = webdriver.Firefox()
        elif br == 'ie':
            self.driver = webdriver.Ie()
        else:
            print('浏览器暂不支持！请在此添加实现代码')
        #默认隐式等待
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def geturl(self,url=None):
        """
        打开浏览器
        :param url:
        :return:
        """
        self.driver.get(url)


    def __find_ele(self,locator=''):
        """
        支持8种定位方式
        :param locator:
        :return:
        """
        ele = None
        self.ele = None
        if locator.startswith('xpath='):
            ele = self.driver.find_element_by_xpath(
                locator[locator.find('=')+1:])
        elif locator.startswith('id='):
            ele = self.driver.find_element_by_xpath(
                locator[locator.find('=')+1:])
        elif locator.startswith('name='):
            ele = self.driver.find_element_by_xpath(
                locator[locator.find('=')+1:])
        elif locator.startswith('tag_name='):
            ele = self.driver.find_element_by_xpath(
                locator[locator.find('=')+1:])
        elif locator.startswith('link_text='):
            ele = self.driver.find_element_by_xpath(
                locator[locator.find('=')+1:])
        elif locator.startswith('partial_link_text='):
            ele = self.driver.find_element_by_xpath(
                locator[locator.find('=')+1:])
        elif locator.startswith('css_selector='):
            ele = self.driver.find_element_by_xpath(
                locator[locator.find('=')+1:])
        else:
            ele = self.driver.find_element_by_xpath(locator)
        self.ele = ele
        return ele

    def click(self,locator=None):
        """
        找到元素，并点击元素
        :param locator:定位器，默认xpath
        :return:
        """
        ele = self.__find_ele(locator)
        ele.click()

    def input(self,locator=None,value=None):
        """
        找到元素，并完成输入
        :param locator: 定位器，默认xpath
        :param value: 需要输入的字符串
        :return:
        """
        ele = self.__find_ele(locator)
        ele.send_keys(value)

    def intoiframe(self,locator=None):
        ele = self.__find_ele(locator)
        self.driver.switch_to.frame(ele)

    def sleep(self,t=1):
        """
        固定等待
        :param t: 默认1s
        :return:
        """
        time.sleep(t)

    def closebrower(self):
        self.driver.quit()
if __name__ == "__main__":
    pass
