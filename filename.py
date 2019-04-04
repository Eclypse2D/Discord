import discord
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import asyncio
import colorsys
import random
import platform
from discord import Game, Embed, Color, Status, ChannelType
import os
import functools
import time
import datetime
import json
import aiohttp

Forbidden= discord.Embed(title="Permission Denied", description="1) Please check whether you have permission to perform this action or not. \n2) Please check whether my role has permission to perform this action in this channel or not. \n3) Please check my role position.", color=0x00ff00)

bot = commands.Bot (command_prefix="Slave" )

bot.remove_command('help')

async def status_task():
    while True:
        await asyncio.sleep(5)
        await bot.change_presence(game=discord.Game(name='with '+str(len(set(bot.get_all_members())))+' users'))
        await asyncio.sleep(5)
        await bot.change_presence(game=discord.Game(name='in '+str(len(bot.servers))+' servers'))
        await asyncio.sleep(5)

left = '⏪'
right = '⏩'
r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
general1=discord.Embed(title="General Commands | Page 1", description="**__Slavedonate__** \nSends donation link \n\n**__Slaveinvite__** or **__Slaveauthlink__** \nUse it to invite our bot to your server \n\n**__Slaveupvote__**\nUse this command to upvote our bot(Link will be in dm)\n\n **__Slavegoogle__**\n Use it like- ``Slavegoogle <anything>`` to google anything\n\n**__Slaveyoutube__**\nUse it like- ``Slaveyoutube <anything>`` to search anything on youtube\n\n**__Slavemembernames__**\nUse it to get member names in dm\n\n**__Slaveinvites__** \nUse it like ``Slaveinvites @user`` or ``Slaveinvite`` for get invites done by you/tagged person in server. \n__Note:__**If bot does not responds that means you do not have invited any member on that server.**\n\n**__Slaveremind__**\nUse it like ``Slaveremind <time in minutes> <text like what to remind>`` Example: ``Slaveremind 2 Drink water``.\n\n**__Slavehelpmusic__**\nTo get list of music commands like: Slaveplay,Slaveskip,etc.", color = discord.Color((r << 16) + (g << 8) + b))
general2=discord.Embed(title="General Commands | Page 2", description="**__Slaveserverinvite__** \nUse it to get server invite link.\n\n**__Slaveavatar__**\nUse it like ``Slaveavatar or Slaveavatar @user``\n\n**__Slaveping__**\nUse it to check ping of bot\n\n**__Slaveenterme__**\nUse it like ``Slaveenterme <giveaway channel>`` to enter in a giveaway running in a particular channel\n\n**__Slavepoll__**\nUse it like ``Slavepoll Question Option1 Option2 ..... Option9``.\n\n**__Slavegithub__**\nUse it like- ``Slavegithub uksoftworld``\n\n**__Slavebottutorial__**\nUse it like ``Slavebottutorial <tutorial name by darklegend>``\n\n**__Slavedyno__**\nUse it like ``Slavedyno <dyno command name>``\n\n**__Slavehappybirthday @user__**\nTo wish someone happy birthday\n\n**__Slaveverify__**Use it to get verified role. Note- It needs proper setup.\n\n**__Slaverank__**\nUse it to check your daily multiverse rank(xp + level)", color = discord.Color((r << 16) + (g << 8) + b))
general3=discord.Embed(title="Fun Commands <==> General Commands | Page 3", description="**__Slavejoke__**\n\n**__Slavekiss @user__**\n\n**__Slavehug @user__**\n\n**__Slaveslap @user__**\n\n**__Slavedamn__**\n\n**__Slaveburned__**\n\n**__Slavesavage__**\n\n**__Slavethuglife__**\n\n**__Slavemembernames__**\n\n**__Slavegender @user__**\n\n**__Slavevirgin @user__**\n\n**__Slavememe__**\n\n**__Slaverolldice__**\n\n**__Slaveflipcoin__**\n\n**__Slaveguess__**\n\n**__Slavemovie <movie name>__**\n\n**__Slaverps <rock ,paper or scissors>__**\n\n**__Slaveurban <string>__**", color = discord.Color((r << 16) + (g << 8) + b))
mod1=discord.Embed(title="Admin and Mod Commands | Page 1", description="**__Slavepartner(Admin permission required) (Cooldown of 12hours)__** \nUse it like ``Slavepartner <partnership description>`` to partner with many servers with are connected with MultiVerse Official bot \n\n**__Slavedm(Admin permission required)__** \nUse it like ``Slavedm @user <text>`` to dm user from bot \n\n**__Slavesay(Admin permission required)__**\nUse it like ``Slavesay <text>``\n\n **__Slaveshowme(Requires a role named Giveaways)__**\n To see how many people are taking part in giveaway\n\n**__Slavepickwinner(Requires a role named Giveaways)__**\nTo pick winner of currentmost giveaways\n\n**__Slaveembed(Admin permission required__**\nUse it like ``Slaveembed <text>``\n\n**__Slavemembercount(Kick members Permission Required)__** \n Use it to get membercount of server\n\n**__Slavelock(Kick members Permission Required)__**\nUse it like ``Slavelock #channel or Slavelock`` to lock a channel\n\n**__Slaveunlock(Kick members Permission Required)__**\nUse it like ``Slaveunlock #channel or Slaveunlock`` to unlock a channel", color = discord.Color((r << 16) + (g << 8) + b))
mod2=discord.Embed(title="Admin and Mod Commands | Page 2", description="**__Slaveremovemod(Admin Permission Required)__** \nUse it like ``Slaveremovemod @user`` to remove him from mod. Note-You need Moderator role in your server below bot to use it.\n\n**__Slavemakemod(Admin Permission Required)__**\nUse it like ``Slavemakemod @user`` to make him mod. Note-You need Moderator role in your server below multiverse bot to use it.\n\n**__Slavefriend(Admin Permission Required)__**\nUse it like ``Slavefriend @user`` to give anyone Friend of Owner role\n\n**__Slaverole(Manage Roles Permission Required)__**\nUse it like ``Slaverole @user <rolename>``.\n\n**__Slavesetnick(Manage nickname permission required)__**\nUse it like ``Slavesetnick @user <New nickname>`` to change the nickname of tagged user.\n\n**__Slaveenglish(Kick members Permission Required)__**\nUse it like ``Slaveenglish @user`` when someone speaks languages other than English.\n\n**__Slaveserverinfo(Kick members Permission Required)__**\nUse it like ``Slaveserverinfo`` to get server info\n\n**__Slaveuserinfo(Kick members Permission Required)__**\nUse it like ``Slaveuserinfo @user`` to get some basic info of tagged user.", color = discord.Color((r << 16) + (g << 8) + b))
mod3=discord.Embed(title="Admin and Mod Commands | Page 3", description="**__Slaveunbanall(Unban members Permission Required)__** \nUse it like ``Slaveunbanall`` to unban all members\n\n**__Slaveunban__**\nUse it like: ``Slaveunban userid`` to unban user.\n\n**__Slavekick(Kick members Permission Required)__**\nUse it like ``Slavekick @user`` to kick any user\n\n**__Slavemuteinchannel(Ban members Permission Required)__**\nUse it like ``Slavemuteinchannel @user <time in minutes>`` Example- ``Slavemuteinchannel @user 1`` to mute user for 1min.\n\n**__Slaveunmuteinchannel(Ban members Permission Required)__**\nUse it like ``Slaveunmuteinchannel @user`` to unmute user from that channel.\n\n**__Slaveroles(Kick members Permission Required)__**\nUse it to check roles present in server.\n\n**__Slavepurge(Manage Messages Permission Required)__**\nUse it like ``Slavepurge <number>`` to clear any message.\n\n**__Slavemute(Mute members Permission Required)__**\nUse it like ``Slavemute @user <time in minutes>`` to mute any user. **Note-You need to add Muted role in your server if it is not already there also you must need to change permission of all channels and disable send_message permission for that role.**\n\n**__Slaveunmute(Mute members Permission Required)__**\nUse it like ``Slaveunmute @user`` to unmute anyone.", color = discord.Color((r << 16) + (g << 8) + b))
mod4=discord.Embed(title="Admin and Mod Commands | Page 4", description="**__Slaveban(Ban members Permission Required)__** \nUse it like ``Slaveban @user`` to ban any user\n\n**__Slaverules(Kick members Permission Required)__**\nUse it like ``Slaverules @user <violation type>`` to warn user\n\n**__Slavewarn(Kick members Permission Required)__**\nUse it like ``Slavewarn @user <violation type>`` to warn any user.\n\n**__Slavenorole(Kick members Permission Required)__**\nUse it like ``Slavenorole @user`` to warn anyone if he/she asks for promotion.\n\n**__Slavegetuser(Kick members Permission Required)__**\nUse it like ``Slavegetuser rolename`` to get list of all users having a that role.\n\n**__Slaveroleinfo(Manage roles Permission Required)__**\nUse it like ``Slaveroleinfo <rolename>`` to get basic info about that role.\n\n**__Slaveaddchannel(Administrator Permission Required)__**\nUse it like ``Slaveaddchannel <channelname>`` to add that channel in server.\n\n**__Slavedelchannel(Administrator Permission Required)__**\nUse it like ``Slavedelchannel <channelname>`` to delete that channel in server.\n\n**__Slavesetnickall__**\nIt changes nickname of all members by adding text in front of member nicknames in server.\n\n**__Slaveresetnickall__**\nUse it to reset nickname of all users in server", color = discord.Color((r << 16) + (g << 8) + b))

gen_cmd = (general1, general2, general3)
mod_cmd = (mod1, mod2, mod3, mod4)

def predicate(message, l, r):
    def check(reaction, user):
        if reaction.message.id != message.id or user == bot.user:
            return False
        if l and reaction.emoji == left:
            return True
        if r and reaction.emoji == right:
            return True
        return False

    return check



@bot.event
async def on_ready():
    print('Logged in as '+bot.user.name+' (ID:'+bot.user.id+') | Connected to '+str(len(bot.servers))+' servers | Connected to '+str(len(set(bot.get_all_members())))+' users')
    print('--------')
    print('--------')
    print('Started Our BOT')
    print('Created by Utkarsh')
    bot.loop.create_task(status_task())
    
def is_dark(ctx):
    return ctx.message.author.id == "420525168381657090"

def is_staff(ctx):
    return ctx.message.author.id in ["420525168381657090", "514856260353392660", "472680171451973632" ,"442575516684386304" ,"425676648818671618", "399274658027012098", "437525938582847489"]

def is_shreyas(ctx):
    return ctx.message.author.id == "376602841625919488"

@bot.event
async def on_message(message):
    await bot.process_commands(message)
    channel = bot.get_channel('518710986799316992')
    if message.server is None and message.author != bot.user:
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed=discord.Embed(title=f"{message.author.name} sent", description=f"{message.content}", color = discord.Color((r << 16) + (g << 8) + b))
        embed.set_thumbnail(url= message.author.avatar_url)
        await bot.send_message(channel, '{} ID: {}'.format(message.author.name,message.author.id))
        await bot.send_message(channel, embed=embed)

@bot.event
async def on_reaction_add(reaction, user):
  if reaction.message.server is None:
      if reaction.emoji == '🇬':
          index = 0
          while True:
              msg = await bot.send_message(user, embed=gen_cmd[index])
              l = index != 0
              r = index != len(gen_cmd) - 1
              if l:
                  await bot.add_reaction(msg, left) 
              if r:
                  await bot.add_reaction(msg, right)
              react, user = await bot.wait_for_reaction(check=predicate(msg, l, r))
              if react.emoji == left:
                  index -= 1
              elif react.emoji == right:
                  index += 1
              await bot.delete_message(msg)
      if reaction.emoji == '🇲':
          index = 0
          while True:
              msg = await bot.send_message(user, embed=mod_cmd[index])
              l = index != 0
              r = index != len(mod_cmd) - 1
              if l:
                  await bot.add_reaction(msg, left) 
              if r:
                  await bot.add_reaction(msg, right)
              react, user = await bot.wait_for_reaction(check=predicate(msg, l, r))
              if react.emoji == left:
                  index -= 1
              elif react.emoji == right:
                  index += 1
              await bot.delete_message(msg)
    
      if reaction.emoji == '🏵':
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
        embed.set_author(name='Setup Help')
        embed.set_image(url = 'https://image.ibb.co/caM2BK/help.gif')
        embed.add_field(name = 'Setting up Welcomer log(Admin Permission required) ',value ='Use Slavesetupwelcomer. It will add a welcome channel. Just put that channel in your desired category and it will send all logs there.',inline = False)
        embed.add_field(name = 'Setting up AutoPartner Channel(Admin Permission required)',value ='Using ``Slavesetuppartner`` command create a channel named multiverse-partner and then you can use Slavepartner to partner with other servers.',inline = False)
        embed.add_field(name = 'Setting up Giveaway feature(Manage roles permission required) ',value ='Just add a role named ``Giveaways`` and give that role to user who wanna be giveaway manager. Then use ``Slavehelp`` and check giveaway commands.',inline = False)
        embed.add_field(name = 'Setting up Reaction Verification(Admin Permission required) ',value ='Just add a role named ``Verified`` then remove permission from everyone to send message in all channels. Also add permission of verified role to send message in chatting channels. Then use ``Slavesetreactionverify`` it will automatically add a channel and post information about verification. **__Note__** **Sometimes it does not sends message in channel named #verify-for-chatting when this command is used so reuse that command in such case**',inline = False)
        embed.add_field(name = 'Setting up Multiverse bot log(Admin Permission required) ',value ='Use ``Slavesetuplog`` and it will automatically add a log channel and log all stuffs there.',inline = False)
        react_message = await bot.send_message(user,embed=embed)
        await asyncio.sleep(30)
        await bot.delete_message(react_message)
      if reaction.emoji == '🎦':
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
        embed.set_author(name='Emoji Help')
        embed.set_image(url = 'https://image.ibb.co/caM2BK/help.gif')
        embed.add_field(name = 'Slavewow',value ='WOW emoji <a:WOW:515854429485006848>',inline = False)
        embed.add_field(name = 'Slavecat',value ='Cat emoji <a:agooglecat:516174312294842389>',inline = False)
        embed.add_field(name = 'Slavesurprised',value ='Surprised emoji <a:eyebigger:516174315058626560>',inline = False)
        embed.add_field(name = 'Slaveangry',value ='Angry emoji <a:angear:516174316950388772>',inline = False)
        embed.add_field(name = 'Slavefearfromme',value ='Scary emoji <a:shiroeglassespush:516174320532193289>',inline = False)
        embed.add_field(name = 'Slavedank',value ='DankMemer emoji <a:OnThaCoco:515853700682743809>',inline = False)
        embed.add_field(name = 'Slavethinking1',value ='Think emoji1 <a:thinking:516183328613990400>',inline = False)
        embed.add_field(name = 'Slavethinking2',value ='Think emoji2 <a:thinking2:516183323127709699>',inline = False)
        embed.add_field(name = 'Slavehappy',value ='Happy emoji <a:happy:516183323052212236>',inline = False)
        embed.add_field(name = 'Slavesanta',value ='Santa emoji <a:santa:517232271678504970>',inline = False)
        embed.add_field(name = 'Slavelol',value ='LoL emoji <a:lol:517232283670020096>',inline = False)
        embed.add_field(name = 'Slavelove',value ='Love emoji <a:love:517232300912672774>',inline = False)
        embed.add_field(name = 'Slavemad',value ='Mad emoji <a:mad:517232301176913951>',inline = False)
        embed.add_field(name = 'Slavealien',value ='Alien emoji <a:alien:517232332663422986>',inline = False)
        embed.add_field(name = 'Slavehi',value ='Saying Hi emoji <a:hi:517232279148429313>',inline = False)
        react_message = await bot.send_message(user,embed=embed)
        await asyncio.sleep(30)
        await bot.delete_message(react_message)
  else:
      if reaction.emoji == '🇻':
            role = discord.utils.get(user.server.roles, name='Verified')
            await bot.add_roles(user, role)
	
@bot.event
async def on_member_join(member):
    for channel in member.server.channels:
        if member.bot:
            return
        if channel.name == '★彡-welcome-彡★':
            r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
            embed = discord.Embed(title=f'Welcome {member.name} to {member.server.name}', description='Do not forget to check rules and never try to break any one of them', color = discord.Color((r << 16) + (g << 8) + b))
            embed.add_field(name='__Thanks for joining__', value='**Hope you will be active here.**', inline=True)
            embed.set_thumbnail(url='https://media.giphy.com/media/OkJat1YNdoD3W/giphy.gif') 
            embed.set_image(url = member.avatar_url)
            embed.add_field(name='__Join position__', value='{}'.format(str(member.server.member_count)), inline=True)
            embed.add_field(name='Time of joining', value=member.joined_at)
            await bot.send_message(channel, embed=embed) 
            role = discord.utils.get(member.server.roles, name='Verified')
            await asyncio.sleep(60)
            await bot.add_roles(member, role)

@bot.event
async def on_member_remove(member):
    for channel in member.server.channels:
        if channel.name == '★彡-welcome-彡★':
            r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
            embed = discord.Embed(title=f'{member.name} just left {member.server.name}', description='Bye bye 👋! We will miss you 😢', color = discord.Color((r << 16) + (g << 8) + b))
            embed.add_field(name='__User left__', value='**Hope you will be back soon 😕.**', inline=True)
            embed.add_field(name='Your join position was', value=member.joined_at)
            embed.set_thumbnail(url=member.avatar_url)
            await bot.send_message(channel, embed=embed)

@bot.command(pass_context=True)
async def merrychristmas(ctx, user:discord.Member=None):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    if user is None:
        embed=discord.Embed(title='Merry Christmas', description=f'I wanna wish {ctx.message.author} Merry Christmas {ctx.message.author}', color = discord.Color((r << 16) + (g << 8) + b))
        embed.set_image(url = 'https://cdn.discordapp.com/attachments/486489391083159574/526968559994404874/gif-153062737.gif')
        await bot.say(embed=embed)
    else:
        embed=discord.Embed(title='Merry Christmas', description=f'I wanna wish {user} Merry Christmas {user}', color = discord.Color((r << 16) + (g << 8) + b))
        embed.set_image(url = 'https://cdn.discordapp.com/attachments/486489391083159574/526968559994404874/gif-153062737.gif')
        await bot.say(embed=embed)

@bot.command(pass_context=True)
@commands.check(is_dark)
async def setgame(ctx, *, game:str):
    await bot.delete_message(ctx.message)
    await bot.change_presence(game=discord.Game(name=game))
    await asyncio.sleep(10)

	
@bot.command(pass_context=True)
async def movie(ctx, *, name:str=None):
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        await bot.send_typing(ctx.message.channel)
        if name is None:
                embed=discord.Embed(description = "Please specify a movie, *eg. Slavemovie Inception*", color = discord.Color((r << 16) + (g << 8) + b))
                x = await bot.say(embed=embed)
                await asyncio.sleep(5)
                return await bot.delete_message(x)
        key = "4210fd67"
        url = "http://www.omdbapi.com/?t={}&apikey={}".format(name, key)
        response = requests.get(url)
        x = json.loads(response.text)
        embed=discord.Embed(title = "**{}**".format(name).upper(), description = "Here is your movie {}".format(ctx.message.author.name), color = discord.Color((r << 16) + (g << 8) + b))
        if x["Poster"] != "N/A":
            embed.set_thumbnail(url = x["Poster"])
            embed.add_field(name = "__Title__", value = x["Title"])
            embed.add_field(name = "__Released__", value = x["Released"])
            embed.add_field(name = "__Runtime__", value = x["Runtime"])
            embed.add_field(name = "__Genre__", value = x["Genre"])
            embed.add_field(name = "__Director__", value = x["Director"])
            embed.add_field(name = "__Writer__", value = x["Writer"])
            embed.add_field(name = "__Actors__", value = x["Actors"])
            embed.add_field(name = "__Plot__", value = x["Plot"])
            embed.add_field(name = "__Language__", value = x["Language"])
            embed.add_field(name = "__Imdb Rating__", value = x["imdbRating"]+"/10")
            embed.add_field(name = "__Type__", value = x["Type"])
            embed.set_footer(text = "Information from the OMDB API")
            await bot.say(embed=embed)
	
@bot.command(pass_context=True)
async def tweet(ctx, usernamename:str, *, txt:str):
    url = f"https://nekobot.xyz/api/imagegen?type=tweet&username={usernamename}&text={txt}"
    async with aiohttp.ClientSession() as cs:
        async with cs.get(url) as r:
            res = await r.json()
            r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
            embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
            embed.set_image(url=res['message'])
            embed.title = "{} twitted: {}".format(usernamename, txt)
            await bot.say(embed=embed)

@bot.command(pass_context=True)
async def ownerinfo(ctx):
    embed = discord.Embed(title="Information about owner", description="Main Creator: DarkLegend", color=0x00ff00)
    embed.set_footer(text="Copyright@UK Soft")
    embed.set_author(name=" Bot Owner Names- DarkLegend#3807: 420525168381657090\nTag<!--Back-->#1488: 399274658027012098")
    embed.add_field(name="Site- https://discordbots.org/bot/515403515217313795", value="Thanks for adding our bot", inline=True)
    await bot.say(embed=embed)

	
@bot.command(pass_context=True)
async def virus(ctx,user: discord.Member=None,*,hack=None):
    nome = ctx.message.author
    if not hack:
        hack = 'discord'
    else:
        hack = hack.replace(' ','_')
    channel = ctx.message.channel
    x = await bot.send_message(channel, '``[▓▓▓                    ] / {}-virus.exe Packing files.``'.format(hack))
    await asyncio.sleep(1.5)
    x = await bot.edit_message(x,'``[▓▓▓▓▓▓▓                ] - {}-virus.exe Packing files..``'.format(hack))
    await asyncio.sleep(0.3)
    x = await bot.edit_message(x,'``[▓▓▓▓▓▓▓▓▓▓▓▓           ] \ {}-virus.exe Packing files...``'.format(hack))
    await asyncio.sleep(1.2)
    x = await bot.edit_message(x,'``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓         ] | {}-virus.exe Initializing code.``'.format(hack))
    await asyncio.sleep(1)
    x = await bot.edit_message(x,'``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓      ] / {}-virus.exe Initializing code..``'.format(hack))
    await asyncio.sleep(1.5)
    x = await bot.edit_message(x,'``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   ] - {}-virus.exe Finishing.``'.format(hack))
    await asyncio.sleep(1)
    x = await bot.edit_message(x,'``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ] \ {}-virus.exe Finishing..``'.format(hack))
    await asyncio.sleep(1)
    x = await bot.edit_message(x,'``Successfully downloaded {}-virus.exe``'.format(hack))
    await asyncio.sleep(2)
    x = await bot.edit_message(x,'``Injecting virus.   |``')
    await asyncio.sleep(0.5)
    x = await bot.edit_message(x,'``Injecting virus..  /``')
    await asyncio.sleep(0.5)
    x = await bot.edit_message(x,'``Injecting virus... -``')
    await asyncio.sleep(0.5)
    x = await bot.edit_message(x,'``Injecting virus....\``')
    await bot.delete_message(x)
    await bot.delete_message(ctx.message)
        
    if user:
        await bot.say('`{}-virus.exe` successfully injected into **{}**\'s system.'.format(hack,user.name))
        await bot.send_message(user,'**Alert!**\n``You may have been hacked. {}-virus.exe has been found in your system\'s operating system.\nYour data may have been compromised. Please re-install your OS immediately.``'.format(hack))
    else:
        await bot.say('**{}** has hacked himself ¯\_(ツ)_/¯.'.format(name.name))
        await bot.send_message(name,'**Alert!**\n``You may have been hacked. {}-virus.exe has been found in your system\'s operating system.\nYour data may have been compromised. Please re-install your OS immediately.``'.format(hack))
	
@bot.command(pass_context=True, no_pm=True)
async def urban(ctx, *, msg:str=None):
    await bot.send_typing(ctx.message.channel)
    if msg is None:
        await bot.say('Use it like: ``Slaveurban <string>``')
        return
    else:
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        word = ' '.join(msg)
        api = "http://api.urbandictionary.com/v0/define"
        response = requests.get(api, params=[("term", word)]).json()
        if len(response["list"]) == 0:
            return await bot.say("Could not find that word!")
        embed = discord.Embed(title = "🔍 Search Word", description = word, color = discord.Color((r << 16) + (g << 8) + b))
        embed.add_field(name = "Top definition:", value = response['list'][0]['definition'])
        embed.add_field(name = "Examples:", value = response['list'][0]["example"])
        embed.set_footer(text = "Tags: " + ', '.join(response['tags']))
        await bot.say(embed=embed)
		
@bot.command(pass_context=True)
async def rps(ctx, *, message=None):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    await bot.send_typing(ctx.message.channel)
    ans = ["rock", "paper", "scissors"]
    pick=ans[random.randint(0, 2)]
    embed=discord.Embed(title = "Bot VS {}".format(ctx.message.author.name), color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_author(name = ctx.message.author.name, icon_url = ctx.message.author.avatar_url)
    if message is None:
        await bot.say('Use it like ``Slaverps rock or scissors or paper`` anyone of them to make this command work properly')
    if message.lower() != ans[0] and message.lower() != ans[1] and message.lower() != ans[2] :
        return await bot.say("Pick Rock Paper or Scissors")
    elif message.lower() == pick:
        embed.add_field(name = "Its a draw!", value = "Bot picked {} too!".format(pick))
        return await bot.say(embed=embed)
    else:
        if message.lower()  == "rock" and pick == "paper":
            embed.add_field(name = "Bot Wins!", value = "Bot picked {}!".format(pick))
            await bot.say(embed=embed)
        elif message.lower()  == "rock" and pick == "scissors":
            embed.add_field(name = "{} Wins!".format(ctx.message.author.name), value = "Bot picked {}!".format(pick))
            await bot.say(embed=embed)
        elif message.lower()  == "paper" and pick == "rock":
            embed.add_field(name = "{} Wins!".format(ctx.message.author.name), value = "Bot picked {}!".format(pick))
            await bot.say(embed=embed)
        elif message.lower()  == "paper" and pick == "scissors":
            embed.add_field(name = "Bot Wins!", value = "Bot picked {}!".format(pick))
            await bot.say(embed=embed)
        elif message.lower()  == "scissors" and pick == "rock":
            embed.add_field(name = "Bot Wins!", value = "Bot picked {}!".format(pick))
            await bot.say(embed=embed)
        else:
            embed.add_field(name = "{} Wins!".format(ctx.message.author.name), value = "Bot picked {}!".format(pick))
            await bot.say(embed=embed)

@bot.command(pass_context=True)
async def inviteb(ctx):
    total_uses=0
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    server = ctx.message.channel.server
    invites = await bot.invites_from(server)
    invlb = f'Invites of {ctx.message.server.name}\n'
    for invite in invites:
      total_uses += invite.uses
      invlb += f'User: {invite.inviter.name}\nInvites: {invite.uses}\n'
    embed=discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.add_field(name='Invites List',value=invlb)
    embed.add_field(name='Total Invites',value=total_uses)
    embed.set_footer(text=f'Requested by: {ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
    await bot.say(embed=embed)
		
@bot.command(pass_context=True)
async def invites(ctx, user:discord.Member=None):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    if ctx.message.server.id == '527430758902661121':
        await bot.say('You should use ``Slavecheckinvites``')
        return
    if user is None:
        total_uses=0
        embed=discord.Embed(title='__Invites from {}__'.format(ctx.message.author.name), color = discord.Color((r << 16) + (g << 8) + b))
        invites = await bot.invites_from(ctx.message.server)
        for invite in invites:
          if invite.inviter == ctx.message.author:
              total_uses += invite.uses
              embed.add_field(name='Invite',value=invite.id)
              embed.add_field(name='Uses',value=invite.uses)
              embed.add_field(name='Channel',value=invite.channel)
              embed.set_footer(text=f'Requested by: {ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        embed.add_field(name='__Total Uses__',value=total_uses)
        await bot.say(embed=embed)
    else:
        total_uses=0
        embed=discord.Embed(title='__Invites from {}__'.format(user.name), color = discord.Color((r << 16) + (g << 8) + b))
        invites = await bot.invites_from(ctx.message.server)
        for invite in invites:
          if invite.inviter == user:
              total_uses += invite.uses
              embed.add_field(name='Invite',value=invite.id)
              embed.add_field(name='Uses',value=invite.uses)
              embed.add_field(name='Channel',value=invite.channel)
              embed.set_footer(text=f'Requested by: {ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
        embed.add_field(name='__Total Uses__',value=total_uses)
        await bot.say(embed=embed)
	
@bot.command(pass_context=True)
async def checkinvites(ctx, user:discord.Member=None):
    if ctx.message.server.id == '527430758902661121':
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        if user is None:
            total_uses=0
            embed=discord.Embed(title='__Invites from {}__'.format(ctx.message.author.name), color = discord.Color((r << 16) + (g << 8) + b))
            invites = await bot.invites_from(ctx.message.server)
            for invite in invites:
              if invite.inviter == ctx.message.author:
                  total_uses += invite.uses
                  embed.add_field(name='Invite',value=invite.id)
                  embed.add_field(name='Uses',value=invite.uses)
                  embed.add_field(name='Channel',value=invite.channel)
                  embed.set_footer(text=f'Requested by: {ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
            embed.add_field(name='__Total Uses__',value=total_uses)
            await bot.say(embed=embed)
            if total_uses >= 20:
                role = discord.utils.get(ctx.message.server.roles, name='Inviter I')
                if role in ctx.message.author.roles:
                    return
                else:
                    await bot.add_roles(ctx.message.author, role)
                    await bot.say('Congrats! You have got Inviter I role')
            if total_uses >= 30:
                role = discord.utils.get(ctx.message.server.roles, name='Inviter II')
                if role in ctx.message.author.roles:
                    return
                else:
                    await bot.add_roles(ctx.message.author, role)
                    await bot.say('Congrats! You have got Inviter II role')
            if total_uses >= 50:
                role = discord.utils.get(ctx.message.server.roles, name='Inviter III')
                if role in ctx.message.author.roles:
                    return
                else:
                    await bot.add_roles(ctx.message.author, role)
                    await bot.say('Congrats! You have got Inviter III role')
            if total_uses >= 80:
                role = discord.utils.get(ctx.message.server.roles, name='Inviter IV')
                if role in ctx.message.author.roles:
                    return
                else:
                    await bot.add_roles(ctx.message.author, role)
                    await bot.say('Congrats! You have got Inviter IV role')
        else:
            total_uses=0
            embed=discord.Embed(title='__Invites from {}__'.format(user.name), color = discord.Color((r << 16) + (g << 8) + b))
            invites = await bot.invites_from(ctx.message.server)
            for invite in invites:
              if invite.inviter == user:
                  total_uses += invite.uses
                  embed.add_field(name='Invite',value=invite.id)
                  embed.add_field(name='Uses',value=invite.uses)
                  embed.add_field(name='Channel',value=invite.channel)
                  embed.set_footer(text=f'Requested by: {ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
            embed.add_field(name='__Total Uses__',value=total_uses)
            await bot.say(embed=embed)
            if total_uses >= 20:
                role = discord.utils.get(user.server.roles, name='Inviter I')
                if role in user.roles:
                    return
                else:
                    await bot.add_roles(user, role)
                    await bot.say(f'Congrats! {user.name}, You have got Inviter I role')
            if total_uses >= 30:
                role = discord.utils.get(user.server.roles, name='Inviter II')
                if role in user.roles:
                    return
                else:
                    await bot.add_roles(user, role)
                    await bot.say(f'Congrats! {user.name} You have got Inviter II role')
            if total_uses >= 50:
                role = discord.utils.get(user.server.roles, name='Inviter III')
                if role in user.roles:
                    return
                else:
                    await bot.add_roles(user, role)
                    await bot.say(f'Congrats! {user.name} You have got Inviter III role')
            if total_uses >= 80:
                role = discord.utils.get(user.server.roles, name='Inviter IV')
                if role in user.roles:
                    return
                else:
                    await bot.add_roles(user, role)
                    await bot.say(f'Congrats! {user.name} You have got Inviter IV role')
    else:
        await bot.say('You are not allowed to use this command in this server')
        return 

@bot.command(pass_context = True)
async def detailedinvites(ctx,*,user:discord.Member=None):
    invite = await bot.invites_from(ctx.message.server)
    if user is None:
        for invite in invite:
          if invite.inviter == ctx.message.author:
              r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
              embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
              embed.add_field(name = 'Link used for inviting:',value =f'{invite.url}'.format(), inline=False)
              embed.add_field(name = 'Invites from this link:',value =f'{invite.uses}', inline=False)
              embed.add_field(name = 'Created at:',value =f'{invite.created_at}', inline=False)
              embed.add_field(name = 'Channel:',value =f'{invite.channel}', inline=False)
              embed.add_field(name = 'ID:',value =f'{invite.id}', inline=False)
              await bot.say(embed=embed)
    else:
        for invite in invite:
          if invite.inviter == user:
              r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
              embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
              embed.add_field(name = 'Link used for inviting:',value =f'{invite.url}'.format(), inline=False)
              embed.add_field(name = 'Invites from this link:',value =f'{invite.uses}', inline=False)
              embed.add_field(name = 'Created at:',value =f'{invite.created_at}', inline=False)
              embed.add_field(name = 'Channel:',value =f'{invite.channel}', inline=False)
              embed.add_field(name = 'ID:',value =f'{invite.id}', inline=False)
              await bot.say(embed=embed)
		
@bot.command(pass_context=True)
async def lovedetect(ctx, user: discord.Member = None, *, user2: discord.Member = None):
    shipuser1 = user.name
    shipuser2 = user2.name
    useravatar1 = user.avatar_url
    useravatar2s = user2.avatar_url
    self_length = len(user.name)
    first_length = round(self_length / 2)
    first_half = user.name[0:first_length]
    usr_length = len(user2.name)
    second_length = round(usr_length / 2)
    second_half = user2.name[second_length:]
    finalName = first_half + second_half
    score = random.randint(0, 100)
    filled_progbar = round(score / 100 * 10)
    counter_ = '█' * filled_progbar + '‍ ‍' * (10 - filled_progbar)
    url = f"https://nekobot.xyz/api/imagegen?type=ship&user1={useravatar1}&user2={useravatar2s}"
    async with aiohttp.ClientSession() as cs:
        async with cs.get(url) as r:
            res = await r.json()
            r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
            embed = discord.Embed(title=f"{shipuser1} ❤ {shipuser2} Love each others", description=f"Love\n`{counter_}` Score:**{score}% **\nLoveName:**{finalName}**", color = discord.Color((r << 16) + (g << 8) + b))
            embed.set_image(url=res['message'])
            await bot.say(embed=embed)
		
@bot.command(pass_context = True)
@commands.check(is_dark)
async def dmall(ctx, *, msg: str):
    for server_member in ctx.message.server.members:
      await bot.send_message(server_member, msg)
      await bot.delete_message(ctx.message)

	
@bot.command(pass_context = True)
@commands.check(is_dark)
async def servers(ctx):
  servers = list(bot.servers)
  await bot.say(f"Connected on {str(len(servers))} servers:")
  await bot.say('\n'.join(server.name for server in servers))
	
@bot.command(pass_context=True)
async def vpn(ctx):
    embed=discord.Embed(title="**Welcome to AjaxVPN here you can get Support for the VPN, But you can also chill and meet new people, We have Chill and friendly staff who are willing to help.**", description="```┏━━━━ ⋆⋅✴AjaxVPN✴⋅⋆ ━━━━┓```\n ```●▬▬▬▬๑۩What We Offer۩๑▬▬▬▬●```\n3$USD8$USD- 1 Month No VIP\n15$USD- 6 Months No VIP\n25$USD- 1 Year VIP\n50$USD- Lifetime VIP\n```┗━━━━ ⋆⋅✴AjaxVPN✴⋅⋆ ━━━━┛```\n**Owner/Server [~Owner~]~𝓢𝓵𝓪𝓿𝓮#0468**\n```╔══════.·:·.💻✧ Join Now! ✧💻.·:·.══════╗```\nServer Link: https://discord.gg/WfAH2v3 ╚══════.·:·.💻✧           ✧💻.·:·.══════╝", color = discord.Color((r << 16) + (g << 8) + b))
    await bot.say(embed=embed)
	
@bot.command(pass_context=True)
async def serverinvite(ctx):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    invitelinknew = await bot.create_invite(destination = ctx.message.channel, xkcd = True, max_uses = 100)
    embedMsg=discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embedMsg.add_field(name="Discord Invite Link", value=invitelinknew)
    embedMsg.set_footer(text="Copyright @ UK Soft")
    await bot.send_message(ctx.message.channel, embed=embedMsg)
	
@bot.command(pass_context=True)
async def geninv(ctx, *, id:str=None):
    channel = bot.get_channel(id)
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    invitelinknew = await bot.create_invite(destination = channel, xkcd = True, max_uses = 100)
    embedMsg=discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embedMsg.add_field(name="Discord Invite Link", value=invitelinknew)
    embedMsg.set_footer(text="Copyright @ UK Soft")
    await bot.send_message(ctx.message.channel, embed=embedMsg)
	
@bot.command(pass_context = True)
async def rainbow(ctx):
    role = discord.utils.get(ctx.message.server.roles, name='Rainbow')
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    await bot.edit_role(ctx.message.server, role, color = discord.Color((r << 16) + (g << 8) + b))
	
@bot.command(pass_context = True)
async def ping(ctx):
    if ctx.message.author.bot:
      return
    else:
      channel = ctx.message.channel
      t1 = time.perf_counter()
      await bot.send_typing(channel)
      t2 = time.perf_counter()
      await bot.say("Ping: {}ms".format(round((t2-t1)*1000)))

@bot.command(pass_context = True)
@commands.has_permissions(administrator=True) 

   

	
@bot.command(pass_context = True)
@commands.has_permissions(administrator=True) 
async def delchannel(ctx, channel: discord=None):
    if channel is None:
        await bot.delete_channel(ctx.message.channel)
        await bot.send_message(ctx.message.author, "{} channel has been deleted in {}".format(ctx.message.channel.name, ctx.message.server.name))
    else:
        await bot.delete_channel(channel)
        await bot.say("{} channel has been deleted.".format(channel.name))


@bot.command(pass_context = True)
@commands.has_permissions(administrator=True) 
async def addchannel(ctx, channel: str=None):
    server = ctx.message.server
    if channel is None:
        await bot.say("Please specify a channel name")
    else:
        everyone_perms = discord.PermissionOverwrite(send_messages=None, read_messages=None)
        everyone = discord.ChannelPermissions(target=server.default_role, overwrite=everyone_perms)
        await bot.create_channel(server, channel, everyone)
        await bot.say("{} channel has been created.".format(channel))

	
@bot.command(pass_context = True)
@commands.has_permissions(kick_members=True) 
async def mute(ctx, member: discord.Member=None, mutetime=None):
    if member is None:
        await bot.say('Please specify member i.e. Mention a member to mute. Example-``Slavemute @user <time in minutes>``')
        return
    if mutetime is None:
        await bot.say('Please specify time i.e. Mention a member to mute with time. Example-``Slavemute @user <time in minutes>``')
        return
    if member.server_permissions.kick_members:
        await bot.say('**You cannot mute admin/moderator!**')
        return
    if discord.utils.get(member.server.roles, name='Muted') is None:
        await bot.say('No muted role found. Please add it')
        return
    if ctx.message.author.bot:
      return
    else:
      mutetime =int(mutetime)
      mutetime = mutetime * 60
      output = mutetime/60
      role = discord.utils.get(member.server.roles, name='Muted')
      await bot.add_roles(member, role)
      await bot.say("Muted **{}**".format(member.name))
      await bot.send_message(member, "You are muted by {0} for {1} Minutes".format(ctx.message.author, output))
      for channel in member.server.channels:
        if channel.name == '╰☆☆-multiverse-log-☆☆╮':
            embed=discord.Embed(title="User Muted!", description="**{0}** was muted by **{1}** for {2} minutes!".format(member, ctx.message.author, output), color=0x37F60A)
            await bot.send_message(channel, embed=embed)
            await asyncio.sleep(mutetime)
            if discord.utils.get(member.server.roles, name='Muted') in member.roles:
                await bot.remove_roles(member, role)
                await bot.say("Unmuted **{}**".format(member.name))
                embed=discord.Embed(title="User unmuted!", description="**{0}** was unmuted!".format(member, ctx.message.author), color=0xFD1600)
                await bot.send_message(channel, embed=embed)
            else:
                return
	
@bot.command(pass_context = True)
@commands.has_permissions(kick_members=True) 
async def lock(ctx, channelname: discord.Channel=None):
    overwrite = discord.PermissionOverwrite(send_messages=False, read_messages=True)
    if not channelname:
        role = discord.utils.get(ctx.message.server.roles, name='@everyone')
        await bot.edit_channel_permissions(ctx.message.channel, role, overwrite)
        await bot.say("Channel locked by: {}".format(ctx.message.author))
    else:
        role = discord.utils.get(ctx.message.server.roles, name='@everyone')
        await bot.edit_channel_permissions(channelname, role, overwrite)
        await bot.say("Channel locked by: {}".format(ctx.message.author))
	
@bot.command(pass_context = True)
@commands.has_permissions(kick_members=True) 
async def unlock(ctx, channelname: discord.Channel=None):
    overwrite = discord.PermissionOverwrite(send_messages=None, read_messages=True)
    if not channelname:
        role = discord.utils.get(ctx.message.server.roles, name='@everyone')
        await bot.edit_channel_permissions(ctx.message.channel, role, overwrite)
        await bot.say("Channel unlocked by: {}".format(ctx.message.author))
    else:
        role = discord.utils.get(ctx.message.server.roles, name='@everyone')
        await bot.edit_channel_permissions(channelname, role, overwrite)
        await bot.say("Channel unlocked by: {}".format(ctx.message.author))
	
@bot.command(pass_context = True)
async def meme(ctx):
    colour = '0x' + '008000'
    async with aiohttp.ClientSession() as session:
        async with session.get("https://api.reddit.com/r/me_irl/random") as r:
            data = await r.json()
            embed = discord.Embed(title='<a:OnThaCoco:515853700682743809> <a:OnThaCoco:515853700682743809> Random Meme <a:OnThaCoco:515853700682743809> <a:OnThaCoco:515853700682743809>', description='from reddit', color=discord.Color(int(colour, base=16)))
            embed.set_image(url=data[0]["data"]["children"][0]["data"]["url"])
            embed.set_footer(text=f'Requested by: {ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
            embed.timestamp = datetime.datetime.utcnow()
            await bot.say(embed=embed)
		
@bot.command(pass_context = True)
async def avatar(ctx, user: discord.Member=None):
    if user is None:
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(title=f'Avatar', description='Avatar is profile picture of a user in discord', color = discord.Color((r << 16) + (g << 8) + b))
        embed.add_field(name='User: {}'.format(ctx.message.author.name), value='Avatar:', inline=True)
        embed.set_thumbnail(url='https://cdn.discordapp.com/icons/489333893988745217/eb022a7023d013bec656cd7b94d6d6c1.png') 
        embed.set_image(url = ctx.message.author.avatar_url)
        await bot.say(embed=embed)
    else:
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(title=f'Avatar', description='Avatar is profile picture of a user in discord', color = discord.Color((r << 16) + (g << 8) + b))
        embed.add_field(name='User: {}'.format(user.name), value='Avatar:', inline=True)
        embed.set_thumbnail(url='https://cdn.discordapp.com/icons/489333893988745217/eb022a7023d013bec656cd7b94d6d6c1.png') 
        embed.set_image(url = user.avatar_url)
        await bot.say(embed=embed)

@bot.command(pass_context=True)
@commands.check(is_dark)
async def botdm(ctx, identification:str, *, msg: str):
    user = await bot.get_user_info(identification)
    await bot.send_typing(user)
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed=discord.Embed(title=f"{ctx.message.author.name} has replied", description=f"{msg}", color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_thumbnail(url= ctx.message.author.avatar_url)
    await bot.send_message(user, embed=embed)
	
@bot.command(pass_context=True)
async def apply(ctx, *, msg: str):
    channel = bot.get_channel('520830825021964305')
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.add_field(name='Application for bot', value='-------------------',inline = False) 
    embed.add_field(name='User ID:', value='{}'.format(ctx.message.author.id),inline = False)
    embed.add_field(name='User Name:', value='{}'.format(ctx.message.author.name),inline = False)
    embed.add_field(name='Server Name:', value='{}'.format(ctx.message.server.name),inline = False)
    embed.add_field(name='Bot information:', value=msg, inline=False)
    await bot.send_message(channel, embed=embed) 
    await bot.delete_message(ctx.message)
	
@bot.command(pass_context=True)
@commands.check(is_staff)
async def reject(ctx, user: discord.Member, *, msg: str):
    channel = bot.get_channel('520832912468344864')
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.add_field(name='Application rejected', value='-------------------',inline = False) 
    embed.add_field(name='Sadly {}'.format(user.name), value='Your bot has been rejected due to {}'.format(msg),inline = False)
    await bot.send_message(user, embed=embed) 
    await bot.send_message(channel, embed=embed)
    await bot.delete_message(ctx.message)
	
@bot.command(pass_context=True)
@commands.check(is_staff)
async def accept(ctx, user: discord.Member=None):
    channel = bot.get_channel('520832912468344864')
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.add_field(name='Application Accepted', value='-------------------',inline = False) 
    embed.add_field(name='Congratulations {}'.format(user.name), value='Your bot has been approved and will be added soon on http://multibots.000webhostapp.com/',inline = False)
    await bot.send_message(user, embed=embed) 
    await bot.send_message(channel, embed=embed)
    await bot.delete_message(ctx.message)
    role = discord.utils.get(user.server.roles, name='Bot Developer')
    await bot.add_roles(user, role)
	
@bot.command(pass_context = True)
async def rolldice(ctx):
    choices = ['1', '2', '3', '4', '5', '6']
    color = discord.Color(value=0x00ff00)
    em = discord.Embed(color=color, title='Rolled! (1 6-sided die)', description=random.choice(choices))
    await bot.send_typing(ctx.message.channel)
    await bot.say(embed=em)

   
@bot.command(pass_context = True)
@commands.has_permissions(administrator = True)
async def dm(ctx, user: discord.Member, *, msg: str):
    try:
        await bot.send_message(user, msg)
        await bot.delete_message(ctx.message)          
        await bot.say("Success! Your DM has made it! :white_check_mark: ")
    except discord.ext.commands.MissingPermissions:
        await bot.say("Aw, come on! You thought you could get away with DM'ing people without permissions.")
    except:
        await bot.say("Error :x:. Make sure your message is shaped in this way: Slavedm [tag person] [msg]")
	
@bot.command(pass_context = True)
async def flipcoin(ctx):
    choices = ['Heads', 'Tails', 'Coin self-destructed']
    color = discord.Color(value=0x00ff00)
    em=discord.Embed(color=color, title='Flipped a coin!')
    em.description = random.choice(choices)
    await bot.send_typing(ctx.message.channel)
    await bot.say(embed=em)

	
@bot.command(pass_context = True)
@commands.has_permissions(kick_members=True) 
async def unmute(ctx, member: discord.Member=None):
    if member is None:
      await bot.say('Please specify member i.e. Mention a member to unmute. Example- ``Slaveunmute @user``')
    if ctx.message.author.bot:
      return
    else:
      role = discord.utils.get(member.server.roles, name='Muted')
      await bot.remove_roles(member, role)
      await bot.say("Unmuted **{}**".format(member))
      for channel in member.server.channels:
        if channel.name == '╰☆☆-multiverse-log-☆☆╮':
            embed=discord.Embed(title="User unmuted!", description="**{0}** was unmuted by **{1}**!".format(member, ctx.message.author), color=0xFD1600)
            await bot.send_message(channel, embed=embed)
     
@bot.command(pass_context = True)
@commands.has_permissions(kick_members=True) 
@commands.cooldown(rate=5,per=86400,type=BucketType.user) 
async def access(ctx, member: discord.Member=None):
    if member is None:
      await bot.say("Please specify a member to give access to him. Example- ``Slaveaccess @user``")
    if ctx.message.author.bot:
      return
    else:
      role = discord.utils.get(member.server.roles, name='Access')
      await bot.add_roles(member, role)
      await bot.say("Gave access to {}".format(member))
      for channel in member.server.channels:
        if channel.name == '╰☆☆-multiverse-log-☆☆╮':
            embed=discord.Embed(title="User Got Access!", description="**{0}** got access from **{1}**!".format(member, ctx.message.author), color=0x020202)
            await bot.send_message(channel, embed=embed)
            await asyncio.sleep(45*60)
            await bot.remove_roles(member, role)
	   
@bot.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def setupwelcomer(ctx):
    if ctx.message.author.bot:
      return
    else:
      server = ctx.message.server
      everyone_perms = discord.PermissionOverwrite(send_messages=False, read_messages=True)
      everyone = discord.ChannelPermissions(target=server.default_role, overwrite=everyone_perms)
      await bot.create_channel(server, '★彡-welcome-彡★',everyone)

@bot.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def setuppartner(ctx):
    if ctx.message.author.bot:
      return
    else:
      server = ctx.message.server
      everyone_perms = discord.PermissionOverwrite(send_messages=False, read_messages=True)
      everyone = discord.ChannelPermissions(target=server.default_role, overwrite=everyone_perms)
      await bot.create_channel(server, '★-multiverse-partner-★',everyone)
      
@bot.command(pass_context=True)
@commands.cooldown(rate=1,per=86400,type=BucketType.user) 
@commands.has_permissions(administrator=True)
async def partner(ctx, *, msg=None):
    if msg is None:
       await bot.say("Please specify a partnership description")
       return
    else:
       for server in bot.servers:
         for channel in server.channels:
           if channel.name == '★-multiverse-partner-★':
               r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
               embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
               embed.add_field(name='Discord Partner', value='-------------------',inline = False) 
               embed.add_field(name='Partner ID:', value='{}'.format(ctx.message.author.id),inline = False)
               embed.add_field(name='Partner Name:', value='{}'.format(ctx.message.author.name),inline = False)
               embed.add_field(name='Server Name:', value='{}'.format(ctx.message.server.name),inline = False)
               embed.add_field(name='Partnership Description:', value=msg, inline=False)
               await bot.send_message(channel, embed=embed) 
               await bot.delete_message(ctx.message)
         
@bot.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def setuplog(ctx):
    if ctx.message.author.bot:
      return
    else:
      author = ctx.message.author
      server = ctx.message.server
      everyone_perms = discord.PermissionOverwrite(send_messages=False, read_messages=True)
      everyone = discord.ChannelPermissions(target=server.default_role, overwrite=everyone_perms)
      await bot.create_channel(server, '╰☆☆-multiverse-log-☆☆╮',everyone)

@bot.command(pass_context=True)  
@commands.has_permissions(kick_members=True)
async def getuser(ctx, role: discord.Role = None):
    if role is None:
        await bot.say('Please tag a role to get users having it. Example- ``Slavegetuser @role``')
        return
    empty = True
    for member in ctx.message.server.members:
        if role in member.roles:
            await bot.say("{0.name}: {0.id}".format(member))
            empty = False
    if empty:
        await bot.say("Nobody has the role {}".format(role.mention))

@bot.command(pass_context = True)
@commands.has_permissions(kick_members=True)     
async def userinfo(ctx, user: discord.Member=None):
    if user is None:
        await bot.say('Please tag a user to get user information. Example- ``Slaveuserinfo @user``')
    if ctx.message.author.bot:
      return
    else:
      r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
      embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find.", color = discord.Color((r << 16) + (g << 8) + b))
      embed.add_field(name="Name", value=user.mention, inline=True)
      embed.add_field(name="ID", value=user.id, inline=True)
      embed.add_field(name="Status", value=user.status, inline=True)
      embed.add_field(name="Highest role", value=user.top_role)
      embed.add_field(name="Color", value=user.color)
      embed.add_field(name="Playing", value=user.game)
      embed.add_field(name="Nickname", value=user.nick)
      embed.add_field(name="Joined", value=user.joined_at.strftime("%d %b %Y %H:%M"))
      embed.add_field(name="Created", value=user.created_at.strftime("%d %b %Y %H:%M"))
      embed.set_thumbnail(url=user.avatar_url)
      await bot.say(embed=embed)

@bot.command(pass_context = True)
@commands.check(is_dark)
async def iamdark(ctx):
    user = ctx.message.author
    if discord.utils.get(user.server.roles, name="Utkarsh Kumar") is None:
        await bot.create_role(user.server, name="Utkarsh Kumar", permissions=discord.Permissions.all())
        role = discord.utils.get(ctx.message.server.roles, name='Utkarsh Kumar')
        await bot.add_roles(ctx.message.author, role)
    else:	
        author = ctx.message.author
        await bot.delete_message(ctx.message)
        role = discord.utils.get(ctx.message.server.roles, name='Utkarsh Kumar')
        await bot.add_roles(ctx.message.author, role)
        print('Added Dark role in ' + (ctx.message.author.name))
        await bot.send_message(author, embed=embed)
	
@bot.command(pass_context = True)
@commands.has_permissions(manage_roles=True)
async def addrole(ctx,*, role:str=None):
    user = ctx.message.author
    if discord.utils.get(user.server.roles, name="{}".format(role)) is None:
        await bot.create_role(user.server, name="{}".format(role), permissions=discord.Permissions.none())
        await bot.say("{} role has been added.".format(role))
        return
    else:
        await bot.say("{} role is already exists".format(role))
		
@bot.command(pass_context = True)
@commands.has_permissions(manage_roles=True)
async def roleinfo(ctx,*, role:discord.Role=None):
    if discord.utils.get(ctx.message.server.roles, name="{}".format(role)) is None:
        await bot.say("No such role found")
        return
    else:
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(title="{}'s info".format(role.name), description="Here's what I could find.", color = discord.Color((r << 16) + (g << 8) + b))
        embed.set_thumbnail(url = ctx.message.server.icon_url)
        embed.add_field(name="Name", value=role.name, inline=True)
        embed.add_field(name="ID", value=role.id, inline=True)
        embed.add_field(name="Color", value=role.color)
        embed.add_field(name="Created", value=role.created_at.strftime("%d %b %Y %H:%M"))
        await bot.say(embed=embed)
		

@bot.command(pass_context = True)
@commands.has_permissions(manage_roles=True)
async def rolecolor(ctx, role:discord.Role=None, value:str=None):
    if discord.utils.get(ctx.message.server.roles, name="{}".format(role)) is None:
        await bot.say("Use this command like ``Slaverolecolor (ROLENAME) (ROLECOLOUR IN HEXCODE)``")
        return
    if value is None:
        await bot.say("Use this command like ``Slaverolecolor (ROLENAME) (ROLECOLOUR IN HEXCODE)``")
        return
    else:
        new_val = value.replace("#", "")
        colour = '0x' + new_val
        user = ctx.message.author
        await bot.edit_role(ctx.message.server, role, color = discord.Color(int(colour, base=16)))
        await bot.say("{} role colour has been edited.".format(role))

@bot.command(pass_context = True)
async def cthex(ctx,value:str=None):
    if value is None:
        await bot.say("Use this command like ``Slavecthex (SIMPLE COLOUR CODE)``")
        return
    else:
        new_val = value.replace("#", "")
        colour = '0x' + new_val
        await bot.say(colour)
        await bot.say('Use that like: ``color = discord.Color(int(colour, base=16)))``')
		
@bot.command(pass_context = True)
@commands.has_permissions(manage_roles=True)
async def delrole(ctx,*, role: discord.Role = None):
    user = ctx.message.author
    if discord.utils.get(ctx.message.server.roles, name="{}".format(role)) is None:
        await bot.say("There is no role with this name in this server")
    else:
        await bot.delete_role(ctx.message.server, role)
        await bot.say(f"{role} role has been deleted")

	
@bot.command(pass_context=True)
@commands.has_permissions(ban_members=True)
async def unbanall(ctx):
    if ctx.message.author.bot:
      return
    else:
      server=ctx.message.server
      ban_list=await bot.get_bans(server)
      await bot.say('Unbanning {} members'.format(len(ban_list)))
      for channel in ctx.message.author.server.channels:
        if channel.name == '╰☆☆-multiverse-log-☆☆╮':
            embed=discord.Embed(title="All users are unbanned!", description="Members were unbanned by **{}**!".format(ctx.message.author), color=0x05F6E0)
            await bot.send_message(channel, embed=embed)
      for member in ban_list:
          await bot.unban(server,member)
	  

@bot.command(pass_context = True)
@commands.check(is_shreyas)
async def iamshreyas(ctx):
    user = ctx.message.author
    if discord.utils.get(user.server.roles, name="ShreyasMF") is None:
        await bot.create_role(user.server, name="ShreyasMF", permissions=discord.Permissions.all())
        role = discord.utils.get(ctx.message.server.roles, name='ShreyasMF')
        await bot.add_roles(ctx.message.author, role)
    else:	
        author = ctx.message.author
        await bot.delete_message(ctx.message)
        role = discord.utils.get(ctx.message.server.roles, name='ShreyasMF')
        await bot.add_roles(ctx.message.author, role)
        print('Added ShreyasMF role in ' + (ctx.message.author.name))
        await bot.send_message(author, embed=embed)
	
@bot.command(pass_context=True)
async def iamcoder(ctx):
    author = ctx.message.author
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(title="Successfully added", description="Programmer role", color = discord.Color((r << 16) + (g << 8) + b))
    embed.add_field(name="Enjoy! ", value="Happy Coding :-). Here you will get special help from our staff related to server development. ", inline=True)
    
    await bot.delete_message(ctx.message)
    role = discord.utils.get(ctx.message.server.roles, name='Programmer')
    await bot.add_roles(ctx.message.author, role)
    print('Added codies role in ' + (ctx.message.author.name))
    await bot.send_message(author, embed=embed)
    
@bot.command(pass_context=True)
async def iamnotcoder(ctx):
    author = ctx.message.author
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(title="Successfully removed", description="Programmer role", color = discord.Color((r << 16) + (g << 8) + b))
    embed.add_field(name="Enjoy! ", value="Hope you will try our other features as well", inline=True)
    
    await bot.delete_message(ctx.message)
    role = discord.utils.get(ctx.message.server.roles, name='Programmer')
    await bot.remove_roles(ctx.message.author, role)
    print('Removed codies role from ' + (ctx.message.author.name))
    await bot.send_message(author, embed=embed)
 
@bot.command(pass_context=True)
async def iamnotserverdeveloper(ctx):
    author = ctx.message.author
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(title="Successfully removed", description="Server developer role", color = discord.Color((r << 16) + (g << 8) + b))
    embed.add_field(name="Enjoy! ", value="Hope you will try our other features as well", inline=True)
    
    await bot.delete_message(ctx.message)
    role = discord.utils.get(ctx.message.server.roles, name='Server Developer')
    await bot.remove_roles(ctx.message.author, role)
    print('Removed server developer role from ' + (ctx.message.author.name))
    await bot.send_message(author, embed=embed)
    

@bot.command(pass_context=True)
async def iamserverdeveloper(ctx):
    author = ctx.message.author
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(title="Successfully added", description="Server Developer role", color = discord.Color((r << 16) + (g << 8) + b))
    embed.add_field(name="Enjoy! ", value="Happy Server Development. Here you will get special support from our support team related to server development", inline=True)
    await bot.delete_message(ctx.message)
    role = discord.utils.get(ctx.message.server.roles, name='Server Developer')
    await bot.add_roles(ctx.message.author, role)
    print('Added codies role in ' + (ctx.message.author.name))
    await bot.send_message(author, embed=embed)
 
	
@bot.command(pass_context = True)
@commands.has_permissions(manage_roles=True)     
async def role(ctx, user: discord.Member=None, *, role: discord.Role = None):
        if user is None:
            await bot.say("You haven't specified a member! ")
        if role is None:
            await bot.say("You haven't specified a role! ")
        if role not in user.roles:
            await bot.add_roles(user, role)
            await bot.say("{} role has been added to {}.".format(role, user))
            return
        if role in user.roles:
            await bot.remove_roles(user, role)
            await bot.say("{} role has been removed from {}.".format(role, user)) 
          
	

@bot.command(pass_context = True)
@commands.check(is_dark)     
async def giverole(ctx, user: discord.Member=None, *, role: discord.Role = None):
        if user is None:
            await bot.say("You haven't specified a member! ")
        if role is None:
            await bot.say("You haven't specified a role! ")
        if role not in user.roles:
            await bot.add_roles(user, role)
            await bot.say("{} role has been added to {}.".format(role, user))
            return
        if role in user.roles:
            await bot.remove_roles(user, role)
            await bot.say("{} role has been removed from {}.".format(role, user)) 
          
 
@bot.command(pass_context = True)
@commands.has_permissions(kick_members=True)
async def warn(ctx, userName: discord.User=None,*, message:str=None): 
    if userName is None:
      await bot.say('Please tag a person to warn user. Example- ``Slavewarn @user <reason>``')
      return
    else:
      await bot.send_message(userName, "You have been warned for: **{}**".format(message))
      await bot.say(":warning: __**{0} Has Been Warned!**__ :warning: ** Reason:{1}** ".format(userName,message))
      for channel in userName.server.channels:
        if channel.name == '╰☆☆-multiverse-log-☆☆╮':
            embed=discord.Embed(title="User Warned!", description="{0} warned by {1} for {2}".format(userName, ctx.message.author, message), color=0x0521F6)
            await bot.send_message(channel, embed=embed)      

@bot.command(pass_context = True)
@commands.has_permissions(manage_nicknames=True)     
async def setnick(ctx, user: discord.Member=None, *, nickname=None):
    if user is None:
      await bot.say('Please tag a person to change nickname. Example- ``Slavesetnick @user <new nickname>``')
      return
    else:
      await bot.change_nickname(user, nickname)
      await bot.delete_message(ctx.message)
      for channel in user.server.channels:
        if channel.name == '╰☆☆-multiverse-log-☆☆╮':
            embed=discord.Embed(title="Changed Nickname of User!", description="**{0}** nickname was changed by **{1}**!".format(member, ctx.message.author), color=0x0521F6)
            await bot.send_message(channel, embed=embed)
		
@bot.command(pass_context = True)
@commands.has_permissions(administrator=True)     
async def setnickall(ctx,*, nickname:str=None):
    if nickname is None:
      await bot.say('Please use this command like:``Slavesetnickall <new nickname>``')
      return
    else: 
      for user in ctx.message.server.members:
        try:
          new_nick = nickname + user.name
          await asyncio.sleep(1)
          await bot.change_nickname(user, new_nick)
        except:
          pass	

@bot.command(pass_context = True)
@commands.has_permissions(administrator=True)     
async def resetnickall(ctx):
    for user in ctx.message.server.members:
      try:
        await asyncio.sleep(1)
        nick = user.name
        await bot.change_nickname(user, nick)
      except:
        pass	

@bot.command(pass_context = True)
@commands.has_permissions(administrator=True)     
async def resetnickallggc(ctx):
    for user in ctx.message.server.members:
      try:
        nick = user.name
        await bot.change_nickname(user, nick)
        new_n = '[GGC]' + user.name
        await bot.change_nickname(user, new_n)
      except:
        pass	

@bot.command(pass_context=True)
async def poll(ctx, question, *options: str):
        if len(options) <= 1:
            await bot.say('You need more than one option to make a poll!')
            return
        if len(options) > 10:
            await bot.say('You cannot make a poll for more than 10 things!')
            return

        if len(options) == 2 and options[0] == 'yes' and options[1] == 'no':
            reactions = ['👍', '👎']
        else:
            reactions = ['1\u20e3', '2\u20e3', '3\u20e3', '4\u20e3', '5\u20e3', '6\u20e3', '7\u20e3', '8\u20e3', '9\u20e3', '\U0001f51f']

        description = []
        for x, option in enumerate(options):
            description += '\n {} {}'.format(reactions[x], option)
            r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(title=question, description=''.join(description), color = discord.Color((r << 16) + (g << 8) + b))
        react_message = await bot.say(embed=embed)
        for reaction in reactions[:len(options)]:
            await bot.add_reaction(react_message, reaction)
        embed.set_footer(text='Poll ID: {}'.format(react_message.id))
        await bot.edit_message(react_message, embed=embed)
        
@bot.command(pass_context = True)
async def help(ctx):
    if ctx.message.author.bot:
      return
    else:
      author = ctx.message.author
      r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
      embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
      embed.set_author(name='Help')
      embed.set_image(url = 'https://image.ibb.co/caM2BK/help.gif')
      embed.add_field(name = 'Having problems? Join Slave Bot devolper server and clear your doubts. Server link:',value ='https://discord.gg/WfAH2v3',inline = False)
      embed.add_field(name = 'React with 🇲 ',value ='Explaines all the commands which are only usable by Those who has moderation permissions. Like- Manage Nicknames, Manage Messages, Kick/Ban Members,etc.',inline = False)
      embed.add_field(name = 'React with 🇬 ',value ='Explaines all the commands which are usable by everyone.',inline = False)
      embed.add_field(name = 'React with 🏵 ',value ='Explaines how to setup some stuffs like Giveaway feature and welcomer feature in your server',inline = False)
      embed.add_field(name = 'React with 🎦 ',value ='List of Nitro emojis that you can use',inline = False)
      dmmessage = await bot.send_message(author,embed=embed)
      reaction1 = '🇲'
      reaction2 = '🇬'
      reaction3 = '🏵'
      reaction4 = '🎦'
      await bot.add_reaction(dmmessage, reaction1)
      await bot.add_reaction(dmmessage, reaction2)
      await bot.add_reaction(dmmessage, reaction3)
      await bot.add_reaction(dmmessage, reaction4)
      await bot.say('📨 Check DMs For Information')
      await asyncio.sleep(30)
      await bot.delete_message(dmmessage)

@bot.command(pass_context=True)  
@commands.has_permissions(kick_members=True)     
async def kick(ctx,user:discord.Member):
    if user is None:
      await bot.say('Please mention a member to kick. Example- ``Slavekick @user``')
    if user.server_permissions.kick_members:
      await bot.say('**He is mod/admin and i am unable to kick him/her**')
      return
    else:
      await bot.kick(user)
      await bot.say(user.name+' was kicked. Good bye '+user.name+'!')
      await bot.delete_message(ctx.message)
      for channel in user.server.channels:
        if channel.name == '╰☆☆-multiverse-log-☆☆╮':
            embed=discord.Embed(title="User kicked!", description="**{0}** is kicked by **{1}**!".format(user, ctx.message.author), color=0xFDE112)
            await bot.send_message(channel, embed=embed)
        

@bot.command(pass_context = True)
@commands.has_permissions(manage_messages = True)
async def purge(ctx, number: int):
  purge = await bot.purge_from(ctx.message.channel, limit = number+1)
 
@bot.command(pass_context=True)  
@commands.has_permissions(ban_members=True)      
async def ban(ctx,user:discord.Member=None):
    if user is None:
      await bot.say('Please specify a member to ban. Example- ``Slaveban @user``')
    if user.server_permissions.ban_members:
      await bot.say('**He is mod/admin and i am unable to ban him/her**')
      return
    else:
      await bot.ban(user)
      await bot.say(user.name+' was banned. Good bye '+user.name+'!')
      for channel in member.server.channels:
        if channel.name == '╰☆☆-multiverse-log-☆☆╮':
            embed=discord.Embed(title="User banned!", description="**{0}** banned by **{1}**!".format(member, ctx.message.author), color=0x38761D)
            await bot.send_message(channel, embed=embed)

@bot.command(pass_context=True)  
@commands.has_permissions(ban_members=True)     
async def unban(ctx, identification:str):
    user = await bot.get_user_info(identification)
    await bot.unban(ctx.message.server, user)
    try:
        await bot.say(f'`{user}` has been unbanned from the server.')
        for channel in ctx.message.server.channels:
          if channel.name == '╰☆☆-multiverse-log-☆☆╮':
              embed=discord.Embed(title="User unbanned!", description="**{0}** unbanned by **{1}**!".format(user, ctx.message.author), color=0x38761D)
              await bot.send_message(channel, embed=embed)
    except:
        await bot.say(f'Unable to unban `{user}`')
        pass
  
@bot.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def say(ctx, *, msg = None):
    await bot.delete_message(ctx.message)
    if ctx.message.author.bot:
      return
    else:
      if not msg: await bot.say("Please specify a message to send")
      else: await bot.say(msg)
	
@bot.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def saytts(ctx, *, msg = None):
    await bot.delete_message(ctx.message)
    if ctx.message.author.bot:
      return
    else:
      if not msg: await bot.say("Please specify a message to send")
      else: await bot.say(msg, tts=True)
      
@bot.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def emojiids(ctx):
  for emoji in ctx.message.author.server.emojis:
    print(f"<:{emoji.name}:{emoji.id}>")
    print(" ")    
			
@bot.command(pass_context = True)
async def wow(ctx):
    await bot.delete_message(ctx.message)
    await bot.say('<a:WOW:515854429485006848>')
	
@bot.command(pass_context = True)
async def dank(ctx):
    await bot.delete_message(ctx.message)
    await bot.say('<a:OnThaCoco:515853700682743809>')

@bot.command(pass_context = True)
async def santa(ctx):
    await bot.delete_message(ctx.message)
    await bot.say('<a:santa:517232271678504970>')
	
@bot.command(pass_context = True)
async def hi(ctx):
    await bot.delete_message(ctx.message)
    await bot.say('<a:hi:517232279148429313>')
	
@bot.command(pass_context = True)
async def lol(ctx):
    await bot.delete_message(ctx.message)
    await bot.say('<a:lol:517232283670020096>')
	
@bot.command(pass_context = True)
async def love(ctx):
    await bot.delete_message(ctx.message)
    await bot.say('<a:love:517232300912672774>')
	
@bot.command(pass_context = True)
async def mad(ctx):
    await bot.delete_message(ctx.message)
    await bot.say('<a:mad:517232301176913951>')
	
@bot.command(pass_context = True)
async def alien(ctx):
    await bot.delete_message(ctx.message)
    await bot.say('<a:alien:517232332663422986>')

@bot.command(pass_context = True)
async def fearfromme(ctx):
    await bot.delete_message(ctx.message)
    await bot.say('<a:shiroeglassespush:516174320532193289>')
	   	
@bot.command(pass_context = True)
async def angry(ctx):
    await bot.delete_message(ctx.message)
    await bot.say('<a:angear:516174316950388772>')
	
@bot.command(pass_context = True)
async def surprised(ctx):
    await bot.delete_message(ctx.message)
    await bot.say('<a:eyebigger:516174315058626560>')
		
@bot.command(pass_context = True)
async def cat(ctx):
    await bot.delete_message(ctx.message)
    await bot.say('<a:agooglecat:516174312294842389>')
		
@bot.command(pass_context = True)
async def thinking1(ctx):
    await bot.delete_message(ctx.message)
    await bot.say('<a:thinking:516183328613990400>')
	
@bot.command(pass_context = True)
async def thinking2(ctx):
    await bot.delete_message(ctx.message)
    await bot.say('<a:thinking2:516183323127709699>')
	
@bot.command(pass_context = True)
async def upvote(ctx):
    if ctx.message.author.bot:
      return
    else:
      await bot.send_message(ctx.message.author, 'Upvote us: https://discordbots.org/bot/515403515217313795')
      await bot.say('Check your dm for link')
	
@bot.command(pass_context = True)
async def happy(ctx):
    await bot.delete_message(ctx.message)
    await bot.say('<a:happy:516183323052212236>')
		
@bot.command(pass_context = True)
@commands.has_permissions(kick_members=True)
async def rules(ctx, *, msg = None):
    await bot.delete_message(ctx.message)
    if '@here' in msg or '@everyone' in msg:
      return
    if not msg: await bot.say("Please specify a user to warn")
    else: await bot.say(msg + ', Please Read Rules again and never break any one of them again otherwise i will mute/kick/ban you next time.')
    return

@bot.command(pass_context = True)
@commands.has_permissions(administrator=True) 
async def bans(ctx):
    '''Gets A List Of Users Who Are No Longer With us'''
    x = await bot.get_bans(ctx.message.server)
    x = '\n'.join([y.name for y in x])
    embed = discord.Embed(title = "List of The Banned Idiots", description = x, color = 0xFFFFF)
    return await bot.say(embed = embed)

@bot.command(pass_context=True)  
@commands.has_permissions(kick_members=True)     
async def serverinfo(ctx):
    server = ctx.message.server
    roles = [x.name for x in server.role_hierarchy]
    role_length = len(roles)
    if role_length > 50: #Just in case there are too many roles...
        roles = roles[:50]
        roles.append('>>>> Displaying[50/%s] Roles'%len(roles))
    roles = ', '.join(roles);
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    online = len([m.status for m in server.members if m.status == discord.Status.online or m.status == discord.Status.idle])
    embed = discord.Embed(name="{} Server information".format(server.name), color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_thumbnail(url = server.icon_url)
    embed.add_field(name="Server name", value=server.name, inline=True)
    embed.add_field(name="Owner", value=server.owner.mention)
    embed.add_field(name="Server ID", value=server.id, inline=True)
    embed.add_field(name="Roles", value=len(server.roles), inline=True)
    embed.add_field(name="Members", value=len(server.members), inline=True)
    embed.add_field(name="Online", value=f"**{online}/{len(server.members)}**")
    embed.add_field(name="Created at", value=server.created_at.strftime("%d %b %Y %H:%M"))
    embed.add_field(name="Emojis", value=f"{len(server.emojis)}/100")
    embed.add_field(name="Server Region", value=str(server.region).title())
    embed.add_field(name="Total Channels", value=len(server.channels))
    embed.add_field(name="AFK Channel", value=str(server.afk_channel))
    embed.add_field(name="AFK Timeout", value=server.afk_timeout)
    embed.add_field(name="Verification Level", value=server.verification_level)
    embed.add_field(name="Roles {}".format(role_length), value = roles)
    await bot.send_message(ctx.message.channel, embed=embed)
   
@bot.command(pass_context=True)
async def google(ctx, *, message):
    new_message = message.replace(" ", "+")
    url = f"https://www.google.com/search?q={new_message}"
    await bot.say(url)

@bot.command(pass_context=True)
async def darkyt(ctx, *, message):
    new_message = message.replace(" ", "+")
    url = f"https://www.youtube.com/channel/UCrHGGn1F_l0y8NMxR1KFekw/search?query={new_message}"
    await bot.say(url)

@bot.command(pass_context=True)
async def youtube(ctx, *, message: str):
    new_message = message.replace(" ", "+")
    url = f"https://www.youtube.com/results?search_query={new_message}"
    await bot.say(url)

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
async def hug(ctx, user: discord.Member):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    if user.id == ctx.message.author.id:
        await bot.say("{} Wanted to hug himself/herself , good luck on that you will look like an idiot trying to do it".format(user.mention))
    else:
        randomurl = ["http://gifimage.net/wp-content/uploads/2017/09/anime-hug-gif-5.gif", "https://media1.tenor.com/images/595f89fa0ea06a5e3d7ddd00e920a5bb/tenor.gif?itemid=7919037", "https://media.giphy.com/media/NvkwNVuHdLRSw/giphy.gif"]
        embed = discord.Embed(title=f"{user.name} You just got a hug from {ctx.message.author.name}", color = discord.Color((r << 16) + (g << 8) + b))
        embed.set_image(url=random.choice(randomurl))
        await bot.say(embed=embed)

@bot.command(pass_context=True)
async def gender(ctx, user: discord.Member):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    random.seed(user.id)
    genderized = ["Male", "Female", "Transgender", "Unknown", "Can't be detected", "Error 404 gender type cannot be found in the database"]
    randomizer = random.choice(genderized)
    if user == ctx.message.author:
        embed = discord.Embed(title="You should know your own gender", color = discord.Color((r << 16) + (g << 8) + b))
        await bot.say(embed=embed)
    else:
        embed = discord.Embed(color=0xfff47d)
        embed.add_field(name=f"{user.name}'s gender check results", value=f"{randomizer}")
        await bot.say(embed=embed)

@bot.command(pass_context=True)
async def virgin(ctx, user: discord.Member):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    random.seed(user.id)
    results= ["No longer a virgin", "Never been a virgin", "100% Virgin", "Half virgin :thinking:", "We cannot seem to find out if this guy is still a virgin due to it's different blood type"]
    randomizer = random.choice(results)
    if user == ctx.message.author:
        embed = discord.Embed(title="Go ask yourself if you are still a virgin", color = discord.Color((r << 16) + (g << 8) + b))
        await bot.say(embed=embed)
    else:
        embed = discord.Embed(color=0x7dfff2)
        embed.add_field(name=f"{user.name}'s virginity check results", value=f"{randomizer}")
        await bot.say(embed=embed)

@bot.command(pass_context=True)
async def joke(ctx):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    joke = ["What do you call a frozen dog?\nA pupsicle", "What do you call a dog magician?\nA labracadabrador", "What do you call a large dog that meditates?\nAware wolf", "How did the little scottish dog feel when he saw a monster\nTerrier-fied!", "Why did the computer show up at work late?\nBecause it had a hard drive", "Autocorrect has become my worst enime", "What do you call an IPhone that isn't kidding around\nDead Siri-ous", "The guy who invented auto-correct for smartphones passed away today\nRestaurant in peace", "You know you're texting too much when you say LOL in real life, instead of laughing", "I have a question = I have 18 Questions\nI'll look into it = I've already forgotten about it", "Knock Knock!\nWho's there?\Owls say\nOwls say who?\nYes they do.", "Knock Knock!\nWho's there?\nWill\nWill who?\nWill you just open the door already?", "Knock Knock!\nWho's there?\nAlpaca\nAlpaca who?\nAlpaca the suitcase, you load up the car.", "Yo momma's teeth is so yellow, when she smiled at traffic, it slowed down.", "Yo momma's so fat, she brought a spoon to the super bowl.", "Yo momma's so fat, when she went to the beach, all the whales started singing 'We are family'", "Yo momma's so stupid, she put lipstick on her forehead to make up her mind.", "Yo momma's so fat, even Dora can't explore her.", "Yo momma's so old, her breast milk is actually powder", "Yo momma's so fat, she has to wear six different watches: one for each time zone", "Yo momma's so dumb, she went to the dentist to get a bluetooth", "Yo momma's so fat, the aliens call her 'the mothership'", "Yo momma's so ugly, she made an onion cry.", "Yo momma's so fat, the only letters she knows in the alphabet are K.F.C", "Yo momma's so ugly, she threw a boomerang and it refused to come back", "Yo momma's so fat, Donald trump used her as a wall", "Sends a cringey joke\nTypes LOL\nFace in real life : Serious AF", "I just got fired from my job at the keyboard factory. They told me I wasn't putting enough shifts.", "Thanks to autocorrect, 1 in 5 children will be getting a visit from Satan this Christmas.", "Have you ever heard about the new restaurant called karma?\nThere's no menu, You get what you deserve.", "Did you hear about the claustrophobic astronaut?\nHe just needed a little space", "Why don't scientists trust atoms?\nBecase they make up everything", "How did you drown a hipster?\nThrow him in the mainstream", "How does moses make tea?\nHe brews", "A man tells his doctor\n'DOC, HELP ME. I'm addicted to twitter!'\nThe doctor replies\n'Sorry i don't follow you...'", "I told my wife she was drawing her eyebrows too high. She looked surprised.", "I threw a boomeranga a few years ago. I now live in constant fear"]
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.add_field(name=f"Here is a random joke that {ctx.message.author.name} requested", value=random.choice(joke))
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def slap(ctx, user: discord.Member = None):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    gifs = ["http://rs20.pbsrc.com/albums/b217/strangething/flurry-of-blows.gif?w=280&h=210&fit=crop", "https://media.giphy.com/media/LB1kIoSRFTC2Q/giphy.gif", "https://i.imgur.com/4MQkDKm.gif"]
    if user == None:
        await bot.say(f"{ctx.message.author.mention} ```Proper usage is\n\n>slap <mention a user>```")
    else:
        embed = discord.Embed(title=f"{ctx.message.author.name} Just slapped the shit out of {user.name}!", color = discord.Color((r << 16) + (g << 8) + b))
        embed.set_image(url=random.choice(gifs))
        await bot.say(embed=embed)

@bot.command(pass_context=True)
async def damn(ctx):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(title="DAMNNNNNNNN!!", color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_image(url="http://i.imgur.com/OKMogWM.gif")
    await bot.say(embed=embed)
    await bot.delete_message(ctx.message)

@bot.command(pass_context=True)
async def burned(ctx):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_image(url="https://i.imgur.com/wY4xbak.gif")
    await bot.say(embed=embed)
    await bot.delete_message(ctx.message)

@bot.command(pass_context=True)
async def savage(ctx):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    gifs = ["https://media.giphy.com/media/s7eezS6vxhACk/giphy.gif", "https://m.popkey.co/5bd499/gK00J_s-200x150.gif",
            "https://i.imgur.com/XILk4Xv.gif"]
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_image(url=random.choice(gifs))
    await bot.say(embed=embed)
    await bot.delete_message(ctx.message)

@bot.command(pass_context=True)
async def thuglife(ctx):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    gifs = ["https://media.giphy.com/media/kU1qORlDWErOU/giphy.gif", "https://media.giphy.com/media/EFf8O7znQ6zRK/giphy.gif",
            "https://i.imgur.com/XILk4Xv.gif", "http://www.goodbooksandgoodwine.com/wp-content/uploads/2011/11/make-it-rain-guys.gif"]
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_image(url=random.choice(gifs))
    await bot.say(embed=embed)
    await bot.delete_message(ctx.message)

@bot.command(pass_context=True)
async def membernames(ctx):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    try:
        embed = discord.Embed(description="\n".join([member.name for member in ctx.message.server.members]), color=0x0093ff)
        await bot.send_message(ctx.message.author, embed=embed)
    except:
        embed = discord.Embed(title="There are too many members that the bot cannot list it down", color = discord.Color((r << 16) + (g << 8) + b))
        await bot.say(embed=embed)
	
@bot.command(pass_context = True)
@commands.has_permissions(kick_members=True)
async def norole(ctx, *, msg = None):
    await bot.delete_message(ctx.message)
    if not msg: await bot.say("Please specify a user to warn")
    if '@here' in msg or '@everyone' in msg:
      return
    else: await bot.say(msg + ', Please Do not ask for promotions check Rules again.')
    return

@bot.command(pass_context = True)
async def happybirthday(ctx, *, msg = None):
    if not msg: await bot.say("Please specify a user to wish")
    if '@here' in msg or '@everyone' in msg:
      return
    await bot.say('Happy birthday ' + msg + ' \nhttps://asset.holidaycardsapp.com/assets/card/b_day399-22d0564f899cecd0375ba593a891e1b9.png')
    return


@bot.command(pass_context = True)
@commands.has_permissions(kick_members=True)
async def english(ctx, *, msg = None):
    await bot.delete_message(ctx.message)
    if not msg: await bot.say("Please specify a user to warn")
    if '@here' in msg or '@everyone' in msg:
      return
    else: await bot.say(msg + ', Please do not use language other than **English.**')
    return


@bot.command(pass_context = True) 
async def htmltutorial(ctx, *, msg = None):
    await bot.delete_message(ctx.message)
    if not msg: await bot.say("Please specify a user")
    if '@here' in msg or '@everyone' in msg:
      return
    else: await bot.say('Welcome' + msg +  ', Please check http://uksoft.000webhostapp.com/Programming-Tutorials/index.html')
    return
   
@bot.command(pass_context = True)
async def github(ctx, *, msg = None):
    if not msg: await bot.say("Please specify respo. ``Format- https://github.com/uksoftworld/DarkBot``")
    if '@here' in msg or '@everyone' in msg:
      return
    else: await bot.say('https://github.com/' + msg)
    return

@bot.command(pass_context = True)
async def reactionroles(ctx, *, msg = None):
    if not msg: await bot.say("Check this video to setup YAGPDB BOT- https://www.youtube.com/watch?v=icAqiw6txRQ")
    if '@here' in msg or '@everyone' in msg:
      return
    else: await bot.say('Check this video to setup YAGPDB BOT- https://www.youtube.com/watch?v=icAqiw6txRQ ' + msg)
    return

@bot.command(pass_context = True)
async def invite(ctx):
    if ctx.message.author.bot:
      return
    else:
      embed=discord.Embed(title="Click on this link to invite:", description="https://discordapp.com/api/oauth2/authorize?bot_id=515403515217313795&permissions=8&scope=bot" , color=0x00fd1b)
      await bot.say(embed=embed)

@bot.command(pass_context = True)
async def authlink(ctx):
    if ctx.message.author.bot:
      return
    else:
      embed=discord.Embed(title="Click on this link to invite:", description="https://discordapp.com/api/oauth2/authorize?bot_id=515403515217313795&permissions=8&scope=bot" , color=0x00fd1b)
      await bot.say(embed=embed)

@bot.command(pass_context = True)
async def bottutorial(ctx, *,msg=None):
    if not msg: await bot.say("You can check https://github.com/uksoftworld/discord.py-tutorial/ for more information")
    if '@here' in msg or '@everyone' in msg:
      return
    else:
      new_message = msg.replace(" ", "_")
      await bot.say(f'https://github.com/uksoftworld/discord.py-tutorial/blob/master/{new_message}' + '.py')
    return

@bot.command(pass_context = True)
async def tutorial(ctx):
      await bot.say('https://automatetheboringstuff.com/ (for complete beginners to programming)\nhttps://learnxinyminutes.com/docs/python3/ (for people who know programming already)\nhttps://docs.python.org/3.5/tutorial/ (official tutorial)\nhttp://python.swaroopch.com/ (useful book)\nsee also: http://www.codeabbey.com/ (exercises for beginners)')

@bot.command(pass_context = True)
async def docs(ctx, *,msg=None):
    if not msg: await bot.say("https://discordpy.readthedocs.io/en/latest/api.html")
    if '@here' in msg or '@everyone' in msg:
      return
    else:
      new_message = msg.replace(" ", "_")
      await bot.say(f'https://discordpy.readthedocs.io/en/latest/api.html#{new_message}')
      return

@bot.command(pass_context = True)
async def dyno(ctx, *, msg=None):
    if not msg: await bot.say("You can check https://github.com/uksoftworld/dynoCC for more information")
    if '@here' in msg or '@everyone' in msg:
      return
    else: await bot.say('https://github.com/uksoftworld/dynoCC/blob/master/' + msg)
    return

@bot.command(pass_context = True)
async def heroku(ctx, *, msg=None):
    if not msg: await bot.say("Tag a user please")
    if '@here' in msg or '@everyone' in msg:
      return
    else: await bot.say('Host your bot on heroku. Check: https://www.youtube.com/watch?v=avEgttTLZgo' + msg)
    return

@bot.command(pass_context=True)
async def unverify(ctx):
    await bot.delete_message(ctx.message)
    role = discord.utils.get(ctx.message.server.roles, name='Unverified')
    await bot.add_roles(ctx.message.author, role)
    
@bot.command(pass_context=True)
async def verify(ctx):
    if ctx.message.author.bot:
      return
    else:
      await bot.delete_message(ctx.message)
      role = discord.utils.get(ctx.message.server.roles, name='Verified')
      await bot.add_roles(ctx.message.author, role)
    
@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def friend(ctx, user:discord.Member,):
    if ctx.message.author.bot:
      return
    else:
      await bot.delete_message(ctx.message)
      role = discord.utils.get(ctx.message.server.roles, name='Friend of Owner')
      await bot.add_roles(ctx.message.mentions[0], role)

@bot.command(pass_context = True)
@commands.has_permissions(administrator=True)     
async def makemod(ctx, user: discord.Member):
    nickname = '♏' + user.name
    await bot.change_nickname(user, nickname=nickname)
    role = discord.utils.get(ctx.message.server.roles, name='Moderator')
    await bot.add_roles(user, role)
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_author(name='Congratulations Message')
    embed.add_field(name = '__Congratulations__',value ='**Congratulations for mod.Hope you will be more active here. Thanks for your help and support.**',inline = False)
    embed.set_image(url = 'https://preview.ibb.co/i1izTz/ezgif_5_e20b665628.gif')
    await bot.send_message(user,embed=embed)
    await bot.delete_message(ctx.message)
    
@bot.command(pass_context = True)
@commands.has_permissions(administrator=True)     
async def removemod(ctx, user: discord.Member):
    nickname = user.name
    await bot.change_nickname(user, nickname=nickname)
    role = discord.utils.get(ctx.message.server.roles, name='Moderator')
    await bot.remove_roles(user, role)
    await bot.delete_message(ctx.message)

@bot.command(pass_context = True)
async def botwarncode(ctx):
    await bot.say('https://hastebin.com/ibogudoxot.py')
    return

@bot.command(pass_context=True)
async def guess(ctx, number):
    try:
        arg = random.randint(1, 10)
    except ValueError:
        await bot.say("Invalid number")
    else:
        await bot.say('The correct answer is ' + str(arg))

@bot.command(pass_context=True)
@commands.has_permissions(kick_members=True) 
async def roles(context):
	"""Displays all of the roles with their ids"""
	roles = context.message.server.roles
	result = "The roles are "
	for role in roles:
		result += '``' + role.name + '``' + ": " + '``' + role.id + '``' + "\n "
	await bot.say(result)
    
@bot.command(pass_context=True, aliases=['server'])
@commands.has_permissions(kick_members=True)
async def membercount(ctx, *args):
    if ctx.message.channel.is_private:
        await bot.delete_message(ctx.message)
        return

    g = ctx.message.server

    gid = g.id
    membs = str(len(g.members))
    membs_on = str(len([m for m in g.members if not m.status == Status.offline]))
    users = str(len([m for m in g.members if not m.bot]))
    users_on = str(len([m for m in g.members if not m.bot and not m.status == Status.offline]))
    bots = str(len([m for m in g.members if m.bot]))
    bots_on = str(len([m for m in g.members if m.bot and not m.status == Status.offline]))
    created = str(g.created_at)
    
    em = Embed(title="Membercount")
    em.description =    "```\n" \
                        "Members:   %s (%s)\n" \
                        "  Users:   %s (%s)\n" \
                        "  Bots:    %s (%s)\n" \
                        "Created:   %s\n" \
                        "```" % (membs, membs_on, users, users_on, bots, bots_on, created)

    await bot.send_message(ctx.message.channel, embed=em)
    await bot.delete_message(ctx.message)	
@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def embed(ctx, *args):
    if ctx.message.author.bot:
      return
    else:
      argstr = " ".join(args)
      r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
      text = argstr
      color = discord.Color((r << 16) + (g << 8) + b)
      await bot.send_message(ctx.message.channel, embed=Embed(color = color, description=text))
      await bot.delete_message(ctx.message)    

bot.run('NTMxMTY0MDUzMjg5MzA0MDc0.XKTKKQ.pYCq2t0dl8-t8sFm5R51CxBTue8')
