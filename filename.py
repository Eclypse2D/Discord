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


