#ほーわー２回目
# coding: UTF-8
import urllib.request, urllib.error
from bs4 import BeautifulSoup


def getNews():
    # アクセスするURL
    url = "https://news.yahoo.co.jp/"
    #urllibでなんかしらの手続き
    html = urllib.request.urlopen(url)
    # htmlをBeautifulSoupで扱う
    soup = BeautifulSoup(html, "html.parser")
    #news_titleまで絞り込み
    news_title_all = soup.find(class_="topicsList_main")
    news_title = news_title_all.findAll("a")
    # タイトル要素を出力
    list=[]
    for i in news_title:
        j = i.getText()
        list.append(j)
    del list[5:]
    return list
