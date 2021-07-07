#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'BIN'
import os,sys,json

import requests

from lib.read_yaml import read_yaml
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
class SendRequests():
    """发送请求数据"""
    # s = requests.sessions()
    def sendRequests(self,apiData):
        #从读取的表格中获取响应的参数作为传递
        try:
            method = (apiData["method"].lower())
            if method == "post":
                method = "post"
            elif method=="get":
                method = "get"
            else:
                print("该框架暂只支持post和get请求，请联系框架维护管理员")
        except:
            print("检查参数名是否有误")
        url = apiData["url"]
        if url =="":
            print("请输入接口地址")
        else:
            url =url
        try:
            if apiData["headers"] == "":
                h = None
            else:
                h = apiData["headers"]
        except Exception as e:
            print("报错了:"+e)
        if apiData["body"] == "":
            body_data = None
        else:
            body_data = apiData["body"]
        type = apiData["type"]
        v = False
        if type == "data":
            body = body_data
        elif type == "json":
            body = json.dumps(body_data)
        else:
            body = body_data
            #发送请求
        re = requests.request(method=method,url=url,headers=h,data=body,verify=v)
        return re

if __name__=='__main__':
    SendRequests().sendRequests()
