# coding: UTF-8

import getWeather
import getNews

weather = getWeather.getWeather()
news = getNews.getNews()


weather_message = "今日の天気は、" + weather[2] + "です。" + "\n最高気温は、" + weather[0] + "\n最低気温は、" + weather[1] + "です。"
print(weather_message)
for i in news:
    print("・" + i)