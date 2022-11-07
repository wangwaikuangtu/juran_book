'''
import re
str_1 = input("请您输入你的电话号码：")
numbers_1 = r'(15825565172)'
numbers_2 = r'(13183496887)'
numbers_3 = r'(18090212932)'
match = re.match(numbers_1,str_1)
match_1 = re.match(numbers_2,str_1)
match_2 = re.match((numbers_3,str_1))
if match ==None:
    if match_1 == None:
        if match_2 == None:
            print(str_1,"此号码归属中国移动")
    else:
        print(str_1,"此号码为归属中国电信")
else:
    print(str_1,"此号码归属中国电信")

import re
str_1 = input("请你输入电话号码：")
numbers_1 = r'(15825565172)'
match = re.match(str_1,numbers_1)
if match == None:
    print(numbers_1,"是有效的中国移动电话号码:",str_1)
else:
    print(numbers_1,"不是有效的中国移动电话号码:")
numbers_1 = r'(13183496887)'
match = re.match((numbers_1,str_1))
if match1 == None:
    print(numbers_1,"是有效的中国移动电话号码:",str_1)
else:
    print(numbers_1,"不是有效的中国移动号码")
'''
import re
str_1 = input("请您输入电话号码")
numbers_0 = r'15[598379]\d{8}'
numbers_1 = r'13[386789]\d{8}'
numbers_2 = r'18[897654]\d{8}'
match = re.match(numbers_0,str_1)
match_0 = re.match(numbers_1,str_1)
match_1 = re.match(numbers_2,str_1)
if match == None:
    if match_0 == None:
        if match_1 == None:
            print(str_1, "此号码不是中国联通号码")
    else:
        print(str_1,"此号码是中国联通电话号码")
    print(str_1,"是中国电信号码")
else:
    print(str_1,"不是中国电信号码")
    else:
    print(str_1,"是中移动号码")
else:
print(str_1,"不是中国移动号码")



