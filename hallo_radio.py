#!/bin/env python3
# This is a radio bot for Heimdall on his Discord server 
# made by Mo_oM on 2023-02-12.
# Feel free to use for your own environment.

import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
PREFIX = os.getenv('DISCORD_PREFIX')

intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True

client = commands.Bot(command_prefix=list(PREFIX), intents=intents)
url = 'https://s1.voscast.com:11187/RadioARA.mp3'

@client.event
async def on_ready():
    print('Music Bot Ready')

@client.command(aliases=['p', 'pla'])
async def play(ctx, url = url):
    channel = ctx.message.author.voice.channel
    global player
    try:
        player = await channel.connect()
    except:
        print('PlayerError: Could not connect to channel.')
        pass
    player.play(discord.FFmpegPCMAudio(url))

@client.command(aliases=['s', 'sto'])
async def stop(ctx):
    try:
        player.stop()
    except:
        print('PlayerError: Could not stop playing the music.')
        pass


@client.command(aliases=['e', 'ex'])
async def exit(ctx):
    try:
        await player.disconnect()
    except:
        print('PlayerError: Could not disconnect from channel.')
        pass

client.run(TOKEN)

