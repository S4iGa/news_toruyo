import discord
from datetime import datetime, timedelta
import config

tk = config.TOKEN
client = discord.Client()

@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('呼び込みくんログインしました')

@client.event
async def on_voice_state_update(member, before, after):
    if member.guild.id == 571557686945120276:
        all_channel = client.get_channel(646266397340729345)
        if before.channel is None:
            msg = f'{member.name} が {after.channel.name} に参加しました。'
            await all_channel.send(msg)

client.run(tk)
