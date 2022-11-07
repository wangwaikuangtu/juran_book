# 导入网络连接模块
import requests
# 导入处理html格式的模块

from lxml

url='https://movie.douban.com/chart'

# 为了应对反爬虫机制，设置头部信息，是一个字典数据{'User-Agent':'...','cookies':'...',...}
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36 Edg/101.0.1210.39'}

# 发送请求，获得响应
r=requests.get(url,headers=headers)
# 把获得的响应文本内容，转换为可操作的html对象
html = etree.HTML(r.text)

# 通过元素特殊的属性，来唯一确定要找的元素（超链接a标签）
# '//'代表从网页的任意位置查找，'div' 代表指定查找所有div元素，'[@class="pl2"]' 是对前面div的限制，代表只查找符合属性class=pl2的div元素，
# '/a' 代表之前找到的div的下级a元素
电影元素=html.xpath('//div[@class="pl2"]/a')
电影名列表=[]
# xpath获得内容一般是多个元素，是一个列表类型
# 使用循环读取每一个元素
for i in 电影元素:
    # i.text 是a标签的内容（也就是链接的文字）
    #print(i.text.rstrip('/ ').strip('\\n').strip())
    电影名=i.text.rstrip('/ ').strip('\\n').strip()
    电影名列表=电影名列表+[电影名]

# '/@href' 代表获取前面a元素的href属性的值
链接元素=html.xpath('//div[@class="pl2"]/a/@href')
链接列表=[]
# xpath获得内容一般是多个元素，是一个列表类型
# 使用循环读取每一个元素
for i in 链接元素:
    # i 是每个a标签的href属性对应的值
    链接列表=链接列表+[i]

# 获取显示评分的元素span，指定这个元素的特点是class属性等于rating_nums
评分元素=html.xpath('//span[@class="rating_nums"]')
评分列表=[]
# xpath获得内容一般是多个元素，是一个列表类型
# 使用循环读取每一个元素
for i in 评分元素:
    # i.text 是span标签里的内容
    评分=i.text
    评分列表=评分列表+[评分]

print('电影名列表',end=':')
print(电影名列表)
print('链接列表',end=':')
print(链接列表)
print('评分列表',end=':')
print(评分列表)

# 把爬取的信息保存到csv文件中（csv文件可以用excel打开，并且能方便后续分析数据）
f= open(E:\python_demo\爬虫\\豆瓣电影排名信息.csv','w')
# 写入标题栏
f.write('电影名,链接,评分\n')
# 循环电影数量的次数，把每个电影的信息保存到同一行
for i in range(len(电影名列表)):
    电影名=电影名列表[i]
    链接=链接列表[i]
    评分=评分列表[i]
    # 以一定的格式（逗号分隔每个信息），写入文件
    f.write(f'{电影名},{链接},{评分}\n')
# 关闭文件对象
f.close()
