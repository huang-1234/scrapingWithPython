'''
import requests
import json
import re
if __name__ == "__main__":
    url = "https://book.douban.com/subject/1873231/comments/"
    # requests.get()方法的参数
    instart = int(input())
    param = {
        'start': '0',
        'limit': '50',
        'status': 'P',
        'sort': 'new_score'
    }
    # UA伪装：
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3756.400 QQBrowser/10.5.4043.400"
    }
    # 2，发起请求
    # 3，获取响应数据
    page_text = requests.get(url=url, headers=headers).text
    # <span class="comment-info">
    #       <a href="https://www.douban.com/people/conetoiles/">浅苍</a>
    #         <span class="user-stars allstar40 rating" title="推荐"></span>
    #       <span class="comment-time">2011-01-09</span>
    #     </span>
    # print(list_data)
    #  4，持久化存储
    ex = '<span class="comment-info">.*?<span class="user-stars allstar([0-9]+) rating.*?</span>'
    moment_list = re.findall(ex, page_text, re.S)
    print(moment_list)
    pingfen = []
    for i in range(len(moment_list)):
        pingfen.append(int(moment_list[i])/10)
    print(pingfen)
    # 结束
    print("over!!!")
'''

# 取前50
import requests
import re
if __name__ == "__main__":
    url = "https://book.douban.com/subject/1873231/comments/"
    # requests.get()方法的参数
    # UA伪装：
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3756.400 QQBrowser/10.5.4043.400"
    }
    pingfen = []
    for start in range(3):
        param = {
            'start': start*20,
            'limit': '20',
            'status': 'P',
            'sort': 'new_score'
        }
        # 2，发起请求
        # 3，获取响应数据
        page_text = requests.get(url=url, params=param, headers=headers).text
        # 用正则表达式向该html标签提取评分
        # <span class="comment-info">
        #       <a href="https://www.douban.com/people/conetoiles/">浅苍</a>
        #         <span class="user-stars allstar40 rating" title="推荐"></span>
        #       <span class="comment-time">2011-01-09</span>
        #     </span>
        # print(list_data)
        #  4，持久化存储
        ex = '<span class="comment-info">.*?<span class="user-stars allstar([0-9]+) rating.*?</span>'
        moment_list = re.findall(ex, page_text, re.S)
        # print(moment_list)
        for i in range(len(moment_list)):
            pingfen.append(int(moment_list[i]) / 10)

    # print(pingfen)
    sum = 0
    for i in range(50):
        sum = sum+pingfen[i]
    average = sum / 50
    print("豆瓣评分的某书评分前50 is " + str(average) + "分")
    # 结束
    print("over!!!")
