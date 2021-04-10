
import requests
from bs4 import BeautifulSoup

url = 'https://img95.699pic.com/photo/40139/2123.gif_wh300.gif'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3756.400 QQBrowser/10.5.4043.400'

}
page_text = requests.get(url=url, headers=headers).text
soup = BeautifulSoup(page_text, 'lxml')
img_src = soup.select()
