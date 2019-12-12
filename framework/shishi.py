import unittest

import HtmlTestRunner
from framework.method import _Element, driver, opens, time
from framework.useException import Exp
from framework.userdate import *
from screenshots.readdb import *
from framework.runtest import *


class ZhuCeCeShi(unittest.TestCase, zhuce, zhuce_zj, Exp):
    def setUp(self):
        opens(zhuce_zj().url())
        #opens('https://www.baidu.com')

    def tearDown(self):
        time.sleep(5)
        #jietu()
        print(1)

    @classmethod
    def tearDownClass(cls):
        driver.close()

    # def test_password_(self):
    #     _element(_send=True, _path=zhuce_zj().password(), sendfor=new_time)
    #     _element(_send=True, _path=zhuce_zj().assure_password(), sendfor=postfor)
    #     _element(_click=True, _path=zhuce_zj().projectleader_phone())
    #     _element(_path='/html/body/div[4]', _click=True)
    #     # time.sleep(5)
    #     # print('1')
    #     # _element(_path='/html/body/div[4]', _click=True)

    # def test_password_2(self):
    #     """
    #
    #     :return: 测试输入验证密码错误修改密码
    #     """
    #     _element(_send=True, _path=zhuce_zj().password(), sendfor=new_time)
    #     _element(_send=True, _path=zhuce_zj().assure_password(), sendfor=postfor)
    #     _element(_click=True, _path=zhuce_zj().projectleader_phone())
    #     _element(_path='/html/body/div[4]', _click=True)
    #     time.sleep(5)
    #     _element(_send=True, _path=zhuce_zj().password(), sendfor=postfor, waittime=8)
    #     time.sleep(1)
    #     _element(_click=True, _path=zhuce_zj().projectleader_phone())
    #     _element(_path='/html/body/div[4]', _click=True, waittime=10)
    # def test_password2(self):
    #     _element(_click=True, _path=self.password(), sendfor='123456798')
    #     _element(_send=True, _path=self.assure_password(), sendfor=postfor)
    #     #self.assertTrue(exp.input_error('//*[@id="password"]', 'class'), msg='没有提示')
    #     _element(_path='/html/body/div[4]', _getfor=True, _searchfor='style')
    def test_login(self):
        RunTest(2).run_test()

if __name__ == '__main__':
    #print(readConf())
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='E:\\Automationtest\\save'))