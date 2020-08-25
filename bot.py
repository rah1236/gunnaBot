# bot.py
import os
import tokens
import random
from PIL import Image
import requests
from io import BytesIO

import discord
from discord.ext import commands



TOKEN = tokens.token_secret

bot = discord.Client()



bot = commands.Bot(command_prefix='!')

@bot.command(name='gunnafy', help='Gunnafies any attached picture, JPEGS only tho. Idk why tbh.')
async def gunnafier(ctx):
    url = str(ctx.message.attachments[0])
    url = str(url).split("'")[3]
    print(url)

    response = requests.get(url)
    

    submitted = Image.open(BytesIO(response.content))
    
    
    submitted2 = submitted.resize((467,350))
    
    gunna = Image.open('gunna.png')

    gunna = gunna.resize((467,350))
    
    Image.blend(submitted2, gunna, .5).save('out.png')
    
    #response = "gunnafied"
    await ctx.send(file=discord.File('out.png'))

bot.run(TOKEN)
