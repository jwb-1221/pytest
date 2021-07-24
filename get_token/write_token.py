#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'BIN'

import yaml
from config.config import get_token, token
from lib import send_requests, log
from lib.read_yaml import read_yaml
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))


def write_yaml(data_path, data):
    with open(data_path, "w", encoding="utf-8") as f:
        yaml.dump(data, f)


def set_token():
    a = read_yaml(get_token).read_yaml()
    dict={}
    try:
        re = send_requests.SendRequests.sendRequests(a[0])
        dict["Authorization"] = re.json()["data"]["token"]
        write_yaml(token, dict)
    except AttributeError as b:
        log.Log().error("*****没有找到json属性，说明登录没有成功，请检查登录请求*****".format(b))
    except TypeError as b:
        log.Log().error("*****错误信息为{0}，服务器返回{1}*****".format(b,re.json()))
set_token()
