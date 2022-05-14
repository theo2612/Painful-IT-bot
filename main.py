import discord
from discord.ext import commands
from secret import secret

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='p!', intents=intents)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

bot.run(secret)