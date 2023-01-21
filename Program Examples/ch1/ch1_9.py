# ch1_9.py
import glob
import openpyxl

files = glob.glob('out1*.xlsx')
for file in files:
    wb = openpyxl.load_workbook(file)
    newfile = 'new' + file
    wb.save(newfile)
newfiles = glob.glob('new*.xlsx')
print("輸出拷貝結果")
for newf in newfiles:
    print(newf)








      




