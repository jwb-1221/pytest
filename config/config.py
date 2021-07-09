#!/usr/bin/python
#!/usr/bin/env python
import sys,os
config = os.path.dirname(os.path.dirname(__file__))
sys.path.append(config)
#配置
CONFIG = os.path.join(config,"config","config.ini")
#HTML报告路径
report = os.path.join(config,"report")
#截图路径
TEST_REPORT = os.path.join(config,"screenshot")
#测试文件
TEST_CASE = os.path.join(config,"testCase")
#测试用例模板
TEST_CONFIG = os.path.join(config,"config","testcase.xlsx")
#日志目录
LOG = os.path.join(config,"log")
