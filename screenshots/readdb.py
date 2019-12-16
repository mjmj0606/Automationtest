import pymysql
import re
from itertools import product
conn = pymysql.connect('192.168.126.100', 'root', 'root', 'autotest')


class GetSql(object):

    def _selectlist(self, sql):
        cursor = conn.cursor()
        cursor.execute(sql)
        return cursor.fetchall()

    def change_select(self, value):
        """

        :return: 提取测试用例
        """
        return list(self._selectlist('select element, motion, text from element where title = %s' % value))

    def select_num(self,value):
        """最大行数"""
        for i in re.findall(r'\d+', str(self._selectlist('select count(*) from element where title = %s' % value))):
            return i

    def get_address(self, value):
        """

        :return:查找地址
        """
        x = self._selectlist('select adress from element where title = %s' % value)
        if len(set(x)) <= 1:
            return set(x)
        else:
            return '有错误数据'

    # def package_list(self, value):
    #
    #     """
    #
    #     :return:组装测试用例信息
    #     """
    #     nrow = self.select_num(value)
    #     #nrow = select_num(value)
    #     a = self.change_select(value)
    #     for x in range(0, int(nrow)):
    #         for y in range(0, len(a[0])):
    #             yield a[x][y]
        # for x, y in zip(range(0, int(nrow)), range(0, len(a[0]))):
        #     yield a[x][y]

    # def test_date(self, value):
    #     """
    #
    #     :param value:用例标记
    #     :return: 元素未知列表
    #     """
    #     for i in [list(self.package_list(value))[i:i+3] for i in range(0, len(list(self.package_list(value))), 3)]:
    #         yield i


# a = GetSql().package_list(1)
# while True:
#     try:
#         print(a.__next__())
#     except:
#         break
#print(GetSql().change_select(1)[0][0])