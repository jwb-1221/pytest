from PIL import ImageGrab
from config.config import *
class scrrrnshot():
    """截图对象"""
    def __init__(self,interface):
        self.page = interface
    def scrrrnshot(self):
        """浏览器截图方法"""
        pic_path = (TEST_REPORT+self.page +".png")
        self.dr.save_screenshot(pic_path)
    def ImageGrab(self):
        """桌面窗口截图方法"""
        ImageGrab.grab().save(TEST_REPORT+"/"+self.page+".png")
