
import discord
import MySQLdb
from discord.ext import commands
from cogs.utils import checks

class dankmemes:
    """Get Curated Spam Delivered Straight to Your Bot!"""

    def __init__(self, bot):
        self.bot = bot
   

    @commands.command()
    async def advice(self):
        """Grab The Newest Advice"""


        #Your code will go here
        db = MySQLdb.connect(host="theendlessweb.com",    # your host, usually localhost
                     user="electrom_dankmemesuser",         # your username
                     passwd="DankMemes",  # your password
                     db="electrom_dankmemes")
        cur = db.cursor()
        cur.execute("SELECT advice from advice ORDER BY id desc LIMIT 1")
        newmsg = cur.fetchall()
        printout = str(newmsg)
        await self.bot.say(printout) 
        db.close()
        
    @commands.command()
    async def submitadvice(self, advice):
        """Submit advice for admins to review. NO LINKS PLEASE"""
        
        
        
        db = MySQLdb.connect(host="theendlessweb.com",    # your host, usually localhost
                     user="electrom_dankmemesuser",         # your username
                     passwd="DankMemes",  # your password
                     db="electrom_dankmemes")
        cur = db.cursor()
        cur.execute("INSERT INTO submitadvice (advice) VALUES (\"{}\")".format(advice))
        db.commit()
        await self.bot.say("Your Advice has been Submitted!")
        db.close()
        
    @commands.command()
    @checks.admin()
    async def graballadvice(self):
        """An Admin Command to grab all memes and IDs to remove them"""
        
        
        
        db = MySQLdb.connect(host="theendlessweb.com",    # your host, usually localhost
                     user="electrom_dankmemesuser",         # your username
                     passwd="DankMemes",  # your password
                     db="electrom_dankmemes")
                     
        cur = db.cursor()
        cur.execute("SELECT advice, id from advice ORDER BY id desc")
        msg = cur.fetchall()
        await self.bot.say(msg)
        db.close()
        
    @commands.command()
    @checks.admin()
    async def deletadvice(self, id):
        """Delete a meme based on ID"""
        
        db = MySQLdb.connect(host="theendlessweb.com",    # your host, usually localhost
                     user="electrom_dankmemesuser",         # your username
                     passwd="DankMemes",  # your password
                     db="electrom_dankmemes")
                     
        cur = db.cursor()
        cur.execute("DELETE FROM advice WHERE id=\"{}\";".format(id))
        db.commit()
        await self.bot.say("Meme Deleted")
        db.close()
        
    @commands.command()
    @checks.admin()
    async def editadviceid(self, oldid, newid):
        """Change the ID of a Meme to make it first"""
        
        
        db = MySQLdb.connect(host="theendlessweb.com",    # your host, usually localhost
                     user="electrom_dankmemesuser",         # your username
                     passwd="DankMemes",  # your password
                     db="electrom_dankmemes")
                     
        cur = db.cursor()
        cur.execute("UPDATE advice SET id = \"{}\" WHERE id = \"{}\"".format(newid, oldid))
        db.commit()
        await self.bot.say("Meme has been updated")
        db.close()
        
    @commands.command()
    @checks.admin()
    async def approveadvice(self, approveid):
         """Approve Advice From The Table (Run [p]grabadvice to get submitted ids"""
    
       db = MySQLdb.connect(host="theendlessweb.com",    # your host, usually localhost
                     user="electrom_dankmemesuser",         # your username
                     passwd="DankMemes",  # your password
                     db="electrom_dankmemes")
                     
       cur = db.cursor()
       cur.execute("SELECT advice FROM submitadvice WHERE id =\"{}\";".format(approveid))
       approved = cur.fetchall()
       cur.execute("INSERT INTO advice (advice) VALUES= (\"{}\")".format(approveid))
       db.commit()
       await self.bot.say("Approved")
       db.close
        

def setup(bot):
    bot.add_cog(dankmemes(bot))
