from tkinter import *
from tkinter import messagebox
import requests
#创建窗口
root =  Tk()
#标题
root.title('中英互译')
#窗口大小
root.geometry('370x100')
#窗口位置
#root.geometry('+600+450')
s_with = root.winfo_screenwidth()#获取屏幕宽
s_height = root.winfo_screenheight()#获取屏幕高度
#计算页面打开在屏幕中央的位置
l_x = str(round)