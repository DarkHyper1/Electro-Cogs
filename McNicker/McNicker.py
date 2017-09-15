
from discord.ext import commands

class McNicker:
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def McNick(self, playername, nickname):
        """Enter a Nickname. It will be changed In-game."""

        #Your code will go here
        await self.bot.say("Nick Changed!")
        message = "nick {} {}".format(playername, nickname)
        await self.bot.send_message(self.bot.get_channel('320638374551748609'), "nick {} {}".format(playername, nickname))

def setup(bot):
    bot.add_cog(McNicker(bot))
