import discord
import urllib, urllib.request
from xml.dom import minidom
    
from discord.ext import commands

class ArxivAPI(commands.Cog):
    def __init__(self,client):
        self.client=client

    @commands.command()
    async def arxivshow(self,ctx,*,search):
        query=search.replace(" ", "+")
        url = f'http://export.arxiv.org/api/query?search_query=all:{query}&start=0&max_results=2'
        data = urllib.request.urlopen(url)
        mytree=minidom.parseString(data.read().decode('utf-8'))
        published=mytree.getElementsByTagName('published')[0]
        summary=mytree.getElementsByTagName('summary')[0]
        title=mytree.getElementsByTagName('title')[1]
        link=mytree.getElementsByTagName('link')[1]
        author=mytree.getElementsByTagName('author')
        await ctx.send(f'Published on: {published.firstChild.data}')
        await ctx.send(f'Title: {title.firstChild.data}')
        for x in author:
            a_name=x.getElementsByTagName('name')[0]
            await ctx.send(f'Author: {a_name.firstChild.data}')
        await ctx.send(f'Summary:{summary.firstChild.data}')
        link1=link.attributes['href'].value
        await ctx.send(f'Link: {link1}')
        

def setup(client):
    client.add_cog(ArxivAPI(client)) 