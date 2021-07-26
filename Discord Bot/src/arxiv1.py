import discord
import urllib, urllib.request
from xml.dom import minidom
    
from discord.ext import commands

class ArxivAPItest(commands.Cog):
    def __init__(self,client):
        self.client=client

    @commands.command()
    async def arxivs(self,ctx,*,search):
        query=search.replace(" ", "+")
        url = f'http://export.arxiv.org/api/query?search_query=all:{query}&start=0&max_results=2'
        data = urllib.request.urlopen(url)
        mytree=minidom.parseString(data.read().decode('utf-8'))
        entry=mytree.getElementsByTagName('entry')
        for y in entry:
            published=y.getElementsByTagName('published')[0]
            summary=y.getElementsByTagName('summary')[0]
            title=y.getElementsByTagName('title')[1]
            link=y.getElementsByTagName('link')[1]
            author=y.getElementsByTagName('author')
            await ctx.send(f'Published on: {published.firstChild.data}')
            await ctx.send(f'Title: {title.firstChild.data}')
            for x in author:
                a_name=x.getElementsByTagName('name')[0]
                await ctx.send(f'Author: {a_name.firstChild.data}')
            await ctx.send(f'Summary:{summary.firstChild.data}')
            link1=link.attributes['href'].value
            await ctx.send(f'Link: {link1}')
            await ctx.send('\n\n')

def setup(client):
    client.add_cog(ArxivAPItest(client)) 