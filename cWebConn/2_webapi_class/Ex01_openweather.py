"""
    전세계날씨제공 API : http://openweathermap.org

    1. 회원가입 : 메뉴 > Sign Up > 사용용도 : Education > 대충가입 (무료는 1번에 60번 호출 가능 )
    2. 개발자모드 : Sign In > API Keys 에서 내가 발급받은 키 (추가 키 가능)
    3. 발급받고 바로 지정 안됨 (시간소요)
"""
import requests
import json

# API 키를 지정합니다. 자신의 키로 변경해서 사용해주세요.
# apikey = "1db47184ebbc18af53fd996be840d270"
apikey = "43f8bbf911db40f2d614fd9b6b53665c"
# 날씨를 확인할 도시 지정하기
cities = ["Seoul,KR", "Tokyo,JP", "New York,US"]

# url 지정
api = "http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={key}"

# 켈빈 온도를 섭씨 온도로 변환하는 함수
k2c = lambda k: k - 273.15

for city in cities:
    url = api.format(city=city, key=apikey)
    # print(url)
    weather_data = requests.get(url)
    # print(weather_data.text)
    print(weather_data.json())
    json_data = json.loads(weather_data.text)
    print('도시 :', json_data["name"])
    print('날씨 :', json_data["weather"][0]["description"])
    # print(*json_data['weather'])  # 찾아볼것 unpacking
    # for weather in json_data["weather"]:
    #     print('날씨 :', weather['description'])
    print('습도 :', json_data['main']['humidity'])
    print('기압 :', json_data['main']['pressure'])
    print('최고온도 :', k2c(json_data['main']['temp_max']))

