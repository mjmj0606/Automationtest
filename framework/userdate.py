import time
import random
postfor = "<script>alert('hello，gaga!');</script>"
new_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
rb_numb = random.randint(99999, 1000000)
denglu = [
    'http://192.168.60.109:8083/gov/a/login',
    '//*[@id="tip-button"]',
    '//*[@id="username"]',
    '简阳属地用户',
    '//*[@id="password"]',
    '666666',
    '//*[@id="login_button"]',
] #登录页面定位
shouye = [
    '//*[@id="tip-button"]',
    '//*[@id="mainMenu"]/ul/li[3]/a/span[1]',
    '//*[@id="mainMenu"]/ul/li[3]/ul/li[1]/a/span',
    'mini-iframe-5',
    '/html/body/div[2]/table/tbody/tr/td[1]/a[1]'
          ] #首页定位
test_fxbs = [
    'mini-iframe-7',
    '//*[@id="county"]/span',
    '//*[@id="mini-5$1"]',
    '//*[@id="street"]/span',
    '//*[@id="mini-9$1"]',
    '//*[@id="source$text"]',
    '//*[@id="firstform"]/fieldset[1]/div/div[1]/div[4]/div/span/span/input',
    '//*[@id="firstform"]/fieldset[1]/div/div[5]/div[2]/div/span/span[1]/textarea',

]
def fengxianleixingkuang():
    return '//*[@id="type$text"]'
def fengxianleixing():
    return '//*[@id="mini-21$' + str(random.randint(0, 18)) + '"]'
def youfuyouhaiqiti():
    return '//*[@id="mini-23$' + str(random.randint(0, 1)) + '"]/span'
def zhoubianyingxiang():
    return '//*[@id="mini-29$' + str(random.randint(0, 1)) + '"]/span'
def youdu():
    return '//*[@id="hazardousGasName$text"]'
def newtime():
    return time.strftime('%Y-%m-%d', time.localtime(time.time()))
class zhuce():
    @staticmethod
    def url():
        return 'http://192.168.60.109:8083/comp/assets/companyRegister.jsp'

    @staticmethod
    def danweileixing_yibandanwei():
        return '//*[@id="mini-1$0"]/span'

    @staticmethod
    def danweileixing_zigc():
        return '//*[@id="mini-1$1"]/span'

    @staticmethod
    def dwmc():
        return '//*[@id="compName$text"]'

    @staticmethod
    def dlmm():
        return '//*[@id="password$text"]'

    @staticmethod
    def qrmm():#确认密码
        return '//*[@id="password2$text"]'

    @staticmethod
    def zcdz():#注册地址
        return '//*[@id="registerAddress$text"]'

    @staticmethod
    def sjdz_cq():
        return '//*[@id="county"]/span'

    @staticmethod
    def sjdz_cq_list():
        return '//*[@id = "mini-12$%s"]' % random.randint(0, 22)

    @staticmethod
    def sjdz_xz():
        return '//*[@id="street"]/span'

    @staticmethod
    def sjdz_xz_list():
        return '//*[@id="mini-16$%s"]/td' % random.randint(0, 3)

    @staticmethod
    def sjdz_sq():
        return '//*[@id="jingjileixing$text"]'

    @staticmethod
    def sjdz_sq_list():
        return '//*[@id="mini-20$%s"]' % random.randint(0, 3)

    @staticmethod
    def sjdz_xxdz():#实际地址详细地址
        return '//*[@id="address$text"]'

    @staticmethod
    def hyly():
        return '//*[@id="secondClass"]/span[1]'

    @staticmethod
    def dwjs():
        return '//*[@id="combo4$text"]'

    @staticmethod
    def dwjs_list():
        return '//*[@id="mini-42$%s"]' % random.randint(1, 2)

    @staticmethod
    def zsgx():
        return '//*[@id="combo1$text"]'

    @staticmethod
    def zsgx_list():
        return '//*[@id="mini-45$%s"]' % random.randint(1, 2)

    @staticmethod
    def clrq():
        return '//*[@id="comInfo"]/div[4]/div/div[4]/p[2]/span/span[1]/input'

    @staticmethod
    def shxyid():
        return '//*[@id="creditCode$text"]'

    @staticmethod
    def zyyw():
        return '//*[@id="comInfo"]/div[4]/div/div[6]/p[2]/span/span[1]/input'

    @staticmethod
    def dwfrxm():
        return '//*[@id="comInfo"]/div[4]/div/div[7]/p[2]/span/span[1]/input'

    @staticmethod
    def dwfzrdh():
        return '//*[@id="comInfo"]/div[4]/div/div[8]/p[2]/span/span[1]/input'

    @staticmethod
    def aqfzrxm():
        return '//*[@id="comInfo"]/div[4]/div/div[9]/p[2]/span/span[1]/input'

    @staticmethod
    def aqfzdh():
        return '//*[@id="comInfo"]/div[4]/div/div[10]/p[2]/span/span[1]/input'

    @staticmethod
    def cyrs():
        return '//*[@id="comInfo"]/div[4]/div/div[11]/p[2]/span/span[1]/input'

    @staticmethod
    def csmj():
        return '//*[@id="comInfo"]/div[4]/div/div[12]/p[2]/span[1]/span[1]/input'

    @staticmethod
    def fdfzrxm():
        return '//*[@id="legalname$text"]'

    @staticmethod
    def fdfzrdh():
        return '//*[@id="legalmobile$text"]'

    @staticmethod
    def zczj():
        return '//*[@id="registeredcapital$text"]'

    @staticmethod
    def sfwysyly():
        return '//*[@id="comInfo"]/div[4]/div/div[17]/p[2]'

    @staticmethod
    def sfwysyly_list():
        return '//*[@id="mini-80$%s"]' % random.randint(1, 2)

    @staticmethod
    def swlymc():
        return '//*[@id="comprehensiveId$text"]'

    @staticmethod
    def lyqsjs():
        return '//*[@id="buildingRole$text"]'

    @staticmethod
    def lyqsjs_list():
        return '/html/body/div[8]/div/div[1]/div[2]/div/table/tbody/tr[%s]/td' % random.randint(1, 4)

    @staticmethod
    def sfsyyq():
        return '/html/body/div[1]/form/div[4]/div/div[18]/p[2]/span/span/input'

    @staticmethod
    def sfsyyq_list():
        return '//*[@id="mini-98$%s"]' % random.randint(1, 2)

    @staticmethod
    def sfsjwxhg():
        return '//*[@id="comInfo"]/div[4]/div/div[19]/p[2]'

    @staticmethod
    def sfsjwxhg_():
        return '//*[@id="mini-101$%s"]' % random.randint(1, 2)

    @staticmethod
    def sfsjyxkj():
        return '//*[@id="comInfo"]/div[4]/div/div[20]/p[2]'

    @staticmethod
    def sfsjyxkj_():
        return '//*[@id="mini-104$%s"]' % random.randint(1, 2)

    @staticmethod
    def weidu():
        return '//*[@id="lng$text"]'

    @staticmethod
    def jingdu():
        return '//*[@id="lat$text"]'

    @staticmethod
    def zhuce():
        return '//*[@id="register"]'
    class hyly_list():
        @staticmethod
        def _JZSG():
            return '//td[@id="1$cell$1"]/div/div/a'


        @staticmethod
        def _JZSG_JZSG():
            return '//td[@id="2$cell$1"]/div/div/a'


        @staticmethod
        def _JZSG_JZSG_1():
            return '//*[@id="mini-27$checkbox$3"]'


        @staticmethod
        def _JZSG_JZSG_2():
            return '//*[@id="mini-27$checkbox$4"]'


        @staticmethod
        def _JZSG_JZSG_3():
            return '//*[@id="mini-27$checkbox$5"]'


class zhuce_zj():

    @staticmethod
    def url():
        return 'http://192.168.60.109:8083/comp/assets/companyRegister.jsp'

    @staticmethod
    def flat_type():
        return '//*[@id="mini-1$1"]/span'

    @staticmethod
    def name_of_project():
        return '//*[@id="compName$text"]'

    @staticmethod
    def password():
        a = '//*[@id="password$text"]'
        return a

    @staticmethod
    def assure_password():
        a = '//*[@id="password2$text"]'
        return a

    @staticmethod
    def name_of_company():
        return '//*[@id="comInfo"]/div[3]/div[2]/p[2]/span/span/input'

    @staticmethod
    def company_adress():
        return '//*[@id="registerAddress$text"]'

    @staticmethod
    def real_address_district():
        return '//*[@id="county$text"]'

    @staticmethod
    def real_address_district_list():
        return '//*[@id="mini-12$%s"]' % random.randint(1, 22)

    @staticmethod
    def real_address_town():
        return '//*[@id="street$text"]'

    @staticmethod
    def real_address_town_list():
        return '//*[@id="mini-16$%s"]' % random.randint(1, 2)

    @staticmethod
    def real_address_community():
        return'//*[@id="jingjileixing$text"]'

    @staticmethod
    def real_address_community_list():
        return '//*[@id="mini-20$%s"]' % random.randint(0, 2)

    @staticmethod
    def detailed_address():
        return '//*[@id="address$text"]'

    @staticmethod
    def Unit_role():
        return '//*[@id="combo4$text"]'

    @staticmethod
    def Unit_role_list():
        return '//*[@id="mini-42$%s"]' % random.randint(1, 2)

    @staticmethod
    def direct_relation():
        return '//*[@id="combo1"]/span'

    @staticmethod
    def direct_relation_list():
        return '//*[@id="mini-45$%s"]' % random.randint(1, 2)

    @staticmethod
    def Security_code_1():
        return '//*[@id="comInfo"]/div[4]/div/div[2]/p[2]/span[1]/span/input'
    @staticmethod
    def Security_code_2():
        return '//*[@id="comInfo"]/div[4]/div/div[2]/p[2]/span[2]/span/input'

    @staticmethod
    def Security_code_3():
        return '//*[@id="comInfo"]/div[4]/div/div[2]/p[2]/span[3]/span/input'

    @staticmethod
    def projectleader_name():
        return '//*[@id="comInfo"]/div[4]/div/div[7]/p[2]/span/span/input'

    @staticmethod
    def projectleader_phone():
        return '//*[@id="comInfo"]/div[4]/div/div[8]/p[2]/span/span[1]/input'

    @staticmethod
    def safetydirector_name():
        return '//*[@id="comInfo"]/div[4]/div/div[9]/p[2]/span/span/input'

    @staticmethod
    def safetydirector_phone():
        return '//*[@id="comInfo"]/div[4]/div/div[10]/p[2]/span/span/input'

    @staticmethod
    def num_peopel():
        return '//*[@id="comInfo"]/div[4]/div/div[11]/p[2]/span/span/input'

    @staticmethod
    def site_area():
        return '//*[@id="comInfo"]/div[4]/div/div[12]/p[2]/span[1]/span[1]/input'


if __name__ =='__main__':
    print(zhuce().url())