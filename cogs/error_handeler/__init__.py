from .error_handeler import Error_handeler

def setup(bot):
    
    bot.add_cog(Error_handeler(bot))