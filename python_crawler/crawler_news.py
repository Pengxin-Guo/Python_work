from builtins import len, range
from datetime import datetime
import urllib.request
from locale import str

import pandas
from bs4 import BeautifulSoup
global a
a = []


def getinfo(newsurl):
    ans = {}
    tmp = urllib.request.urlopen(newsurl)
    soup = BeautifulSoup(tmp, 'html.parser')
    ans['head'] = soup.select('div.m-text.m-text-b h1')[0].text+soup.select('div.m-text.m-text-b h2')[1].text
    ans['text'] = soup.select('div#vsb_content')[0].text.strip()
    ss = soup.select('div.l span')
    ans['time'] = datetime.strptime(ss[0].text, '日期：%Y-%m-%d')
    ans['dept'] = ss[1].text.strip('发布单位：')
    a.append(ans)


def func(newsurl):
    tmp = urllib.request.urlopen(newsurl)
    soup = BeautifulSoup(tmp, 'html.parser')
    for tmp in soup.select('div.main div.m-news ul.ul-news a'):
        s = 'http://news.nefu.edu.cn/' + tmp['href'].strip('..').strip('/')
        # print(s)
        getinfo(s)


def main():
    for i in range(1, 130):
        i = i * 2
        try:
            print("正在爬取第" + str(i) + "页新闻")
            func('http://news.nefu.edu.cn/dlyw/' + str(i) + '.htm')
        except:
            print("error")
    print("新闻爬取完毕," + "共" + str(len(a)) + "条新闻")

    x = pandas.DataFrame(a)
    x.head(10)
    x.to_excel('./nefu_news.xlsx')


# 程序从这里开始执行
main()
