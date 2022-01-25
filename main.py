import os
import discord
import re
import asyncio
import json
import time
import logging
import threading 
from replit import db
from keep_alive import keep_alive


try:
    import discum
except:
    os.system("pip install git+https://github.com/Merubokkusu/Discord-S.C.U.M.git#egg=discum")
    import discum

client = discord.Client()

class Collectibles():
  agents = {}

  def __init__(self):
    self.agents={"Astra":False, "Breach":False, "Brimstone":False, "Chamber":False, "Cypher":False,"Jett":False, "KAY/O":False, "Killjoy":False, "Neon":False, "Omen":False, "Phoenix":False, "Raze":False, "Reyna":False, "Sage":False, "Skye":False, "Sova":False,  "Viper":False, "Yoru":False}


@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith('$hello'):
    await message.channel.send('```Hello {}```'.format(message.author.name))
  if message.content.startswith('$startnew'):
    new_user = False
    for k in db.keys():
      if str(message.author) == k:
        new_user = True
        break
      
    if new_user == True:
      await message.channel.send('```This user has an account associated with MEV Bot```')
    else:
      user = Collectibles()
      print(user.agents["Astra"])
      db[message.author] = {"Astra":False, "Breach":False, "Brimstone":False, "Chamber":False, "Cypher":False,"Jett":False, "KAY/O":False, "Killjoy":False, "Neon":False, "Omen":False, "Phoenix":False, "Raze":False, "Reyna":False, "Sage":False, "Skye":False, "Sova":False,  "Viper":False, "Yoru":False}

      await message.channel.send('```Welcome to MEV Bot, this is a bot that will allow you to collect different valorant abilities, charms, skins and agents. Since this is your first time you have one free lootbox for an agent and their abilities, 2 charms and a skin. Take part in the casino, complete daily and weekly tasks, random pop questions, and many more to earn more currency to collect them all. If you roll a duplicate use $claim to earn currency. Good luck and enjoy MEV Bot```')
  
  if message.content.startswith('$reset'):
    del db[str(message.author)]
    print(db.keys())
  
  

keep_alive()
my_secret = os.environ['TOKEN']
client.run(my_secret)
