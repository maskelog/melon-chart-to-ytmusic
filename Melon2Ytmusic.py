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

def authenticate_ytmusic():
    script_dir = os.path.dirname(os.path.abspath(__file__))  # Melon2Ytmusic.py 파일이 위치한 폴더
    os.chdir(script_dir)  # 작업 디렉토리 변경

    # OAuth 인증 명령 실행
    try:
        subprocess.Popen(["ytmusicapi", "oauth"])
        messagebox.showinfo("Info", "브라우저에서 OAuth 인증 절차를 완료해 주세요.")
    except Exception as e:
        messagebox.showerror("Error", f"OAuth 인증 중 오류가 발생했습니다: {e}")

def crawl_and_create_playlist():
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
    playlist_name = f"맬론 Top100 - {today}"

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
        text_area.see(tk.END)  # 스크롤 자동 이동

    text_area.insert(tk.END, "플레이리스트 생성 완료\n")

def start_crawling():
    # 스레드를 사용하여 UI가 멈추지 않도록 함
    thread = Thread(target=crawl_and_create_playlist)
    thread.start()

# Tkinter UI 생성
root = tk.Tk()
root.title("Melon2Ytmusic")

# OAuth 인증 버튼
oauth_button = tk.Button(root, text="OAuth 인증", command=authenticate_ytmusic)
oauth_button.pack()

# 시작 버튼
start_button = tk.Button(root, text="Start Crawling", command=start_crawling)
start_button.pack()

# 로그 표시를 위한 스크롤 텍스트 영역
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10)
text_area.pack(pady=10)

# UI 실행
root.mainloop()