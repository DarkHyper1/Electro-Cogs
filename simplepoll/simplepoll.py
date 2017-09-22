import discord
from discord.ext import commands

class simplepoll:
    """A Simple Poll System Using Reactions"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def startpoll(self, *, question):
        """Starts a poll"""

        #Your code will go here
        message = await self.bot.say("POLL: {}".format(question))
        await self.bot.add_reaction(message,"\N{REGIONAL INDICATOR SYMBOL LETTER N}")
        await self.bot.add_reaction(message,"\N{REGIONAL INDICATOR SYMBOL LETTER Y}")
        
    @commands.command(pass_context=True)    
    async def endpoll(self, ctx, pollid):
        """Ends a poll"""
        #les do this
        channel = ctx.message.channel
        message = await self.bot.get_message(channel, pollid)
        reaction = discord.utils.get(message.reactions, emoji="\N{REGIONAL INDICATOR SYMBOL LETTER N}")
        reaction2 = discord.utils.get(message.reactions, emoji="\N{REGIONAL INDICATOR SYMBOL LETTER Y}")
        react1count = self.reaction.count(reaction)
        react2count = self.reaction.count(reaction2)
        if (reaction1 > reaction2):
            await self.bot.say("The Poll has ended! The users have chosen NO!")
        else:
            await self.bot.say("The Poll has ended! The users have chosen YES!")

def setup(bot):
    bot.add_cog(simplepoll(bot))
