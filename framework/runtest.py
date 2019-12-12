from framework.method import _Element, driver, opens, time
from framework.useException import Exp
from framework.userdate import *
from screenshots.readdb import *
from framework.useException import Exp


class RunTest(object):
    def __init__(self, value):
        self.value = value

    def run_test(self):
        """
        读取数据库中的用例并加载
        :param value: 用例标记
        :return: 加载用例
        """
        date = GetSql().test_date(self.value)
        nrow = GetSql().select_num(self.value)
        nrow = int(nrow)
        a = []
        try:
            while True:
                a.append(date.__next__())
        except Exception:
            pass
        finally:
            try:
                """
                x为用例行数
                """
                for x in (0, nrow - 1):
                    _Element(_path=a[x][0], _motion=a[x][1], sendfor=a[x][2])
            except IndexError:
                raise Exp('请检查用例数据')