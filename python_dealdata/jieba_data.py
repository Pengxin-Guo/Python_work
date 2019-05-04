import jieba


def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='gbk').readlines()]
    for i in stopwords:
       if i == '':
            stopwords.remove(i)
    stopwords.append('')
    return stopwords


def seg_sentence(sentence):
    sentence_seged = jieba.cut(sentence.strip())
    stopwords = stopwordslist('../python_jieba/discontinuation_words.txt')
    stopword = {"\\", "n", "学校", "工作", "学院", "我校"}
    outstr = ''
    for word in sentence_seged:
        if word not in stopwords and word not in stopword:
            if (word != '\t') & (word != 'text'):
                outstr += word
                outstr += " "
    return outstr


def main():
    datapath = "../python_scikit_learn/cluster_content.txt"
    fp = open(datapath, encoding='utf-8')
    data = []
    for lines in fp.readlines():
        lines = lines.replace("\n", "").split(",")
        data.append(lines)
    fp.close()
    data_jieba = []
    for data_sen in data:
        data_sentence = str(data_sen)
        data_str = seg_sentence(data_sentence)
        data_jieba.append(data_str)
    print(data_jieba)
    f = open("./content_jieba.txt", 'w', encoding='utf-8')
    for data in data_jieba:
        f.write(data)
        f.write('\n')


main()
