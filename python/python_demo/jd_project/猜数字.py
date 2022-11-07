import random   #   随机函数
def compare(guess,answeer):
    if (guess == answeer):
        return '='
    elif (guess < answeer):
        return '<'
    else:
        return '>'
print("猜一个我想的数字(0-20)是什么:")
answer = random.randint(0,20)       #   随机生成数字
while 1:
    guess = int(input("请你输入20以内的奇偶数数字:"))   #
    nember = '你的结果'
    judge_answer=compare(guess,answer,) # 定义变量比较
    if(judge_answer == "<"):    #   判断
        print("你的结果是：" + str(guess))    #   转换answer为字符串
        print("恭喜你猜对了，答案就是" + str(answer))  #   转换answer为字符串
        break
    elif(judge_answer == "<"):
        print("你的结果是：" + str(nember))   #   转换number为字符串
        print("你猜的数字要比答案要小，再试试" + str(guess))
    elif(judge_answer == ">"):
        print("你的结果是" + str(guess))
        print("你的数字超出范围")
        print(answer)






