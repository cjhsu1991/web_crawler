import requests
from bs4 import BeautifulSoup
url = 'https://invest.cnyes.com/twstock/TWS/2603/overview'
response = requests.get(url)
# tv-lightweight-charts
soup = BeautifulSoup(response.text,"html.parser")
chart = soup.find(class_='jsx-413197148 jsx-556393929 transition-ratio-stock__body')
print(chart)
