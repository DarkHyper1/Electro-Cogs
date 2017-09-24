import discord
from discord.ext import commands
from raven import Client
from cogs.utils import checks

class reporterror:
    """A cog that sends errors to Electromaster. You may not use without permission (it wont work)!"""

    def __init__(self, bot):
        self.bot = bot
        
        
         
    @checks.mod()
    @commands.command(pass_context=True)
    async def senderror(self, ctx, *, errormessage):
        """Send's the error!"""
        
        
         
        client = Client('')
        channel = ctx.message.channel
        sender = ctx.message.author.display_name
        server = ctx.message.server.name
        strchannel = str(channel)
        strsender = str(sender)
        strserver = str(server)
        
        await self.bot.say("Processing Report")
        client.captureMessage("User " + strsender + " Has sent an error from the server " + strserver + ", in the channel " + strchannel + ". Their message: " + errormessage)
        await self.bot.say("Message Sent!")

def setup(bot):
    bot.add_cog(reporterror(bot))
