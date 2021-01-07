'''
用户模块接口,按模块管理
'''

def register(url,baserequests,data):
    '''
    注册接口
    :param url: 环境数据，比如http://jy002:8082、
    :param baserequests: BaseRequests的实例
    :param data: 注册的数据
    :return: 响应
    '''
    url= url + "/futureloan/mvc/api/member/register"
    return baserequests.post(url,data=data)



def login(url,baserequests,data):
    url = url + "/futureloan/mvc/api/member/login"
    return baserequests.post(url, data=data)