#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'BIN'
import os
import random


def new_report(test_report):
    """获取最新HTML文件"""
    lists = os.listdir(test_report)[-1]  # 获取最后一个文件
    file_new1 = os.path.join(test_report, lists)  # 文件路径
    return str(file_new1)


def choice_report(test_report):
    """随机获取html文件"""
    lists = os.listdir(test_report)
    file = random.choice(lists)
    file = os.path.join(test_report, file)
    return str(file)
