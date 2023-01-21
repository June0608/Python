# ch1_10.py
import glob
import openpyxl

files = glob.glob('out1*.xlsx')
for file in files:
    wb = openpyxl.load_workbook(file)
    newfile = file.replace('out','new')
    wb.save(newfile)
newfiles = glob.glob('new1*.xlsx')
print("輸出拷貝結果")
for newf in newfiles:
    print(newf)








      




