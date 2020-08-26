# bot.py
import os
import markovify
import tokens
import random
from PIL import Image
import requests
from io import BytesIO
import discord
from discord.ext import commands
TOKEN = tokens.token_secret
bot = discord.Client()

bot = commands.Bot(command_prefix='gunna ')




@bot.command(name='gunnafy', help='Gunnafies any attached picture (Now supports all image types!)')
async def gunnafier(ctx):
    url = str(ctx.message.attachments[0])
    url = str(url).split("'")[3]
    print(url)
    response = requests.get(url)
    submitted = Image.open(BytesIO(response.content))
    if not submitted.mode == 'RGB':
        submitted = submitted.convert('RGB')
    submitted = submitted.resize((467,350))
    gunna = Image.open('gunna.png')
    gunna = gunna.resize((467,350))
    Image.blend(submitted, gunna, .5).save('out.png')
    await ctx.send(file=discord.File('out.png'))

@bot.command(name='wisdom', help='Generates wisdom directly from Gunnas Lyrics.')
async def lyricgen(ctx):
    
    with open("gunnaLyrics.txt", encoding='utf-8') as f:
        text = f.read()

# Build the model.
    def generateLyric():
        text_model = markovify.Text(text, reject_reg = r"@")
        text_model.well_formed = True

        return text_model.make_short_sentence(200, tries=500)

    lyric = generateLyric()
    print(lyric)
    await ctx.send(str(lyric))

bot.run(TOKEN)
