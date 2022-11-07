# import pygame
# file = r'D:\酷狗音乐下载\KGMusic\韩安旭 - 不在.mp3'
# pygame.mixer.init()
# track = pygame.mixer.music.load(file)
# pygame.mixer.music.play()
#____________________________________________________________
import pygame
# 音乐的路径
file=r'E:\python_demo\jd_project\sr\12.mp3'
# 初始化
pygame.mixer.init()
# 加载音乐文件
bg_mu = pygame.mixer.Sound(./sr/12.mp3)
# 开始播放音乐流
bg_mu.play()