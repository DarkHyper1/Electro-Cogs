import discord
try:
    import MySQLdb
    MySQLdb_available = True
except:
    MySQLdb_available = False
from discord.ext import commands
from cogs.utils import checks

class dankmemes:
    """Dem Gosh Darn Dank Memes"""

    def __init__(self, bot):
        self.bot = bot
   

    @commands.command()
    async def dankmemes(self):
        """Grab The Newest Dank Meme!"""



        db = MySQLdb.connect(host="mysql.theendlessweb.com",    # your host, usually localhost
                     user="electrom_dankmemesuser",         # your username
                     passwd="DankMemes",  # your password
                     db="electrom_dankmemes")
        cur = db.cursor()
        cur.execute("SELECT link from stuff ORDER BY id desc LIMIT 1")
        newmsg = cur.fetchall()
        printout = str(newmsg) [3:-5]
        await self.bot.say(printout) 
        db.close()
        
    @commands.command()
    async def submitmemes(self, link):
        """Submit memes. Or Dank ones."""
        
        
         
        db = MySQLdb.connect(host="mysql.theendlessweb.com",    # your host, usually localhost
                     user="electrom_dankmemesuser",         # your username
                     passwd="DankMemes",  # your password
                     db="electrom_dankmemes")
        cur = db.cursor()
        cur.execute("INSERT INTO stuff (link) VALUES (\"{}\")".format(link))
        db.commit()
        await self.bot.say("Your Meme has been Submitted!")
        db.close()
        
    @commands.command()
    @checks.admin()
    async def graballmemes(self):
        """An Admin Command to grab all memes and IDs to remove them"""
        
        
         
        db = MySQLdb.connect(host="mysql.theendlessweb.com",    # your host, usually localhost
                     user="electrom_dankmemesuser",         # your username
                     passwd="DankMemes",  # your password
                     db="electrom_dankmemes")
                     
        cur = db.cursor()
        cur.execute("SELECT link, id from stuff ORDER BY id desc")
        msg = cur.fetchall()
        await self.bot.say(msg)
        db.close()
        
    @commands.command()
    @checks.admin()
    async def deletememe(self, id):
        """Delete a meme based on ID"""
        
        
         
        db = MySQLdb.connect(host="mysql.theendlessweb.com",    # your host, usually localhost
                     user="electrom_dankmemesuser",         # your username
                     passwd="DankMemes",  # your password
                     db="electrom_dankmemes")
                     
        cur = db.cursor()
        cur.execute("DELETE FROM stuff WHERE id=\"{}\";".format(id))
        db.commit()
        await self.bot.say("Meme Deleted")
        db.close()
        
    @commands.command()
    @checks.admin()
    async def editmemeid(self, oldid, newid):
        """Change the ID of a Meme to make it first"""
        
        
         
        db = MySQLdb.connect(host="mysql.theendlessweb.com",    # your host, usually localhost
                     user="electrom_dankmemesuser",         # your username
                     passwd="DankMemes",  # your password
                     db="electrom_dankmemes")
                     
        cur = db.cursor()
        cur.execute("UPDATE stuff SET id = \"{}\" WHERE id = \"{}\"".format(newid, oldid))
        db.commit()
        await self.bot.say("Meme has been updated")
        db.close()
    
        

def setup(bot):
    if MySQLdb_available is False:
        raise RuntimeError("You don't have MySQLdb installed.")
        return
    bot.add_cog(dankmemes(bot))

