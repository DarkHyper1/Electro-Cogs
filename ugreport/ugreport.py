import discord
from discord.ext import commands

class UGReport:
    """Report Users"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def report(self, ctx, player, *, reason):
        """Report a user. Please provide evidence."""


        
        authorobj = ctx.message.author
        author = str(authorobj)
        embed=discord.Embed(title="Report:", description="A Report has been filed!")
        embed.set_author(name="DJ ElectroBOT Report System")
        embed.add_field(name="User:", value=player, inline=False)
        embed.add_field(name="Reason:", value=reason, inline=False)
        embed.add_field(name="Reported By:", value=author, inline=True)
        embed.set_footer(text="Created with love by DJ Electro")
        await self.bot.say("Your report againist " + player + " Has been created.")
        await self.bot.send_message(self.bot.get_channel('361734544971268109'), embed=embed)
        

def setup(bot):
    bot.add_cog(UGReport(bot))
