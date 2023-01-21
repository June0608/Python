# ch1_6.py
import openpyxl

fn = 'sales.xlsx'
wb = openpyxl.load_workbook(fn)  # 開啟sales.xlsx活頁簿
wb.save('out1_6.xlsx')           # 將活頁簿儲存至out1_6.xlsx
print("複製完成")










