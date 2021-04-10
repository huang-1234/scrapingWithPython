
import requests
from bs4 import BeautifulSoup
if __name__ == "__main__":
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3756.400 QQBrowser/10.5.4043.400'
    }
    url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
    page_text = requests.get(url=url, headers=headers).text
    # 在首页中解析出章节的标题和详情页的url
    # 1.实例化BeautifulSoup对象，需要将页面源码数据加载到该对象中
    soup = BeautifulSoup(page_text, 'lxml')
    path1 = './get/sanguo' + '.html'
    path2 = './get/sanguo' + '.docx'
    fp1 = open(path1, 'w', encoding='utf-8')
    fp2 = open(path2, 'w', encoding='utf-8')
    li_list = soup.select('.book-mulu > ul > li')
    for li in li_list:
        title = li.a.string
        detail_url = 'https://www.shicimingju.com' + li.a['href']
        # 对详情页发起请求，解析出章节内容
        detail_page_text = requests.get(url=detail_url, headers=headers).text
        # 解析出详情页中相关的章节内容
        detail_soup = BeautifulSoup(detail_page_text, 'lxml')
        div_tag = detail_soup.find('div', class_='chapter_content')
        fp1.write(li + ':' + div_tag)
        print(li, '爬取成功！！！')
        contents = div_tag.text
        fp2.write(title + ':' + contents + '\n')
        print(title, '爬取成功！！！')
