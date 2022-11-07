    # requests模块
    # urllib模块    古老
# requests模块
# 便捷和方便,python中原生的一款基于网络请求的模块，功能十分强大，简单编辑，效率极高
# 作用：模拟浏览器发请求。
# ------------------------
# 如何使用：（requests模块的编码流程）
#       - 指定URL
#         - 发起请求，get或者post，requests会同时发起get和post
#         - 获取响应的数据
#         - 持久化存储
# ------------  ---------------------
'''
爬取搜狗首页数据
'''
# import requests
# if __name__ == "main":
#     url = 'https://www.sogou.com/'  #指定url
#     response = requests.get(url=url)   #发起请求,获取响应数据，get方法会返回一个响应对象，所对应的对象是get响应的对象
#     pang_text = response.text   #获取响应数据。text返回的是字符串形式的响应数据
#     print(pang_text)
#     with open('./sogo.html','w',encoding='utf-8') as fp:#持久化存储
#         fp.write(pang_text)
#         print('爬取数据结束')
#     import fileinput

# import requests
# if __name__ == 'main':
#     url = 'www.jd.com/'
#     response = requests.get(url = url)
#     pang_text = response.text
#     print(pang_text)
#     with open('./爬虫.html','w',encoding='utf-8') as fp:
#         fp.write(pang_text)
#     print('爬取成功')
# import requests
#
# if __name__ == '__main__':
#     # 第一步：指定url
#     url = 'https://www.jd.com/'
#     # 第二步：发起请求
#     response = requests.get(url)
#     # 第三步：获取响应数据
#     page_text = response.text
#     print(page_text)
#     # 第四步：持久化存储
#     with open('./搜狗首页.html', 'w', encoding='utf-8') as fp:
#         fp.write(page_text)
#     print('爬取结束')
import requests
if __name__ == '__main__':
    url = 'https://www.microsoft.com/'
    response = requests.get(url)
    page_text = response.text
    print(page_text)
    with open('./实战爬虫.html','w',encoding='utf-8') as fp:
        fp.write(page_text)
        print('爬取成功')
# import requests
# if __name__ == 'main':
#     # url = 'https://www.microsoft.com/'
#     url = 'https://www.jd.com'
#     response = requests.get(url)
#     page_text = response.text
#     print(page_text)
#     # response = requsts.get(url)
#     # page_text = response.text
#     # print(page_text)
#     # with open('./爬虫.html','w',encoding='urf-8') as fp:
#     #     fp.write(page_text)
#     #     print('爬取成功')