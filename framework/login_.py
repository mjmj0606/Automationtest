from framework.method import (
    sleep_hand, opens, driver, click, send, isdisplayed
)
from framework.userdate import *
from framework.useException import exp
import unittest


class zhuceceshi(unittest.TestCase, zhuce, exp):
    @classmethod
    def setUp(self):
        opens(self.url())

    @classmethod
    def tearDown(self):
        sleep_hand(3)
        #jietu()
        driver.close()

    def test_lodin_(self):#注册页面XSS
        try:
            click(self.danweileixing_yibandanwei())
            send(self.dwmc(), postfor)
            send(self.dlmm(), postfor)
            send(self.qrmm(), postfor)
            send(self.zcdz(), postfor)
            try:
                click(self.sjdz_cq())
                click(self.sjdz_cq_list())
                click(self.sjdz_xz())
                click(self.sjdz_xz_list())
                click(self.sjdz_sq())
                click(self.sjdz_sq_list())
                send(self.sjdz_xxdz(), postfor)
            except Exception:
                pass

            time.sleep(1)
            click(self.dwjs())
            click(self.dwjs_list())
            click(self.zsgx())
            click(self.zsgx_list())
            send(self.clrq(), newtime())
            send(self.shxyid(), postfor)
            send(self.zyyw(), postfor)
            send(self.dwfrxm(), postfor)
            send(self.dwfzrdh(), postfor)
            send(self.aqfzrxm(), postfor)
            send(self.aqfzdh(), postfor)
            send(self.cyrs(), postfor)
            send(self.csmj(), postfor)
            send(self.fdfzrxm(), postfor)
            send(self.fdfzrdh(), postfor)
            send(self.zczj(), postfor)

            try:
                click(self.sfwysyly())
                click(self.sfwysyly_list())
                if isdisplayed(self.swlymc()) == True:
                   send(self.swlymc(),postfor)
                   click(self.lyqsjs_list())
            except:
                pass

            click(self.sfsyyq())
            click(self.sfsyyq_list())
            click(self.sfsjwxhg())
            click(self.sfsjwxhg_())
            click(self.sfsjyxkj())
            click(self.sfsjyxkj_())

            send(self.weidu(), str(round(random.uniform(0, 100), 3)))
            send(self.jingdu(), str(round(random.uniform(0, 100), 3)))

            #行业领域
            click(self.hyly())
            click(self.hyly_list._JZSG())
            click(self.hyly_list._JZSG_JZSG())
            click(self.hyly_list._JZSG_JZSG_1())
            click(self.hyly_list._JZSG_JZSG_2())
            click(self.hyly_list._JZSG_JZSG_3())
            click(self.zhuce())

        except Exception as e:
            if self.getcuowu(str(e)):
                raise
            else:
                raise