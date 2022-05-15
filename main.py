# Import main discord library
import discord
from discord.ext import commands

# Import secret from secret.py
from secret import secret

# Import configs
from config import *

# Import cogs
from cogs.ping import ping
from cogs.help import help
from cogs.joke import joke
from cogs.pandafact import pandafact

# Create bot and remove the help command since we will make our own
bot = commands.Bot(command_prefix=prefix, help_command=None)

# Run after bot is ready
@bot.event
async def on_ready():
    # Change discord presence and print message
    await bot.change_presence(activity=discord.Game(f"My prefix is {prefix}"))
    print("I'm up and running!")

# Add ping cog
bot.add_cog(ping(bot))

# Add help cog
bot.add_cog(help(bot))

# Add joke cog
bot.add_cog(joke(bot))

# Add pandafact cog
bot.add_cog(pandafact(bot))

# Run bot with specified secret
bot.run(secret)
