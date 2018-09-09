import xlrd

rb = xlrd.open_workbook(r'../python_jieba/jieba_news_nefu.xlsx')
sheet = rb.sheet_by_index(0)
strs = ''
for i in range(1, 4040):
    str1 = sheet.cell(i, 5).value
    str1 += '\n'
    strs += str1
with open("./corpus_nefu.txt", 'w', encoding='utf-8') as f:
        f.writelines(strs)