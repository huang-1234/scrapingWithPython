
# encoding:UTF-8
import requests


def getPage(url):
    # 1,指定url
    url1 = url
    # UA伪装：
    # UA：User-Agent
    headers = {
        'User-Agent': "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Mobile Safari/537.36"
    }
    # 2，发起请求
    response = requests.get(url=url1, headers=headers)
    # 3，获取响应数据
    page_text = response.text
    # 打印爬取的网页
    print(page_text)
    # 为存储文件指定名字
    filestr = input("please input the file name you want:")
    fileName = filestr + '.html'
    #  4，持久化存储
    with open(fileName, 'w', encoding='utf-8') as fp:
        fp.write(page_text)


url1 = "http://product.dangdang.com/23834026.html#ddclick_reco_product_alsobuy"
getPage(url1)
