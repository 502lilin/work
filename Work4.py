#coding=UTF-8

"""
输入三个整数x,y,z，请把这三个数由小到大输出
"""

x=float(input("请输入x的数字："))
y=float(input("请输入y的数字："))
z=float(input("请输入z的数字："))

if x>y:
	x,y=y,x
if x>z:
	x,z=z,x
if y>z:
	y,z=z,y

print(x,y,z)


