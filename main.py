import discord
from discord.ext import commands
from decouple import config
#import Greetings


bot = commands.Bot(command_prefix="^")
todo_list = []
class todo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @bot.group()
    async def todo(ctx):
        pass

    @todo.command()
    async def add(ctx,*,todo:str):
        todo_list.append(todo)
        await ctx.send("Sucessfully added a todo to the bot")

    @todo.command()
    async def list(ctx):
        emb = discord.Embed(title="My todo List")
    
        final_string = ""
        for ind in range(len(todo_list)):
            final_string+= f"{ind+1}. {todo_list[ind]}\n"

        emb.description = final_string
        await ctx.send(embed=emb)

    @todo.command()
    async def remove(ctx,index:int):
        todo_removed = todo_list[index-1]
        todo_list.pop(index-1)
        await ctx.send(f"Removed todo {todo_removed}")

@bot.command()
async def ping(ctx):
  await ctx.send("pong")



@bot.command()
async def bye(ctx,number:int):
  await ctx.send(number+1)
 
@bot.command()
async def shutdown(ctx):
  await ctx.send("Shutting down")
  await bot.close()
@bot.command()
async def add_cog(ctx,cog:str):
  bot.add_cog(todo(bot))
  await ctx.send(f"Cog {cog} added")

@bot.command()
async def remove_cog(ctx,cog:str):
    bot.remove_cog(cog)
    await ctx.send(f"Cog {cog} removed")



bot.run(config('DISCORD_API_KEY'))