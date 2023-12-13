import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command()
async def start(ctx):
  await ctx.send(f'Привет! Я специальный бот-помощник, который поможет тебе с правильной сортировкой мусора. У меня есть несколько функций. Напиши $help_, чтобы узнать о них.')

@bot.command()
async def help_(ctx):
  await ctx.send(f'Напиши $info для того, чтобы я рассказал тебе типы мусора перерабатываются в нашей стране. Напиши $photo, чтобы я показал тебе, как выглядит значок переработки.')

@bot.command()
async def info(ctx):
  with open('images/info.jpeg', 'rb') as f:
        picture = discord.File(f)
  await ctx.send(file=picture)

@bot.command()
async def photo(ctx):
  with open('photos/photo.jpg', 'rb') as f:
        picture = discord.File(f)
  await ctx.send(file=picture)

@bot.command()
async def main(ctx, n:int):
  if message.content <= 10:
    await message.channel.send(f'Это пластик')
  if message.content > 10 and message.content <= 20:
    await message.channel.send(f'Это cтекло')
  if message.content > 20 and message.content <= 30:
    await message.channel.send(f'Это металл')  
  

bot.run('MTExNzg1NzY5MTMxOTE0MDM1Mg.G42OCA.vhtmVZDKaPwygGmlKndp_ZW2GHB25R_JTR-R54')



  


