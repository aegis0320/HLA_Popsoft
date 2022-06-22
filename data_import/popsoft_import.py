import xlrd
import os
import re

xl_path = 'D:\\Gu\\Desktop\\大软目录\\【1995年8月】.xlsx'
file_path = 'D:\\Gu\\Desktop\\大软目录'
data = xlrd.open_workbook(xl_path)
table = data.sheet_by_name('Sheet1')

# 获取总行数
nrows = table.nrows
print(nrows)
# 获取总列数
ncols = table.ncols

# 获取一行的全部数值，例如第5行
row_value = table.row_values(5)
# 获取一列的全部数值，例如第6列
col_values = table.col_values(0)
print(col_values)
# 获取一个单元格的数值，例如第5行第6列
cell_value = table.cell(40, 0).value
print(cell_value)

print(os.listdir(file_path))
# -------------------
file_list = os.listdir(file_path)


for i in range(4, nrows):
    print(table.cell(i, 0).value)