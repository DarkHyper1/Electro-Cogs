import discord
from discord.ext import commands

class simplepoll:
    """A Simple Poll System Using Reactions"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def startpoll(self, question):
        """Starts a poll"""

        #Your code will go here
        message = await self.bot.say("POLL: {}".format(question))
        await self.bot.add_reaction(message,"\N{REGIONAL INDICATOR SYMBOL LETTER N}")

def setup(bot):
    bot.add_cog(simplepoll(bot))
