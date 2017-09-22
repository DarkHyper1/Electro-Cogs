from discord.ext import commands


class simplepoll:
    """A Simple Poll System Using Reactions"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def startpoll(self, *, question, channel):
        """Starts a poll"""

        # Your code will go here
        message = await self.bot.send_message(self.bot.get_channel(channel), question)
        await self.bot.add_reaction(message, "\N{REGIONAL INDICATOR SYMBOL LETTER N}")
        await self.bot.add_reaction(message, "\N{REGIONAL INDICATOR SYMBOL LETTER Y}")
        

    @commands.command(pass_context=True)
    async def endpoll(self, ctx, pollid):
        """Ends a poll"""
        # les do this
        channel = ctx.message.channel
        message = await self.bot.get_message(channel, pollid)
        reactions = [x.count for x in message.reactions]
        if reactions[0] > reactions[1]:
            await self.bot.say("The Poll has ended! The users have chosen NO!")
        else:
            await self.bot.say("The Poll has ended! The users have chosen YES!")


def setup(bot):
    bot.add_cog(simplepoll(bot))
