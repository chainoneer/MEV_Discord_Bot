import os
import discord
import re
import asyncio
import json
import time
import logging
import threading 
from keep_alive import keep_alive

client = discord.Client()


@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith('$hello'):
    await message.channel.send('Hello {}'.format(message.author.name))

keep_alive()
my_secret = os.environ['TOKEN']
client.run(my_secret)
