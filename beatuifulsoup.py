# 要安裝的套件(如果沒裝以下兩個套件請先安裝)
# !pip3 install beautifulsoup4
# !pip3 install requests

# 使用 beautifulsoup 分析爬取的資料
import requests
from bs4 import BeautifulSoup
url = '要爬取的url'
response = requests.get(url)

# 如果只有一個的話
soup = BeautifulSoup(response.text,"html.parser")
chart = soup.find(class_='要爬取的class名稱')
print(chart)

# 如果有多個的話 使用 find_
charts = soup.find_all(class_='要爬取的class名稱')
for chart in charts:
    print(chart.text)

  
# 取得 tag 為 <title></title>的資料
title = soup.find("title")
# 印出 title 的文字 remove html tag 後
print(title.text)

# 取得 <h3> tag 的所有資料
h3s = soup.find_all("h3")
for h3 in h3s:
    print(h3.text)
