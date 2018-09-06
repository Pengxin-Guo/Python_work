import xlrd
from K_means import clf_labels
from K_means import n_cluster
rb = xlrd.open_workbook(r'../python_jieba/jieba_news_nefu.xlsx')
sheet1 = rb.sheet_by_index(0)
labels1=[]
labels2=[]
for i in range(n_cluster):                 # 创建n_cluster个列表，用来存储各个类中包含哪些新闻
    labels1.append([])
    labels2.append([])
for i in range(len(clf_labels)):
    #下面这些是把标题加进去
    '''strs=sheet1.cell(i+1,2).value     #去掉前面的text:
    labels[clf_labels[i]].append(strs)'''
    #下面这些是把新闻序号加进去
    labels2[clf_labels[i]].append(i)       # 新闻在数据库中的主码
    #下面这些是把新闻内容加进去
    strs = sheet1.cell(i + 1, 3).value     # 去掉前面的text:
    labels1[clf_labels[i]].append(strs)
f1=open("./cluster_content.txt",'w',encoding='utf-8')
f2=open("./cluster_id.txt",'w',encoding='utf-8')
for i in range(n_cluster):
    f1.write(str(labels1[i]))
    f1.write('\n')
    f2.write(str(labels2[i]))
    f2.write('\n')