import discord
try:
    import MySQLdb
    MySQLdb_available = True
except:
    MySQLdb_available = False
from discord.ext import commands
from cogs.utils import checks

class mcrecipe:
    """Minecraft Recipe Control System"""

    def __init__(self, bot):
        self.bot = bot
   

    @commands.command(pass_context=True)
    async def getrecipe(self, ctx, item):
        """Send a recipe in chat"""


        
        authorobj = ctx.message.mention
        author = str(authorobj)
        itemfull = "http://www.minecraftcrafting.info/imgs/craft_" + item + ".png"
        embed=discord.Embed(title="Recipe", description="Your Requested Recipe", color=0xce0000)
        embed.set_author(name="DJ ElectroBOT")
        embed.add_field(name="User:", value=author, inline=False)
        embed.add_field(name="Recipe:", value=itemfull, inline=False)     
        embed.set_footer(text="Made with love by DJ Electro")
        await self.bot.say(embed=embed)
   
def setup(bot):
    bot.add_cog(mcrecipe(bot))
