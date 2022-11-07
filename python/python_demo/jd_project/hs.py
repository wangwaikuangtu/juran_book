# import re
# def phone_number():
#     n = input("请输入一个手机号：")
#     if re.match(r'1[345789]\d{9}',n):
#         print("该号码合法：",n)
#         if re.match(r"13[456789]\d{8}",n) or \
#                re.match(r"15[012789]\d{8}",n) or \
#                re.match(r"147\d{8}|178\d{8}",n) or \
#                re.match("18[23478]\d{8}", n):
#             print("该号码属于：中国移动")
#         elif re.match(r'13[012]\d{8}',n) or \
#              re.match(r"18[56]\d{8}",n)  or \
#              re.match(r"15[56]\d{8}", n) or \
#              re.match(r"14[056]\d{8}", n) or \
#              re.match(r"17[56]\d{8}|166\d{8}", n):
#             print("该号码属于：中国联通")
#         else:
#                print("中国电信")
#     else:
#         print("该手机号码格式不正确")
# if  __name__ == '__main__':
#     # phone_number()
def add(x,y):
    return x+y
# print(add(100,200))
def subtarction(x,y):
    return x-y
if __name__ == '__main__':
    pass
    # print(__name__)
    print(subtarction(1,2))