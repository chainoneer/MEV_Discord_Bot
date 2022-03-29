import os
import random
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

agents = ["Astra", "Breach", "Brimstone", "Chamber", "Cypher", "Jett", "KAY/O",
          "Killjoy", "Neon", "Omen", "Phoenix", "Raze", "Reyna", "Sage", "Skye",
          "Sova", "Viper", "Yoru"]

emotes = ["<:astra:958420104490663986>","<:breach:958420500839804938>","<:brimstone:958420774736252948>","<:chamber:958421177422983239>","<:cypher:958425821578682378>","<:jett:958426375168073809>","<:kayo:958426726822727711>","<:killjoy:958427157539983440>","<:neon:958427417528131624>","<:omen:958427990029660230>","<:phoenix:958428146330374164>","<:raze:958428251485782046>","<:reyna:958428346428059648>","<:sage:958428493211902003>","<:skye:958428627517730876>","<:sova:958429598989811812>","<:viper:958429995989086238>","<:yoru:958430128977895504>"]

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith('$hello'):
    await message.channel.send('```Hello {}```'.format(message.author.name))
  if message.content.startswith('$emote'):
    await message.channel.send("<:sussy:935624408855363666>")

  if message.content.startswith('$startnew'):
    new_user = False
    for k in db.keys():
      if str(message.author) == k:
        new_user = True
        break
      
    if new_user == True:
      await message.channel.send('```This user has an account associated with MEV Bot```')
    else:
      await message.channel.send('```Welcome to MEV Bot, this is a bot that will allow you to collect different valorant abilities, charms, skins and agents. Since this is your first time you have one free lootbox for an agent and their abilities, 2 charms and a skin. Take part in the casino, complete daily and weekly tasks, random pop questions, and many more to earn more currency to collect them all. If you roll a duplicate use $claim to earn currency. Good luck and enjoy MEV Bot```')
  
  if message.content.startswith('$reset'):
    del db[str(message.author)]
    print(db.keys())

  if message.content.startswith('$randomval'):
    l = len(message.content)
    if l>10:
      if message.content[11] == "c":
        print("Custom Game")
        attside = int(message.content[13])
        defside = int(message.content[15]) 
        attackers = []
        emotesatt = []
        defenders = []
        emotesdef = []
        for i in range(attside):
          attackers.append(agents[random.randint(0,17)])
        for i in range(defside):
          defenders.append(agents[random.randint(0,17)])
        response = "Attackers: "+ attackers[0] + 
        await message.channel.send(response)
        
      else:
        print("Error")
    else:
      print("Random Agent")
    await message.channel.send('```Hello {}```'.format(message.author.name))
  
  if message.content.startswith('$embed'):
    embedVar = discord.Embed(title="Title", description="Desc", color=0x00ff00)
    embedVar.add_field(name="Field1", value="hi", inline=False)
    embedVar.add_field(name="Field2", value="hi2", inline=False)
    embedVar.set_image(url="https://www.looper.com/img/gallery/valorant-release-date-platforms-trailer-and-gameplay/intro-1591383833.jpg")
    await message.channel.send(embed=embedVar)
  
keep_alive()
my_secret = os.environ['TOKEN']
client.run(my_secret)
