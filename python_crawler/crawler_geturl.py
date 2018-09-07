import requests
import json
res = requests.get('http://api.roll.news.sina.com.cn/zt_list?channel=news&cat_1=gnxw&cat_2==gdxw1||=gatxw||=zs-pl||=mtjj&level==1||=2&show_ext=1&show_all=1&show_num=22&tag=1&format=json&page=2&callback=newsloadercallback&_=1527213192046')
jd = json.loads(res.text.lstrip('  newsloadercallback(').rstrip(');'))
print(jd)
for ent in jd['result']['data']:
    print(ent['url'])