import discord
import getWeather
import config
import getNews
from datetime import datetime
from discord.ext import tasks

tk = config.TOKEN
client = discord.Client()

@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('お天気お姉さんログインしました。')

@client.event
async def on_message(message):
    # 送り主がBotだった場合反応したくないので
    if client.user != message.author:
        if message.content.startswith("てんき") or message.content.startswith("天気"):
            weather = getWeather.getWeather()
            m = "今日の天気は、" + weather[2] + "です。" + "\n最高気温は、" + weather[0] + "\n最低気温は、" + weather[1] + "です。"
            await message.channel.send(m)
@tasks.loop(seconds=60)
async def loop():
    now = datetime.now().strftime('%H:%M')
    if now == '07:00':
        channel = client.get_channel(646945099531550741)
        weather = getWeather.getWeather()
        m = "おはようございます。\n今日の天気は、" + weather[2] + "です。" + "\n最高気温は、" + weather[0] + "\n最低気温は、" + weather[1] + "です。\n最新のニュースです。"
        await channel.send(m)
        news = getNews.getNews()
        for i in news:
            await channel.send("・" + i)

loop.start()
client.run(tk)
