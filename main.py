import discord
import pyfiglet
from discord.ext import tasks 
from GoogleNews import GoogleNews
from discord.colour import Color
import discord
from discord.ext import commands
from discord import Intents
from discord.ext.commands import Bot
import os
import sys
import time
from discord import Member
import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
from pyfiglet import Figlet
from datetime import datetime
from discord.ext import commands
from discord.ext.commands import has_permissions
import requests
import os
import datetime
import random
import scapy
import json
from googlesearch import search 
from discord.ext import commands
import wikipedia
import requests
import time
import reddit
from bs4 import BeautifulSoup
from discord import Webhook, AsyncWebhookAdapter
from discord.ext import commands, tasks
from discord.ext.commands import Bot
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import discord
from datetime import datetime
import os
import random
from discord import Member
from discord.ext.commands import has_permissions, MissingPermissions
from discord.ext import commands
from discord.utils import find
import asyncio
import functools
import itertools
import math
import youtube_dl
from async_timeout import timeout
import numpy
import sympy
import urllib.request

api_key = "0c2dc79d8c59155c1ca6b5676fde24e7"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
googlenews = GoogleNews()    
client = discord.Client()
TOKEN = "OTIxNjgxMzM1NzA0MjQ0MjQ0.Yb2cog.DJVwmHvcfVxOTXDi6_UDe1OjzSs"
 
bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
 await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="a deadly song by MesonicDawn"))
 print('Logged in as')
 print(bot.user.name)
 print(bot.user.id)
 print(discord.__version__)
 print('------')
 print('Servers connected to:')
 for guild in bot.guilds:
        print(guild.name)

@bot.event
async def on_message(message):
    if client.user.mentioned_in(message):
        await message.channel.send('!d bump')
 
@bot.event
async def on_message(message):
    if message.channel.id == 921310288417013770:
        await message.add_reaction("✅") 
        await message.add_reaction("❌")
                                               
    if message.author == bot.user:
        return

    if message.content == 'Hello':
        await message.channel.send(f'Hi {message.author}')
    if message.content == 'Bye':
        await message.channel.send(f'Goodbye {message.author}')
    if message.content == 'Dumbcatto':
        await message.channel.send(f'Dumbhead is you >:C {message.author}')
    if message.content == 'Tell about luna':
        await message.channel.send(f'Just like you. {message.author}')
    if message.content == 'Kekw':
        await message.channel.send(f'lel ya dumb{message.author}')
    if message.content == 'lel':
        await message.channel.send(f'laugh as u die today{message.author}')
    if message.content == 'die':
        await message.channel.send(f'you should die first {message.author}')
    if message.content == 'RIP':
        await message.channel.send(f'RIP MESONIC AKA PROFESSIONAL BRO')
    if message.content == 'lol':
        await message.channel.send(f'RIP {message.author}-death by drownin')
    if message.content == 'Fuck':
        await message.delete()
    await bot.process_commands(message)

@bot.command()
async def square(ctx, arg): 
    print(arg) 
    
    await ctx.send(int(arg) ** 2) 

@bot.command()
async def scrabblepoints(ctx, arg):
    
    score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}
    points = 0
     
    for c in arg:
        points += score[c]
    await ctx.send(points)
  
@bot.command()
async def wiki(ctx, *, arg=None):
  async with ctx.typing():
    try:
        if arg == None:
            await ctx.send("dumbass, specify what do you want me to search dumb head wikipedia dont hab intel on thet")
        elif arg:
            start = arg.replace(" ", "")
            end = wikipedia.summary(start)
            await ctx.send(end)
    except:
        try:
            start = arg.replace(" ", "")
            end = wikipedia.summary(start, sentences=100)
            await ctx.send(end)
        except:
            await ctx.send("yo gimme the correct word fool")
            
@bot.command()
async def ping(ctx):
  calc = bot.latency * 1000
  pong = round(calc)
  await ctx.message.delete()

  x = discord.Embed(title='**Pong**', description=f'{pong} `ms`', color=0xff0000) 

  y = discord.Embed(title='**Pong**', description=f'{pong} `ms`', color=0xffff00) 

  z = discord.Embed(title='**Pong**', description=f'{pong} `ms`', color=0x008000) 

  if pong > 160: 
    msg = await ctx.send(embed=x)
    await msg.add_reaction('??')
  elif 80 <= pong <= 160:
    msg = await ctx.send(embed=y)
    await msg.add_reaction('??')
  elif pong < 80:
    msg = await ctx.send(embed=z)
    await msg.add_reaction('??')

@bot.command()
async def find(ctx,*, query):
		author = ctx.author.mention
		await ctx.channel.send(f"Here are the links related to your question now :moyai: {author} !")
		async with ctx.typing():
				for j in search(query, tld="co.in", num=1, stop=1, pause=2): 
						await ctx.send(f"\n:point_right: {j}")
				await ctx.send("Have any more questions:question:\nNevah Feel free to ask again :smiley: !")

@bot.command(description = 'Add a suggestion for this community!')
async def suggest(ctx, *,suggestion):

        
        await ctx.channel.purge(limit = 1)
        channel = discord.utils.get(ctx.guild.text_channels, name = 'ﾉ≧∇≦ﾉ-ﾐ-suggestions⊙☉')

        suggestEmbed = discord.Embed(colour = 0xFF0000)
        suggestEmbed.set_author(name=f'Suggested by {ctx.message.author}', icon_url = f'{ctx.author.avatar_url}')
        suggestEmbed.add_field(name = 'New suggestion!', value = f'{suggestion}')
        message = await ctx.send(embed=suggestEmbed)
        await message.add_reaction('✅')
        await message.add_reaction('❌')
   
@bot.command()
@commands.guild_only()
async def serverinfo(ctx):
    name = str(ctx.guild.name)
    description = str(ctx.guild.description)
    owner = str(ctx.guild.owner)
    id = str(ctx.guild.id)
    region = str(ctx.guild.region)
    memberCount = str(ctx.guild.member_count)

    icon = str(ctx.guild.icon_url)

    embed = discord.Embed(
        title=name + " Server Information",
        description=description,
        color=discord.Color(0x00000)
    )
    embed.set_thumbnail(url=icon)
    embed.add_field(name="Owner", value=owner, inline=True)
    embed.add_field(name="Server ID", value=id, inline=True)
    embed.add_field(name="Region", value=region, inline=True)
    embed.add_field(name="Member Count", value=memberCount, inline=True)
    await ctx.channel.send(embed=embed)
           
   
@bot.command()
@has_permissions(manage_messages=True)
async def delete(ctx,amount=10):
  await ctx.channel.purge(limit=amount)

@bot.command()
async def calc(ctx):
    def check(m):
        return len(m.content) >= 1 and m.author != bot.user

    await ctx.send("Number 1: ")
    number_1 = await bot.wait_for("message", check=check)
    await ctx.send("Operator: ")
    operator = await bot.wait_for("message", check=check)
    await ctx.send("number 2: ")
    number_2 = await bot.wait_for("message", check=check)
    try:
        number_1 = float(number_1.content)
        operator = operator.content
        number_2 = float(number_2.content)
    except:
        await ctx.send("That is fkin wrng bruh")
        return
    output = None
    if operator == "+":
        output = number_1 + number_2
    elif operator == "-":
        output = number_1 - number_2
    elif operator == "/":
        output = number_1 / number_2
    elif operator == "*":
        output = number_1 * number_2
    else:
        await ctx.send("such gehness go calculate it urself")
        return
    await ctx.send("Answer: " + str(output))

@bot.command()   
@has_permissions(manage_channels=True)
async def dcl(ctx):   
 await ctx.message.channel.delete()   
 
@bot.command()
@commands.has_role('DEV(+_+)')
async def say(ctx,*,message):
     await ctx.channel.send('%s'%message)
     await ctx.message.delete()
     
@bot.command(description= 'Limit of the contents are 4000 so content should be simple example:HI')
async def figlet(ctx,*,message):
    result = pyfiglet.figlet_format('%s'%message,font = "doh")
    await ctx.channel.send('%s'%result)
    
    if message=='None':
        await ctx.message.channel.send('Please specify the content')    
        
@bot.command()
async def news(ctx, *, search):
    sear = str(search)
    googlenews = GoogleNews(lang='en', period='1d')
    googlenews.search(search)   
    googlenews.page_at(2)

    texts = googlenews.get_texts()
    urls = googlenews.get_links()
    img = googlenews.get_texts()
    news_em = discord.Embed(
        title = f'News regarding {sear}', 
        color = discord.Color.dark_gold(), 
    )
    
    for j in range(10, len(img)):
        news_em.add_field(name=str(img[j]), value=f'[Click to read the full article]({str(urls[j])}) \n --------- \n', inline=False)
    await ctx.send(embed = news_em)    
    
@bot.command(description='Talk with meh lol')
async def twc(ctx,*,message):
    author = ctx.author
    print({ctx.author},message)
    Reply=input('reply?\n')
    await ctx.message.channel.send('%s'%Reply)
    
@bot.command()
async def weather(ctx, *,message):
    city_name = message
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    print(complete_url)  
    x = response.json()
    channel = ctx.message.channel
    if x["cod"] != "404":
        async with channel.typing():
            y = x["main"]
            current_temperature = y["temp"]
            current_temperature_celsiuis = str(round(current_temperature - 273.15))
            current_pressure = y["pressure"]
            current_humidity = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
            weather_description = z[0]["description"]
            embed = discord.Embed(title=f"Weather in {city_name}",
                              color=ctx.guild.me.top_role.color,
                              timestamp=ctx.message.created_at,)
            embed.add_field(name="Descripition", value=f"**{weather_description}**", inline=False)
            embed.add_field(name="Temperature(C)", value=f"**{current_temperature_celsiuis}°C**", inline=False)
            embed.add_field(name="Humidity(%)", value=f"**{current_humidity}%**", inline=False)
            embed.add_field(name="Atmospheric Pressure(hPa)", value=f"**{current_pressure}hPa**", inline=False)
            embed.set_thumbnail(url="https://i.ibb.co/CMrsxdX/weather.png")
            embed.set_footer(text=f"Requested by {ctx.author.name}")
            await channel.send(embed=embed)
    else:
       await channel.send("City not found.")

@bot.command() 
async def meinf(ctx):
    author = ctx.author
    await ctx.message.channel.send({ctx.author})
    
@bot.command()
async def game(ctx):
    number = random.randint(0, 100)
    for i in range(0, 5):
        await ctx.send('guess it')
        response = await bot.wait_for('message')
        guess = int(response.content)
        if guess > number:
            await ctx.send('bigger')
        elif guess < number:
            await ctx.send('smaller')
        else:
            await ctx.send('mf got brains')
                                                          
custom_fig = Figlet(font='graffiti')
ascii_banner = pyfiglet.figlet_format("PROJ NEKO")
print(ascii_banner)
print("================================= By DEV(+_+)")
            
bot.run(TOKEN)