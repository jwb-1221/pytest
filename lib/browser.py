from selenium import webdriver
from config.URL import URL
class config():
    """浏览器类"""

    def open_firefox(self):
        """打开火狐浏览器"""
        self.dr=webdriver.Firefox()
        self.config()
    def open_Chrome(self):
        """打开谷歌浏览器"""
        self.dr=webdriver.Chrome()
    def config_Chrome_admin(self):
        self.dr=webdriver.Chrome()
        self.dr.implicitly_wait(5)
        self.dr.maximize_window()
        self.dr.get(URL.admin_url(self))

    def config_Chrome_merchant(self):
        """打开谷歌浏览器
        进入商户端
        隐式等待为10秒"""
        self.open_Chrome()
        self.dr.get(URL.merchant_url(self))

    def config(self):
        "配置浏览器信息"
        self.dr.implicitly_wait(5)
        self.dr.maximize_window()


