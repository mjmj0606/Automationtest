import configparser


conf = configparser.ConfigParser()
def readConf():
    '''读取配置文件'''
    conf.read('setting.ini')  # 文件路径
    #print(conf.sections())
    return conf.get('savepath', 'path')

# if __name__ == '__main__':
# #      print(readConf())