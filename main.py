import os
import selenium.webdriver as webdriver
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0'
edge_driver_path=os.path.join(os.getcwd(), 'msedgedriver.exe')
edge_service=Service(edge_driver_path)
edge_options=Options()
edge_options.add_argument(f'user-agent={user_agent}')
driver=webdriver.Edge(service=edge_service,options=edge_options)
driver.get("https://www.ptt.cc/bbs/Baseball/index.html")
tags = driver.find_elements(By.CLASS_NAME,'title')
for tag in tags:
    print(tag.text)
#按上一頁
link = driver.find_element(By.LINK_TEXT,'‹ 上頁')
link.click()
tags = driver.find_elements(By.CLASS_NAME,'title')
for tag in tags:
    print(tag.text)

driver.save_screenshot("test1.png")
print(driver.page_source)
driver.close()


