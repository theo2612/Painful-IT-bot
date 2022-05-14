import discord
from discord.ext import commands
from secret import secret

bot = commands.Bot(command_prefix='p!')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

bot.run(secret)
