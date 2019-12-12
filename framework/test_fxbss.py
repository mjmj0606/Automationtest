from framework.method import (
    jietu,sleep_hand,driver,click,send
)
from framework.userdate import (
    postfor,test_fxbs,fengxianleixing,youfuyouhaiqiti,zhoubianyingxiang,fengxianleixingkuang,youdu
)
from framework.useException import (
    exp
)
def fxbss():
    try:
        sleep_hand(1)
        driver.switch_to.frame('mini-iframe-7')
        map(click, test_fxbs[1:4])
        # click(test_fxbs[1])
        # click(test_fxbs[2])
        # click(test_fxbs[3])
        # click(test_fxbs[4])
        send(test_fxbs[5], postfor)
        send(test_fxbs[6], postfor)
        send(test_fxbs[7], postfor)
        sleep_hand(2)
        click(str(fengxianleixingkuang()))
        click(str(fengxianleixing()))
        click(str(youfuyouhaiqiti()))
        click(str(zhoubianyingxiang()))
        try:
            send(youdu(), postfor)
            print('2')
        except Exception:
            print('1')
            pass

    except Exception as e:
        jietu()
        if exp.getcuowu(str(e)):
            pass
        else:
            pass

