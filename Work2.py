#coding=UTF-8
"""
企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；
利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；
60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
程序分析：请利用数轴来分界，定位。注意定义时需把奖金定义成长整型。
"""


# I<=10         10%
# I>10 I<20     7.5%
# I>=20 I<40    5%  
# I>=40 I<60    3% 
# I>=60 I<100   1.5% 
# I>=100        1% 

i=input("请输入你的数字（单位：万）：")
I=float(i)
if I<=10:
	M=I*0.1
elif I>10 and I<20:
	M=(I-10)*0.075+10*0.1
elif I>=20 and I<40:
	M=(I-20)*0.05+10*0.075+10*0.1
elif I>=40 and I<60:
	M=(I-40)*0.03+20*0.05+10*0.075+10*0.1
elif I>=60 and I<100:
	M=(I-60)*0.015+20*0.03+20*0.05+10*0.075+10*0.1
elif I>=100:
	M=(I-100)*0.01+40*0.015+20*0.03+20*0.05+10*0.075+10*0.1
print('奖励金为：',M)

