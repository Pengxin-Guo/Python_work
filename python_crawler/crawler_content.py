import requests
import re
from datetime import datetime
from bs4 import BeautifulSoup
newsurl = 'http://news.sina.com.cn/2018-05-24/doc-ihaysviy0007849.shtml'
res = requests.get(newsurl)
res.encoding = 'utf-8'
#print(res.text)
soup = BeautifulSoup(res.text, 'html.parser')
print(soup.select('.main-title')[0].text)
#print(soup.select('.date-source'))
datesource = soup.select('.date')[0].text
dt=datetime.strptime(datesource, '%Y年%m月%d日 %H:%M')
print(datesource)
print(dt)
medianame = soup.select('.source')[0].text
print(medianame)
#article=[]
#for p in soup.select('#article p')[:-1]:
#    article.append(p.text.strip())
#print(article)
#print('\n'.join(article))
artcle='\n'.join([p.text.strip() for p in soup.select('#article p')[:-1]])
print(artcle)
editor = soup.select('.show_author')[0].text.lstrip('责任编辑：')
print(editor)
m=re.search('doc-i(.+).shtml', newsurl)
newid = m.group(1)
print(newid)