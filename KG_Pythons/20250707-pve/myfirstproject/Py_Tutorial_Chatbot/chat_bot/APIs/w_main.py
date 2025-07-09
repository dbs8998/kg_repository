# 날씨 정보: https://www.weatherapi.com/docs/ 
# 내 API key: 951f04d16802409abef22836242604 

import requests
import json

key = '951f04d16802409abef22836242604'
base_url = 'http://api.weatherapi.com/v1'
api_current = '/current.json'  # 현재 날씨(xml도 가능: /current.xml)
q = 'Seoul'
# aqi(air quality index: 옵션항목)

def weather_info():
    response = requests.get(f'{base_url}{api_current}?key={key}&q={q}&aqi=yes')
    print(response.text)

    # JSON -> 딕셔너리로 변환
    weather = json.loads(response.text)

    print(weather['current']['temp_c'])
    print(weather['current']['condition']['text'])
    
    return weather

# json 내용 보기
# weather_info()

###########################
# ?: 쿼리 문자열 시작
# &: 매개변수 구분자
# 매개변수: '키=값' 형태
# url = 기본 경로 + 쿼리 문자열
###########################