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
        await self.bot.add_reaction(question, <:regional_indicator_n:360581436379627542>)

def setup(bot):
    bot.add_cog(Mycog(bot))
