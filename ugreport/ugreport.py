import discord
from discord.ext import commands

class UGReport:
    """Report Users"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def report(self, ctx, player, *, reason):
        """Report a user. Please provide evidence."""


        
        author = ctx.message.author
        await self.bot.say("Your report againist " + player + " Has been created.")
        await self.bot.send_message(self.bot.get_channel('361734544971268109'), "A Report has been filed! \n User: " + player + "\n Reason: " + reason + "\n Reported by: " + author)

def setup(bot):
    bot.add_cog(UGReport(bot))
