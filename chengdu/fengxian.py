from framework.method import (
    jietu, sleep_hand, driver
)
from framework.test_fxbss import fxbss
from framework.openshouye import shouye1

import unittest
class Testfengxianbianshi(unittest.TestCase):

    @classmethod
    def setUp(cls):
        shouye1()

    def tearDown(self):
        sleep_hand(3)
        jietu()
        driver.close()

    def test_fxbss(self):#风险辨识与评估管控
        fxbss()