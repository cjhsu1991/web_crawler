#!pip3 install beautifulsoup4

from bs4 import BeautifulSoup
import requests
r = requests.get('https://ithelp.ithome.com.tw')
print(r)

soup = BeautifulSoup(r.text, 'html.parser')

#print(soup)
#呈現正常的html格式
print(soup.prettify())

#取得<title></title>的資料
title = soup.title

#取得<title></title> remove html tag 後的資料
titleText = title.text


# find qa-list all data
qa_lists = soup.find_all("div", class_="qa-list")
for qa_list in qa_lists:
    print(qa_list) 
    

# 爬取技術文章
qa_lists = soup.find_all("div", class_="qa-list")
i = 0
# 印出前30篇文章的標題、描述、作者及發布時間
for qa_list in qa_lists:
    i = i + 1
    print("第",i,"篇技術文章")
    # 文章標題
    print(qa_list.find("h3").text.strip())
    # 文章描述
    print(qa_list.find("p", class_="qa-list__desc").text.strip())
    # 作者
    print(qa_list.find("a", class_="qa-list__info-link").text.strip())
    # 發布時間
    print(qa_list.find("a", class_="qa-list__info-time").text.strip())