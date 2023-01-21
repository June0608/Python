# ch1_7.py
import glob

print("方法1:列出\\Python\\ch1資料夾的所有Excel檔案")
for file in glob.glob('D:\\Python_Excel\\ch1\*.xlsx'):
    print(file)
    
print("方法2:列出目前資料夾的Excel檔案")
for file in glob.glob('*.xlsx'):
    print(file)

print("方法3:列出目前資料夾out1開頭的Excel檔案")
for file in glob.glob('out1*.xlsx'):
    print(file)
    
print("方法4:列出目前資料夾out1_開頭的Excel檔案")
for file in glob.glob('out1_?.xlsx'):
    print(file)




      




