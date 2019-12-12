from selenium import webdriver
import time
from PIL import ImageGrab
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *

driver = webdriver.Chrome()


def sleep_hand(*args):#多此一举 显式暂停
    time.sleep(*args)


def opens(*args):#打开url
    driver.get(*args)
    driver.maximize_window()
    driver.implicitly_wait(2)
# def click(*args):
#     try:
#         element = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath(*args))
#         element.click()
#     except:
#         print('元素不存在')
#
# def send(path,sendfor):
#
#     element = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath(path))
#     element.clear()
#     element.send_keys(sendfor)
# def isdisplayed(path):#判断是否显示
#     try:
#         items = driver.find_element_by_xpath(path).is_displayed()
#         return items
#     except:
#         print('元素不存在')


# def _getfor(post, attribute):
#     return WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath(post)).get_attribute(attribute)
def jietu():
    ImageGrab.grab().save('E:\\Automationtest\\save\\%s.jpg' % str(time.strftime("%y-%m-%d %H_%M_%Y")))

# class _element(object):
#     def __init__(self,
#                  _path=None,
#                  sendfor=None,
#                  _searchfor=None,
#                  _motion=None,
#                  waittime=2
#                  ):
#         self.waittime = waittime
#         self._path = _path
#         self.sendfor = sendfor
#         self._searchfor = _searchfor
#         element = WebDriverWait(driver, waittime).until(lambda x: x.find_element_by_xpath(_path))
#         if _motion == 'click':
#             try:
#                 element.click()
#             except ElementNotVisibleException:
#                 raise
#             except TimeoutException:
#                 raise
#         if _motion == 'send':
#             """
#             send:发送信息
#             """
#             element.clear()
#             element.send_keys(sendfor)
#         if _motion == 'getfor':#
#             """
#             获取元素属性
#             """
#             try:
#                 element.get_attribute(_searchfor)
#             except:
#                 print('未找到元素')
#         if _motion == '_isdisplayed':
#             """
#             #判断是否可见
#             """
#             try:
#                 element.is_displayed()
#             except TimeoutException:
#                 raise print('元素不可见')
#             # driver.find_element_by_xpath(_path).is_displayed()
#         else:
#             pass


class _Element(object):
    def __init__(self,
                 _path,
                 _motion,
                 sendfor='',
                 waittime=2
                 ):
        self.waittime = waittime
        self._path = _path
        self.sendfor = sendfor
        if _motion == 'click':
            try:
                WebDriverWait(driver, waittime).until(lambda x: x.find_element_by_xpath(_path)).click()
            except ElementNotVisibleException:
                raise
            except TimeoutException:
                raise
        if _motion == 'send':
            """
            send:发送信息
            """
            WebDriverWait(driver, waittime).until(lambda x: x.find_element_by_xpath(_path)).clear()
            WebDriverWait(driver, waittime).until(lambda x: x.find_element_by_xpath(_path)).send_keys(sendfor)
        if _motion == 'getfor':
            """
            获取元素属性
            """
            try:
                WebDriverWait(driver, waittime).until(lambda x: x.find_element_by_xpath(_path)).get_attribute(sendfor)
            except:
                print('未找到元素')
        if _motion == '_isdisplayed':
            """
            #判断是否可见
            """
            try:
                WebDriverWait(driver, waittime).until(lambda x: x.find_element_by_xpath(_path)).is_displayed()
            except TimeoutException:
                raise print('元素不可见')
            # driver.find_element_by_xpath(_path).is_displayed()
        else:
            pass
        if _motion == 'iframe':
            """切入iframe"""
            try:
                driver.switch_to.frame(_path)
            except:
                raise print('请核对iframe元素位置')
        if _motion == 'outiframe':
            """退出iframe到主界面"""
            try:
                driver.switch_to.default_content()
            except:
                raise print('请核对iframe元素位置')


# if __name__ == '__main__':
#     jietu()