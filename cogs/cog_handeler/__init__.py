from .cog import cog_handeler
def setup(bot):
    bot.add_cog(cog_handeler(bot))
