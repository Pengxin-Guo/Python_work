import requests
from datetime import datetime
from bs4 import BeautifulSoup

def getNewsDetail(newsurl):
    result={}
    res=requests.get(newsurl)
    res.encoding='utf-8'
    soup=BeautifulSoup(res.text,'html.parser')
    result['title'] = soup.select('.main-title')[0].text                                       #标题
    datesource = soup.select('.date')[0].text
    result['date'] = datesource                                                                #时间
    #result['date'] = datetime.strptime(datesource,'%Y年%m月%d日 %H:%M')                        #时间
    result['medianame'] = soup.select('.source')[0].text                                       #来源
    result['artcle'] = '\n'.join([p.text.strip() for p in soup.select('#article p')[:-1]])     #正文
    result['editor'] = soup.select('.show_author')[0].text.lstrip('责任编辑：')                  #编辑
    return result
def main():
    newsurl = 'http://news.sina.com.cn/2018-05-24/doc-ihaysviy0007849.shtml'
    result = getNewsDetail(newsurl)
    print(result)
main()