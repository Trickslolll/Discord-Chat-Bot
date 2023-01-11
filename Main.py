import discord
from discord.ext import commands
import json
import asyncio
import function
import os

url = "Target URL"  # url here
channel_id = # channel id stored here
sec = 30*60  # minute * 60


intents = discord.Intents.all()
intents.message_content = True
client = discord.Client(intents=intents)

with open('items.json', "r", encoding='utf8') as file:
    data = json.load(file)

bot = commands.Bot(command_prefix="!", intents=intents, owner_ids=data['owner_id'])

for file in os.listdir("cogs"):
    if file.endswith(".py"):
        name = file[:-3]
        bot.load_extension(f"cogs.{name}")


@bot.event
async def on_ready():
    global channel_id, sec, url
    print('Bot in ready')
    await bot.get_channel(channel_id).send('我開始爬網站惹')
    await bot.get_channel(channel_id).send('現在偵測的網址為： ' + url)
    await bot.get_channel(channel_id).send('目前偵測的頻率為： ' + str(sec/60)+'分鐘一次')

    while True:
        flag = function.check_status(url)
        if flag:
            await bot.get_channel(channel_id).send(f"<@{user_id}>") # user id stored here
            await bot.get_channel(channel_id).send('目前有偵測到物件在網站上')
        else:
            await bot.get_channel(channel_id).send('目前沒東西')

        await asyncio.sleep(sec)


bot.run(data['token'])
