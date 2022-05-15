import discord
from discord.ext import commands

class ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    # Define ping command
    @commands.command()
    async def ping(self, ctx):
        # Reply to the message with "pong!"
        await ctx.reply("pong!")