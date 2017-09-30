import discord
from discord.ext import commands

class halflife:
    """If Someone Says Half-Life, They Must Be Punished"""
    
    def __init__(self, bot):
        self.bot = bot
        self.number = 2017
    @commands.command()
    async def halflife(self):
        """Punish a User for Saying Half-Life"""
        
         
        self.number = self.number + 1
        await self.bot.say("You have mentioned Half-Life 3 or a game set in the Half-Life Universe, and as such have delayed the game by a year.")
        await self.bot.say("The game will now be released on January 18, {}".format(self.number))

def setup(bot):
    bot.add_cog(halflife(bot))
