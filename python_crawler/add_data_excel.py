import xlrd
import xlwt
from xlutils.copy import copy

rb = xlrd.open_workbook(r'news.xlsx')
wb = copy(rb)
sheet = wb.get_sheet(0)
for i in range(1, 60):
    sheet.write(i, 5, "实验一下")
wb.save(r'news1.xlsx')
