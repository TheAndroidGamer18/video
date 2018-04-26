import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import os

Client = discord.Client()
clinet = commands.Bot(command_prefix = ";")
@client.event
async def on_ready():
    print("Bot Is Online")
    await clinet.change_presence(game=dsicord.Game(name="Videos"))

    @cleint.event
    async def on_message(message):
        if message.content.startswith(';hello'):
            msg = 'Hello {0.author.mention} How Are You Todat'.format(message)
            await client.send_message(message.channel, msg)



client.run(os.getenv('TOKEN'))
