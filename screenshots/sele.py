# # import unittest
# #
# # import HtmlTestRunner
# # from framework.method import _element, driver, opens, time
# # from framework.useException import exp
# # from framework.userdate import *
# #
# #
# # class zhuceceshi(unittest.TestCase, zhuce, zhuce_zj, exp):
# #     def setUp(self):
# #         opens('http://192.168.126.2:8080/index')
# #         #opens('https://www.baidu.com')
# #
# #     def tearDown(self):
# #         #jietu()
# #         print(1)
# #
# #     @classmethod
# #     def tearDownClass(cls):
# #         driver.close()
# #
# #     def test_password_(self):
# #         map(_element, )
# #         _element(_send=True, _path='//*[@id="username"]', sendfor='admin')
# #         _element(_send=True, _path='//*[@id="password"]', sendfor='123456')
# #         _element(_send=True, _path='//*[@id="validateCode"]', sendfor='1234')
# #         _element(_path='//*[@id="login_button"]', _click=True)
# #         _element(_path='/html/body/div[3]/span[2]', _click=True)
# #         # time.sleep(5)
# #         # print('1')
# #         # _element(_path='/html/body/div[4]', _click=True)
# #
# #
# # if __name__ == '__main__':
# #     #print(readConf())
# #     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='E:\\Automationtest\\save'))
# #     unittest.main()
# from screenshots.readdb import *
# from ddt import ddt, data, unpack
# #from framework.method import _element
# #from framework.userdate import *
# import unittest
#
# import HtmlTestRunner
# from framework.method import _Element, driver, opens, time
# from framework.useException import Exp
# from framework.userdate import *
# from screenshots.readdb import *
# #
# # class test(object):
# #     def __init__(self, _path, _motion, _sendfor=''):
# #         self._path = _path
# #         self._motion = _motion
# #         self._senfor = _sendfor
# #
# #     def __format__(self, format_spec):
# #         fm = data_format[format_spec]
# #         return fm.format(obj=self)
# # d = test(test_date().__next__())
# #
# # print(_date.__next__())
# # test.__format__(_date.__next__())
#
# # date = test_date()
# # # @ddt
# # # class ZhuCeCeShi(unittest.TestCase):
# # #
# # #     def setUp(self):
# # #         opens(zhuce_zj().url())
# # #
# # #     def tearDown(self):
# # #         time.sleep(5)
# # #
# # #     @data(date.__next__())
# # #     @unpack
# # #     def test_password_(self, a, b, c):
# # #         _element(_path=a, _motion=b, sendfor=c)
# # #
# # #
# # # if __name__ == '__main__':
# # #     unittest.main(verbosity=2)
# opens(zhuce_zj().url())
# date = GetSql().test_date(1)
# nrow = GetSql().select_num(1)
# nrow = int(nrow)
# u = GetSql().change_select(1)
# a = []
# _Element.run_test(1)
# try:
#     while True:
#         a.append(date.__next__())
# except:
#         pass
# finally:
#     try:
#         for x in (0, nrow-1):
#             _Element(_path=a[x][0], _motion=a[x][1], sendfor=a[x][2])
#     except:
#         Exception()
# # date = GetSql().test_date(1)
# # a = []
# # #print(date.__next__())
# # for i in date.__next__():
# #     print(i)
# #     _element(_path=i[0], _motion=i[1], sendfor=i[-1])
# # for i in date.__next__():
# #     print(i)
#     #_element(_path=date.__next__()[0], _motion=date.__next__()[1], sendfor=date.__next__()[-1])
#
# # class ZhuCeCeShi(unittest.TestCase):
# #
# #     def setUp(self):
# #         opens(zhuce_zj().url())
# #
# #     def tearDown(self):
# #         pass
# #
# #     def test_password_(self):
# #         _element(_path=date.__next__()[0], _motion=date.__next__()[1], sendfor=date.__next__()[-1])
# #
# #
# # if __name__ == '__main__':
# #     unittest.main(verbosity=2)