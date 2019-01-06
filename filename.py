import discord
from discord.ext import commands
import asyncio

bot = commands.Bot(command_prefix='Slave')

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
async def warn():	
	await bot.say('Bad boy! You just got warned')
	
@bot.command()
async def thing():	
	await bot.say('@Sl𝓐ve Thing#0468 is bad')
 





bot.run('NTMxMTY0MDUzMjg5MzA0MDc0.DxJ9VA.rLYqQzO-xsc051ZDp5aQtYaNmlU')
