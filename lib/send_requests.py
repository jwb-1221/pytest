#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'BIN'
import os,sys,json

from lib import loging

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import requests
class SendRequests():
    """发送请求数据"""
    # s = requests.sessions()
    def sendRequests(self,apiData):
        #从读取的表格中获取响应的参数作为传递
        loging.Log().info("*****开始发送请求*****")
        try:
            method = (apiData["method"].lower())
            if method == "post":
                method = "post"
            elif method=="get":
                method = "get"
            else:
                loging.Log().error("*****该框架暂不支持-----{0}-----请求方式，请联系框架维护管理员*****".format(method))
        except Exception as a:
            loging.Log().error("*****该条用例没有找到-----{0}-----的参数名,请检查是否参数名有误*****".format(a))
        try:
            url = apiData["url"]
            if url =="":
                loging.Log().info("*****该条用例没有输入url*****")
                print("请输入接口地址")
            else:
                url =url
        except Exception as a:
            loging.Log().error("*****该条用例没有找到-----{0}-----的参数名,请检查是否参数名有误*****".format(a))
        try:
            if apiData["headers"] == "":
                h = None
            else:
                h = apiData["headers"]
        except Exception as a:
            loging.Log().error("*****该条用例没有找到-----{0}-----的参数名,请检查是否参数名有误*****".format(a))
        try:
            if apiData["body"] == "":
                body_data = None
            else:
                body_data = apiData["body"]
        except Exception as a:
            loging.Log().error("*****该条用例没有找到-----{0}-----的参数名,请检查是否参数名有误*****".format(a))
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
            loging.Log().error("*****接口请求发送失败哟，报错信息为{0}*****".format(a))
        finally:
            loging.Log().info("*****发送请求结束*****")
            return re

if __name__=='__main__':
    SendRequests().sendRequests()
