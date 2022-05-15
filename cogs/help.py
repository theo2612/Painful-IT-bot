import discord
from discord.ext import commands
from config import help_message

class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    # Define help command
    @commands.command()
    async def help(self, ctx):
        # Reply to the message with the help message
        await ctx.reply(help_message)