import discord
try:
    import MySQLdb
    MySQLdb_available = True
except:
    MySQLdb_available = False
from discord.ext import commands
from cogs.utils import checks

class mcrecipe:
    """Dem Gosh Darn Dank Memes"""

    def __init__(self, bot):
        self.bot = bot
   

    @commands.command(pass_context=True)
    async def getrecipe(self, ctx, *, item):
        """Send a recipe in chat"""



        db = MySQLdb.connect(host="mysql.theendlessweb.com",    # your host, usually localhost
                     user="electrom_dankmemesuser",         # your username
                     passwd="DankMemes",  # your password
                     db="electrom_dankmemes")
        cur = db.cursor()
      
        db.close()
def setup(bot):
    bot.add_cog(mcrecipe(bot))
