# ch22_5.py
import pandas as pd
import numpy as np

pd.set_option('display.unicode.east_asian_width',True)
# 讀取員工資料
df = pd.read_excel("data22_5.xlsx")
# 建立樞紐分析表
pvt = df.pivot_table(values='銷售額', 
		     index='年度',
                     columns='地區',
		     aggfunc=np.sum)

print(pvt)



