for i in range(3):
    real_name = "阿布"
    real_pwd = 123456
    user = input("用户名：")
    password = int(input("密码："))
    if user == real_name and password == real_pwd:
        print("欢迎进入")
    else:
        print("用户名或密码错误！请重新输入")