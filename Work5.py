#coding=UTF-8
"""
有一对兔子，从出生后第3个月起每个月都生一对兔子，
小兔子长到第三个月后每个月又生一对兔子，
假如兔子都不死，问每个月的兔子总数为多少？
"""
#菲波那切数列：方法一
def recur_fibo(n):
	if n<=1:
		return n
	else:
		return (recur_fibo(n-1)+recur_fibo(n-2))

#输入数字
nterms = int(input("要输出几个月的？"))

#检查输入的数字
if nterms<=0:
	print("请输入正整数")
else:
	print("菲波那切数列")
	for i in range(nterms):
		if recur_fibo(i)!=0:
			print(recur_fibo(i)*2)


#方法二：生成器
import sys
def fibonacci(n):
	a,b,counter = 0,1,0
	while True:
		if (counter > n):
			return
		yield a
		a,b = b,a+b
		counter +=1
n=int(input("输入的月数是："))
f = fibonacci(n)
next(f)  #去除为0的
while True:
	try:

		print(next(f)*2,end=" ")
	except StopIteration:
		sys.exit()