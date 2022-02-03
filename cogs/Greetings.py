from discord.ext import commands
import discord


class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send('Welcome {0.mention}.'.format(member))

    @commands.command()
    async def hello(self, ctx, *, member: discord.Member = None):
        """Says hello"""
        member = member or ctx.author
        if self._last_member is None or self._last_member.id != member.id:
            await ctx.send('Hello {0.name}~'.format(member))
        else:
            await ctx.send('Hello {0.name}... This feels familiar.'.format(member))
        self._last_member = member
        await ctx.send(f"{1/0}")
    @hello.error
    async def example_error(self, ctx: commands.Context, error: commands.CommandError):
        """Handle errors for the example command."""
        
        await ctx.send('Error: {}'.format(error))

def setup(bot:commands.Bot):
    bot.add_cog(Greetings(bot))
