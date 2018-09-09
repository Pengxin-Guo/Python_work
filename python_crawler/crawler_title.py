import requests
from bs4 import BeautifulSoup
res=requests.get('http://news.sina.com.cn/china/')
res.encoding = 'utf-8'
#print(res.text)
soup=BeautifulSoup(res.text, 'html.parser')
for news in soup.select('.news-item'):
    if len(news.select('h2')) > 0:
        title = news.select('h2')[0].text    #标题
        time = news.select('.time')[0].text  #时间
        href = news.select('a')[0]['href']   #链接
        print(time, title, href)
