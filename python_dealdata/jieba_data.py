import jieba
from collections import Counter
from xlutils.copy import copy

def stopwordslist(filepath):
    stopwords=[line.strip() for line in open(filepath, 'r', encoding='gbk').readlines()]
    for i in stopwords:
       if i=='':
            stopwords.remove(i)
    stopwords.append('')
    return stopwords

def seg_sentence(sentence):
    sentence_seged = jieba.cut(sentence.strip())
    stopwords = stopwordslist('/home/gpx/PycharmProjects/Python_work/python_jieba/discontinuation_words.txt')
    stopword = {"\\", "n","学校","工作","学院","我校"}
    outstr = ''
    for word in sentence_seged:
        if word not in stopwords and word not in stopword:
            if (word != '\t') & (word!='text'):
                outstr += word
                outstr += " "
    return outstr


def main():
    datapath = "/home/gpx/PycharmProjects/Python_work/python_scikit_learn/cluster_content.txt"
    fp = open(datapath,encoding='utf-8')
    data  = []
    for lines in fp.readlines():
        lines = lines.replace("\n", "").split(",")
        data.append(lines)
    fp.close()
    #sheet1 = rb.sheet_by_index(0)
    #wb = copy(rb)
    #sheet2 = wb.get_sheet(0)
    #for i in range(1, 4040):
    #    sentence = str(sheet1.cell(i, 3))
    #    outstr = seg_sentence(sentence)
    #    print(outstr)
    #   sheet2.write(i, 5, outstr)
    #wb.save(r'jieba_news_nefu.xlsx')
    data_jieba = []
    for data_sen in data:
        data_sentence = str(data_sen)
        data_str = seg_sentence(data_sentence)
        data_jieba.append(data_str)
    print(data_jieba)
    f = open("E:\Python\Python_work\python_dealdata\content_jieba.txt", 'w', encoding='utf-8')
    for data in data_jieba:
        f.write(data)
        f.write('\n')
main()