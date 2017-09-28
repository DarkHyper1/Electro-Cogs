import discord
from discord.ext import commands

class UGReport:
    """Report Users"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def report(self, player, *, reason):
        """Report a user. Please provide evidence."""


        
        
        await self.bot.say("Your report againist " + player + " Has been created.")
        await self.bot.send_message(self.bot.get_channel('361734544971268109'), "A Report has been filed! \n User: " + player "\n Reason: " + reason)

def setup(bot):
    bot.add_cog(UGReport(bot))
