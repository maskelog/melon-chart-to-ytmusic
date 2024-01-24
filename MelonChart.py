from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time

driver_path = "C:\\Temp\\chromedriver.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

# 순위 페이지로 이동
driver.get("https://www.melon.com/chart/index.htm")

# 페이지 로드를 위해 잠시 대기
time.sleep(5)

# 페이지 소스 가져오기
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

rankings = soup.find_all(class_='rank01')

# 순위 출력
for rank in rankings:
    title = rank.find('a').get_text()
    print(title)

# WebDriver 닫기
driver.quit()
