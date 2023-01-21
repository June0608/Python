import eikon as ek
import numpy as np
import pandas as pd
import cufflinks as cf
import configparser as cp
cf.set_config_file(offline=True) # set the piotting mode to offline
ek.set_app_key('9340bdf329f545c9a60008a2b4bc52fe6a8a074d')

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


headlines = ek.get_news_headlines('R:TSLA.O',count=3) # 擷取 TSLA.O 最新3則新聞
for index, headline_row in headlines.iterrows():
    print(headline_row['text']+"\n")      # 輸出 新聞標題
    #print("\n"+"\n")  
    story = ek.get_news_story(headline_row['storyId'])
    #print(story+"\n"+"\n"+"\n")       # 輸出 新聞內容

    #content.attach(MIMEText("Demo python send email"))  #郵件內容
    import smtplib
    with smtplib.SMTP(host="smtp.gmail.com", port="587") as smtp:  # 設定SMTP伺服器
        content = MIMEMultipart()  #建立MIMEMultipart物件
        content["subject"] = headline_row['text']  #郵件標題
        content["from"] = "junelinlin@gmail.com"  #寄件者
        content["to"] = "june.lin@lseg.com" #收件者
        content.attach(MIMEText(story, "html"))  # HTML郵件內容
        smtp.ehlo()  # 驗證SMTP伺服器
        smtp.starttls()  # 建立加密傳輸
        smtp.login("junelinlin@gmail.com", "scudoesqzyiffmjh")  # 登入寄件者gmail
        smtp.send_message(content)  # 寄送郵件