import discord
from discord.ext import commands


class Moderation(commands.Cog):
    def __init__(self, client) -> None:
        self.client = client
        self.last_member = None

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=5):
        await ctx.channel.purge(limit=amount + 1)

