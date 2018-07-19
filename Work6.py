#coding=UTF-8
"""
输入某年某月某日，判断这一天是这一年的第几天？
"""
import time
D=input("请输入日期，格式XXX-XX-XX:")
d=time.strptime(D,'%Y-%m-%d').tm_yday
print("是这一年的第{}天".format(d))

