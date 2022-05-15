import discord
from discord.ext import commands
from secret import secret
from cogs.ping import ping
from config import *

bot = commands.Bot(command_prefix=prefix)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(f"My prefix is {prefix}"))
    print("I'm up and running!")

bot.add_cog(ping(bot))

bot.run(secret)
