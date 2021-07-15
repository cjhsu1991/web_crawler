# 要安裝的套件
!pip3 install beautifulsoup4
!pip3 install requests

# 使用 beautifulsoup 分析爬取的資料
import requests
from bs4 import BeautifulSoup
url = 'https://invest.cnyes.com/twstock/TWS/2603/overview'
response = requests.get(url)
# tv-lightweight-charts
soup = BeautifulSoup(response.text,"html.parser")
chart = soup.find(class_='jsx-413197148 jsx-556393929 transition-ratio-stock__body')
print(chart)

# find_all
charts = soup.find_all(class_='jsx-413197148 jsx-556393929 transition-ratio-stock__body')
for chart in charts:
  print(chart.text)
