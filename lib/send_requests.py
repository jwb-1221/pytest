#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'BIN'
import os
import sys
import json

from config.config import token
from lib import log
import requests

from lib.read_yaml import read_yaml

sys.path.append(os.path.dirname(os.path.dirname(__file__)))


class SendRequests:
    """发送请求数据"""
    # s = requests.sessions()

    @staticmethod
    def sendRequests(apiData, headers=None):
        #从读取的表格中获取响应的参数作为传递
        log.Log().info("*****开始发送请求*****")
        try:
            method = (apiData["method"].lower())
            if method == "post":
                method = "post"
            elif method=="get":
                method = "get"
            else:
                log.Log().error("*****该框架暂不支持-----{0}-----请求方式，请联系框架维护管理员*****".format(method))
            log.Log().info("*****请求方式是-----{0}-----*****".format(method))
        except Exception as a:
            log.Log().error("*****该条用例没有找到-----{0}-----参数名,请检查是否参数名有误*****".format(a))
        try:
            url = apiData["url"]
            if url =="":
                log.Log().error("*****该条用例没有输入url*****")
            else:
                url =url
            log.Log().info("*****请求路径是{0}*****".format(url))

        except Exception as a:
            log.Log().error("*****该条用例没有找到-----{0}-----参数名,请检查是否参数名有误*****".format(a))
        try:
            if apiData["headers"] == "None":
                if apiData["url"] == "http://account-admin-webos-test.lastmiles.cn/account-admin-web/login":
                    h = None
                else:
                    h = read_yaml(token).read_yaml()
                    log.Log().info("*****请求头信息是{0}*****".format(h))
            else:
                h = apiData["headers"]
        except KeyError as a:
            log.Log().error("*****该条用例没有找到-----{0}-----参数名,请检查是否参数名有误*****".format(a))
        try:
            if apiData["body"] == "None":
                body_data = None
            else:
                body_data = apiData["body"]
                log.Log().info("*****请求体信息是{0}*****".format(body_data))
        except Exception as a:
            log.Log().error("*****该条用例没有找到-----{0}-----参数名,请检查是否参数名有误*****".format(a))
        v = False
        if type == "data":
            body = body_data
        elif type == "json":
            body = json.dumps(body_data)
        else:
            body = body_data
            #发送请求
        try:
            re = requests.request(method=method,url=url,headers=h,data=body,verify=v)
        except Exception as a:
            log.Log().error("*****接口请求发送失败哟，报错信息为{0}*****".format(a))
        else:
            return re
        finally:
            log.Log().info("*****发送请求结束*****")


if __name__=='__main__':
    SendRequests().sendRequests()
