# 921402724493443142 client
# OTIxNDAyNzI0NDkzNDQzMTQy.YbyZKA.C7UkZAKwkJt-oa5TdL-kGmHfk2w token
# 190528

import discord
from discord.utils import get
from discord.ext import commands
from datetime import datetime, timedelta
import itertools
from song import songAPI

# wrapper / decorator

message_lastseen = datetime.now()
message2_lastseen = datetime.now()

bot = commands.Bot(command_prefix='!',help_command=None)

songsInstance = songAPI()

@bot.event
async def on_ready():
    print(f"logged in as{bot.user}")

@bot.command()
async def test(ctx, *, par):
    await ctx.channel.send("You typed {0}".format(par))

@bot.command()
async def help(ctx):
    # help
    # test
    # send
    emBed = discord.Embed(title="Tutorial Bot help", description="All available bot commands", color=0x42f5a7)
    emBed.add_field(name="help", value="Get help command", inline=True)
    emBed.add_field(name="test", value="Respond message that you've send", inline=True)
    emBed.add_field(name="send", value="Send hello message to user", inline=True)
    emBed.set_thumbnail(url='https://www.darkcarnival.co.za/wp-content/uploads/2018/08/discord-logo.jpg')
    emBed.set_footer(text='test footer', icon_url='https://www.darkcarnival.co.za/wp-content/uploads/2018/08/discord-logo.jpg')
    await ctx.channel.send(embed=emBed)

@bot.command()
async def send(ctx):
    print(ctx.channel)
    await ctx.channel.send('Hello')

@bot.event
async def on_message(message):
    global message_lastseen, message2_lastseen
    if  message.content == '!user':
        await message.channel.send('Hello ' + str(message.author.name))    
    elif message.content == 'คุณชื่ออะไรหรอ' and datetime.now() >= message_lastseen:
        message_lastseen = datetime.now() + timedelta(seconds=5)
        await message.channel.send('ฉันชื่อ ' + str(bot.user.name))
        #loging
        print('{0} เรียกใช้ คุณชื่ออะไรหรอ ตอน {1} และจะเรียกใช้อีกทีตอน {2}'.format(message.author.name,datetime.now(),message_lastseen))
    elif message.content == 'ผมชื่ออะไรครับ' and datetime.now() >= message2_lastseen:
        message2_lastseen = datetime.now() + timedelta(seconds=5)
        await message.channel.send('คุณชื่อ ' + str(message.author.name))
    elif message.content == '!logout':
        await bot.logout()
    await bot.process_commands(message)

@bot.command()
async def play(ctx,* , search: str):
    await songsInstance.play(ctx,search)

@bot.command()
async def stop(ctx):
    await songsInstance.stop(ctx)

@bot.command()
async def pause(ctx):
    await songsInstance.pause(ctx)

@bot.command()
async def resume(ctx):
    await songsInstance.resume(ctx)

@bot.command()
async def leave(ctx):
    await songsInstance.leave(ctx)

@bot.command()
async def queueList(ctx):
    await songsInstance.queueList(ctx)

@bot.command()
async def skip(ctx):
   await songsInstance.skip(ctx)

bot.run('OTIxNDAyNzI0NDkzNDQzMTQy.YbyZKA.C7UkZAKwkJt-oa5TdL-kGmHfk2w')