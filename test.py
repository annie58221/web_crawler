import requests
from bs4 import BeautifulSoup
from selenium import webdriver

url = "https://www.ptt.cc/bbs/Baseball/M.1747748607.A.D81.html"
resp = requests.get(url)
soup = BeautifulSoup(resp.text, "html.parser")

for entry in soup.find_all(class_="push"):
    title = entry.find(class_="f3 push-content")
    if title:
        print(title.text.strip().lstrip(": ").strip())
    else:
        print("[已刪除]", title.text.strip() if title else "(無標題區)")

