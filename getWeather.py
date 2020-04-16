# coding: UTF-8
import urllib.request, urllib.error
from bs4 import BeautifulSoup

def getWeather():
    # アクセスするURL
    url = "https://weather.yahoo.co.jp/weather/jp/13/4410.html"
    #urllibでなんかしらの手続き
    html = urllib.request.urlopen(url)
    # htmlをBeautifulSoupで扱う
    soup = BeautifulSoup(html, "html.parser")
    #news_titleまで絞り込み
    how_weather = soup.find(class_="pict")
    temperature = soup.find(class_="temp")
    temperature_h = temperature.find(class_="high")
    temperature_l = temperature.find(class_="low")
    #news_title = news_title_all.findAll("a")
    # タイトル要素を出力
    valid_temp = []
    valid_temp.append(temperature_h.getText())
    valid_temp.append(temperature_l.getText())
    valid_temp.append(how_weather.getText())
    return valid_temp
