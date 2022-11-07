total = 99
for number in range(1,100):
    if number % 7 == 0:
        continue
    else:
        string = str(number)
        if string.endswith('7'):    # 将数值转换成字符串
            continue
    total -=1
print("拍腿次数是",total,"次")