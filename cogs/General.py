from ast import alias
from discord.ext import commands
import discord
from backend import backend


class General(commands.Cog):
    
    def __init__(self,bot):
        self.bot = bot
        self.database=backend.storage("main")

    @commands.command()
    async def ping(self,ctx):
      await ctx.send("pong")
    @commands.command()
    
    async def prefix(self,ctx,prefix:str):
        if ctx.guild is None:
            self.database.set_prefix("no_guild",prefix)
        else:
            self.database.set_prefix(ctx.guild.id,prefix)
        await ctx.send("prefix set to "+prefix)
    @commands.command()
    async def bye(self,ctx,number:int):
      await ctx.send(number+1)
    
    @commands.command(alias=['shut'])
    async def shutdown(self,ctx):
      await ctx.send("Shutting down")
      await self.bot.close()




def setup(bot:commands.Bot):
    bot.add_cog(General(bot))