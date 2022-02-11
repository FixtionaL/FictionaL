from discord.ext import commands
from backend import backend

class cog_handeler(commands.Cog):
    def __init__(self,bot):
        self.bot=bot
        self.database=backend.storage("cog_handler")

        cogs=self.database.get_cog_list()
        print(cogs)
        self.loaded_cogs={}
        self.available_cogs={}
        for i in cogs:
            self.available_cogs[i]=cogs[i][0]
            if cogs[i][1]:
                self.loaded_cogs[i]=cogs[i][0]
                if "cog_handeler"!=i:
                    self.bot.load_extension(cogs[i][0])
        
        

    
    # @commands.is_owner()
    @commands.group()
    async def cog(self,ctx):
        """command to maintain cogs"""
        if ctx.invoked_subcommand is None:
            await ctx.send_help(ctx.command)
    
    @cog.command()
    async def add(self,ctx,cog_name:str):
        if cog_name in self.available_cogs:
            self.bot.load_extension(self.available_cogs[cog_name])
            self.database.update_cog_list(cog_name,True)
        else:
            try:
                self.bot.load_extension(f"cogs.{cog_name}")
                self.bot.remove_cog(f"{cog_name}")
            except commands.ExtensionAlreadyLoaded:
                await ctx.send("Cog is loaded")
            except commands.ExtensionNotFound:
                await ctx.send("Cog not found")
            
            self.database.add_cog_to_list(f"cogs.{cog_name}")
            await ctx.send(f"Cog {cog_name} added")


    async def add_cog(self,ctx,cog:str):
      self.bot.load_extension(f"cogs.{cog}")
      self.database.add_cog_to_list(f"cogs.{cog}")
      await ctx.send(f"Cog {cog} added")

    # @commands.command()
    async def remove_cog(self,ctx,cog:str):
        self.bot.remove_cog(cog)
        self.database.remove_cog_from_list(f"cogs.{cog}")
        await ctx.send(f"Cog {cog} removed")

    # @commands.command()
    async def reload_cog(self,ctx,cog:str):
        self.bot.reload_extension(cog)
        await ctx.send(f"Cog {cog} reloaded")
    
    # @commands.command()
    async def cogs(self,ctx):
      await ctx.send(self.bot.cogs)
    
