# Python_work
#### 大创项目---个性化高校新闻分类推荐应用研究

注：此代码为聚类模块代码，支持语言`python3.6`，运行系统`Windows`、`Linux`均可。

1. 首先执行代码`crawler.py`，从学校新闻网站爬取所有新闻，存储到`nefu_news.xlsx`里面；
2. 然后执行代码`jieba_news.py`，利用哈工大的停用词表（存储在`discontinuation_words.txt`中）去除停用词，生成经过结巴切词后的新闻信息，并将其存储在`jieba_nefu_news.xlsx`中；
3. 为方便后面的计算或对接一些`sklearn`或`w2v`等工具，执行代码`change_xlsx_to_txt.py`，将所有新闻的分词结果存储在`nefu_news.txt`中，每行表示一条新闻的分词结果；
4. 接下来执行`get_tfidf.py`，计算新闻文本的`tfidf`矩阵，并将结果存储到`Tfidf_nefu_news.txt`中；
5. 之后执行`K_means.py`，先执行包含肘部法则的代码，得到畸变程度变化曲线，判断聚几类合适，然后将这部分代码注释掉，进行最终的聚类；
6. 然后执行`get_cluster.py`，将聚类结果保存到`cluster_id.txt`与`cluster_content.txt`中；
7. 然后执行`jieba_data.py`，对聚好类的新闻内容进行切词；
8. 最后执行`data_main_word.py`，得到每一类出现频率高的词语，挑选一个作为该类的类名。