import requests
import json
import pandas
import sqlite3
from datetime import datetime
from bs4 import BeautifulSoup

def getNewsDetail(newsurl):
    result = {}
    res = requests.get(newsurl)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    result['1_title'] = ' '.join([h.text.strip() for h in soup.select('.article h1')[:]])     # 标题
    result['2_article'] = ' '.join([p.text.strip() for p in soup.select('.article p')[:-1]])  # 正文
    #result['3_editor'] = soup.select('.article p')[-1].text                                  # 编辑
    return result


def main():
    urls = 'http://news.tsinghua.edu.cn/publish/thunews/9648/index_{}.html'
    news_total = []
    for i in range(2, 34):
        url = urls.format(i)
        print(url)
        res = requests.get(url)
        res.encoding = 'utf-8'
        soup = BeautifulSoup(res.text, 'html.parser')
        for j in range(20):
            newsurl = soup.select('.picwraper')[j].get('href')
            newsurl = 'http://news.tsinghua.edu.cn' + newsurl
            newsary = getNewsDetail(newsurl)
            news_total.append(newsary)
    df = pandas.DataFrame(news_total)
    # print(df)
    df.to_excel('news.xlsx')         # 将数据保存到Excel中
    # 下面是将数据存到数据库中
    # with sqlite3.connect('news.sqlite') as db:
    #    df.to_sql('news1',con=db)
    # 下面是从sqlite中读取数据
    # with sqlite3.connect('news.sqlite') as db:
    #    df2=pandas.read_sql_query('select * from news1',con=db)
    # print(df2)


main()
