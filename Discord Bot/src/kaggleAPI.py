import discord
import kaggle
import requests
from discord.ext import commands

class KaggleAPI(commands.Cog):
    def __init__(self,client):
        self.client=client

    @commands.command()
    async def list(self,ctx):
        lists=kaggle.competition.download
        await ctx.send(lists)


def setup(client):
    client.add_cog(KaggleAPI(client)) 
