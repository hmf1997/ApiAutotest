'''
脚本层的一些公共方法
'''
import pytest
from  src.com.hmf.zonghe.caw import DataRead
from  src.com.hmf.zonghe.caw.BaseRequests import BaseReqests
import sys
import os
env_path = r"data_env\env.ini"
# print(sys.path)
cp = os.path.realpath(__file__)  #D:\ApiAutoTest\zonghe\caw\DataRead.py
print(cp)
cd = os.path.dirname(cp) #D:\ApiAutoTest\zonghe\caw
print(cd)
cd = os.path.dirname(cd)
print(cd)
cd = os.path.dirname(cd)
print(cd)
sys.path.append(cd)
print(os.getcwd())
# 读取env.ini中的url，设置session级别的，整个执行过程读一次
@pytest.fixture(scope='session')
def url():
    return DataRead.read_ini(env_path,"url")

@pytest.fixture(scope='session')
def db():
    return eval(DataRead.read_ini(env_path,'db'))

# 创建一个的实例，设置session级别的，整个执行过程只有一个实例，自动管理cookie
@pytest.fixture(scope='session')
def baserequests():
    return BaseReqests()