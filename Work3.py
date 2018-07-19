#coding=UTF-8
"""
一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
提示：数学好的仔细编程，数学差的参考第三方库 math
"""
# a=i+100
# b=a+168


import math
#这里我有点不明白range后面再怎么大，也只有这3个数
for n in range(100000):
	x=math.sqrt(n+100)
	y=math.sqrt(n+268)
	if int(x)*int(x)==n+100 and int(y)*int(y)==n+268:
		print("这个数是：",n)
		print(x,y)