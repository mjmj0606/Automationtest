from framework.method import (
    sleep_hand,opens,driver,click,send
)
from framework.userdate import (
    denglu,shouye
)

def shouye1():
        opens(denglu[0])
        click(denglu[1])
        send(denglu[2], denglu[3])
        send(denglu[4], denglu[5])
        click(denglu[6])
        sleep_hand(3)
        click(shouye[0])
        click(shouye[1])
        click(shouye[2])
        sleep_hand(1)

        driver.switch_to.frame(shouye[3])
        click(shouye[4])
        driver.switch_to.default_content()