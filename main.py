import os
from discord.ext import tasks
import discord
from discord.ext import commands
from dotenv import load_dotenv
import re
import asyncio
import json
import time
import logging
import threading 
# from keep_alive import keep_alive


try:
    import discum
except:
    os.system("pip install git+https://github.com/Merubokkusu/Discord-S.C.U.M.git#egg=discum")
    import discum

client = commands.Bot(command_prefix="!", case_insensitive=True)

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
  return await client.change_presence(activity=discord.Activity(type=1, name='Vibing'))

'''
@tasks.loop(seconds=5)# 1 day
async def mytask(message):
 await message.channel.send("```Hello World```")
'''

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith('$hello'):
    await message.channel.send('```Hello {}```'.format(message.author.name))
  if message.content.startswith('$timer'):
    start_time = time.time()
    seconds = 5
    while True:
      current_time=time.time()
      elapsed_time=current_time - start_time
      if elapsed_time > seconds:
        break
    await message.channel.send('```5 second timer expired```')
  if message.content.startswith('$sussy'):
    await message.channel.send("<:sussy:935624408855363666>")
  if message.content.startswith('$startnew'):

    new_user = False
    f = open('stats.json', "r")
    data = json.loads(f.read())
    i = data["Users"]
    for j in i:
      if str(message.author) == j["Name"]:
        new_user= True
        break
    f.close()
      
    if new_user == True:
      await message.channel.send('```This user has an account associated with MEV Bot```')
    else:
      new_user = {
        "Name":str(message.author),
        "Agents":{
          "Astra":"False",       
          "Breach":"False", 
          "Brimstone":"False", 
          "Chamber":"False", 
          "Cypher":"False", 
          "Jett":"False",  
          "KAY/O":"False", 
          "Killjoy":"False", 
          "Neon":"False",  
          "Omen":"False", 
          "Phoenix":"False", 
          "Raze":"False", 
          "Reyna":"False", 
          "Sage":"False",  
          "Skye":"False",  
          "Sova":"False",  
          "Viper":"False",   
          "Yoru":"False"
        }
      }
      write_json(new_user)
      
      await message.channel.send('```Welcome to MEV Bot, this is a bot that will allow you to collect different valorant abilities, charms, skins and agents. Since this is your first time you have one free lootbox for an agent and their abilities, 2 charms and a skin. Take part in the casino, complete daily and weekly tasks, random pop questions, and many more to earn more currency to collect them all. If you roll a duplicate use $claim to earn currency. Good luck and enjoy MEV Bot```')
  if message.content.startswith('$reset'):
    return

  if message.content.startswith('$embed'):
    embedVar = discord.Embed(title="Title", description="Desc", color=0x00ff00)
    embedVar.add_field(name="Field1", value="hi", inline=False)
    embedVar.add_field(name="Field2", value="hi2", inline=False)
    embedVar.set_image(url="https://www.looper.com/img/gallery/valorant-release-date-platforms-trailer-and-gameplay/intro-1591383833.jpg")
    await message.channel.send(embed=embedVar)
  
def write_json(new_data, filename='stats.json'):
    with open(filename,'r+') as file:
          # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data["Users"].append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)



keep_alive()
# Get token from .env
my_secret = os.getenv('TOKEN')
client.run(my_secret)


'''
    f = open('stats.json', "r")
    data = json.loads(f.read())
    print(data)
    i = data["Users"]
    for j in i:
      print(j["Name"])
    f.close()
    '''