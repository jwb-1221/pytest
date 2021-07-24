#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import sys
import os
config = os.path.dirname(os.path.dirname(__file__))
sys.path.append(config)
# 配置
CONFIG = os.path.join(config, "config", "config.ini")
# HTML报告路径
report = os.path.join(config, "report")
# 截图路径
TEST_REPORT = os.path.join(config, "screenshot")
# 测试文件
TEST_CASE = os.path.join(config, "testCase")
# yaml文件
YAML = os.path.join(config, "config", "data.yaml")
# 日志目录
LOG = os.path.join(config, "log")
# 登录获取token
get_token = os.path.join(config, "get_token", "login.yaml")
# token存放地
token = os.path.join(config, "get_token", "token.yaml")
