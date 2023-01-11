from discord.ext import commands
import discord


class Readme(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def help(self, ctx):
        message = discord.Embed(title="說明",
                                description="指令應該都寫在這裡惹", color=0x4599)

        message.add_field(name='!start', value='開始進行爬蟲', inline=False)
        message.add_field(name='!check', value='確認基本資訊', inline=False)
        message.add_field(name='貓貓', value='喵喵叫', inline=False)
        message.add_field(name='嗨', value='打招呼', inline=False)


        message.set_thumbnail(url="https://pic.baike.soso.com/ugc/baikepic2/12471/20220228173944-1377436487_png_871_928_455258.jpg/0")
        
        await ctx.send(embed=message)


async def setup(client):
    await client.add_cog(Readme(client))