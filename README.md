# Melon2Ytmusic

## 프로젝트 개요

![image](https://github.com/maskelog/melon-chart-to-ytmusic/assets/30742914/280a7f7a-154e-4ac2-8ce4-2929eaf26e04)

Melon2Ytmusic은 멜론 차트와 빌보드 Hot 100 차트에서 음악을 크롤링하여 YouTube Music 플레이리스트에 자동으로 추가하는 파이썬 스크립트입니다. 이 프로그램은 GUI 인터페이스를 통해 사용자가 편리하게 음악 차트의 최신 곡들을 YouTube Music 플레이리스트에 추가할 수 있도록 도와줍니다.

## 주요 기능

- 멜론 차트와 빌보드 Hot 100 차트에서 상위 곡 목록 크롤링
- YouTube Music OAuth 인증
- 크롤링된 곡들을 YouTube Music 플레이리스트에 자동으로 추가

## 설치 방법

이 프로젝트를 사용하기 위해 다음과 같은 파이썬 라이브러리들이 필요합니다:

- `selenium`
- `beautifulsoup4`
- `ytmusicapi`

라이브러리들은 pip을 사용하여 설치할 수 있습니다:

```bash
pip install selenium beautifulsoup4 ytmusicapi
```

또한, 프로그램은 Google Chrome 브라우저와 해당 Chrome 버전에 맞는 ChromeDriver가 필요합니다. ChromeDriver는 [여기서](https://sites.google.com/a/chromium.org/chromedriver/downloads) 다운로드할 수 있습니다.

## 사용 방법

1. 터미널을 열고 `ytmusicapi oauth` 명령을 실행하여 YouTube Music 인증을 완료합니다.
2. `Melon2Ytmusic.py` 파일을 실행합니다.
3. GUI에서 "Start Crawling Melon" 또는 "Start Crawling Billboard" 버튼을 클릭하여 멜론 차트 또는 빌보드 Hot 100 차트 크롤링 및 YouTube Music 플레이리스트 생성을 시작합니다.

## 최근 업데이트

- 빌보드 차트 크롤링 로직을 최신 웹사이트 레이아웃에 맞게 업데이트하였습니다.
- YouTube Music API와의 충돌을 처리하기 위해 중복 곡 체크 및 API 요청 지연 로직을 추가하였습니다.
- OAuth 인증 및 파일 존재 확인 절차를 개선했습니다.

## 주의 사항

- 이 스크립트는 멜론 웹사이트와 YouTube Music의 비공식 API를 사용합니다.
- 멜론 웹사이트의 이용 약관과 YouTube Music의 정책을 준수하며 사용해야 합니다.
