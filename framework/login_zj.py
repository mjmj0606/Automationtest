from framework.method import (
    sleep_hand, opens, driver, click, send
)
from framework.userdate import *
from framework.useException import exp
import unittest

class zhuceceshi(unittest.TestCase, zhuce_zj, exp, zhuce):
    @classmethod
    def setUp(self):
        opens(self.url())

    @classmethod
    def tearDown(self):
        sleep_hand(3)
        #jietu()
        driver.close()

    def test_login(self):
        try:
            click(self.flat_type())
            send(self.name_of_project(), postfor)
            send(self.password(), postfor)
            send(self.assure_password(), postfor)
            send(self.name_of_company(), postfor)
            send(self.company_adress(), postfor)
            click(self.real_address_district())
            click(self.real_address_district_list())
            click(self.real_address_town())
            click(self.real_address_town_list())
            try:
                click(self.real_address_community())
                click(self.real_address_community_list())

            except:
                pass
            send(self.detailed_address(), postfor)
            click(self.direct_relation())
            click(self.direct_relation_list())
            send(self.Security_code_1(), postfor)
            send(self.Security_code_2(), postfor)
            send(self.Security_code_3(), postfor)
            send(self.projectleader_name(), postfor)
            send(self.projectleader_phone(), postfor)
            send(self.safetydirector_name(), postfor)
            send(self.safetydirector_phone(), postfor)
            send(self.num_peopel(), postfor)
            send(self.site_area(), postfor)

            send(self.clrq(), newtime())
            click(self.sfsyyq())
            click(self.sfsyyq_list())
            click(self.sfsjwxhg())
            click(self.sfsjwxhg_())
            click(self.sfsjyxkj())
            click(self.sfsjyxkj_())

            send(self.weidu(), str(round(random.uniform(0, 100), 3)))
            send(self.jingdu(), str(round(random.uniform(0, 100), 3)))

        except Exception as e:
            self.getcuowu(str(e))