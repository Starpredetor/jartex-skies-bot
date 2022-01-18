import discord
from discord.ext import commands
import os
from os import listdir
from ruamel.yaml import YAML
from dotenv import load_dotenv

from Commands.giveaway import giveaway


load_dotenv()


client = commands.Bot(command_prefix="?")
client.remove_command('help')

def convert(time):
    pos = ["s", "m", "h", "d", "w"]
    time_dict = {"s": 1, "m": 60, "h": 3600, "d": 3600 * 24, "w": 3600 * 24 * 7}
    unit = time[-1]

    if unit not in pos:
        return -1
    try:
        val = int(time[:-1])
    except:
        return -2

    return val * time_dict[unit]
TOKEN = os.getenv("TOKEN")


    
@client.event
async def on_ready():
    print('------')
    print('Online! Details:')
    print(f"Bot Username: {client.user.name}")
    print(f"BotID: {client.user.id}")
    print('------')
    client.add_cog(giveaway(client))

@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount + 1)

client.run(TOKEN)
