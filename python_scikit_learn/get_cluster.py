import xlrd
from Kmeans import clf_labels
from Kmeans import n_cluster
rb = xlrd.open_workbook(r'E:\Python\Python_work\python_jieba\jieba_news_nefu.xlsx')
sheet1 = rb.sheet_by_index(0)
labels=[]
for i in range(n_cluster):   #创建n_cluster个列表，用来存储各个类中包含哪些新闻
    labels.append([])
for i in range(len(clf_labels)):
    #下面这些是把标题加进去
    '''strs=sheet1.cell(i+1,2).value     #去掉前面的text:
    labels[clf_labels[i]].append(strs)'''
    #下面这些是把新闻序号加进去
    #labels[clf_labels[i]].append(i)  #新闻在数据库中的主码
    #下面这些是把新闻内容加进去
    strs = sheet1.cell(i + 1, 3).value  # 去掉前面的text:
    labels[clf_labels[i]].append(strs)
f=open("E:\Python\Python_work\python_scikit_learn\cluster_content.txt",'w',encoding='utf-8')
for i in range(n_cluster):
    f.write(str(labels[i]))
    f.write('\n')