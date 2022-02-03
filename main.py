import discord
from discord.ext import commands
from decouple import config

from backend import backend



database=backend.storage("main")

bot = commands.Bot(command_prefix=database.get_prefix)
bot.load_extension("cogs.General")

bot.run(config('DISCORD_API_KEY'))
                
@bot.event
async def on_ready():
    print("Bot is ready, with prefix: "+bot.command_prefix)