import requests
import os

if __name__ == "__main__":
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3756.400 QQBrowser/10.5.4043.400'
    }
    # 创建一个文件夹，保存所有的图片
    if not os.path.exists('./3Cfile'):
        os.mkdir('./3Cfile')
    url = 'https://m.sohu.com/a/190240571_744790'
    page_text = requests.get(url=url, headers=headers).text
    filePath = './3Cfile/xiaodaijiemi' + '.html'
    fp = open(filePath, 'w', encoding='utf-8')
    fp.write(page_text)
    print('over!!!')
    fp.close()
