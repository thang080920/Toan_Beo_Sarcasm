import os
import json
import random
import re
import discord
from dotenv import load_dotenv
from discord.ext import commands

# take parameters from .env file

load_dotenv()
TOKEN = os.getenv('TOKEN')
GUILD = os.getenv('GUILD')
ID = '<@325921495853563915>'

# create new params

bot = commands.Bot(command_prefix='!')
client = discord.Client()


# interact with JSON

file = open('./data.json', encoding="utf8")
data = json.load(file)

keywords = []
normal_list = []

# keyword list insertion

for index in data['keys']:
    keywords.append(index['text'])

# normal list insertion

for index in data['normal']:
    normal_list.append(index['text'])

file.close()

# main session of Bot

@bot.event
async def on_ready():
    print(
        f'{bot.user.name} has connected to Discord!\n'
        )



@bot.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content in keywords:
        response = random.choice(normal_list)
        output = f'{response} %s' %ID
        await message.channel.send(output)


bot.run(TOKEN)