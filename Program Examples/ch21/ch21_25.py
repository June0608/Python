# ch21_25.py
import pandas as pd

pd.set_option('display.unicode.east_asian_width', True)
# 讀取總公司員工資料
top = pd.read_excel("data21_21a.xlsx",
                    skiprows=1,usecols="B:E")
# 讀取分公司員工資料
bottom = pd.read_excel("data21_21b.xlsx",
                       skiprows=1,usecols="B:E")
df = top.append(bottom,ignore_index=True)    
print("總公司員工資料")
print(top)
print("-"*70)
print("分公司員工資料")
print(bottom)
print("-"*70)
print("合併結果")
print(df)





