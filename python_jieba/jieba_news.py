import jieba
from collections import Counter
import xlrd
import xlwt
from xlutils.copy import copy

def stopwordslist(filepath):
    stopwords=[line.strip() for line in open(filepath, 'r').readlines()]
    for i in stopwords:
       if i=='':
            stopwords.remove(i)
    stopwords.append('')
    return stopwords

def seg_sentence(sentence):
    sentence_seged = jieba.cut(sentence.strip())
    stopwords = stopwordslist('discontinuation_words.txt')
    outstr = ''
    for word in sentence_seged:
        if word not in stopwords:
            if (word != '\t') & (word!='text'):
                outstr += word
                outstr += " "
    return outstr

def main():
    rb = xlrd.open_workbook(r'E:\Python\Python_work\python_crawler\haha4040.xlsx')
    sheet1 = rb.sheet_by_index(0)
    wb = copy(rb)
    sheet2 = wb.get_sheet(0)
    for i in range(1, 4040):
        sentence = str(sheet1.cell(i, 3))
        outstr = seg_sentence(sentence)
        print(outstr)
        sheet2.write(i, 5, outstr)
    wb.save(r'jieba_news_nefu.xlsx')
main()