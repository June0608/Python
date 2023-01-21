# ch1_8.py
import glob
import openpyxl

files = glob.glob('out1*.xlsx')
for file in files:
    wb = openpyxl.load_workbook(file)
    print(f'下載 {file} 成功')
    print(f'{file} = {wb.sheetnames}')






      




