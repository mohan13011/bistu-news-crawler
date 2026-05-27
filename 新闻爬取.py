import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from bs4 import BeautifulSoup
import requests
import os
print("当前目录：",os.getcwd())
count=1
with open("C:/Users/yangmohan/OneDrive/桌面/练习/news.txt","w",encoding="utf-8") as f:
    for page in range(0,20):
        if page==0:
            respond=requests.get("https://news.bistu.edu.cn/xxxw/index.html",verify=False)
        else:
            respond=requests.get(f"https://news.bistu.edu.cn/xxxw/index{page}.html",verify=False)
        respond.encoding="utf-8"
        respond_text=respond.text
        #print(respond.status_code)
        if respond.status_code==200:
            soup=BeautifulSoup(respond_text,"html.parser")
            find1=soup.find_all(attrs={"class":"gp-f20 gp-ellipsis sub1tit"})
            find2=soup.find_all(attrs={"class":"gp-f16 gp-ellipsis sub1btit"})
            find=find1+find2
            for news in find:
                print(f"{count}.",news.text)
                f.write(f"{count}.{news.text.strip()}\n")
                count+=1
        else:
            print("错误！")