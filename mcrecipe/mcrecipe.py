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
    async def tempgetrecipe(self, ctx, item):
        """Send a recipe in chat"""


        
        authorobj = ctx.message.author.mention
        author = str(authorobj)
        
        if "helmet" in item or "sword" in item or "chestplate" in item or "leggings" in item or "boots" in item:
            itemfull = "http://www.minecraftcrafting.info/imgs/craft_" + item + ".gif"
            embed=discord.Embed(title="Recipe", description="Your Requested Recipe", color=0xce0000)
            embed.set_author(name="DJ ElectroBOT")
            embed.add_field(name="User:", value=author, inline=False)
            embed.add_field(name="Recipe:", value=itemfull, inline=False)     
            embed.set_footer(text="Made with love by DJ Electro")
            await self.bot.say(embed=embed)
            await self.bot.say(itemfull)
            
        else:    
            itemfull = "http://www.minecraftcrafting.info/imgs/craft_" + item + ".png"
            embed=discord.Embed(title="Recipe", description="Your Requested Recipe", color=0xce0000)
            embed.set_author(name="DJ ElectroBOT")
            embed.add_field(name="User:", value=author, inline=False)
            embed.add_field(name="Recipe:", value=itemfull, inline=False)     
            embed.set_footer(text="Made with love by DJ Electro")
            await self.bot.say(embed=embed)
            await self.bot.say(itemfull)
   

    @commands.command()
    async def addrecipe(self, item, piclink):
          """Adds a recipe"""
         
        db = MySQLdb.connect(host="mysql.theendlessweb.com",    # your host, usually localhost
                       user="electrom_dankmemesuser",         # your username
                       passwd="DankMemes",  # your password
                       db="electrom_dankmemes")
        cur = db.cursor()
        cur.execute("INSERT INTO recipes {item,itemlink}" + " VALUES (\"{}\", \"{}\");".format(item, piclink))        
        db.commit()
        await self.bot.say("Added")
        db.close()
          
def setup(bot):
    bot.add_cog(mcrecipe(bot))
