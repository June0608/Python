# ch1_13.py
import glob
import os

mydir = input('請輸入指定資料夾 : ')
key = input('請輸入關鍵字 : ')
for dirName, sub_dirNames, fileNames in os.walk(mydir):
    print(f"目前資料夾名稱 : {dirName}")
    keyword = dirName + '\*' + key + '*.xlsx'
    files = glob.glob(keyword)
    for fn in files:
        print(fn)
   








      




