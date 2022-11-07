import getpass
import re
# 判断用户名合法性函数，字母、下划线、数字组成，至少4位，最多20位长
def userValid(username):
    nameRe = re.compile(r'[a-zA-z_]\w{3,20}')
    if(nameRe.match(username)):
        return True
    else:
        return False

# 判断密码复杂度函数，必须包含大小写和数字，至少8位
def passValid(password):
    ara = re.compile(r'(.*)?[0-9]')     # 数字0-9
    arb = re.compile(r'(.*)?[a-zA-Z]')  # 英文字母从小写a-z,大写字母A-Z
    arc = re.compile(r'.{8,}')      # 至少有8位数字
    if(ara.match(password) and arb.match(password) and (arc.match(password))):
        return True
    else:
        return False


# 用户数据库，预置了2个用户帐号信息 帐号：密码
users={'zhangsan':'123456','lisi':'qwerty'}
# 注册过程
# 欢迎信息
print('#####欢迎来到Python学习平台注册程序#####')
while True:
    # 用户输入
    username=input('请输入用户名：')
    password1=getpass.getpass('请输入密码：')
    password2=getpass.getpass('请再次输入密码：')
    # 处理注册信息
    if(users.get(username)):
        print('用户已存在，请重新输入！')
    elif(userValid(username)):
        if(password1==password2):
            if(passValid(password1)):
                users[username]=password1
                print('注册成功！')
                print(f'当前系统用户有：{list(users.keys())}')
                break
            else:
                print('密码太简单，必须包含大小写字母和数字，至少8位，请重新输入！')
        else:
            print('密码不一致，请重新输入！')
    else:
        print('用户名只能由字母、下划线开头，并且不能包含特殊符号,请重新输入！')