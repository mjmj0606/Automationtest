from framework.method import _Element
error = 'mini-error'


class Exp(BaseException):
    def __init__(self, message):
        self.message = message

    # def getcuowu(self, e):
    #     if 'unexpected alert open' in e:
    #         print('包含XSS')
    #         return True
    #     else:
    #         return False

    # @staticmethod
    # def input_error(path, whatpath):#输入框格式是否验证，需要输入框顶层定位
    #     if str(_element(_getfor=True, _path=path, sendfor=whatpath)).find(error) > 0:
    #         return False
    #     else:
    #         # print(str(_element(_getfor=True, path=path, sendfor=whatpath)).find(error))
    #         return True