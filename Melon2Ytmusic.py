import tkinter as tk
from tkinter import scrolledtext, messagebox
from threading import Thread
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from ytmusicapi import YTMusic
import time
from datetime import datetime
import os
import subprocess
import requests

def authenticate_ytmusic():
    script_dir = os.path.dirname(os.path.abspath(__file__))  # 스크립트가 위치한 폴더
    os.chdir(script_dir)  # 작업 디렉토리 변경

    # OAuth 인증 명령 실행
    try:
        subprocess.Popen(["ytmusicapi", "oauth"])
        messagebox.showinfo("Info", "브라우저에서 인증 후, 터미널에서 Enter 키를 눌러 인증을 완료해주세요.")
    except Exception as e:
        messagebox.showerror("Error", f"OAuth 인증 중 오류가 발생했습니다: {e}")

def crawl_melon():
    if not os.path.exists('oauth.json'):
        messagebox.showwarning("Warning", "OAuth 파일이 없습니다. 터미널에서 'ytmusicapi oauth'를 실행해 주세요.")
        return

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

    # YouTube Music에 로그인
    ytmusic = YTMusic('oauth.json')

    # 오늘 날짜를 포함한 플레이리스트 이름 생성
    today = datetime.now().strftime("%Y-%m-%d")
    playlist_name = f"Melon Top 100 - {today}"

    # 플레이리스트 생성
    playlist_id = ytmusic.create_playlist(playlist_name, "Melon chart top songs")

    # 각 곡을 YouTube Music에서 검색하고 플레이리스트에 추가
    for index, title in enumerate(song_titles):
        search_results = ytmusic.search(title, filter='songs')
        if search_results:
            song_id = search_results[0]['videoId']
            ytmusic.add_playlist_items(playlist_id, [song_id])
            text_area.insert(tk.END, f"{index + 1}/{len(song_titles)}: '{title}' added to the playlist.\n")
        else:
            text_area.insert(tk.END, f"{index + 1}/{len(song_titles)}: '{title}' not found.\n")
        text_area.see(tk.END)

    text_area.insert(tk.END, "Melon 플레이리스트 생성 완료\n")

def crawl_billboard():
    if not os.path.exists('oauth.json'):
        messagebox.showwarning("Warning", "OAuth 파일이 없습니다. 터미널에서 'ytmusicapi oauth'를 실행해 주세요.")
        return

    # 빌보드 Hot 100 페이지 URL
    url = 'https://www.billboard.com/charts/hot-100/'

    # 페이지 요청 및 HTML 파싱
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # 차트에서 곡 정보 추출
    chart_entries = soup.find_all('li', class_='o-chart-results-list__item')

    # 각 곡의 제목과 아티스트 추출
    song_titles = []
    for entry in chart_entries:
        title_element = entry.find('h3', class_='c-title')
        artist_element = entry.find('span', class_='c-label')

        if title_element and artist_element:
            title = title_element.get_text(strip=True)
            artist = artist_element.get_text(strip=True)
            song_titles.append(f"{title} by {artist}")

    # YouTube Music에 로그인
    ytmusic = YTMusic('oauth.json')

    # 오늘 날짜를 포함한 플레이리스트 이름 생성
    today = datetime.now().strftime("%Y-%m-%d")
    playlist_name = f"Billboard Hot 100 - {today}"

    # 플레이리스트 생성
    playlist_id = ytmusic.create_playlist(playlist_name, "Billboard Hot 100 songs")

    # 각 곡을 YouTube Music에서 검색하고 플레이리스트에 추가
    for index, title in enumerate(song_titles):
        search_results = ytmusic.search(title, filter='songs')
        if search_results:
            song_id = search_results[0]['videoId']
            ytmusic.add_playlist_items(playlist_id, [song_id])
            text_area.insert(tk.END, f"{index + 1}/{len(song_titles)}: '{title}' added to the playlist.\n")
        else:
            text_area.insert(tk.END, f"{index + 1}/{len(song_titles)}: '{title}' not found.\n")
        text_area.see(tk.END)

    text_area.insert(tk.END, "Billboard 플레이리스트 생성 완료\n")

def start_crawling_melon():
    thread = Thread(target=crawl_melon)
    thread.start()

def start_crawling_billboard():
    thread = Thread(target=crawl_billboard)
    thread.start()

# Tkinter UI 생성
root = tk.Tk()
root.title("Music Chart to YouTube Music")

# OAuth 인증 버튼
oauth_button = tk.Button(root, text="OAuth 인증", command=authenticate_ytmusic)
oauth_button.pack()

# 멜론 크롤링 시작 버튼
start_melon_button = tk.Button(root, text="Start Crawling Melon", command=start_crawling_melon)
start_melon_button.pack()

# 빌보드 크롤링 시작 버튼
start_billboard_button = tk.Button(root, text="Start Crawling Billboard", command=start_crawling_billboard)
start_billboard_button.pack()

# 로그 표시를 위한 스크롤 텍스트 영역
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10)
text_area.pack(pady=10)

# UI 실행
root.mainloop()