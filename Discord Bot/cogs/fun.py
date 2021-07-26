import discord
import random
from discord.ext import commands

class Fun(commands.Cog):

    def __init__(self,client):
        self.client=client

    @commands.command()
    async def quality(self,ctx,*,name):
        responses=['intelligent','dumbfuck','sexy','noob','chilli chicken']
        await ctx.send(f'{name} is {random.choice(responses)}')


def setup(client):
    client.add_cog(Fun(client)) 