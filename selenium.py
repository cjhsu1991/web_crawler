from selenium import webdriver # 引入 selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import requests

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome = webdriver.Chrome(chrome_options=chrome_options) # 如果 driver 沒跟你程式放一起 可以這樣寫driver = webdriver.Chrome("這裡放你的driver路徑")

chrome.get("輸入要抓取的網址") # 輸入要抓取的網址
text_data = chrome.find_element_by_class_name("要抓取的class的名稱").text # 取得特定class的資料(remove html tag後)

text_data = chrome.find_element_by_id_name("要抓取的id的名稱").text # 取得特定id的資料(remove html tag後)


element = chrome.find_element_by_class_name("要抓取的class的名稱") 
print(element.get_attribute("innerHTML")) # 取得特定 id 資料的 html source code
