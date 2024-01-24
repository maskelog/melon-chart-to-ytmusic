from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from ytmusicapi import YTMusic
import time
from datetime import datetime

# 크롬 드라이버 설정
driver_path = "C:\\Temp\\chromedriver.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

# 멜론 차트 페이지로 이동
driver.get("https://www.melon.com/chart/index.htm")

# 페이지 로드를 위해 대기
time.sleep(5)

# 페이지 소스 가져오기
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# 순위 데이터 추출
rankings = soup.find_all(class_='rank01')
song_titles = [rank.find('a').get_text() for rank in rankings]

# WebDriver 닫기
driver.quit()

# ytmusicapi를 이용해 YouTube Music에 로그인
ytmusic = YTMusic('oauth.json')

# 오늘 날짜를 포함한 플레이리스트 이름 생성
today = datetime.now().strftime("%Y-%m-%d")
playlist_name = f"Melon Top Chart - {today}"

# 플레이리스트 생성
playlist_id = ytmusic.create_playlist(playlist_name, "Melon chart top songs")

# 각 곡을 YouTube Music에서 검색하고 플레이리스트에 추가
for index, title in enumerate(song_titles):
    search_results = ytmusic.search(title, filter='songs')
    if search_results:
        song_id = search_results[0]['videoId']
        ytmusic.add_playlist_items(playlist_id, [song_id])
        print(f"{index + 1}/{len(song_titles)}: '{title}' added to the playlist.")
    else:
        print(f"{index + 1}/{len(song_titles)}: '{title}' not found.")

print("플레이리스트 생성 완료")