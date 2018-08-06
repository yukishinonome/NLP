import requests
import json
import sys
import datetime

# APIキーの設定
API_KEY = '自分で取得したAPIキー'
api = 'http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={key}&units=metric'

# 調べたい場所
city_name = "Tokyo"

# URLの取得
url = api.format(city=city_name, key=API_KEY)
response = requests.get(url)

# URL先のデータをJSON形式で取得する
data = json.loads(response.text)

# 現在の天気
print("天気：{}".format(data['weather'][0]['main']))
# 現在の気温
print("気温：{}度".format(data['main']['temp']))
# 日の出
print("日の出：{}".format(datetime.datetime.fromtimestamp(data['sys']['sunrise'])))
# 日の入り
print("日の入り：{}".format(datetime.datetime.fromtimestamp(data['sys']['sunset'])))