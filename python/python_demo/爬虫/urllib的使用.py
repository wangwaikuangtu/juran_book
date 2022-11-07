'''
import urllib.request
response = urllib.request.urlopen('http://www.baidu.com')   #   抓取目标页面数据
print(type(response))   #   判断resqpmse变量是哪种类型的数据
print(response.read().decode('utf-8'))  # read在未指定参数的情况下读取整个文件,decode   decode告诉程序这个是utf-8格式
#   答：（1）形式参数就是定义函数时函数名后面括号内的参数列表（简称“形参”）
# （2）实际参数就是我们在调用函数时函数名后面括号中的若干个参数（简称“实参”）
#str = 'aBc'
#print(str.upper())
jiangxb = 80
jingj = 60
def wine(x,y,person = 'VIP贵宾'):
    total = jiangxb * x + jingj * y
    print(person,'你的酒总价为',total)

#
# '''
# import jieba
#
# txt = input("请输入一段中文文本:")
# ls  = jieba.lcut(txt)
# for i in ls[::-1]:
#     print(i,end='')
# sum = 0
# for i in range(0,100):
#     if i%2==0:
#         sum = sum -i
#     else:
#         sum = sum +i
# print(sum)
'''
（1）什么是形参
（2）什么是实参
形式参数：在定义函数时，函数名后面空号中的参数称为，“形式参数”（“简称形参”）
实际参数：在调用一个函数时，函数名后面括号中的参数为“实际参数”也就是将函数给调用者提供函数的叫做“实际参数”（简称实际参数）
'''
n = eval(input("请输入数量："))
if n==1:
    cost=150
elif n>=2 and n<=3:
    cost=int(n*150*0.9)
elif n>=4 and n<=9:
    cost=int(n*150*0.8)
elif n>=10:
     cost=int(n*150*0.7)
print("总额为:",cost)

