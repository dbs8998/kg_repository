from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# 크롬드라이버 경로 설정
service = Service('chromedriver 경로')
driver = webdriver.Chrome(service=service)


# 웹 페이지 열기
driver.get('https://www.google.com')

# 검색창에 값 입력
search_box = driver.find_element(By.NAME, 'q')
search_box.send_keys('OpenAI ChatGPT')
search_box.submit()

# 잠시 대기 후 종료
import time
time.sleep(5)
driver.quit()
