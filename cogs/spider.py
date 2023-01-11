from discord.ext import commands
import function
import asyncio

url = "https://www.apple.com/tw/shop/refurbished/mac" # change url here
channel_id = 1058326938101502053
sec = 30*60  # minute * 60


class Spider(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is Online.')
        await self.client.get_channel(channel_id).send('機器人上線惹\n請輸入!help來查看指令')

    # Commands
    @commands.command()
    async def start(self, ctx):

        await self.client.get_channel(channel_id).send('現在偵測的網址為： ' + url)
        await self.client.get_channel(channel_id).send('目前偵測的頻率為： ' + str(sec / 60) + '分鐘一次')

        while True:

            flag = function.check_status(url)
            if flag:
                await ctx.send(f"<@{661625091603562507}>")  # Tag user id
                await ctx.send('目前有偵測到東西在網站上')
            else:
                await ctx.send('目前沒東西')

            await asyncio.sleep(sec)

    @commands.command()
    async def check(self, ctx):
        await ctx.send('現在偵測的網址為： ' + url+'\n'+'目前偵測的頻率為： ' + str(sec / 60) + '分鐘一次')



async def setup(client):
    await client.add_cog(Spider(client))
