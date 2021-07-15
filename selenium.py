from selenium import webdriver # 引入 selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import requests

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome = webdriver.Chrome(chrome_options=chrome_options) # 如果 driver 沒跟你程式放一起 可以這樣寫driver = webdriver.Chrome("這裡放你的driver路徑")

chrome.get("https://finance.sina.com.cn/futures/quotes/I0.shtml") # 輸入要抓取的網址
price_text = chrome.find_element_by_class_name("open-price").text
print("開盤價:",price_text)

red_text = chrome.find_element_by_class_name("price").text
print("現價:",red_text)

# 漲幅 amt
amt_text = chrome.find_element_by_class_name("amt").text
print("漲幅:",amt_text)

# 成交量 volume
volume_text = chrome.find_element_by_class_name("volume").text
print("成交量:",volume_text)
