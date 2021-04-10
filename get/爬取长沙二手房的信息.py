# 爬取长沙二手房的信息
import requests
from bs4 import BeautifulSoup
import re

if __name__ == "__main__":
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3756.400 QQBrowser/10.5.4043.400'
    }
    filePath = './get/ershoufang_page' + '.html'
    fp1 = open(filePath, 'w', encoding='utf-8')
    url = 'https://cs.lianjia.com/ershoufang/rs%E9%95%BF%E6%B2%99%E5%90%8D%E9%83%BD%E8%8A%B1%E5%9B%AD/'
    page_text = requests.get(url=url, headers=headers).text
    # fp1.write(page_text)
    soup = BeautifulSoup(page_text, 'lxml')
    li_list = soup.select('.leftContent > ul > li',)
    # print(li_list[0])
    # 每一个li下面图片的链接href
    pic_href_list = []
    detail_tag = []
    for li in li_list:
        # 对每一个li标签，实例化BeautifulSoup对象，需要将页面源码数据加载到该对象中
        # li_text = li.text  li.text就是文本:'房东诚心出售  地铁口  精装修 满五唯一必看好房名都花园    -  赤岗冲 3室2厅 | 124.64平米 | 南 | 精装 | 中楼层(共30层) | 2007年建 | 板塔结合10人关注 / 3个月以前发布近地铁VR房源房本满五年132.8万单价10655元/平米关注加入对比'

        li_soup = BeautifulSoup(li_text, 'lxml')
        # 找到每一个图片链接并保存在pic_href_list列表中
        img = li.a.img['src']
        print(img + 'over!!!')
        pic_href_list.append(img)
        # 存储每一个二手房的详情信息

        # detail_soup = BeautifulSoup(li, 'lxml')
        info_list = li_soup.select('li > .info clear')
        print(info_list[0])
        break
