# ch1_6_1.py
import openpyxl

fn = 'sales.xlsx'
wb = openpyxl.load_workbook(fn)  # 開啟sales.xlsx活頁簿
wb.save('out1_6_1.xlsx')         # 活頁簿儲存至out1_6_1.xlsx
print("複製完成")
wb.close()











