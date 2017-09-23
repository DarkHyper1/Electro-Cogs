import discord
from discord.ext import commands
from raven import Client
from cogs.utils import checks

class reporterror:
    """A Cog to report errors to me. You may not use without permission (it wont work!)!"""

    def __init__(self, bot):
        self.bot = bot
        
        
    @checks.mod()
    @commands.command(pass_context=True)
    async def reporterror(self, ctx, *, errormessage):
        """This does stuff!"""
        client = Client('')
        channel = ctx.message.channel
        sender = ctx.message.author.display_name
        server = ctx.message.server.name
        #Your code will go here
        await self.bot.say("Processing Report")
        client.captureMessage("User " + sender + " Has sent an error from the server " + server + ", in the channel " + channel + ". Their message: " + errormessage)
        await self.bot.say("Message Sent!")

def setup(bot):
    bot.add_cog(reporterror(bot))
