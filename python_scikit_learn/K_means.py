# coding=utf-8
"""
Created on 2016-01-06 @author: Eastmount
"""

import time
import re
import os
import sys
import codecs
import shutil
import numpy as np
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer


#########################################################################
#                           第一步 计算TFIDF

corpus = []  # 文档预料 空格连接

# 读取预料 一行预料为一个文档
for line in open('./corpus_nefu.txt', 'r', encoding='utf-8').readlines():
    print(line)  #显示每一条新闻
    corpus.append(line.strip())
    # print corpus
time.sleep(5)

# 将文本中的词语转换为词频矩阵 矩阵元素a[i][j] 表示j词在i类文本下的词频
vectorizer = CountVectorizer()

# 该类会统计每个词语的tf-idf权值
transformer = TfidfTransformer()

# 第一个fit_transform是计算tf-idf 第二个fit_transform是将文本转为词频矩阵
tfidf = transformer.fit_transform(vectorizer.fit_transform(corpus))

# 获取词袋模型中的所有词语
word = vectorizer.get_feature_names()

# 将tf-idf矩阵抽取出来，元素w[i][j]表示j词在i类文本中的tf-idf权重
weight = tfidf.toarray()

resName = "Tfidf_Result_nefu.txt"
result = codecs.open(resName, 'w', encoding='utf-8')
for j in range(len(word)):
    result.write(word[j] + ' ')
result.write('\r\n\r\n')

# 打印每类文本的tf-idf词语权重，第一个for遍历所有文本，第二个for便利某一类文本下的词语权重
for i in range(len(weight)):
    print(u"-------这里输出第", i, u"类文本的词语tf-idf权重------")
    for j in range(len(word)):
        result.write(str(weight[i][j]) + ' ')
    result.write('\r\n\r\n')

result.close()

########################################################################
#                               第二步 聚类Kmeans

print('Start Kmeans:')
from sklearn.cluster import KMeans
########################################################################
#这儿为改进部分，利用肘部法则确定最优K值
# """
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
font = FontProperties(fname=r"/usr/share/fonts/opentype/noto/NotoSerifCJK-Regular.ttc", size=10)  #deepin中的字体
# font = FontProperties(fname=r"C:\Windows\Fonts\STSONG.TTF", size=10)                              #Windows中的字体
from scipy.spatial.distance import cdist
K=range(1,10)
meandistortions=[]
for k in K:
    print("k=%d 聚类ing"%(k))
    kmeans=KMeans(n_clusters=k)
    kmeans.fit(weight)
    meandistortions.append(sum(np.min(cdist(weight, kmeans.cluster_centers_, 'euclidean'), axis=1))/weight.shape[0])
plt.plot(K,meandistortions, 'bx-')
plt.xlabel('k')
plt.ylabel(u'平均畸变程度', fontproperties=font)
plt.title(u'用肘部法则来确定最佳的K值', fontproperties=font)
plt.show()
# """


########################################################################
#下方为原始算法
n_cluster=5  #引入n_cluster方便其他py文件引用
clf = KMeans(n_clusters=n_cluster)
s = clf.fit(weight)
print(s)

# 5个中心点
print("下面为5个中心点")
print(clf.cluster_centers_)
clf_labels=clf.labels_   #引入clf_labels方便其他py文件引用这个变量
# 每个样本所属的簇
print(clf.labels_)
i = 0
while i < len(clf.labels_):
    print(i, clf.labels_[i])
    i = i + 1
# 用来评估簇的个数是否合适，距离越小说明簇分的越好，选取临界点的簇个数
print(clf.inertia_)