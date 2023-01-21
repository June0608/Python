# ch2_7.py
import openpyxl

fn = "data2_7.xlsx"
wb = openpyxl.load_workbook(fn)             # 開啟活頁簿
ws1 = wb['2025Q1']
ws1.sheet_properties.tabColor = "0000FF"
ws2 = wb['2025Q2']
ws2.sheet_properties.tabColor = "00FF00"
ws3 = wb['2025Q3']
ws3.sheet_properties.tabColor = "FF0000"
ws4 = wb['2025Q4']
ws4.sheet_properties.tabColor = "FFFF00"
wb.save('out2_7.xlsx')                      # 將活頁簿儲存





