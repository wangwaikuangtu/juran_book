import datetime
number = ["今天星期一:\n "
          "你知道我喜欢吃什么吗?\n"
          "我喜欢痴痴的望着你。",
          "今天星期二:\n"
          " 你会弹吉他吗？\n"
          "为什么拨动能我的心弦。",
          "今天星期三:\n "
          "我有一个超能力\n"
          "超喜欢你。",
          "今天星期四:\n "
          "你今天怪怪的\n"
          "怪好看的。",
          "今天星期五:\n"
          "你知道我喜欢喝什么吗?\n"
          "呵护你",
          "今天星期六:\n "
          "你知道我最爱上什么课吗?\n"
          "爱上你的每一刻。",
          "今天星期天:\n"
          "今天是你的生日\n"
          "祝你生日快乐"]
day = datetime.datetime.now().weekday()
print(number[day])