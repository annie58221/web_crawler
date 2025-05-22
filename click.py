import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

options = Options()
options.add_argument("--headless")
service = Service("web_crawler/chromedriver-linux64/chromedriver")

browser = webdriver.Chrome(service = service,options = options)
browser.get("https://www.ptt.cc/bbs/NBA/index.html")

title = browser.find_elements(By.CSS_SELECTOR, ".title > a")
article_urls = [link.get_attribute("href") for link in title]

for link in article_urls:
    browser.get(link)
    print("url = ", link)

    try:
        content = browser.find_element(By.ID, "main-content")
        lines = content.text.splitlines()

        content_lines = []
        for line in lines:
            if line.strip() == "--":
                break
            if any(keyword in line for keyword in ["作者", "標題", "時間", "看板"]):
                continue
            content_lines.append(line)

        print("文章內文：")
        print("\n".join(content_lines))
    except:
        print("nothing")

    time.sleep(1)

browser.quit()