# ch1_11.py
import glob

key = input('請輸入關鍵字 : ')
keyword = '*' + key + '*.xlsx'  # 組成關鍵字的字串
files = glob.glob(keyword)
for fn in files:
    print(fn)








      




