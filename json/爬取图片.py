import requests
import re
import json
import os
if __name__ == "__main__":
    # 创建新的文件夹存放图片
    if not os.path.exists('./picturelibs'):
        os.mkdir('./picturelibs')
    if not os.path.exists('./filelibs'):
        os.mkdir('./filelibs')
    headers = {
        'User-Agent': "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Mobile Safari/537.36"
    }
    param = {
        'uigs_productid': 'pic',
        'ua': ' Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHT',
        'pagetype': 'searchlist_page',
        'p': '40230500',
        'st': '255',
        '_t': '1604240708423',
        '_r': '334',
        'uigs_st': '0'
    }
    url = "https://pic.sogou.com/pics?query=%E8%8B%B1%E9%9B%84%E8%81%94%E7%9B%9F%E5%90%84%E4%B8%AA%E8%8B%B1%E9%9B%84%E5%9B%BE%E7%89%87&ie=utf8&p=40230500&st=255&mode=255&policyType=0&rawQuery=%E8%8B%B1%E9%9B%84%E8%81%94%E7%9B%9F%E5%90%84%E4%B8%AA%E8%8B%B1%E9%9B%84%E5%9B%BE%E7%89%87"
    # 使用通用爬虫对url对应的一整张页面进行爬取
    page_text = requests.get(url=url, params=param, headers=headers).text
    fileNamePath = './filelibs/LOLyingxing' + '.html'
    with open(fileNamePath, 'w', encoding='utf-8') as fp:
        fp.write(page_text)
    # 使用聚焦爬虫将页面中所有的糗图进行解析/提取
    ex = '<li style="height: 158.442px; width: 288.395px;">.*?<img drag-img="(.*?)"onload.*?</li>'
    img_src_list = re.findall(ex, page_text, re.S)
    # 1, <img drag-img="https://i02piccdn.sogoucdn.com/cf1bff99529e2253"
    # 2, <img drag-img="https://i02piccdn.sogoucdn.com/731ae988fb5bc4e1"
    print(img_src_list)
