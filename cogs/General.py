from ast import alias
from discord.ext import commands
import discord
from backend import backend

class General(commands.Cog):
    
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def ping(self,ctx):
      await ctx.send("pong")
    @commands.command()
    
    async def prefix(self,ctx,prefix:str):
        database=backend.storage("main")
        database.set_prefix(prefix,ctx.guild.id)
        self.bot.command_prefix=prefix
        await ctx.send("prefix set to "+prefix)
    @commands.command()
    async def bye(self,ctx,number:int):
      await ctx.send(number+1)
    
    @commands.command(alias=['shut'])
    async def shutdown(self,ctx):
      await ctx.send("Shutting down")
      await self.bot.close()

    @commands.command()
    async def add_cog(self,ctx,cog:str):
      self.bot.load_extension(f"cogs.{cog}")
      await ctx.send(f"Cog {cog} added")

    @commands.command()
    async def remove_cog(self,ctx,cog:str):
        self.bot.remove_cog(cog)
        await ctx.send(f"Cog {cog} removed")

    @commands.command()
    async def reload_cog(self,ctx,cog:str):
        self.bot.reload_extension(cog)
        await ctx.send(f"Cog {cog} reloaded")
    
    @commands.command()
    async def cogs(self,ctx):
      await ctx.send(self.bot.cogs)



def setup(bot:commands.Bot):
    bot.add_cog(General(bot))