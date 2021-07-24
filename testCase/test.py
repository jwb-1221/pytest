#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import pytest
import allure
from config.config import YAML
from get_token.write_token import set_token
from lib import send_requests, log
from lib.read_yaml import read_yaml
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

set_token()
@allure.feature('登录模块')
class Testcase(object):
    def setup_class(self):  # 类级别的 setup
        pass

    def teardown_class(self):  # 类级别的teardown
        pass

    def setup_method(self):  # 类方法级别的 setup.....
        pass

    def teardown_method(self):  # 类方法级别的 teardown.....
        pass
    list = read_yaml(YAML).read_yaml()

    @pytest.mark.parametrize('name, requests', list)
    @allure.story('登录模块下的子模块:正确账号密码登录')
    @allure.title('{name}')
    @allure.description('这是测试用例用例1的描述信息')
    def test_case01(self, name, requests):
        log.Log().info("*****正在执行-----{0}-----用例*****".format(name))
        re = send_requests.SendRequests.sendRequests(requests)


if __name__ == '__main__':
    Testcase().test_case01()
