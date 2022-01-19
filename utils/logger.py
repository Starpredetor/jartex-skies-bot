import discord
from discord.ext import commands
import datetime as dt


class Logs(commands.Cog):
    def __init__(self, client)-> None:
        self.client=client

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        author = message.author
        channel = self.client.get_channel(927294831108186122)
        logs_embed = discord.Embed(title="**Message Deleted**", color=0xffff00)
        logs_embed.set_author(name=author.name,icon_url=author.avatar_url)
        logs_embed.add_field(name=f"**Message deleted in**", value=channel.name, inline=False)
        logs_embed.add_field(name="**Message**", value=message.content, inline=False)
        logs_embed.timestamp = dt.datetime.now()
        await channel.send(embed=logs_embed)
    @commands.Cog.listener()
    async def on_message_edit(self, prev_message, new_message):
        author = prev_message.author
        channel = self.client.get_channel(927294831108186122)
        logs_embed = discord.Embed(title="**Message Edited**", color=0xffff00)
        logs_embed.set_author(name=author.name,icon_url=author.avatar_url)
        logs_embed.add_field(name=f"**Message edited in**", value=channel.name, inline=False)
        logs_embed.add_field(name="**Previous Message**", value=prev_message.content, inline=False)
        logs_embed.add_field(name="**New Message**", value=new_message.content, inline=False)
        logs_embed.timestamp = dt.datetime.now()
        await channel.send(embed=logs_embed)

    

    
    