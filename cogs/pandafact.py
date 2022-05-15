import discord
from discord.ext import commands
import requests
import json

class pandafact(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    # Define joke command
    @commands.command()
    async def pandafact(self, ctx):
       await ctx.send("Holdon a second...")
       # Get a joke
       fact = json.loads(requests.get('https://some-random-api.ml/facts/panda').text)['fact']
       await ctx.reply(fact)
