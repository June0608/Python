# ch2_12.py
import openpyxl

fn = "data2_12.xlsx"
wb = openpyxl.load_workbook(fn)
ws = wb.active
ws.protection.sheet = True
ws.protection.enable()
wb.save("out2_12.xlsx")




