import discord
from discord.ext import commands
import requests
import json

class joke(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    # Define joke command
    @commands.command()
    async def joke(self, ctx):
       # Get a joke
       joke = json.loads(requests.get('https://some-random-api.ml/joke').text)['joke']
       await ctx.reply(joke)
