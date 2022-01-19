from discord.ext import commands
import os
from dotenv import load_dotenv
from Commands.giveaway import Giveaway
from Commands.moderation import Moderation
from utils.logger import Logs


load_dotenv()


client = commands.Bot(command_prefix="?")
client.remove_command('help')


TOKEN = os.getenv("TOKEN")


    
@client.event
async def on_ready():
    print('------')
    print('Online! Details:')
    print(f"Bot Username: {client.user.name}")
    print(f"BotID: {client.user.id}")
    print('------')
    client.add_cog(Giveaway(client))
    client.add_cog(Moderation(client))
    client.add_cog(Logs(client))



client.run(TOKEN)
