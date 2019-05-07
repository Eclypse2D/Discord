import os
import pip
import discord
from discord.ext import commands
import asyncio
import colorsys
import random
import platform
from discord import Game, Embed, Color, Status, ChannelType
import functools
import time
import datetime
import requests
import json

import aiohttp


bot = commands.Bot(command_prefix='s!')

@bot.event
async def on_ready():
	print('The Bot is ready!')
	print(bot.user.name)
	print(bot.user.id)

@bot.command()
async def ping():
	await bot.say('ping pong')
	await bot.say('Why did you ping me tho?')

@bot.command()
async def thing():	
	await bot.say('@Sl𝓐ve Thing#0468 is bad')

@bot.command(pass_context=True) 
async def mute(ctx,target:discord.Member):
	role=discord.utils.get(ctx.message.server.roles,name='Muted')

	await bot.add_roles(target,role)

@bot.command(pass_context=True) 
async def warn(ctx,target:discord.Member):
	await bot.send_message(target,'You have got warned. Please do not keep doing whatever you did')

@bot.command(pass_context=True)
async def kick(ctx,target:discord.Member):
	await bot.kick(target)

@bot.command(pass_context=True)
async def ban(ctx,target:discord.Member):
	await bot.ban(target)
	

@bot.command(pass_context=True)
async def hug(ctx, user: discord.Member):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    if user.id == ctx.message.author.id:
        await bot.say("Hugging yourself is pretty hard {}...".format(user.mention))
    else:
        randomurl = ["http://gifimage.net/wp-content/uploads/2017/09/anime-hug-gif-5.gif", "https://media1.tenor.com/images/595f89fa0ea06a5e3d7ddd00e920a5bb/tenor.gif?itemid=7919037", "https://media.giphy.com/media/NvkwNVuHdLRSw/giphy.gif"]
        embed = discord.Embed(title=f"{user.name} You just got a hug from {ctx.message.author.name}", color = discord.Color((r << 16) + (g << 8) + b))
        embed.set_image(url=random.choice(randomurl))
        await bot.say(embed=embed)


@bot.command(pass_context=True)
async def kiss(ctx, user: discord.Member):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    randomurl = ["https://media3.giphy.com/media/G3va31oEEnIkM/giphy.gif", "https://i.imgur.com/eisk88U.gif", "https://media1.tenor.com/images/e4fcb11bc3f6585ecc70276cc325aa1c/tenor.gif?itemid=7386341", "http://25.media.tumblr.com/6a0377e5cab1c8695f8f115b756187a8/tumblr_msbc5kC6uD1s9g6xgo1_500.gif"]
    if user.id == ctx.message.author.id:
        await bot.say("Goodluck kissing yourself {}".format(ctx.message.author.mention))
    else:
        embed = discord.Embed(title=f"{user.name} You just got a kiss from {ctx.message.author.name}", color = discord.Color((r << 16) + (g << 8) + b))
        embed.set_image(url=random.choice(randomurl))
        await bot.say(embed=embed)
 
@bot.command(pass_context=True)
async def lick(ctx, user: discord.Member):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    randomurl = ["https://cdn.discordapp.com/attachments/573790125960593424/575268501955149834/giphy.gif", "https://cdn.discordapp.com/attachments/573790125960593424/575268501955149835/tenor_1.gif", "https://cdn.discordapp.com/attachments/573790125960593424/575268502626107397/ed1.gif"]
    if user.id == ctx.message.author.id:
        await bot.say("Goodluck licking yourself {}".format(ctx.message.author.mention))
    else:
        embed = discord.Embed(title=f"{user.name} You just got licked by {ctx.message.author.name}", color = discord.Color((r << 16) + (g << 8) + b))
        
bot.run(') 
