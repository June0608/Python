# ch1_12.py
import glob

mydir = input('請輸入指定資料夾 : ')
key = input('請輸入關鍵字 : ')
keyword = mydir + '*' + key + '*.xlsx'
files = glob.glob(keyword)
for fn in files:
    print(fn)








      




