import discord
from discord.ext import commands
from decouple import config
from backend import backend



database=backend.storage("main")

bot = commands.Bot(command_prefix=database.get_prefix)
@bot.event
async def on_ready():
    print("Bot is ready, with prefix: --")

bot.load_extension("cogs.cog_handeler")

bot.run(config('DISCORD_API_KEY'))
                
