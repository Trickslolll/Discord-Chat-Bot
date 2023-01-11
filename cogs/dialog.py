from discord.ext import commands
import discord
from discord.ext.commands import bot

class Dialog(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):

        if message.author == self.client.user:
            return

        if message.content.startswith('嗨'):
            await message.channel.send('Hello!')

        if message.content.startswith('貓貓'):
            await message.channel.send('喵～～～')

async def setup(client):
    await client.add_cog(Dialog(client))
