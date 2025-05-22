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
browser.get("https://www.dcard.tw/f/relationship")

