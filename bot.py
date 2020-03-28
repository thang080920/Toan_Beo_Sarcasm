import os

import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('TOKEN')

bot = commands.Bot(command_prefix='!')

# interact with JS



@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

# @bot.command(name)


bot.run(TOKEN)