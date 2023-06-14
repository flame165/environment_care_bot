
import discord
from discord.ext import commands
import random, os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$',intents=intents)

@bot.event
async def on_ready():
    print('BOT TELAH SIAP')

@bot.command()
async def idesampah(ctx):
    img_name = random.choice(os.lisdir('code/kerajinan'))
    with open(f'code/kerajinan/{img_name}','rb') as gambar:
        picture = discord.File(gambar)
    await ctx.send(picture)

bot.run('your token here')
