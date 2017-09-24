import discord
from discord.ext import commands

class McNicker:
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def McNick(self, ctx, playername, nickname):
        """Enter a Nickname. It will be changed In-game."""


        author = ctx.message.author
        await self.bot.say(ctx.message.author.mention + " Has updated " + playername + "s Nickname!")
        await self.bot.say("Nick Changed!")
        message = "nick {} {}".format(playername, nickname)
        await self.bot.send_message(self.bot.get_channel('320638374551748609'), "nick {} {}".format(playername, nickname))

def setup(bot):
    bot.add_cog(McNicker(bot))
