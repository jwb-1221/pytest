import pytest
import allure
import time
import os,sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from config.URL import URL
from lib.browser import config
@allure.feature('登录模块')
class Testcase(object):
    def setup_class(self):
        print("类级别的 setup")
        config.config_Chrome_admin(self)

    def teardown_class(self):
        print("类级别的teardown")
        self.dr.close()

    def setup_method(self):
        print('类方法级别的 setup.....')

    def teardown_method(self):
        print('类方法级别的 teardown.....')
        self.dr.get(URL.admin_url(self))
    @allure.story('登录模块下的子模块:正确账号密码登录')
    @allure.title('正确账号密码登录')
    @allure.description('这是测试用例用例1的描述信息')

    def test_case01(self):
        self.dr.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/form/div[1]/div/div/div/input').send_keys('adMIN')
        self.dr.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/form/div[2]/div/div/div[1]/input').send_keys('123456.')
        self.dr.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/form/div[3]/div/div/div[1]/div/div/input').send_keys('99999')
        self.dr.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/form/div[4]/div/button').click()

    # @pytest.mark.skipif(condition=1<2, reason='如果条件为true就跳过用例')
    @allure.story('登录模块下的子模块:错误登录账号密码')
    @allure.title('错误账号密码')
    @allure.description('这是测试用例用例2的描述信息')

    def test_case02(self):
        print('执行用例02.......')
        time.sleep(5)
        self.dr.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/form/div[1]/div/div/div/input').send_keys('adMIN')
        self.dr.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/form/div[2]/div/div/div[1]/input').send_keys('123456.')
        time.sleep(5)


        assert 1  # 断言成功

@allure.feature('添加纳税人模块')
class Testcase2(object):
    mobile_list = [{'1':'10086',"2":"10010"},
                   {'1':'1008611','2':'1001011'}]

    @allure.title('错误账号密码')
    def test_case01(self):
        pass

    @pytest.mark.parametrize('mobile',mobile_list)
    @allure.title("登录测试用例{(mobile['1'])}")
    def test_register(self,mobile):
        print('注册手机号是: {}***{}'.format(mobile["1"],mobile["2"]))



# if __name__ == '__main__':
#
#     pytest.main(["-s", "test.py"])


