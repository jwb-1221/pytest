#!/usr/bin/python
#!/usr/bin/env python
import pytest
import allure
import time
import os,sys
import requests
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from lib import send_requests, loging
from lib.read_yaml import read_yaml

@allure.feature('登录模块')
class Testcase(object):
    def setup_class(self):#类级别的 setup
        pass
    def teardown_class(self):#类级别的teardown
        pass
    def setup_method(self):#类方法级别的 setup.....
        pass
    def teardown_method(self):#类方法级别的 teardown.....
        pass
    list = read_yaml("C:\\Users\86158\Desktop\新建文件夹\pytest_request\config\\requests.yaml").read_yaml()
    @pytest.mark.parametrize('name,requests',list)
    @allure.story('登录模块下的子模块:正确账号密码登录')
    @allure.title('{name}')
    @allure.description('这是测试用例用例1的描述信息')

    def test_case01(self, name, requests):
        loging.Log().info("*****正在执行-----{0}-----用例*****".format(name))
        re = send_requests.SendRequests.sendRequests(self,requests)
        # print(re.text)
        loging.Log().error(re.json())
if __name__ == '__main__':
    Testcase().test_case01()



