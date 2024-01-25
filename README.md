# Melon2Ytmusic

## 프로젝트 개요
Melon2Ytmusic은 멜론 차트에서 음악을 크롤링하여 YouTube Music 플레이리스트에 자동으로 추가하는 파이썬 스크립트입니다. 이 프로그램은 GUI 인터페이스를 통해 사용자가 편리하게 멜론 차트의 최신 곡들을 YouTube Music 플레이리스트에 추가할 수 있도록 도와줍니다.

## 주요 기능
- 멜론 차트에서 상위 곡 목록 크롤링
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

또한, 프로그램은 Google Chrome 브라우저와 해당 Chrome 버전에 맞는 ChromeDriver가 필요합니다. ChromeDriver는 [이곳](https://sites.google.com/a/chromium.org/chromedriver/downloads)에서 다운로드할 수 있습니다.

## 사용 방법
1. 터미널을 열고 `ytmusicapi oauth` 명령을 실행하여 YouTube Music 인증을 완료합니다.
2. `Melon2Ytmusic.py` 파일을 실행합니다.
3. GUI에서 "Start Crawling" 버튼을 클릭하여 멜론 차트 크롤링 및 YouTube Music 플레이리스트 생성을 시작합니다.

## 주의 사항
- 이 스크립트는 멜론 웹사이트와 YouTube Music의 비공식 API를 사용합니다.
- 멜론 웹사이트의 이용 약관과 YouTube Music의 정책을 준수하며 사용해야 합니다.

---

이 README 파일은 프로젝트에 대한 기본적인 정보를 제공합니다. 필요에 따라 더 자세한 설명이나 추가 섹션을 포함시킬 수 있습니다. 예를 들어, "기여 방법", "라이선스 정보", "개발자 연락처" 등의 섹션을 추가할 수 있습니다.
